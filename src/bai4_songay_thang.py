# Bài 4: Tính số ngày của một tháng
def so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12 or nam < 1:
        return "Dữ liệu không hợp lệ (tháng 1-12, năm > 0)"
    
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    else:  # tháng 2
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        return 28

# Test cases
tests = [
    (2, 2024),  # nhuận → 29
    (2, 2023),  # không nhuận → 28
    (4, 2025),  # 30
    (13, 2024), # invalid
    (0, 2024),  # invalid
    (12, 0)     # invalid năm
]

print("\n=== BÀI 4: Số ngày của một tháng ===")
for t, n in tests:
    print(f"Tháng {t}/{n} → {so_ngay_trong_thang(t, n)} ngày")