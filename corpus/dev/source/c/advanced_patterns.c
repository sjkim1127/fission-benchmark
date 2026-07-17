/* Advanced semantic patterns: lists, structs, indirect calls, nested strides.
 * Pure C, no libc heap — suitable for PE oracle harness recompile.
 */
#include <stddef.h>
#include <stdint.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

typedef struct Kv {
    int key;
    int value;
} Kv;

typedef int (*binop_fn)(int, int);

/* Struct + pointer + loop: sum linked-list values until null. */
int list_sum(const Node *head) {
    int total = 0;
    const Node *cur = head;
    while (cur != NULL) {
        total += cur->value;
        cur = cur->next;
    }
    return total;
}

/* Struct array field access: first matching key's value, or -1. */
int kv_lookup(const Kv *items, size_t len, int key) {
    for (size_t i = 0; i < len; i++) {
        if (items[i].key == key) {
            return items[i].value;
        }
    }
    return -1;
}

/* Indirect call through function pointer (binop table style). */
int apply_binop(binop_fn op, int a, int b) {
    if (op == NULL) {
        return 0;
    }
    return op(a, b);
}

int add_ints(int a, int b) {
    return a + b;
}

int mul_ints(int a, int b) {
    return a * b;
}

/* Nested loop + pointer stride over a row-major matrix (no VLA). */
int dot_product_stride(const int *a, const int *b, size_t n, size_t stride) {
    int acc = 0;
    if (stride == 0) {
        stride = 1;
    }
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
            size_t idx = i * stride + j;
            acc += a[idx] * b[idx];
        }
    }
    return acc;
}

/* Bounded memcpy-like byte accumulate with early exit (pointer + loop). */
unsigned int bounded_checksum(const unsigned char *p, size_t len, size_t max_take) {
    unsigned int sum = 0;
    size_t n = len < max_take ? len : max_take;
    for (size_t i = 0; i < n; i++) {
        sum = (sum * 33u) + (unsigned int)p[i];
    }
    return sum;
}

int main(void) {
    Node c = {3, NULL};
    Node b = {2, &c};
    Node a = {1, &b};
    Kv table[] = {{1, 10}, {2, 20}, {3, 30}};
    int row_a[] = {1, 2, 3, 4};
    int row_b[] = {5, 6, 7, 8};
    unsigned char bytes[] = {1, 2, 3, 4, 5};
    int r = list_sum(&a);
    r ^= kv_lookup(table, 3, 2);
    r ^= apply_binop(add_ints, 3, 4);
    r ^= apply_binop(mul_ints, 2, 5);
    r ^= dot_product_stride(row_a, row_b, 2, 2);
    r ^= (int)bounded_checksum(bytes, 5, 3);
    return r & 0xff;
}
