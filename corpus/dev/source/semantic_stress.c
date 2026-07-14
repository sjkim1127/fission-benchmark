#include <stddef.h>
#include <stdint.h>

uint32_t rolling_hash32(const uint8_t *data, size_t len, uint32_t seed) {
    uint32_t hash = seed ^ 0x9e3779b9u;

    for (size_t i = 0; i < len; i++) {
        hash ^= data[i];
        hash = (hash << 5) | (hash >> 27);
        hash *= 0x045d9f3bu;
    }

    return hash;
}

uint32_t bounded_tlv_sum(const uint8_t *data, size_t len) {
    size_t cursor = 0;
    uint32_t total = 0;

    while (cursor + 2 <= len) {
        uint8_t tag = data[cursor];
        uint8_t width = data[cursor + 1];
        uint32_t payload = 0;

        cursor += 2;
        if ((size_t)width > len - cursor) {
            break;
        }

        for (size_t i = 0; i < width; i++) {
            payload += data[cursor + i];
        }
        total += ((uint32_t)tag << 8) ^ payload;
        cursor += width;
    }

    return total;
}

int state_machine_score(const uint8_t *events, size_t len) {
    int state = 0;
    int score = 0;

    for (size_t i = 0; i < len; i++) {
        switch (events[i]) {
        case 0:
            state = 0;
            break;
        case 1:
            if (state == 0) {
                state = 1;
            } else {
                score -= 1;
            }
            break;
        case 2:
            if (state == 1) {
                state = 2;
                score += 3;
            } else {
                state = 0;
                score -= 2;
            }
            break;
        case 3:
            if (state == 2) {
                score += 7;
                state = 0;
            } else {
                score -= 3;
            }
            break;
        default:
            score -= events[i] & 3;
            state = 0;
            break;
        }
    }

    return score + state;
}

size_t overlap_move(uint8_t *buffer, size_t dst, size_t src, size_t count) {
    if (count == 0 || dst == src) {
        return count;
    }

    if (dst < src) {
        for (size_t i = 0; i < count; i++) {
            buffer[dst + i] = buffer[src + i];
        }
    } else {
        for (size_t i = count; i > 0; i--) {
            buffer[dst + i - 1] = buffer[src + i - 1];
        }
    }

    return count;
}

int32_t mixed_width_accumulate(const int16_t *values, size_t len, int32_t bias) {
    int32_t total = bias;

    for (size_t i = 0; i < len; i++) {
        int32_t value = values[i];
        if (value < 0) {
            total -= value;
        } else {
            total += value * 2;
        }
    }

    return total;
}

uint32_t rotate_words(uint32_t *items, size_t len, unsigned int shift) {
    uint32_t checksum = 0;

    shift &= 31u;
    for (size_t i = 0; i < len; i++) {
        uint32_t value = items[i];
        uint32_t rotated = value;
        if (shift != 0) {
            rotated = (value << shift) | (value >> (32u - shift));
        }
        items[i] = rotated;
        checksum ^= rotated + (uint32_t)i;
    }

    return checksum;
}

int main(void) {
    uint8_t bytes[] = {1, 2, 3, 4, 5, 6, 7, 8};
    uint8_t tlv[] = {1, 2, 3, 4, 2, 1, 5};
    uint8_t events[] = {1, 2, 3, 0};
    int16_t values[] = {-3, 4, -5, 6};
    uint32_t words[] = {0x12345678u, 0xdeadbeefu};
    uint32_t result = rolling_hash32(bytes, 8, 7);

    result ^= bounded_tlv_sum(tlv, 7);
    result ^= (uint32_t)state_machine_score(events, 4);
    result ^= (uint32_t)overlap_move(bytes, 1, 0, 4);
    result ^= (uint32_t)mixed_width_accumulate(values, 4, 10);
    result ^= rotate_words(words, 2, 5);
    return (int)(result & 0xffu);
}
