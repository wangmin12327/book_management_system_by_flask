from time import sleep

import allure
import pytest
import requests
import sys


# Demo1: pytest 测试用例的基本结构


# def inc(x):
#     """
#        自定义测试规则
#     :param x:
#     :return:
#     """
#     return x + 1
#
#
# def test_answer():  # 文件名/方法/函数 以test_开头
#     # 测试步骤1
#     # 测试步骤2
#     # ...
#     pass
#     # 断言   实际结果 对比 预期结果
#     assert inc(3) == 5


# Demo2: pytest 类级别的测试用例示例

# class TestXXX:
#     def setup(self):
#         #  资源准备 ：测试用例的前置条件
#         pass
#
#     def test_xxx(self):
#         #  测试用例步骤
#         # 预期结果判断
#         pass
#
#     def teardown(self):
#         # 资源销毁  ：测试用例结束后资源销毁
#         pass


# Demo3: pytest 断言的用法示例
# def test_a():
#     # assert <布尔表达式>
#     assert True
#
#
# def test_b():
#     a = 1
#     b = 2
#     c = 3
#     # assert  <布尔表达式>,<描述>
#     assert a + b == c, f"{a}+{b}={c},结果为真"
#
#
# def test_c():
#     # assert <表达式>
#     a = 1
#     b = 1
#     c = 2
#     assert 'abc' in "abcd"
#
#
# def test_plat():
#     # assert <表达式>
#     assert ('linux' in sys.platform), "该代码只能在Linux下执行"


# Demo4: pytest测试框架结构(setup/teardown)
# setup： 测试用例的前置条件
# teardown： 测试用例结束的后置工作


# pytest  "setup  +   类外函数   +  teardown"  框架结构的测试装置 Demo


# def setup_module():
#     """
#        模块级别的setup，只被执行一次，在测试模块被调用前执行
#     :return:
#     """
#     print("\n资源准备：setup module")
#
#
# def setup_function():
#     """
#        方法级别的setup, 在每次类外函数test_case1()调用前，都会执行一次setup_function()
#     :return:
#     """
#     print("资源准备：setup function")
#
#
# def test_case1():
#     """
#        pytest框架中的类外函数，需要以test_开头命名
#     :return:
#     """
#     print("case1")
#
#
# def teardown_function():
#     """
#        方法级别的teardown, 在每次类外函数test_case1()调用后，都会执行一次teardown_function()
#     :return:
#     """
#     print("资源销毁：teardown function")
#
#
# def teardown_module():
#     """
#        模块级别的teardown，只被执行一次，在测试模块结束测试后执行
#     :return:
#     """
#     print("资源销毁：teardown module")


# pytest  "setup  +   类内函数   +  teardown"  框架结构的测试装置 Demo

# class TestDemo:
#     """
#     pytest的测试类，类名命名规则以Test开头
#     """
#
#     @staticmethod
#     def setup_class(self):
#         """
#         类级别的setup，只被执行一次，在测试类被调用之前执行
#         :return:
#         """
#         print("\n资源准备：setup_class")
#
#     @staticmethod
#     def setup_method(self):
#         """
#         类内方法级别的setup，能被执行多次，在每次类内方法被调用之前执行
#         :return:
#         """
#         print("\n资源准备：setup_method")
#
#     def test_case2(self):
#         """
#         pytest框架中的类内方法，需要以test_开头命名
#         :return:
#         """
#         pass
#
#     def test_case3(self):
#         """
#         pytest框架中的类内方法，需要以test_开头命名
#         :return:
#         """
#         pass
#
#     @staticmethod  # 类中静态方法，无参调用
#     def teardown_method(self):
#         """
#         类内方法级别的teardown，能被执行多次，在每次类内方法被调用之后执行
#         :return:
#         """
#         print("\n资源销毁：teardown_method")
#
#     @staticmethod
#     def teardown_class(self):
#         """
#         类级别的teardown，只被执行一次，在测试类被调用之后执行
#         :return:
#         """
#         print("资源销毁：teardown_class")


# Demo5: pytest参数化用例实现方法
# 通过参数的方式传递数据，从而实现数据和脚本分离
# 并且可以实现用例的重复生成与执行
#
# 普通测试用例方法 VS 参数化应用场景
# 测试场景-登录：
#   测试登录成功，登录失败(账号错误，密码错误)
#   创建多种账号：中文账号，英文账号
# 1、普通测试用例方法
#   需要复制多份代码或者读入参数
#   一次性执行多个输入参数
# def login(username, password):
#     if username == 'right' and password == 'right':
#         return True
#     else:
#         return False
#
#
# def test_param_login_ok():
#     # 登录成功
#     username = "right"
#     password = "right"
#     login(username, password)
#
#
# def test_param_login_fail():
#     # 登录失败
#     username = "wrong"
#     password = "wrong"
#     login(username, password)


# 2、参数化应用场景
#  用pytest参数化实现：
# @pytest.mark.parametrize
# @pytest.mark.parametrize("username,password", [['right', 'right'], ['wrong', 'wrong']])
# def test_param(username, password):
#     """
#     测试登录用户账号、密码
#     :param username: 用户名
#     :param password: 密码
#     :return: 登录结果
#     """
#     login(username, password)
#     if username == 'right' and password == 'right':
#         assert login(username, password) == True
#     else:
#         assert login(username, password) == False


# Demo6: pytest单参数，参数化用例：将实际结果数据放在列表中，赋值给单参数后，进行判断
# search_list = ['select', 'delete', 'add']
#
#
# @pytest.mark.parametrize('name', search_list)
# def test_search(name):
#     assert name in search_list


# Demo7: pytest多参数，参数化用例，修改别名，处理中文字符乱码，以笛卡尔积形式参数化用例:
# 将实际测试用例数据和预期结果数据放在列表嵌套元组中
# 或者将实际测试用例数据和预期结果数据放在列表嵌套列表中
# 通过ids将列表中表达式修改为中文别名
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7+5", 12)],
#                          ids=["3和5相加", "2和5相加", "7和5相加"])
# def test_mark_more(test_input, expected):
#     assert eval(test_input) == expected


# 创建conftest.py文件，将下面内容添加进去，运行脚本:
# 将用例名name和用例标识nodeid的中文信息显示在控制台上
# def pytest_collection_modify_items(items):
#     for i in items:
#         i.name = i.name.encode('utf-8').decode('unicode_escape')
#         i._nodeid = i.nodeid.encode('utf-8').decode('unicode_escape')


# pytest以笛卡尔积形式参数化用例
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
#
#
# @pytest.mark.parametrize("b", b)
# @pytest.mark.parametrize("a", a)
# def test_paraml(a, b):
#     print(f"笛卡尔积形式的参数化结果为a={a},b={b}")


# Demo8: pytest标记测试用例，并在控制台console上只打印标记好的测试用例
# 场景：只执行符合要求的某一部分用例，可以把一个web项目划分多个模块，然后指定模块名称执行
# 解决：在测试用例的方法上（注意：不是被测函数）加@pytest.mark.标签名

# def login(username, password):
#     """
#     测试登录用户账号、密码
#     :param username: 用户名
#     :param password: 密码
#     :return: 登录结果
#     """
#     login(username, password)
#     if username == 'right' and password == 'right':
#         assert login(username, password) == True
#     else:
#         assert login(username, password) == False
#
#
# @pytest.mark.login_demo
# @pytest.mark.parametrize('username,password,expected',
#                          [['Administrator', 'usename123', 'Administrator' + 'usename123']])
# def test_login(username, password, expected):
#     assert username + password == expected


# 执行：在console控制台执行，-m 执行自定义标记的相关用例
#    pytest -s pytest_demo.py -m=login_demo
#
# Demo9: pytest设置始终跳过 @pytest.mark.skip 标记的测试用例
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
#
#
# @pytest.mark.skip
# @pytest.mark.parametrize("a", a)
# @pytest.mark.parametrize("b", b)
# def test_paraml(a, b):
#     print(f"笛卡尔积形式的参数化结果为a={a},b={b}")


# Demo10: pytest设置遇到特殊情况跳过跳过 @pytest.mark.skip 标记的测试用例、设置预期失败的测试用例
# @pytest.mark.skipif
# @pytest.mark.login_demo
# @pytest.mark.parametrize('username,password,expected',
#                          [['Administrator', 'usename123', 'Administrator' + 'usename123']])
# def test_login(username, password, expected):
#     assert username + password == expected


# Demo11: pytest设置预期失败的(即使用例失败了也不会报异常)被 @pytest.mark.xfail 标记的测试用例
# @pytest.mark.xfail
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7+5", 12)],
#                          ids=["3和5相加", "2和5相加", "7和5相加"])
# def test_mark_more(test_input, expected):
#     assert eval(test_input) == expected


# Demo12: pytest运行多条测试用例
# 运行包下所有测试用例：pytest 包名 , 将执行包中所有以test_开头的函数
# 执行单独一个pytest模块：pytest 文件名.py
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
#
#
# class TestDemo:
#     @pytest.mark.parametrize("a", a)
#     @pytest.mark.parametrize("b", b)
#     def test_paraml(self, a, b):
#         print(f"笛卡尔积形式的参数化结果为a={a},b={b}")


# 运行某个模块里面某个类(在某个模块的路径下执行命令)：pytest 文件名.py::类名
# 运行某个模块里面某个类中的方法(在某个模块的路径下执行命令)：pytest 文件名.py::类名::方法名
#
# Demo13: pytest测试用例调度与运行
# 命令行参数-使用缓存状态
# -if(--last-failed)只重新运行故障
# -ff(--failed-first)先运行故障，然后再运行其余的测试


# Demo14: pytest常用命令行参数
# --help
# -x 用例一旦失败(fail/error),就立刻停止
# --maxfail=num 最大失败用例达到个数
# -m 标记用例
# -k 执行包含某个关键字的测试用例
# -v 打印详细日志
# -s 打印输出日志(一般-vs一起使用)
# –collect-only (测试平台，pytest 自动导入功能)
#
#
# Demo15: Python代码执行pytest
# 使用main函数
# 使用python -m pytest 调用pytest(jenkins持续集成用到)
# def main():
#     assert True
#
#
# if __name__ == '__main__':
#     # 1、运行当前目录下所有符合规则的用例，包括子目录(test_*.py 和 *_test.py)
#     pytest.main()
#     # 2、运行test_mark1.py::test_dkej模块中的某一条用例
#     pytest.main(['test_mark1.py::test_dkej', '-vs'])
#     # 3、运行某个标签
#     pytest.main(['test_mark1.py', '-vs', '-m', 'dkej'])


# console控制台运行方式
#    `python test_*.py`


# Demo16: pytest常用的异常处理方法
# try ... except
# pytest.raise()

# 异常处理方法try...except
# try:
# 可能产生异常的代码块
# except Error1, Error2, ... as e:
# 处理异常的代码块1
# except Error3, Error4, ... as e:
# 处理异常的代码块2
# except Exception:
# 处理其他异常

# 异常处理方法pytest.raise()
# 可以捕获特定的异常
# 获取捕获的异常的细节(异常类型，异常信息)
# 发生异常，后面的代码将不会被执行
# def test_raise():
#     with pytest.raises(ValueError, match='must be 0 or None'):
#         raise ValueError("value must be 0 or None")
#
#
# def test_raise1():
#     with pytest.raises(ValueError) as exc_info:
#         raise ValueError("value must be 42")
#     assert exc_info.type is ValueError
#     assert exc_info.value.args[0] == "value must be 42"


# Demo17: pytest结合数据驱动YAML
# Demo18: pytest结合数据驱动excel
# Demo19: pytest结合数据驱动csv
# Demo20: pytest结合数据驱动json

# Demo21: pytest Fixture在自动化中的应用-基本用法
# @pytest.fixture(scope="module")  # fixture只在模块被调用时生效一次
# def login():
#     print("完成登录操作")
#
#
# def test_cart(login):
#     print("购物车")


# Demo22: pytest Fixture在自动化中的应用-作用域
# @pytest.fixture(scope="class")  # fixture只在类被调用时生效一次
# def login_area():
#     print("完成登录操作")
#
#
# class TestFixture:
#
#     def test_search(self, login_area):
#         print("搜索")
#
#     def test_order(self, login_area):
#         print("下单功能")


# Demo23: pytest Fixture在自动化中的应用-yield
"""
@pytest.fixture(scope="function")
def login():
    #setup操作，例如输入账号、密码等
    token = "abcabcacb"
    yield token   # 返回一个数值，例如需要返回登录成功的账户，密码，进行其他操作时，需要用到yield
    #teardown操作，例如清除数据，登出操作等
"""

# @pytest.fixture(scope="function")
# def login_yield():
#     # setup操作
#     token = "abcabcacb"
#     yield token  # yield 返回值  ； 相当于 return 返回值
#     # teardown操作
#     print("\n登录操作")
#
#
# def test_cart(login_yield):
#     print("购物车")

# Demo24: pytest 数据共享(conftest.py文件)
# def test_cart(login, connect_db):
#     print("购物车")
#
#
# def test_order(login, connect_db):
#     print("下单命令")

# Demo25: pytest 自动应用(conftest.py文件中的login函数前使用 @pytest.fixture(scope="function", autouse=True))
# def test_cart():  # 由于使用了自动应用 autouse=True ， 因此，函数调用fixture修饰的函数时，不需要传参也能生效
#     print("购物车")
#
#
# def test_order():
#     print("下单命令")

# Demo26: pytest fixture参数化
# @pytest.fixture(params=[["selenium", 123], ["appium", 123456]])
# def login(request):  # request为pytest内置的fixture函数，通过request
#     print(f"用户名：{request.param}")
#     return request.param
#
#
# def test_demo(login):
#     print(f"\ndemo:数据为：{login}")


# Demo27: pytest pytest.ini文件：测试用例配置文件
# 改变运行规则：执行以check_和test_开头的文件、执行所有的以Test和Check开头的类、执行所有以test_和check_开头的方法
# 添加默认参数：addopts = -v -s --alluredir = ./results
# 指定/忽略执行目录
# 配置日志

# Demo28: pytest pytest.ini文件：测试用例配置文件

# Demo29: pytest 测试用例并行与分布式并发执行
# def test_foo():
#     sleep(1)
#     assert True
#
#
# def test_bar():
#     sleep(1)
#     assert True
#
#
# def test_bar1():
#     sleep(1)
#     assert True
#
#
# def test_bar2():
#     sleep(1)
#     assert True
#
#
# def test_bar3():
#     sleep(1)
#     assert True
#
#
# def test_bar4():
#     sleep(1)
#     assert True
#
#
# def test_bar5():
#     sleep(1)
#     assert True


# Demo30: pytest 内置插件hook体系

# def test_hook():
#     print("password\n")

# Demo31: 编写插件-修改默认编码（该Demo只包含测试用例名称和测试用例路径）
# 1、修改测试用例名字
# 2、修改测试用例路径

# @pytest.mark.parametrize('name', ['张三', '李四'])
# def test_name(name):
#     print(f"name:{name}")


# Demo32: 编写插件-添加命令行参数
# def test_addoption(cmd_option):
#     print(cmd_option)


# Demo33: 打包发布
