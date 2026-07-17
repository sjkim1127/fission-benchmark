#include <stddef.h>

// Reverse string in-place with pointers
void reverse_string(char *str, size_t length) {
    if (length == 0) return;
    char *start = str;
    char *end = str + length - 1;
    char temp;
    while (start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

// Naive substring search
int find_substring(const char *haystack, const char *needle) {
    if (!haystack || !needle) return -1;
    if (*needle == '\0') return 0;
    
    int i = 0;
    while (haystack[i] != '\0') {
        int j = 0;
        while (needle[j] != '\0' && haystack[i + j] == needle[j]) {
            j++;
        }
        if (needle[j] == '\0') {
            return i;
        }
        i++;
    }
    return -1;
}

int main(void) {
    char str[] = "hello";
    reverse_string(str, 5);
    return find_substring(str, "ol");
}
