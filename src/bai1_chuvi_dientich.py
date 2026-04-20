# Bài 1: Tính chu vi và diện tích hình chữ nhật
# Đầu vào: 2 số thực a (chiều dài), b (chiều rộng) > 0
# Đầu ra: Chu vi = 2*(a+b), Diện tích = a*b

def tinh_chuvi_dientich(a, b):
    if a <= 0 or b <= 0:
        return None, None  # Dữ liệu không hợp lệ
    chuvi = 2 * (a + b)
    dientich = a * b
    return chuvi, dientich

# Test cases
test_cases = [
    (5.0, 3.0),   # normal
    (10, 4),      # normal
    (0, 5),       # invalid (a=0)
    (-2, 3),      # invalid (a<0)
    (7.5, 2.5)    # normal float
]

print("=== BÀI 1: Chu vi và diện tích hình chữ nhật ===")
for a, b in test_cases:
    cv, dt = tinh_chuvi_dientich(a, b)
    if cv is None:
        print(f"Input: a={a}, b={b} → Dữ liệu không hợp lệ!")
    else:
        print(f"Input: a={a}, b={b} → Chu vi = {cv}, Diện tích = {dt}")