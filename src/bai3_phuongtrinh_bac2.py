import math

# Bài 3: Giải phương trình bậc 2
def giai_phuong_trinh_bac2(a, b, c):
    if a == 0:
        return "Không phải phương trình bậc 2 (a phải khác 0)"
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Hai nghiệm: x1 = {x1}, x2 = {x2}"

# Test cases
tests = [
    (1, -3, 2),   # normal: x=1, x=2
    (1, 2, 1),    # nghiệm kép
    (1, 1, 1),    # vô nghiệm
    (0, 5, 6),    # invalid (a=0)
    (2, -4, -6)   # normal
]

print("\n=== BÀI 3: Giải phương trình bậc 2 ===")
for a, b, c in tests:
    print(f"Input: a={a}, b={b}, c={c} → {giai_phuong_trinh_bac2(a, b, c)}")