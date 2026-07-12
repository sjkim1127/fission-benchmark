/* Multi-TU entry that links util_lib.c — models third-party multi-object PE. */
#include <stdint.h>
#include <stdio.h>

uint32_t util_hash(const char *s);
int util_clamp(int v, int lo, int hi);
int util_count_bits(uint32_t x);

int app_process(const char *msg, int score) {
    uint32_t h = util_hash(msg ? msg : "");
    int bits = util_count_bits(h);
    int c = util_clamp(score + bits, 0, 100);
    return c ^ (int)(h & 0xffu);
}

int main(void) {
    int r = app_process("realworld-fixture", 40);
    printf("%d\n", r);
    return r >= 0 ? 0 : 1;
}
