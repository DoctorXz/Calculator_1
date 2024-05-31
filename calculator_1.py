# PUBLIC VERSION FOR REVIEW

# XÁC ĐỊNH MỨC ĐỘ ƯU TIÊN CỦA TOÁN TỬ
def precedence(opt):
    if opt == '+' or opt == '-':
        return 1
    elif opt == '*' or opt == '/':
        return 2
    elif opt == '^':
        return 3
    return 0


# HÀM THỰC HIỆN PHÉP TOÁN:
def run_opt(x, y, opt):
    if opt == '+':
        return x + y
    elif opt == '-':
        return x - y
    elif opt == '*':
        return x * y
    elif opt == '/':
        return x / y
    elif opt == '^':
        return x ** y


# CHUYỂN BIỂU THỨC TRUNG TỐ SANG HẬU TỐ
def infix_to_postfix(infix_expression):
    operator_stack = []      # Ngăn xếp (list) lưu trữ toán tử
    operand_stack = []       # Ngăn xếp lưu trữ toán hạng và kết quả trung gian
    i = 0                    # Khởi tạo biến đếm i xác định vị trí trong biểu thức trung tố infix_expression
    while i < len(infix_expression):
        char = infix_expression[i]
        if char.isdigit():
            num = char
            while i + 1 < len(infix_expression) and infix_expression[i + 1].isdigit():
                i += 1
                num += infix_expression[i]
            operand_stack.append(num)
# (63-64)Tạo vòng lặp để duyệt qua từng ký tự char trong biểu thức infix_expression cho đến khi hết biểu thức
# Phần tử thứ i của infix_expression được gán với biến char
# (65-70): Nếu char là số, khởi tạo chuỗi num (số có 1 hoặc nhiều chữ số) bằng ký tự char, và
# Tạo vòng lặp kiểm tra với 2 điều kiện:
# ĐK1: vị trí tiếp theo (i+1) < độ dài biểu thức infix. Tức là duyệt tới vị trí thứ i+1 cho đến hết biểu thức
# ĐK2: giá trị của phần tử tại vị trí i+1 trong biểu thức infix_expression là số
# Khi 2 điều kiện này True thì i = i+1 (tăng i lên vị trí tiếp theo),
# Rồi thêm phần tử hiện tại đó vào chuỗi num (vì các phần tử ở dạng string nên đây là lệnh thêm vào)
# Kết thúc vòng lặp, thêm chuỗi num đó vào stack toán hạng operand_stack

        elif char == '(':           # Thêm dấu mở ngoặc vào operator_stack
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                operand_stack.append(operator_stack.pop())
            operator_stack.pop()
# Nếu thấy ký tự hiện tại char là ')', thì tạo vòng lặp kiểm tra 2 điều kiện
# ĐK1: operator_stack không rỗng
# ĐK2: Giá trị trên đỉnh operator_stack không phải là '('
# Khi 2 điều kiện trên là True thì lấy ra phần tử trên đỉnh của operator_stack bằng pop()
# và thêm vào operand_stack bằng append(). Nôm na là lấy hết toán tử trong operator_stack chuyển sang
# operand_stack cho đến khi gặp dấu '('
# Khi phần tử còn lại là '(' , loại bỏ dấu '(' ra khỏi operator_stack bằng pop()
# hoàn tất việc xử lý dấu ngoặc và các phần từ giữa dấu '(' và ')'

        else:
            while operator_stack and precedence(operator_stack[-1]) >= precedence(char):
                operand_stack.append(operator_stack.pop())
            operator_stack.append(char)
        i += 1
# 95: Điều kiện còn lại là khi char gặp các ký hiệu toán tử +-*/^
# Tạo vòng lặp với 2 điều kiện:
# ĐK1: operator_stack không rỗng. Nếu rỗng thì push thẳng toán tử đó vào operator_stack
# ĐK2: toán tử ở vị trí đỉnh trong operator_stack có độ ưu tiên cao hơn hoặc bằng char (phần tử trong biểu thức)
# Khi 2 điều kiện này True, thì lấy ra phần tử trên đỉnh operator_stack và thêm vào operand_stack
# Ví dụ như precedence của: (operator_stack[-1] là cộng)  <  của (char là nhân) thì:
# push toán tử đó (char, là dấu nhân) vào operator_stack
# Còn nếu precedence của: (operator_stack[-1] là chia hoặc cộng)  >=  của (char là trừ) thì:
# lấy dấu chia hoặc cộng ra khỏi operator_stack và thêm vào operand_stack. Còn dấu trừ thì bỏ vào operator_stack
# i += 1, tiến lên 1 đơn vị, chuyển sang ký tự tiếp theo để xử lý theo các điều kiện trên

    while operator_stack:
        operand_stack.append(operator_stack.pop())
    return ' '.join(operand_stack)
# Vòng lặp này chuyển các toán tử còn lại trong operator_stack sang operand_stack
# (bằng cách lấy theo thứ tự từ đỉnh của operator_stack) sau khi đã duyệt hết biểu thức
# Đến khi hết biểu thức, vòng lặp không được tiếp tục thực hiện thì
# Kết hợp các phần tử trong operand_stack thành một chuỗi và ngăn cách bằng khoảng trắng


# XỬ LÝ VÀ TÍNH TOÁN BIỂU THỨC HẬU TỐ
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
# (105-110) Nếu item là toán tử thì: lấy ra toán hạng trên đỉnh của stack (dùng biến y để hiểu là
# toán hạng sau cùng) và lấy tiếp toán hạng ngay dưới y, là x.
# Dùng hàm run_opt để tính toán với x, y và toán tử item.
# Kết quả tính được, gán cho biến result, đẩy biến này trở lại stack (là 1 giá trị mới ở đỉnh ngăn xếp)
# Khi duyệt hết các item trong items và xử lý, thì vòng lặp kết thúc
# stack lúc này chỉ có duy nhất 1 giá trị là result.
# Vòng lặp kết thúc, trả về giá trị tại vị trí đầu tiên trong stack, là giá trị result cuối cùng.
# Ví dụ: biểu thức hậu tố là [20 4 2 + * 10 5 / -]
# Push 20 vào stack: [20]
# Push 4 vào stack: [20, 4]
# Push 2 vào stack: [20, 4, 2]
# Gặp toán tử + nên lấy ra 2 (là y) và 4 (là x) rồi thực hiện phép tính + được 6
# Push 6 vào stack: [20, 6]
# Gặp toán tử * nên lấy ra 6 (là y) và 20 (là x), thực hiện phép tính được 120
# Push 120 vào stack: [120]
# Push 5 vào stack: [120, 10]
# Push 5 vào stack: [120, 10, 5]
# Gặp toán tử / nên lấy ra 5 (là y) và 10 (là x), thực hiện phép tính được 2
# Push 2 vào stack: [120, 2]
# Gặp toán tử - nên lấy 2 (là y) và 120 (là x), thực hiện phép tính được 118
# Push 118 vào stack: [118]
# 118 là phần tử tại stack[0], và là kết ủa của biểu thức


# HÀM KIỂM TRA CÁC KÝ TỰ NHẬP VÀO:
def valid_expression(character):
    valid_char = "0123456789+-*/^() "
    for char in character:
        if char not in valid_char:
            return False
    return True


# HÀM TÍNH TOÁN BIỂU THỨC TRUNG TỐ
def evaluate_expression(a):
    completed_postfix = infix_to_postfix(a)
    return evaluate_postfix(completed_postfix)
# Hàm evaluate_expression nhận vào một biểu thức Trung tố (tạm gọi là a) để:
# Gọi hàm infix_to_postfix để thực hiện chuyển biểu thức Trung tố a sang Hậu tố
# Gọi hàm evaluate_postfix để thực hiện tính toán biểu thức Hậu tố hoàn chỉnh (completed_postfix)
# đã được chuyển đổi từ infix_to_postfix(a)


# NHẬP BIỂU THỨC VÀ IN KẾT QUẢ:
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
