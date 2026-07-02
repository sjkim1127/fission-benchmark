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
    "rc4_init": [
        "\nint main() { uint8_t s[256]; uint8_t key[] = {1,2,3,4}; rc4_init(s,key,4); uint8_t e[] = {194,82,8,12,50,235,33,44}; for (int i=0;i<8;i++) if (s[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256]; uint8_t key[] = {1}; rc4_init(s,key,1); uint8_t e[] = {0,2,3,4,5,6,7,8}; for (int i=0;i<8;i++) if (s[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256]; uint8_t key[] = {0,0,0}; rc4_init(s,key,3); uint8_t e[] = {0,35,3,43,9,11,65,229}; for (int i=0;i<8;i++) if (s[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256]; uint8_t key[] = {65,66,67}; rc4_init(s,key,3); uint8_t e[] = {84,132,201,55,83,155,226,96}; for (int i=0;i<8;i++) if (s[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256]; uint8_t key[] = {1,2,3,4}; rc4_init(s,key,4); int seen[256]={0}; for (int i=0;i<256;i++) { seen[s[i]]++; } for (int i=0;i<256;i++) if (seen[i]!=1) return 1; return 0; }\n",
    ],
    "rc4_crypt": [
        "\nint main() { uint8_t s[256] = {194, 82, 8, 12, 50, 235, 33, 44, 251, 165, 149, 141, 87, 163, 119, 188, 19, 161, 11, 57, 226, 249, 180, 45, 156, 114, 107, 130, 2, 49, 231, 9, 43, 253, 25, 127, 10, 203, 244, 109, 72, 215, 108, 26, 204, 176, 95, 54, 77, 128, 36, 191, 38, 134, 75, 123, 216, 205, 131, 4, 16, 93, 15, 59, 55, 14, 71, 96, 179, 250, 133, 243, 122, 105, 151, 168, 174, 221, 214, 79, 210, 172, 80, 41, 173, 17, 74, 142, 106, 73, 135, 129, 126, 150, 146, 177, 40, 21, 245, 222, 147, 89, 162, 117, 92, 197, 63, 189, 160, 153, 220, 3, 195, 100, 171, 56, 112, 213, 167, 20, 186, 184, 84, 241, 52, 219, 124, 83, 209, 182, 166, 185, 6, 110, 207, 88, 240, 223, 140, 62, 159, 29, 46, 234, 113, 125, 35, 152, 202, 178, 218, 239, 118, 158, 94, 67, 120, 183, 212, 255, 187, 230, 28, 170, 238, 217, 68, 31, 97, 246, 102, 206, 232, 70, 145, 99, 148, 48, 247, 237, 208, 85, 137, 169, 23, 39, 136, 111, 157, 37, 236, 224, 199, 154, 1, 30, 190, 7, 98, 76, 196, 211, 229, 53, 225, 61, 78, 192, 143, 198, 242, 121, 66, 18, 252, 115, 34, 101, 155, 201, 103, 116, 200, 27, 233, 69, 91, 254, 64, 104, 193, 132, 164, 65, 0, 24, 13, 139, 181, 248, 227, 60, 42, 81, 175, 86, 138, 32, 22, 144, 58, 47, 90, 5, 51, 228}; uint8_t data[] = {10,20,30}; rc4_crypt(s,data,3); uint8_t e[] = {22,254,143}; for (int i=0;i<3;i++) if (data[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256] = {194, 82, 8, 12, 50, 235, 33, 44, 251, 165, 149, 141, 87, 163, 119, 188, 19, 161, 11, 57, 226, 249, 180, 45, 156, 114, 107, 130, 2, 49, 231, 9, 43, 253, 25, 127, 10, 203, 244, 109, 72, 215, 108, 26, 204, 176, 95, 54, 77, 128, 36, 191, 38, 134, 75, 123, 216, 205, 131, 4, 16, 93, 15, 59, 55, 14, 71, 96, 179, 250, 133, 243, 122, 105, 151, 168, 174, 221, 214, 79, 210, 172, 80, 41, 173, 17, 74, 142, 106, 73, 135, 129, 126, 150, 146, 177, 40, 21, 245, 222, 147, 89, 162, 117, 92, 197, 63, 189, 160, 153, 220, 3, 195, 100, 171, 56, 112, 213, 167, 20, 186, 184, 84, 241, 52, 219, 124, 83, 209, 182, 166, 185, 6, 110, 207, 88, 240, 223, 140, 62, 159, 29, 46, 234, 113, 125, 35, 152, 202, 178, 218, 239, 118, 158, 94, 67, 120, 183, 212, 255, 187, 230, 28, 170, 238, 217, 68, 31, 97, 246, 102, 206, 232, 70, 145, 99, 148, 48, 247, 237, 208, 85, 137, 169, 23, 39, 136, 111, 157, 37, 236, 224, 199, 154, 1, 30, 190, 7, 98, 76, 196, 211, 229, 53, 225, 61, 78, 192, 143, 198, 242, 121, 66, 18, 252, 115, 34, 101, 155, 201, 103, 116, 200, 27, 233, 69, 91, 254, 64, 104, 193, 132, 164, 65, 0, 24, 13, 139, 181, 248, 227, 60, 42, 81, 175, 86, 138, 32, 22, 144, 58, 47, 90, 5, 51, 228}; uint8_t data[] = {0,0,0,0}; rc4_crypt(s,data,4); uint8_t e[] = {28,234,145,97}; for (int i=0;i<4;i++) if (data[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256] = {84, 132, 201, 55, 83, 155, 226, 96, 220, 192, 12, 90, 57, 234, 111, 119, 221, 49, 1, 50, 137, 77, 161, 56, 145, 236, 179, 10, 13, 99, 194, 35, 21, 208, 46, 174, 23, 239, 31, 70, 181, 232, 140, 63, 68, 18, 76, 131, 42, 38, 160, 122, 5, 209, 138, 28, 230, 215, 64, 71, 128, 2, 17, 34, 248, 164, 126, 115, 45, 88, 9, 74, 87, 202, 185, 41, 133, 134, 85, 36, 159, 252, 238, 130, 65, 151, 228, 203, 98, 121, 235, 16, 173, 110, 224, 102, 141, 170, 93, 163, 198, 108, 146, 78, 229, 143, 135, 184, 172, 48, 197, 61, 120, 168, 54, 67, 250, 97, 213, 32, 158, 127, 19, 125, 106, 249, 62, 254, 225, 89, 183, 242, 113, 8, 162, 0, 167, 251, 182, 195, 86, 129, 37, 196, 253, 205, 24, 103, 171, 136, 245, 218, 92, 166, 30, 123, 214, 40, 66, 200, 191, 222, 104, 156, 4, 15, 75, 26, 219, 204, 59, 58, 187, 175, 188, 52, 177, 53, 22, 189, 199, 95, 25, 247, 190, 152, 114, 94, 227, 73, 153, 176, 112, 44, 107, 33, 241, 217, 148, 244, 6, 117, 100, 80, 223, 82, 255, 139, 39, 79, 72, 211, 20, 60, 240, 165, 51, 193, 212, 3, 118, 178, 180, 124, 105, 246, 116, 7, 237, 207, 69, 186, 169, 101, 91, 150, 142, 233, 243, 216, 154, 14, 149, 157, 43, 206, 47, 81, 147, 27, 210, 109, 11, 29, 231, 144}; uint8_t data[] = {1,2,3,4,5}; rc4_crypt(s,data,5); uint8_t e[] = {207,38,93,151,74}; for (int i=0;i<5;i++) if (data[i]!=e[i]) return i+1; return 0; }\n",
        "\nint main() { uint8_t s[256] = {194, 82, 8, 12, 50, 235, 33, 44, 251, 165, 149, 141, 87, 163, 119, 188, 19, 161, 11, 57, 226, 249, 180, 45, 156, 114, 107, 130, 2, 49, 231, 9, 43, 253, 25, 127, 10, 203, 244, 109, 72, 215, 108, 26, 204, 176, 95, 54, 77, 128, 36, 191, 38, 134, 75, 123, 216, 205, 131, 4, 16, 93, 15, 59, 55, 14, 71, 96, 179, 250, 133, 243, 122, 105, 151, 168, 174, 221, 214, 79, 210, 172, 80, 41, 173, 17, 74, 142, 106, 73, 135, 129, 126, 150, 146, 177, 40, 21, 245, 222, 147, 89, 162, 117, 92, 197, 63, 189, 160, 153, 220, 3, 195, 100, 171, 56, 112, 213, 167, 20, 186, 184, 84, 241, 52, 219, 124, 83, 209, 182, 166, 185, 6, 110, 207, 88, 240, 223, 140, 62, 159, 29, 46, 234, 113, 125, 35, 152, 202, 178, 218, 239, 118, 158, 94, 67, 120, 183, 212, 255, 187, 230, 28, 170, 238, 217, 68, 31, 97, 246, 102, 206, 232, 70, 145, 99, 148, 48, 247, 237, 208, 85, 137, 169, 23, 39, 136, 111, 157, 37, 236, 224, 199, 154, 1, 30, 190, 7, 98, 76, 196, 211, 229, 53, 225, 61, 78, 192, 143, 198, 242, 121, 66, 18, 252, 115, 34, 101, 155, 201, 103, 116, 200, 27, 233, 69, 91, 254, 64, 104, 193, 132, 164, 65, 0, 24, 13, 139, 181, 248, 227, 60, 42, 81, 175, 86, 138, 32, 22, 144, 58, 47, 90, 5, 51, 228}; uint8_t data[] = {10,20,30}; rc4_crypt(s,data,0); if (data[0]!=10||data[1]!=20||data[2]!=30) return 1; return 0; }\n",
    ],
    "crc32": [
        "\nint main() { uint8_t d[] = {10,20,30}; if (crc32(d,3) != 0x2677b6f2u) return 1; return 0; }\n",
        "\nint main() { uint8_t d[] = {0}; if (crc32(d,0) != 0u) return 1; return 0; }\n",
        "\nint main() { uint8_t d[] = {'1','2','3','4','5','6','7','8','9'}; if (crc32(d,9) != 0xcbf43926u) return 1; return 0; }\n",
        "\nint main() { uint8_t d[] = {0}; if (crc32(d,1) != 0xd202ef8du) return 1; return 0; }\n",
        "\nint main() { uint8_t d[] = {255}; if (crc32(d,1) != 0xff000000u) return 1; return 0; }\n",
        "\nint main() { uint8_t d[] = {1,2,3}; if (crc32(d,3) != 0x55bc801du) return 1; return 0; }\n",
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
