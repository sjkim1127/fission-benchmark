#include <stddef.h>

typedef struct Pair {
    int key;
    int value;
} Pair;

int sum_array(const int *items, size_t len) {
    int sum = 0;
    for (size_t i = 0; i < len; i++) {
        sum += items[i];
    }
    return sum;
}

int reverse_in_place(int *items, size_t len) {
    for (size_t i = 0; i < len / 2; i++) {
        int tmp = items[i];
        items[i] = items[len - 1 - i];
        items[len - 1 - i] = tmp;
    }
    return len > 0 ? items[0] : 0;
}

int find_pair_value(const Pair *pairs, size_t len, int key) {
    for (size_t i = 0; i < len; i++) {
        if (pairs[i].key == key) {
            return pairs[i].value;
        }
    }
    return -1;
}

int accumulate_pairs(const Pair *pairs, size_t len) {
    int total = 0;
    for (size_t i = 0; i < len; i++) {
        total += pairs[i].key * pairs[i].value;
    }
    return total;
}

int pointer_stride_sum(const int *items, size_t len) {
    const int *end = items + len;
    int total = 0;
    while (items < end) {
        total += *items;
        items += 2;
    }
    return total;
}

int main(void) {
    int values[] = {1, 2, 3, 4, 5, 6};
    Pair pairs[] = {{1, 10}, {2, 20}, {3, 30}};
    return sum_array(values, 6) + reverse_in_place(values, 6) +
           find_pair_value(pairs, 3, 2) + accumulate_pairs(pairs, 3) +
           pointer_stride_sum(values, 6);
}
