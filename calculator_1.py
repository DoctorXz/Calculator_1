# PUBLIC VERSION FOR REVIEW

# XÁC ĐỊNH MỨC ĐỘ ƯU TIÊN CỦA TOÁN TỬ
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


# THỰC HIỆN PHÉP TOÁN:
def run_op(x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y
    if op == '^':
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
# Khi kiểm tra ký tự hiện tại char là ')', thì tạo vòng lặp kiểm tra 2 điều kiện
# ĐK1: operator_stack không rỗng
# ĐK2: Giá trị trên đỉnh operator_stack không phải là '('
# Khi 2 điều kiện trên là True thì lấy ra phần tử trên đỉnh của operator_stack bằng pop()
# và thêm vào ngăn xếp toán hạng operand_stack bằng append()
# Sau khi vòng lặp kết thúc thì phần tử còn lại là '(' , operator_stack.pop() sẽ loại bỏ
# dấu '(' khỏi operator_stack, hoàn tất việc xử lý dấu ngoặc và các phần từ giữa dấu '(' và ')'
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                operand_stack.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and precedence(operator_stack[-1]) >= precedence(char):
                operand_stack.append(operator_stack.pop())
            operator_stack.append(char)
        i += 1
    while operator_stack:
        operand_stack.append(operator_stack.pop())
    return ' '.join(operand_stack)


# ĐÁNH GIÁ BIỂU THỨC HẬU TỐ ĐỂ TRẢ VỀ KẾT QUẢ
def evaluate_postfix(expression):
    stack = []
    items = expression.split()
    for item in items:
        if item.isdigit():
            stack.append(int(item))
        else:
            y = stack.pop()
            x = stack.pop()
            result = run_op(x, y, item)
            stack.append(result)
    return stack[0]


def valid_expression(expression):
    valid_char = "0123456789+-*/^() "
    for char in expression:
        if char not in valid_char:
            return False
    return True


def evaluate_expression(a):
    postfix = infix_to_postfix(a)
    return evaluate_postfix(postfix)


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