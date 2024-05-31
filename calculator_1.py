# PUBLIC VERSION FOR REVIEW
#

# XÁC ĐỊNH MỨC ĐỘ ƯU TIÊN CỦA TOÁN TỬ
def precedence(opt):
    if opt == '+' or opt == '-':
        return 1
    if opt == '*' or opt == '/':
        return 2
    if opt == '^':
        return 3
    return 0


# THỰC HIỆN PHÉP TOÁN:
def run_opt(x, y, opt):
    if opt == '+':
        return x + y
    if opt == '-':
        return x - y
    if opt == '*':
        return x * y
    if opt == '/':
        return x / y
    if opt == '^':
        return x ** y


# CHUYỂN BIỂU THỨC TRUNG TỐ SANG HẬU TỐ
def infix_to_postfix(infix_expression):
    operator_stack = []      # Ngăn xếp lưu trữ toán tử
    operand_stack = []       # Ngăn xếp lưu trữ toán hạng
    i = 0                    # Khởi tạo biến i xác định vị trí
    while i < len(infix_expression):
        char = infix_expression[i]
        if char.isdigit():
            num = char
            while i + 1 < len(infix_expression) and infix_expression[i + 1].isdigit():
                i += 1
                num += infix_expression[i]
            operand_stack.append(num)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                operand_stack.append(operator_stack.pop())
            operator_stack.pop()
# Khi kiểm tra ký tự hiện tại char là ')', thì tạo vòng lặp kiểm tra 2 điều kiện
# ĐK1: operator_stack không rỗng
# ĐK2: Giá trị trên đỉnh operator_stack không phải là '('
# Khi 2 điều kiện trên là True thì lấy ra phần tử trên đỉnh của operator_stack bằng pop()
# và thêm vào ngăn xếp toán hạng operand_stack bằng append()
# Sau khi vòng lặp kết thúc thì phần tử còn lại là '(' , operator_stack.pop() sẽ loại bỏ
# dấu '(' khỏi operator_stack, hoàn tất việc xử lý dấu ngoặc và các phần từ giữa dấu '(' và ')'

        else:
            while operator_stack and precedence(operator_stack[-1]) >= precedence(char):
                operand_stack.append(operator_stack.pop())
            operator_stack.append(char)
        i += 1
    while operator_stack:
        operand_stack.append(operator_stack.pop())
    return ' '.join(operand_stack)


# ĐÁNH GIÁ BIỂU THỨC HẬU TỐ ĐỂ TRẢ VỀ KẾT QUẢ
def evaluate_postfix(postfix_expression):   # Tham số postfix_expression là 1 biểu thức hậu tố
    stack = []                              # Tạo ngăn xếp (hoặc list) rỗng lưu trữ toán hạng
    items = postfix_expression.split()
# items: Tách chuỗi biểu thức hậu tố (postfix_expression) thành các item và sử dụng khoảng trắng
# để phân cách, kết quả là một danh sách items chứa các toán hạng và toán tử dạng string

    for item in items:                 # Duyệt từng item trong danh sách items
        if item.isdigit():
            stack.append(int(item))    # Nếu item là số thì thêm vào stack (item được chuyển thành số nguyên)
        else:
            y = stack.pop()
            x = stack.pop()
            result = run_opt(x, y, item)
            stack.append(result)
    return stack[0]
# (105-110) Nếu item là toán tử thì: loại bỏ toán hạng trên đỉnh của stack (dùng biến y để hiểu là
# toán hạng sau cùng) và loại bỏ tiếp toán hạng ngay dưới y, là x.
# Dùng hàm run_opt để tính toán với x, y và toán tử item.
# Kết quả tính được, gán cho biến result, thêm biến này trở lại stack (là 1 giá trị mới ở đỉnh ngăn xếp)
# Khi duyệt hết các item trong items và xử lý, thì vòng lặp kết thúc
# stack lúc này chỉ có duy nhất 1 giá trị là result.
# Vòng lặp kết thúc, trả về giá trị tại vị trí đầu tiên trong stack, là giá trị result cuối cùng.


# Hàm valid_expression kiểm tra các ký tự nhập vào:
def valid_expression(character):
    valid_char = "0123456789+-*/^(). "
    for char in character:
        if char not in valid_char:
            return False
    return True


# Hàm evaluate_expression nhận vào một biểu thức Trung tố (tạm gọi là a) để
# chuyển thành biểu thức Hậu tố và đánh giá nó bằng cách gọi hàm infix_to_postfix để thực hiện
# kết quả là một biểu thức Hậu tố hoàn chỉnh được gán cho biến completed_postfix.
# Trả về: Dùng hàm evaluate_postfix để tính toán biểu thức hậu tố đó (completed_postfix)
def evaluate_expression(a):
    completed_postfix = infix_to_postfix(a)
    return evaluate_postfix(completed_postfix)


# Nhập biểu thức và in kết quả
# Cách 1:
def main():
    while True:
        nhapbieuthuc = input('Nhập vào đi, chờ gì nữa! (nhập quit để thoát): ')
        if nhapbieuthuc == "quit":
            break
        elif not valid_expression(nhapbieuthuc):
            print("Biểu thức chứa ký tự không hợp lệ !!!")
            continue
        try:
            ketqua = evaluate_expression(nhapbieuthuc)
            print("Kết quả", nhapbieuthuc, "=", ketqua)
        except ZeroDivisionError:
            print("Nhập lại đi Bro")
main()

# Cách 2:
# while True:
#     nhapbieuthuc = input('Nhập vào đi, chờ gì nữa! (nhập "quit" để thoát): ')
#     if nhapbieuthuc == "quit":
#         break
#     elif valid_expression(nhapbieuthuc):
#         try:
#             result = evaluate_expression(nhapbieuthuc)
#             print('Kết quả', nhapbieuthuc, '=', result)
#         except ZeroDivisionError:
#             print('Nhập lại đi Bro')
#     else:
#         print('Giá trị không hợp lệ !!!')