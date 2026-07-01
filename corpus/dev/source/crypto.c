#include <stdint.h>
#include <stddef.h>

// RC4 Key Scheduling Algorithm
void rc4_init(uint8_t *s, const uint8_t *key, int key_len) {
    int i, j = 0;
    uint8_t temp;
    for (i = 0; i < 256; i++) {
        s[i] = i;
    }
    for (i = 0; i < 256; i++) {
        j = (j + s[i] + key[i % key_len]) % 256;
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}

// RC4 Encryption/Decryption
void rc4_crypt(uint8_t *s, uint8_t *data, int data_len) {
    int i = 0, j = 0, k;
    uint8_t temp;
    for (k = 0; k < data_len; k++) {
        i = (i + 1) % 256;
        j = (j + s[i]) % 256;
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        data[k] ^= s[(s[i] + s[j]) % 256];
    }
}

// Standard CRC32 Checksum Algorithm
uint32_t crc32(const uint8_t *data, size_t length) {
    uint32_t crc = 0xFFFFFFFF;
    for (size_t i = 0; i < length; i++) {
        uint8_t byte = data[i];
        crc ^= byte;
        for (int j = 0; j < 8; j++) {
            uint32_t mask = -(crc & 1);
            crc = (crc >> 1) ^ (0xEDB88320 & mask);
        }
    }
    return ~crc;
}

int main(void) {
    uint8_t s[256];
    uint8_t key[] = {1, 2, 3, 4};
    uint8_t data[] = {10, 20, 30};
    rc4_init(s, key, 4);
    rc4_crypt(s, data, 3);
    return (int)crc32(data, 3);
}
