
---

### 2. File: `TEST_CASES.md`

```markdown
# TEST CASES - Kiểm thử hộp đen (Black-box Testing)

Repository: Black Box Testing - Bài thực hành 03

## Mục tiêu
Áp dụng kỹ thuật **phân lớp tương đương** và **phân tích giá trị biên** cho 8 bài toán.

---

## Issue 1: Test Cases - Dữ liệu hợp lệ (Valid / Positive Cases)

### Bài 1: Chu vi & diện tích hình chữ nhật
| Test ID | Mô tả                  | Input (a, b)   | Expected Output                  | Actual | Pass/Fail |
|---------|------------------------|----------------|----------------------------------|--------|-----------|
| TC01    | Giá trị nguyên dương   | 5, 3           | Chu vi = 16, Diện tích = 15      |        |           |
| TC02    | Giá trị float          | 7.5, 2.5       | Chu vi = 20, Diện tích = 18.75   |        |           |
| TC03    | Giá trị lớn            | 100, 50        | Chu vi = 300, Diện tích = 5000   |        |           |

### Bài 3: Giải phương trình bậc 2
| Test ID | Mô tả                  | Input (a, b, c) | Expected Output                     | Actual | Pass/Fail |
|---------|------------------------|-----------------|-------------------------------------|--------|-----------|
| TC01    | Hai nghiệm phân biệt   | 1, -3, 2        | Hai nghiệm: x1=2, x2=1              |        |           |
| TC02    | Nghiệm kép             | 1, 2, 1         | Nghiệm kép x = -1                   |        |           |
| TC03    | Vô nghiệm              | 1, 1, 1         | Phương trình vô nghiệm              |        |           |

### Bài 4: Số ngày của một tháng
| Test ID | Mô tả                     | Input (tháng, năm) | Expected Output     | Actual | Pass/Fail |
|---------|---------------------------|--------------------|---------------------|--------|-----------|
| TC01    | Tháng 2 năm nhuận         | 2, 2024            | 29                  |        |           |
| TC02    | Tháng 2 năm thường        | 2, 2023            | 28                  |        |           |
| TC03    | Tháng 31 ngày             | 12, 2025           | 31                  |        |           |

*(Bạn tiếp tục bổ sung cho các bài còn lại tương tự)*

---

## Issue 2: Test Cases - Dữ liệu không hợp lệ, biên & ngoại lệ (Invalid / Boundary / Exception Cases)

### Bài 1: Chu vi & diện tích hình chữ nhật
| Test ID | Mô tả                        | Input (a, b)   | Expected Output                  | Actual | Pass/Fail |
|---------|------------------------------|----------------|----------------------------------|--------|-----------|
| TC01    | Cạnh = 0                     | 0, 5           | Dữ liệu không hợp lệ             |        |           |
| TC02    | Cạnh âm                      | -2, 3          | Dữ liệu không hợp lệ             |        |           |
| TC03    | Cả hai cạnh âm               | -1, -1         | Dữ liệu không hợp lệ             |        |           |

### Bài 3: Giải phương trình bậc 2
| Test ID | Mô tả                        | Input (a, b, c) | Expected Output                     | Actual | Pass/Fail |
|---------|------------------------------|-----------------|-------------------------------------|--------|-----------|
| TC01    | a = 0 (không phải bậc 2)     | 0, 5, 6         | Không phải phương trình bậc 2       |        |           |
| TC02    | a âm                         | -1, 2, 3        | (Tùy code xử lý)                    |        |           |

### Bài 7: UCLN(a, b)
| Test ID | Mô tả                        | Input (a, b)   | Expected Output                  | Actual | Pass/Fail |
|---------|------------------------------|----------------|----------------------------------|--------|-----------|
| TC01    | a = 0                        | 0, 5           | Dữ liệu không hợp lệ             |        |           |
| TC02    | a và b âm                    | -8, 4          | Dữ liệu không hợp lệ             |        |           |

*(Tiếp tục bổ sung cho Bài 4, 5, 6, 8…)*

---

**Ghi chú**:
- Các cột **Actual** và **Pass/Fail** sẽ được điền sau khi chạy test thực tế.
- Code đã xử lý ngoại lệ bằng cách trả về thông báo rõ ràng khi dữ liệu không hợp lệ.

**Cập nhật lần cuối**: 20/04/2026