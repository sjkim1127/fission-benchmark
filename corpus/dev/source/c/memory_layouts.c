#include <stdint.h>
#include <stddef.h>

// Struct with nested unions and bitfields
struct Flags {
    uint32_t is_active : 1;
    uint32_t is_admin : 1;
    uint32_t privilege_level : 4;
    uint32_t reserved : 26;
};

union DataValue {
    int32_t int_val;
    float float_val;
    char char_vals[4];
};

struct ConfigNode {
    struct Flags flags;
    union DataValue val;
};

// Accessing and writing bitfield structure
uint32_t manipulate_bitfields(struct ConfigNode *node, int32_t val) {
    node->flags.is_active = 1;
    node->flags.is_admin = (val > 100);
    node->flags.privilege_level = val & 0xF;
    node->val.int_val = val;
    return node->flags.privilege_level + (node->flags.is_admin ? 100 : 0);
}

// Matrix multiplication (2D arrays, pointers)
void matrix_multiply(const float *a, const float *b, float *c, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            float sum = 0.0f;
            for (int k = 0; k < n; k++) {
                sum += a[i * n + k] * b[k * n + j];
            }
            c[i * n + j] = sum;
        }
    }
}

int main(void) {
    struct ConfigNode node;
    float a[4] = {1.0f, 2.0f, 3.0f, 4.0f};
    float b[4] = {1.0f, 2.0f, 3.0f, 4.0f};
    float c[4] = {0.0f};
    matrix_multiply(a, b, c, 2);
    return (int)manipulate_bitfields(&node, 42) + (int)c[0];
}
