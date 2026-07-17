//! Rust corpus family: intentional Rust control flow with a stable C ABI surface.
//!
//! `#[no_mangle] pub extern "C"` exports allow the existing PE wine + C harness
//! semantic oracle to measure decompiler recovery (recovered-C vs original PE).
//! Native Rust driver oracles can replace this later without renaming exports.

#![allow(dead_code)]

#[no_mangle]
pub extern "C" fn rust_add_ints(a: i32, b: i32) -> i32 {
    a.wrapping_add(b)
}

#[no_mangle]
pub extern "C" fn rust_clamp_int(value: i32, lo: i32, hi: i32) -> i32 {
    if value < lo {
        lo
    } else if value > hi {
        hi
    } else {
        value
    }
}

#[no_mangle]
pub extern "C" fn rust_max3(a: i32, b: i32, c: i32) -> i32 {
    let mut m = a;
    if b > m {
        m = b;
    }
    if c > m {
        m = c;
    }
    m
}

#[no_mangle]
pub extern "C" fn rust_count_bits(x: u32) -> u32 {
    let mut n = x;
    let mut count = 0u32;
    while n != 0 {
        count += n & 1;
        n >>= 1;
    }
    count
}

/// Sum `a[i]*b[i]` for i in 0..n. Null/empty → 0.
#[no_mangle]
pub unsafe extern "C" fn rust_dot_product(a: *const i32, b: *const i32, n: usize) -> i32 {
    if a.is_null() || b.is_null() || n == 0 {
        return 0;
    }
    let mut acc = 0i32;
    for i in 0..n {
        let av = *a.add(i);
        let bv = *b.add(i);
        acc = acc.wrapping_add(av.wrapping_mul(bv));
    }
    acc
}

/// C-string length; null → 0.
#[no_mangle]
pub unsafe extern "C" fn rust_cstr_len(s: *const u8) -> usize {
    if s.is_null() {
        return 0;
    }
    let mut n = 0usize;
    loop {
        if *s.add(n) == 0 {
            break;
        }
        n += 1;
    }
    n
}

/// Sum first n elements; null/empty → 0.
#[no_mangle]
pub unsafe extern "C" fn rust_sum_range(data: *const i32, n: usize) -> i32 {
    if data.is_null() || n == 0 {
        return 0;
    }
    let mut acc = 0i32;
    for i in 0..n {
        acc = acc.wrapping_add(*data.add(i));
    }
    acc
}

/// Saturating-style clamp of a+b into i32 range via wrapping then clamp to i32::MIN/MAX
/// of a simple checked path: if overflow flags, return MAX/MIN sign-aware.
#[no_mangle]
pub extern "C" fn rust_saturating_add(a: i32, b: i32) -> i32 {
    match a.checked_add(b) {
        Some(v) => v,
        None => {
            if b > 0 {
                i32::MAX
            } else {
                i32::MIN
            }
        }
    }
}

fn main() {
    let a = [1i32, 2, 3];
    let b = [4i32, 5, 6];
    let s = b"hi\0";
    let _ = rust_add_ints(1, 2)
        + rust_clamp_int(9, 0, 5)
        + rust_max3(1, 9, 3)
        + rust_count_bits(13) as i32
        + unsafe { rust_dot_product(a.as_ptr(), b.as_ptr(), 3) }
        + unsafe { rust_cstr_len(s.as_ptr()) as i32 }
        + unsafe { rust_sum_range(a.as_ptr(), 3) }
        + rust_saturating_add(1, 2);
}
