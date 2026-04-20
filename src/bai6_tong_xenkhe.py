# Bài 6: Tổng S = 1 - 2 + 3 - 4 + ... ± n
def tinh_tong_xenkhe(n):
    if n < 1:
        return "Dữ liệu không hợp lệ (n >= 1)"
    
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            tong += i
        else:
            tong -= i
    return tong

# Test cases
tests = [1, 5, 10, 0, -3]

print("\n=== BÀI 6: Tổng xen kẽ ===")
for n in tests:
    print(f"n = {n} → S = {tinh_tong_xenkhe(n)}")