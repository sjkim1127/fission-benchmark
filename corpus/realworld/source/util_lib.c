/* Multi-TU realworld-style utility library (redistributable benchmark fixture). */
#include <stdint.h>
#include <string.h>

uint32_t util_hash(const char *s) {
    uint32_t h = 2166136261u;
    if (!s) return 0;
    for (; *s; s++) {
        h ^= (uint8_t)*s;
        h *= 16777619u;
    }
    return h;
}

int util_clamp(int v, int lo, int hi) {
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}

int util_count_bits(uint32_t x) {
    int n = 0;
    while (x) {
        n += (int)(x & 1u);
        x >>= 1;
    }
    return n;
}
