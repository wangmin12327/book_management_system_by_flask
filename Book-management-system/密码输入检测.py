def process_password(input_stream):
    stack = []
    for char in input_stream:
        if char == '<':
            if stack:
                stack.pop()
        else:
            stack.append(char)

    password = ''.join(stack)
    return password

def check_password_requirements(password):
    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    digit_check = any(char.isdigit() for char in password)
    special_char_check = any(not char.isalnum() and not char.isspace() for char in password)

    return length_check and uppercase_check and lowercase_check and digit_check and special_char_check

if __name__ == "__main__":
    input_stream = input().strip()
    password = process_password(input_stream)
    is_valid = check_password_requirements(password)

    print(f"{password},{is_valid}")

# 定义一个输入控制的函数
def input_password(input_str):
    #字符串转换成列表
    list_password = []
    for char in input_str:
        if char == '<':
            list_password.pop()
        else:
            list_password.append(char)
    #列表转换成字符串
    password = ''.join(list_password)
    return password

#定义一个检查密码长度的函数
def check_password_length(password):

    if len(password) >= 8:
        return True
    else:
        return False

if __name__ == '__main__':
    input_str = input().strip()
    password = input_password(input_str)

    #检查密码格式
    check_password_format =  any(char.isupper() for char in password) and any(char.islower() for char in password)\
                             and any(char.isdigit() for char in password)
    check_password_special = any(not char.isalnum() and not char.isspace() for char in password)
    check_password_length = check_password_length(password)

    check_password = False
    if check_password_format and check_password_length and check_password_special:
        check_password = True
    print(f'{password},{check_password}')

def main():
    cells = input().split(",")
    print(cells)
    array = [None] * 26
    for i in range(len(cells)):  #遍历输入的字符串
        array[i] = cells[i][0]
    print(array)

if __name__ == "__main__":
    main()




