import math

# Bài 5: Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test cases
tests = [2, 17, 1, 0, -5, 25, 97]

print("\n=== BÀI 5: Kiểm tra số nguyên tố ===")
for n in tests:
    print(f"{n} → {'Là số nguyên tố' if la_so_nguyen_to(n) else 'Không phải số nguyên tố'}")