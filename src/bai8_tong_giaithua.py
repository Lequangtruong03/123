# Bài 8: Tổng giai thừa S = 1! + 2! + ... + n!
def tinh_tong_giaithua(n):
    if n < 1:
        return "Dữ liệu không hợp lệ (n >= 1)"
    
    tong = 0
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua *= i
        tong += giai_thua
    return tong

# Test cases
tests = [1, 5, 10, 0, -2]

print("\n=== BÀI 8: Tổng giai thừa ===")
for n in tests:
    print(f"n = {n} → S = {tinh_tong_giaithua(n)}")