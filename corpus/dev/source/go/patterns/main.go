// CGO package: Go control-flow behind a stable C ABI surface for PE wine +
// C-harness semantic measurement (same intermediate policy as C++/Rust tracks).
//
// Build (windows PE):
//
//	CGO_ENABLED=1 GOOS=windows GOARCH=amd64 CC=x86_64-w64-mingw32-gcc \
//	  go build -o patterns.exe .
package main

/*
#include <stdint.h>
#include <stddef.h>
#include <stdlib.h>
*/
import "C"
import "unsafe"

//export go_add_ints
func go_add_ints(a, b C.int) C.int {
	return a + b
}

//export go_clamp_int
func go_clamp_int(value, lo, hi C.int) C.int {
	if value < lo {
		return lo
	}
	if value > hi {
		return hi
	}
	return value
}

//export go_max3
func go_max3(a, b, c C.int) C.int {
	m := a
	if b > m {
		m = b
	}
	if c > m {
		m = c
	}
	return m
}

//export go_count_bits
func go_count_bits(x C.uint) C.uint {
	n := uint32(x)
	var count C.uint
	for n != 0 {
		count += C.uint(n & 1)
		n >>= 1
	}
	return count
}

//export go_dot_product
func go_dot_product(a, b *C.int, n C.size_t) C.int {
	if a == nil || b == nil || n == 0 {
		return 0
	}
	var acc C.int
	// Manual indexing avoids Go slice headers in the export surface.
	ap := unsafe.Pointer(a)
	bp := unsafe.Pointer(b)
	for i := C.size_t(0); i < n; i++ {
		ai := *(*C.int)(unsafe.Pointer(uintptr(ap) + uintptr(i)*unsafe.Sizeof(*a)))
		bi := *(*C.int)(unsafe.Pointer(uintptr(bp) + uintptr(i)*unsafe.Sizeof(*b)))
		acc += ai * bi
	}
	return acc
}

//export go_cstr_len
func go_cstr_len(s *C.char) C.size_t {
	if s == nil {
		return 0
	}
	var n C.size_t
	p := unsafe.Pointer(s)
	for {
		c := *(*byte)(unsafe.Pointer(uintptr(p) + uintptr(n)))
		if c == 0 {
			break
		}
		n++
	}
	return n
}

//export go_sum_range
func go_sum_range(data *C.int, n C.size_t) C.int {
	if data == nil || n == 0 {
		return 0
	}
	var acc C.int
	p := unsafe.Pointer(data)
	for i := C.size_t(0); i < n; i++ {
		v := *(*C.int)(unsafe.Pointer(uintptr(p) + uintptr(i)*unsafe.Sizeof(*data)))
		acc += v
	}
	return acc
}

//export go_saturating_add
func go_saturating_add(a, b C.int) C.int {
	// Match rust_saturating_add: checked add, else sign-aware min/max.
	sum := int64(a) + int64(b)
	if sum > int64(0x7fffffff) {
		return C.int(0x7fffffff)
	}
	if sum < int64(-0x80000000) {
		return C.int(-0x80000000)
	}
	return C.int(sum)
}

func main() {
	// Keep exports live so the linker retains them.
	a := []C.int{1, 2, 3}
	b := []C.int{4, 5, 6}
	s := C.CString("hi")
	defer C.free(unsafe.Pointer(s))
	_ = go_add_ints(1, 2) +
		go_clamp_int(9, 0, 5) +
		go_max3(1, 9, 3) +
		C.int(go_count_bits(13)) +
		go_dot_product(&a[0], &b[0], 3) +
		C.int(go_cstr_len(s)) +
		go_sum_range(&a[0], 3) +
		go_saturating_add(1, 2)
}
