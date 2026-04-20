# Bài 7: Ước chung lớn nhất (UCLN)
def ucln(a, b):
    if a <= 0 or b <= 0:
        return "Dữ liệu không hợp lệ (a, b phải > 0)"
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
tests = [(12, 18), (7, 13), (0, 5), (25, 10), (-8, 4)]

print("\n=== BÀI 7: UCLN ===")
for a, b in tests:
    print(f"UCLN({a}, {b}) = {ucln(a, b)}")