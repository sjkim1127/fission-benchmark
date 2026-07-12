/* Minimal PE mapper for Wine-hosted original-binary oracle reference calls.
 * Linked into the generated differential translation unit.
 */
#include <windows.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    uint8_t *base;
    size_t size;
} OraclePeImage;

static void oracle_pe_free(OraclePeImage *image) {
    if (image && image->base) {
        VirtualFree(image->base, 0, MEM_RELEASE);
        image->base = NULL;
        image->size = 0;
    }
}

static int oracle_pe_apply_relocations(uint8_t *base, uint64_t preferred_base, uint64_t actual_base) {
    IMAGE_DOS_HEADER *dos = (IMAGE_DOS_HEADER *)base;
    IMAGE_NT_HEADERS *nt = (IMAGE_NT_HEADERS *)(base + dos->e_lfanew);
    IMAGE_DATA_DIRECTORY dir = nt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC];
    if (!dir.VirtualAddress || !dir.Size) {
        return (preferred_base == actual_base) ? 0 : -1;
    }
    ptrdiff_t delta = (ptrdiff_t)(actual_base - preferred_base);
    if (delta == 0) {
        return 0;
    }
    uint8_t *rel = base + dir.VirtualAddress;
    uint8_t *end = rel + dir.Size;
    while (rel < end) {
        IMAGE_BASE_RELOCATION *block = (IMAGE_BASE_RELOCATION *)rel;
        if (block->SizeOfBlock < sizeof(IMAGE_BASE_RELOCATION)) {
            break;
        }
        DWORD count = (block->SizeOfBlock - sizeof(IMAGE_BASE_RELOCATION)) / sizeof(WORD);
        WORD *entries = (WORD *)(rel + sizeof(IMAGE_BASE_RELOCATION));
        for (DWORD i = 0; i < count; i++) {
            WORD type = entries[i] >> 12;
            WORD offset = entries[i] & 0x0FFF;
            uint8_t *patch = base + block->VirtualAddress + offset;
            if (type == IMAGE_REL_BASED_DIR64) {
                *(uint64_t *)patch += (uint64_t)delta;
            } else if (type == IMAGE_REL_BASED_HIGHLOW) {
                *(uint32_t *)patch += (uint32_t)delta;
            } else if (type == IMAGE_REL_BASED_ABSOLUTE) {
                /* padding */
            } else {
                return -1;
            }
        }
        rel += block->SizeOfBlock;
    }
    return 0;
}

static int oracle_pe_resolve_imports(uint8_t *base) {
    IMAGE_DOS_HEADER *dos = (IMAGE_DOS_HEADER *)base;
    IMAGE_NT_HEADERS *nt = (IMAGE_NT_HEADERS *)(base + dos->e_lfanew);
    IMAGE_DATA_DIRECTORY dir = nt->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT];
    if (!dir.VirtualAddress) {
        return 0;
    }
    IMAGE_IMPORT_DESCRIPTOR *imp = (IMAGE_IMPORT_DESCRIPTOR *)(base + dir.VirtualAddress);
    for (; imp->Name; imp++) {
        const char *mod_name = (const char *)(base + imp->Name);
        HMODULE mod = LoadLibraryA(mod_name);
        if (!mod) {
            return -1;
        }
        IMAGE_THUNK_DATA *oft = (IMAGE_THUNK_DATA *)(base + (imp->OriginalFirstThunk ? imp->OriginalFirstThunk : imp->FirstThunk));
        IMAGE_THUNK_DATA *ft = (IMAGE_THUNK_DATA *)(base + imp->FirstThunk);
        for (; oft->u1.AddressOfData; oft++, ft++) {
            FARPROC proc;
            if (IMAGE_SNAP_BY_ORDINAL(oft->u1.Ordinal)) {
                proc = GetProcAddress(mod, (LPCSTR)(uintptr_t)IMAGE_ORDINAL(oft->u1.Ordinal));
            } else {
                IMAGE_IMPORT_BY_NAME *name = (IMAGE_IMPORT_BY_NAME *)(base + oft->u1.AddressOfData);
                proc = GetProcAddress(mod, (LPCSTR)name->Name);
            }
            if (!proc) {
                return -1;
            }
            ft->u1.Function = (ULONG_PTR)proc;
        }
    }
    return 0;
}

static int oracle_pe_load(const char *path, OraclePeImage *out) {
    HANDLE file = CreateFileA(path, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (file == INVALID_HANDLE_VALUE) {
        return -1;
    }
    DWORD file_size = GetFileSize(file, NULL);
    if (file_size == INVALID_FILE_SIZE || file_size < sizeof(IMAGE_DOS_HEADER)) {
        CloseHandle(file);
        return -1;
    }
    uint8_t *file_buf = (uint8_t *)malloc(file_size);
    if (!file_buf) {
        CloseHandle(file);
        return -1;
    }
    DWORD read_n = 0;
    if (!ReadFile(file, file_buf, file_size, &read_n, NULL) || read_n != file_size) {
        free(file_buf);
        CloseHandle(file);
        return -1;
    }
    CloseHandle(file);

    IMAGE_DOS_HEADER *dos = (IMAGE_DOS_HEADER *)file_buf;
    if (dos->e_magic != IMAGE_DOS_SIGNATURE) {
        free(file_buf);
        return -1;
    }
    IMAGE_NT_HEADERS *nt = (IMAGE_NT_HEADERS *)(file_buf + dos->e_lfanew);
    if (nt->Signature != IMAGE_NT_SIGNATURE) {
        free(file_buf);
        return -1;
    }
    SIZE_T image_size = nt->OptionalHeader.SizeOfImage;
    uint8_t *base = (uint8_t *)VirtualAlloc(NULL, image_size, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
    if (!base) {
        free(file_buf);
        return -1;
    }
    memcpy(base, file_buf, nt->OptionalHeader.SizeOfHeaders);
    IMAGE_SECTION_HEADER *sec = IMAGE_FIRST_SECTION(nt);
    for (unsigned i = 0; i < nt->FileHeader.NumberOfSections; i++) {
        if (!sec[i].SizeOfRawData) {
            continue;
        }
        memcpy(base + sec[i].VirtualAddress, file_buf + sec[i].PointerToRawData, sec[i].SizeOfRawData);
    }
    uint64_t preferred = (uint64_t)nt->OptionalHeader.ImageBase;
    if (oracle_pe_apply_relocations(base, preferred, (uint64_t)(uintptr_t)base) != 0) {
        VirtualFree(base, 0, MEM_RELEASE);
        free(file_buf);
        return -1;
    }
    if (oracle_pe_resolve_imports(base) != 0) {
        VirtualFree(base, 0, MEM_RELEASE);
        free(file_buf);
        return -1;
    }
    free(file_buf);
    out->base = base;
    out->size = image_size;
    return 0;
}

static DWORD oracle_pe_rva(const char *path, unsigned long long addr) {
    HANDLE file = CreateFileA(path, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (file == INVALID_HANDLE_VALUE) {
        return 0;
    }
    IMAGE_DOS_HEADER dos;
    DWORD read_n = 0;
    if (!ReadFile(file, &dos, sizeof(dos), &read_n, NULL) || read_n != sizeof(dos)) {
        CloseHandle(file);
        return 0;
    }
    SetFilePointer(file, dos.e_lfanew, NULL, FILE_BEGIN);
    IMAGE_NT_HEADERS nt;
    if (!ReadFile(file, &nt, sizeof(nt), &read_n, NULL) || read_n != sizeof(nt)) {
        CloseHandle(file);
        return 0;
    }
    CloseHandle(file);
    unsigned long long image_base = (unsigned long long)nt.OptionalHeader.ImageBase;
    if (addr >= image_base) {
        return (DWORD)(addr - image_base);
    }
    return (DWORD)addr;
}
