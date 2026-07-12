#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Recursive Fibonacci */
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

/* Iterative Fibonacci */
int fibonacci_iter(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int c = a + b;
        a = b;
        b = c;
    }
    return b;
}

/* Simple max */
int max(int a, int b) {
    return a > b ? a : b;
}

/* Bubble sort */
void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

/* Linear search */
int linear_search(int *arr, int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

/* Binary search */
int binary_search(int *arr, int n, int target) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

/* Factorial */
long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

/* GCD (Euclidean) */
int gcd(int a, int b) {
    while (b != 0) {
        int t = b;
        b = a % b;
        a = t;
    }
    return a;
}

/* Power */
long long power(long long base, int exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp & 1) result *= base;
        base *= base;
        exp >>= 1;
    }
    return result;
}

/* Process status codes */
int process_code(int code) {
    if (code == 0) return 1;
    if (code > 0 && code < 100) return 2;
    if (code >= 100 && code < 200) return 3;
    if (code >= 400 && code < 500) return -1;
    return 0;
}

int main(void) {
    int values[] = {1, 3, 5, 7, 9};
    int sortable[] = {5, 4, 3, 2, 1};
    bubble_sort(sortable, 5);
    return fibonacci(6) + fibonacci_iter(6) + max(3, 9) +
           linear_search(values, 5, 7) + binary_search(values, 5, 7) +
           (int)factorial(5) + gcd(48, 18) + (int)power(2, 8) +
           process_code(100) + sortable[0];
}
