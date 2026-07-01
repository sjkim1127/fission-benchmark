"""
Test wrappers for semantic verification.

Each entry maps a function name to a list of main() test cases.
Each case is a complete `int main() { ... }` body that returns 0 on success, non-zero on failure.

Coverage target: ≥5 cases per function covering:
  - 2+ normal inputs
  - 1+ boundary/edge values (0, 1, empty, max)
  - 1+ negative/overflow inputs where applicable
  - 1+ larger inputs
"""

TEST_WRAPPERS: dict[str, list[str]] = {
    "fibonacci": [
        "\nint main() { if (fibonacci(0) != 0) return 1; return 0; }\n",
        "\nint main() { if (fibonacci(1) != 1) return 1; return 0; }\n",
        "\nint main() { if (fibonacci(5) != 5) return 1; return 0; }\n",
        "\nint main() { if (fibonacci(10) != 55) return 1; return 0; }\n",
        "\nint main() { if (fibonacci(2) != 1) return 1; return 0; }\n",
        "\nint main() { if (fibonacci(15) != 610) return 1; return 0; }\n",
    ],
    "fibonacci_iter": [
        "\nint main() { if (fibonacci_iter(0) != 0) return 1; return 0; }\n",
        "\nint main() { if (fibonacci_iter(1) != 1) return 1; return 0; }\n",
        "\nint main() { if (fibonacci_iter(5) != 5) return 1; return 0; }\n",
        "\nint main() { if (fibonacci_iter(10) != 55) return 1; return 0; }\n",
        "\nint main() { if (fibonacci_iter(2) != 1) return 1; return 0; }\n",
        "\nint main() { if (fibonacci_iter(15) != 610) return 1; return 0; }\n",
    ],
    "max": [
        "\nint main() { if (max(10, 20) != 20) return 1; return 0; }\n",
        "\nint main() { if (max(30, 15) != 30) return 1; return 0; }\n",
        "\nint main() { if (max(-5, -10) != -5) return 1; return 0; }\n",
        "\nint main() { if (max(7, 7) != 7) return 1; return 0; }\n",       # equal values
        "\nint main() { if (max(0, -1) != 0) return 1; return 0; }\n",     # zero vs negative
        "\nint main() { if (max(2147483647, 0) != 2147483647) return 1; return 0; }\n",  # INT_MAX
    ],
    "bubble_sort": [
        "\nint main() { int a[] = {5,2,4,1,3}; bubble_sort(a,5); if (a[0]!=1||a[1]!=2||a[2]!=3||a[3]!=4||a[4]!=5) return 1; return 0; }\n",
        "\nint main() { int a[] = {1}; bubble_sort(a,1); if (a[0]!=1) return 1; return 0; }\n",        # single element
        "\nint main() { int a[] = {1,2,3}; bubble_sort(a,3); if (a[0]!=1||a[1]!=2||a[2]!=3) return 1; return 0; }\n",  # already sorted
        "\nint main() { int a[] = {3,2,1}; bubble_sort(a,3); if (a[0]!=1||a[1]!=2||a[2]!=3) return 1; return 0; }\n",  # reverse sorted
        "\nint main() { int a[] = {-3,0,2,-1}; bubble_sort(a,4); if (a[0]!=-3||a[1]!=-1||a[2]!=0||a[3]!=2) return 1; return 0; }\n",  # negatives
    ],
    "linear_search": [
        "\nint main() { int a[] = {10,20,30,40,50}; if (linear_search(a,5,30)!=2) return 1; return 0; }\n",
        "\nint main() { int a[] = {10,20,30,40,50}; if (linear_search(a,5,60)!=-1) return 1; return 0; }\n",
        "\nint main() { int a[] = {10,20,30,40,50}; if (linear_search(a,5,10)!=0) return 1; return 0; }\n",  # first element
        "\nint main() { int a[] = {10,20,30,40,50}; if (linear_search(a,5,50)!=4) return 1; return 0; }\n",  # last element
        "\nint main() { int a[] = {42}; if (linear_search(a,1,42)!=0) return 1; return 0; }\n",              # single element found
        "\nint main() { int a[] = {42}; if (linear_search(a,1,99)!=-1) return 1; return 0; }\n",            # single element not found
    ],
    "binary_search": [
        "\nint main() { int a[] = {10,20,30,40,50}; if (binary_search(a,5,30)!=2) return 1; return 0; }\n",
        "\nint main() { int a[] = {10,20,30,40,50}; if (binary_search(a,5,60)!=-1) return 1; return 0; }\n",
        "\nint main() { int a[] = {10,20,30,40,50}; if (binary_search(a,5,10)!=0) return 1; return 0; }\n",  # first element
        "\nint main() { int a[] = {10,20,30,40,50}; if (binary_search(a,5,50)!=4) return 1; return 0; }\n",  # last element
        "\nint main() { int a[] = {7}; if (binary_search(a,1,7)!=0) return 1; return 0; }\n",               # single element found
        "\nint main() { int a[] = {7}; if (binary_search(a,1,8)!=-1) return 1; return 0; }\n",              # single element not found
    ],
    "factorial": [
        "\nint main() { if (factorial(0) != 1) return 1; return 0; }\n",
        "\nint main() { if (factorial(1) != 1) return 1; return 0; }\n",
        "\nint main() { if (factorial(5) != 120) return 1; return 0; }\n",
        "\nint main() { if (factorial(3) != 6) return 1; return 0; }\n",
        "\nint main() { if (factorial(10) != 3628800) return 1; return 0; }\n",   # larger input
    ],
    "gcd": [
        "\nint main() { if (gcd(54, 24) != 6) return 1; return 0; }\n",
        "\nint main() { if (gcd(17, 3) != 1) return 1; return 0; }\n",
        "\nint main() { if (gcd(0, 5) != 5) return 1; return 0; }\n",
        "\nint main() { if (gcd(12, 12) != 12) return 1; return 0; }\n",          # same values
        "\nint main() { if (gcd(100, 75) != 25) return 1; return 0; }\n",
        "\nint main() { if (gcd(1, 999) != 1) return 1; return 0; }\n",           # coprime
    ],
    "power": [
        "\nint main() { if (power(2, 10) != 1024) return 1; return 0; }\n",
        "\nint main() { if (power(3, 3) != 27) return 1; return 0; }\n",
        "\nint main() { if (power(5, 0) != 1) return 1; return 0; }\n",
        "\nint main() { if (power(1, 100) != 1) return 1; return 0; }\n",         # base 1
        "\nint main() { if (power(2, 0) != 1) return 1; return 0; }\n",           # exponent 0
        "\nint main() { if (power(7, 2) != 49) return 1; return 0; }\n",
    ],
    "process_code": [
        "\nint main() { if (process_code(0) != 1) return 1; return 0; }\n",
        "\nint main() { if (process_code(50) != 2) return 1; return 0; }\n",
        "\nint main() { if (process_code(150) != 3) return 1; return 0; }\n",
        "\nint main() { if (process_code(450) != -1) return 1; return 0; }\n",
        "\nint main() { if (process_code(999) != 0) return 1; return 0; }\n",
    ],
    "count_bits": [
        "\nint main() { if (count_bits(0) != 0) return 1; return 0; }\n",
        "\nint main() { if (count_bits(7) != 3) return 1; return 0; }\n",
        "\nint main() { if (count_bits(10) != 2) return 1; return 0; }\n",
        "\nint main() { if (count_bits(1) != 1) return 1; return 0; }\n",         # single bit
        "\nint main() { if (count_bits(255) != 8) return 1; return 0; }\n",       # all bits in byte
        "\nint main() { if (count_bits(0xFFFFFFFF) != 32) return 1; return 0; }\n",  # all bits
    ],
    "clamp": [
        "\nint main() { if (clamp(5, 10, 20) != 10) return 1; return 0; }\n",     # below min
        "\nint main() { if (clamp(25, 10, 20) != 20) return 1; return 0; }\n",    # above max
        "\nint main() { if (clamp(15, 10, 20) != 15) return 1; return 0; }\n",    # in range
        "\nint main() { if (clamp(10, 10, 20) != 10) return 1; return 0; }\n",    # exactly min
        "\nint main() { if (clamp(20, 10, 20) != 20) return 1; return 0; }\n",    # exactly max
        "\nint main() { if (clamp(-5, -10, 0) != -5) return 1; return 0; }\n",   # negative range
    ],
    "signum": [
        "\nint main() { if (signum(5) != 1) return 1; return 0; }\n",
        "\nint main() { if (signum(-5) != -1) return 1; return 0; }\n",
        "\nint main() { if (signum(0) != 0) return 1; return 0; }\n",
        "\nint main() { if (signum(1000) != 1) return 1; return 0; }\n",
        "\nint main() { if (signum(-1000) != -1) return 1; return 0; }\n",
    ],
    "checksum": [
        "\nint main() { unsigned char d[] = {10,20,30,40}; if (checksum(d,4) != 100) return 1; return 0; }\n",
        "\nint main() { unsigned char d[] = {0}; if (checksum(d,1) != 0) return 1; return 0; }\n",     # zero element
        "\nint main() { unsigned char d[] = {255}; if (checksum(d,1) != 255) return 1; return 0; }\n", # max byte
        "\nint main() { unsigned char d[] = {1,2,3}; if (checksum(d,3) != 6) return 1; return 0; }\n",
        "\nint main() { unsigned char d[] = {100,100}; if (checksum(d,2) != 200) return 1; return 0; }\n",
    ],
    "classify_range": [
        "\nint main() { if (classify_range(0) != 0) return 1; return 0; }\n",
        "\nint main() { if (classify_range(2) != 1) return 1; return 0; }\n",
        "\nint main() { if (classify_range(10) != 2) return 1; return 0; }\n",
        "\nint main() { if (classify_range(-5) != -1) return 1; return 0; }\n",
        "\nint main() { if (classify_range(100) != 3) return 1; return 0; }\n",
    ],
    "saturating_add": [
        "\nint main() { if (saturating_add(10, 20) != 30) return 1; return 0; }\n",
        "\nint main() { if (saturating_add(2147483640, 10) != 2147483647) return 1; return 0; }\n",
        "\nint main() { if (saturating_add(-2147483640, -10) != -2147483648) return 1; return 0; }\n",
        "\nint main() { if (saturating_add(0, 0) != 0) return 1; return 0; }\n",
        "\nint main() { if (saturating_add(1, -1) != 0) return 1; return 0; }\n",
    ],
    "sum_array": [
        "\nint main() { int a[] = {1,2,3,4,5}; if (sum_array(a,5) != 15) return 1; return 0; }\n",
        "\nint main() { int a[] = {0}; if (sum_array(a,1) != 0) return 1; return 0; }\n",              # single zero
        "\nint main() { int a[] = {42}; if (sum_array(a,1) != 42) return 1; return 0; }\n",            # single element
        "\nint main() { int a[] = {-1,-2,-3}; if (sum_array(a,3) != -6) return 1; return 0; }\n",     # all negative
        "\nint main() { int a[] = {100,200,300}; if (sum_array(a,3) != 600) return 1; return 0; }\n",
    ],
    "reverse_in_place": [
        "\nint main() { int a[] = {1,2,3,4,5}; if (reverse_in_place(a,5)!=5) return 1; if (a[0]!=5||a[4]!=1) return 2; return 0; }\n",
        "\nint main() { int a[] = {1}; reverse_in_place(a,1); if (a[0]!=1) return 1; return 0; }\n",   # single element
        "\nint main() { int a[] = {2,1}; reverse_in_place(a,2); if (a[0]!=1||a[1]!=2) return 1; return 0; }\n",  # two elements
        "\nint main() { int a[] = {1,2,3,4}; reverse_in_place(a,4); if (a[0]!=4||a[3]!=1) return 1; return 0; }\n",  # even count
        "\nint main() { int a[] = {5,5,5}; reverse_in_place(a,3); if (a[0]!=5||a[1]!=5||a[2]!=5) return 1; return 0; }\n",  # all same
    ],
    "find_pair_value": [
        "\nint main() { Pair p[] = {{1,10},{2,20},{3,30}}; if (find_pair_value(p,3,2)!=20) return 1; return 0; }\n",
        "\nint main() { Pair p[] = {{1,10},{2,20},{3,30}}; if (find_pair_value(p,3,4)!=-1) return 1; return 0; }\n",
        "\nint main() { Pair p[] = {{1,10}}; if (find_pair_value(p,1,1)!=10) return 1; return 0; }\n",  # single entry found
        "\nint main() { Pair p[] = {{1,10}}; if (find_pair_value(p,1,2)!=-1) return 1; return 0; }\n", # single entry not found
        "\nint main() { Pair p[] = {{1,10},{2,20},{3,30}}; if (find_pair_value(p,3,1)!=10) return 1; return 0; }\n",  # first element
    ],
    "accumulate_pairs": [
        "\nint main() { Pair p[] = {{1,5},{2,10},{3,15}}; if (accumulate_pairs(p,3)!=70) return 1; return 0; }\n",
        "\nint main() { Pair p[] = {{1,0}}; if (accumulate_pairs(p,1)!=0) return 1; return 0; }\n",    # zero value
        "\nint main() { Pair p[] = {{2,3}}; if (accumulate_pairs(p,1)!=6) return 1; return 0; }\n",   # single pair
        "\nint main() { Pair p[] = {{1,1},{2,2}}; if (accumulate_pairs(p,2)!=5) return 1; return 0; }\n",  # two pairs: 1*1 + 2*2 = 5
        "\nint main() { Pair p[] = {{3,0},{0,5}}; if (accumulate_pairs(p,2)!=0) return 1; return 0; }\n",  # zeros: 3*0 + 0*5 = 0
    ],
    "pointer_stride_sum": [
        "\nint main() { int a[] = {1,2,3,4,5,6,7}; if (pointer_stride_sum(a,7)!=16) return 1; return 0; }\n",
        "\nint main() { int a[] = {1}; if (pointer_stride_sum(a,1)!=1) return 1; return 0; }\n",       # single element
        "\nint main() { int a[] = {5,10}; if (pointer_stride_sum(a,2)!=5) return 1; return 0; }\n",    # two elements, stride picks first
        "\nint main() { int a[] = {2,99,4,99,6}; if (pointer_stride_sum(a,5)!=12) return 1; return 0; }\n",  # stride=2: 2+4+6=12
        "\nint main() { int a[] = {0,0,0,0}; if (pointer_stride_sum(a,4)!=0) return 1; return 0; }\n", # all zeros
    ],
}
