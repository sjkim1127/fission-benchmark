/* C++ corpus family: intentional C++ features with extern "C" export surface
 * so the existing PE wine / C-harness semantic oracle can measure recovery.
 *
 * C++ internals (namespace, templates, std algorithms) stay behind the ABI
 * boundary; exported symbols are stable C names for nm + wrappers.
 */
#include <algorithm>
#include <cstddef>
#include <cstdint>

namespace fission_bench {
namespace cpp_patterns {

template <typename T>
T clamp_t(T value, T lo, T hi) {
    return std::max(lo, std::min(value, hi));
}

class Accumulator {
public:
    explicit Accumulator(int seed = 0) : total_(seed) {}

    void add(int v) { total_ += v; }
    int total() const { return total_; }

private:
    int total_;
};

int max3_impl(int a, int b, int c) {
    return std::max(a, std::max(b, c));
}

unsigned count_bits_impl(unsigned x) {
    unsigned count = 0;
    while (x != 0u) {
        count += x & 1u;
        x >>= 1u;
    }
    return count;
}

int dot_product_impl(const int *a, const int *b, std::size_t n) {
    int acc = 0;
    for (std::size_t i = 0; i < n; ++i) {
        acc += a[i] * b[i];
    }
    return acc;
}

std::size_t cstr_len_impl(const char *s) {
    if (s == nullptr) {
        return 0;
    }
    std::size_t n = 0;
    while (s[n] != '\0') {
        ++n;
    }
    return n;
}

int sum_range_impl(const int *begin, const int *end) {
    Accumulator acc;
    for (const int *p = begin; p != end; ++p) {
        acc.add(*p);
    }
    return acc.total();
}

}  // namespace cpp_patterns
}  // namespace fission_bench

extern "C" {

int cpp_add_ints(int a, int b) {
    return a + b;
}

int cpp_clamp_int(int value, int lo, int hi) {
    return fission_bench::cpp_patterns::clamp_t(value, lo, hi);
}

int cpp_max3(int a, int b, int c) {
    return fission_bench::cpp_patterns::max3_impl(a, b, c);
}

unsigned cpp_count_bits(unsigned x) {
    return fission_bench::cpp_patterns::count_bits_impl(x);
}

int cpp_dot_product(const int *a, const int *b, std::size_t n) {
    if (a == nullptr || b == nullptr) {
        return 0;
    }
    return fission_bench::cpp_patterns::dot_product_impl(a, b, n);
}

std::size_t cpp_cstr_len(const char *s) {
    return fission_bench::cpp_patterns::cstr_len_impl(s);
}

int cpp_sum_range(const int *data, std::size_t n) {
    if (data == nullptr || n == 0) {
        return 0;
    }
    return fission_bench::cpp_patterns::sum_range_impl(data, data + n);
}

int main(void) {
    int a[] = {1, 2, 3};
    int b[] = {4, 5, 6};
    return cpp_add_ints(1, 2) + cpp_clamp_int(9, 0, 5) + cpp_max3(1, 9, 3) +
           static_cast<int>(cpp_count_bits(13u)) + cpp_dot_product(a, b, 3) +
           static_cast<int>(cpp_cstr_len("hi")) + cpp_sum_range(a, 3);
}

}  // extern "C"
