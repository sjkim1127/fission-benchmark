#include <stddef.h>

int count_bits(unsigned int x) {
    int count = 0;
    while (x != 0) {
        count += (int)(x & 1u);
        x >>= 1;
    }
    return count;
}

int clamp(int value, int lo, int hi) {
    if (value < lo) return lo;
    if (value > hi) return hi;
    return value;
}

int signum(int value) {
    if (value > 0) return 1;
    if (value < 0) return -1;
    return 0;
}

int checksum(const unsigned char *buf, size_t len) {
    unsigned int sum = 0;
    for (size_t i = 0; i < len; i++) {
        sum = (sum + buf[i]) & 0xffu;
    }
    return (int)sum;
}

int classify_range(int value) {
    switch (value) {
        case 0:
            return 0;
        case 1:
        case 2:
        case 3:
            return 1;
        case 10:
            return 2;
        default:
            return value < 0 ? -1 : 3;
    }
}

int saturating_add(int a, int b) {
    int result = a + b;
    if (b > 0 && result < a) return 2147483647;
    if (b < 0 && result > a) return -2147483647 - 1;
    return result;
}

int main(void) {
    unsigned char data[] = {1, 2, 3, 4, 5};
    return count_bits(13) + clamp(8, 0, 5) + signum(-4) +
           checksum(data, 5) + classify_range(10) + saturating_add(1, 2);
}
