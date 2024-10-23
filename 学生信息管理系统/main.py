def menu():
    """
    菜单
    :return:返回用户输入的编号
    """
    print("****************************************")
    print("*                                学生管理系统                         *")
    print("*              1. 添加新学生信息              *")
    print("*              2. 通过学号修改学生信息                 *")
    print("*              3. 通过学号删除学生信息                 *")
    print("*              4. 通过姓名删除学生信息                 *")
    print("*              5. 通过学号查询学生信息          *")
    print("*              6. 通过姓名查询学生信息          *")
    print("*              7. 显示所有学生信息             *")
    print("*              8. 退出系统                                           *")
    print("****************************************")
    select_op = input("输入编号选择操作：")
    return select_op


def control(select_op, sid_list, name_list, stu_list):
    """
    控制函数：用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
    :param select_op: 输入编号
    :param sid_list: 定义学号空列表，用于判断添加学生信息时，学号是否重复；用于判断修改学生信息时，学号是否存在；用于判断查询学生信息时，学号是否存在；
    :param name_list: 定义姓名空列表，用于判断修改学生信息时，姓名是否存在；用于判断查询学生信息时，姓名是否存在；
    :param stu_list: 定义空列表，用于接收多条学生个人信息记录
    :return: 返回菜单的输出
    """
    if select_op == '1':
        sid = input("请输入新学生学号：")
        name = input("请输入新学生姓名：")
        age = input("请输入新学生年龄：")
        sex = input("请输入新学生性别：")
        add_stu_list = add_stu(sid=sid, exit_sid_list=sid_list, name=name, exit_name_list=name_list, age=age,
                               sex=sex, add_stu_list=stu_list)
        print_all_stu(all_stu_list=add_stu_list)

    elif select_op == '2':
        sid = input("请输入待修改的学生学号：")
        name = input("请输入修改后学生姓名：")
        age = input("请输入待修改后学生年龄：")
        sex = input("请输入待修改后学生性别：")
        alter_stu_list = alter_stu(sid=sid, exit_sid_list=sid_list, alter_stu_list=stu_list, name=name, age=age,
                                   sex=sex)
        print_all_stu(all_stu_list=alter_stu_list)

    elif select_op == '3':
        delete_sid = input("请输入待删除的学生学号：")
        del_stu_list = del_stu_by_sid(del_sid=delete_sid, exit_sid_list=sid_list, del_stu_list=stu_list)
        print_all_stu(all_stu_list=del_stu_list)

    elif select_op == '4':
        delete_name = input("请输入待删除的学生姓名：")
        del_stu_list = del_stu_by_name(del_name=delete_name, exit_name_list=name_list,
                                       exit_sid_list=sid_list, del_stu_list=stu_list)
        print_all_stu(all_stu_list=del_stu_list)

    elif select_op == '5':
        sear_sid = input("请输入待查询的学生学号：")
        sear_stu_by_sid(sear_sid=sear_sid, exit_sid_list=sid_list, sear_stu_list=stu_list)

    elif select_op == '6':
        name = input("请输入待查询的学生姓名：")
        sear_stu_by_name(sear_stu_list=stu_list, exit_name_list=name_list, sear_name=name)

    elif select_op == '7':
        print_all_stu(all_stu_list=stu_list)

    elif select_op == '8':
        exit()


def add_stu(sid, exit_sid_list, name, exit_name_list, age, sex, add_stu_list):
    """
    添加新学生信息：函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
    :param sid: 新学生的学号
    :param exit_sid_list: 已存在的学生学号列表
    :param name: 新学生的姓名
    :param exit_name_list: 已存在的学生姓名列表
    :param age: 新学生的年龄
    :param sex: 新学生的性别
    :param add_stu_list: 待添加的学生个人信息记录列表
    :return: 返回是否添加成功的结果
    """
    while sid in exit_sid_list:
        sid = input("学号不可重复,添加失败,请重新输入学号：")
    else:
        exit_sid_list.append(sid)
    if name not in exit_name_list:
        exit_name_list.append(name)
    stu_ele = {"sid": sid, "name": name, "age": age, "sex": sex}
    add_stu_list.append(stu_ele)
    print("添加成功！")
    return add_stu_list


def alter_stu(sid, exit_sid_list, alter_stu_list, name, age, sex):
    """
    通过学号修改学生信息：参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
    :param sid: 待修改的学生学号
    :param exit_sid_list: 已存在的学生学号列表
    :param alter_stu_list: 待修改的学生个人信息记录列表
    :param name: 待修改的学生姓名
    :param age: 待修改的学生年龄
    :param sex: 待修改的学生性别
    :return: 不存在输出提示，并返回是否修改成功
    """
    while sid not in exit_sid_list:
        sid = input("学号不存在,修改失败，请重新输入学号：")
    for stu_ele in alter_stu_list:
        if stu_ele['sid'] == sid:
            stu_ele['name'] = name
            stu_ele['age'] = age
            stu_ele['sex'] = sex
    print(f"修改成功!")
    return alter_stu_list


def del_stu_by_sid(del_sid, exit_sid_list, del_stu_list):
    """
    通过学号删除学生信息：参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
    :param del_sid: 待删除的学生学号
    :param exit_sid_list: 已存在的学生学号列表
    :param del_stu_list: 待删除的学生个人信息记录列表
    :return:返回是否删除成功
    """
    while del_sid not in exit_sid_list:
        del_sid = input("学号不存在,查询失败，请重新输入学号：")

    for i in reversed(del_stu_list):
        if i['sid'] == del_sid:
            del_stu_list.remove(i)
            exit_sid_list.remove(del_sid)
    print(f"删除成功!")
    return del_stu_list


def del_stu_by_name(del_name, exit_name_list, exit_sid_list, del_stu_list, student_del_list=None):
    """
    通过姓名删除学生信息：参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
    :param del_name: 待删除的学生姓名
    :param exit_name_list: 已存在的学生姓名列表
    :param exit_sid_list: 已存在的学生学号列表
    :param del_stu_list: 待删除的学生个人信息记录列表
    :param student_del_list：已匹配待删除学生姓名的个人信息记录列表
    :return: 返回是否删除成功，并返回删除后的学生个人信息记录列表
    """
    if student_del_list is None:
        student_del_list = []

    while del_name not in exit_name_list:
        del_name = input("姓名不存在,查询失败，请重新输入姓名：")

    student_del_list = [stu_ele for stu_ele in del_stu_list if stu_ele['name'] == del_name]
    for i in student_del_list:
        if i['sid'] in exit_sid_list:
            exit_sid_list.remove(i['sid'])
    for j in reversed(del_stu_list):
        if j['name'] == del_name:
            del_stu_list.remove(j)
    exit_name_list.remove(del_name)
    print("删除成功！")
    return del_stu_list


def sear_stu_by_sid(sear_sid, exit_sid_list, sear_stu_list):
    """
    通过学号查询学生信息：参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
    :param sear_sid: 待查询的学生学号
    :param exit_sid_list: 已存在的学生学号列表
    :param sear_stu_list: 待查询的学生个人信息记录列表
    :return: 不存在输出提示，并返回是否查询成功
    """
    while sear_sid not in exit_sid_list:
        sear_sid = input("学号不存在,查询失败，请重新输入学号：")
    sear_stu_list = [stu_ele for stu_ele in sear_stu_list if stu_ele['sid'] == sear_sid]
    print(f"查询成功！查询当前学号的学生信息为:")
    print(sear_stu_list)


def sear_stu_by_name(sear_name, exit_name_list, sear_stu_list):
    """
    通过姓名查询学生信息：参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否查询成功
    :param sear_name: 待查询的学生姓名
    :param exit_name_list: 已存在的学生姓名列表
    :param sear_stu_list: 待查询的学生个人信息记录列表
    :return:返回存在的学生信息（同名学生全部输出）并返回查询成功 or 返回不存在输出提示，并返回查询失败
    """
    while sear_name not in exit_name_list:
        sear_name = input("姓名不存在,查询失败，请重新输入姓名：")
    sear_stu_list = [stu_ele for stu_ele in sear_stu_list if stu_ele['name'] == sear_name]
    print("查询成功！查询当前姓名的学生信息为：")
    print(sear_stu_list)


def print_all_stu(all_stu_list):
    """
    输出所有学生信息
    :param all_stu_list: 所有学生的个人信息记录列表
    :return:返回所有学生信息
    """
    for stu_ele in all_stu_list:
        return (f"学号：{stu_ele['sid']}\n姓名：{stu_ele['name']}\n年龄：{stu_ele['age']}\n性别：\
{stu_ele['sex']}\n\n")


if __name__ == '__main__':
    # 定义空字典student，用于接收单个学生个人信息
    student = {}

    # 定义空列表，用于接收多条学生个人信息记录
    init_stu_list = []

    # 定义学号空列表，用于判断添加学生信息时，学号是否重复；用于判断修改学生信息时，学号是否存在；用于判断查询学生信息时，学号是否存在；
    init_sid_list = []

    # 定义姓名空列表，用于判断修改学生信息时，姓名是否存在；用于判断查询学生信息时，姓名是否存在；
    init_name_list = []

    SELECT_OP = '0'
    while SELECT_OP != '8':
        SELECT_OP = menu()
        control(select_op=SELECT_OP, stu_list=init_stu_list, sid_list=init_sid_list, name_list=init_name_list)
