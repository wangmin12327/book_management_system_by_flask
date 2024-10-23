from typing import Optional, List

import pytest
import yaml


# @pytest.fixture(scope="function", autouse=True)
# def login():
#     # setup操作，例如输入账号、密码等
#     print("登入操作")
#     token = "abcabcacb"
#     yield token  # 返回一个数值，例如需要返回登录成功的账户，密码，进行其他操作时，需要用到yield
#     # teardown操作，例如清除数据，登出操作等
#     print("登出操作")
#
#
# @pytest.fixture(scope="function", autouse=True)
# def connect_db():
#     print("连接数据库操作")
#     yield
#     print("断开数据库操作")

# 重写hook函数：pytest_runtest_setup,执行测试用例的前置条件
def pytest_runtest_setup(item: "Item") -> None:
    print("hook : setup")


# 重写hook函数：pytest_collection_modifyitems，收集完测试用例之后被调用的hook函数
def pytest_collection_modifyitems(items):
    """
    更改测试用例的编码格式
    :param items: 测试用例，test_开头的函数
    :return:
    """
    print(items)
    # name 用例的名字
    # nodeid 测试用例路径

    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode_escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')


# 重写hook函数：pytest_runtest_teardown,执行测试用例后的操作
def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook : teardown")


# 重写hook函数：pytest_addoption,为 hogwarts 命令定义命令行参数 --env
def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup('hogwarts')  # 通过getgroup函数获取某一组命令
    mygroup.addoption("--env",  # 通过addoption函数为该组命令注册一个命令行选项"--env"
                      default="test",  # 参数的默认值
                      dest='env',  # 存储的变量， 为属性命令，可以使用Option对象访问到这个值，暂时用不到
                      help='set your run env'  # 帮助提示， 参数的描述信息
                      )
    mygroup.addoption("--env1",
                      default="test1",
                      dest='env1',
                      help='set your run env1'
                      )


# 通过fixture拿到定义好的参数
# 针对传入的不同参数完成不同的逻辑处理(例如测试环境和开发环境)
@pytest.fixture(scope='session')
def cmd_option(request):
    global data_path
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        data_path = "datas/test/data.yaml"
    elif myenv == 'dev':
        data_path = "datas/dev/data.yaml"

    with open(data_path) as f:

        datas = yaml.safe_load(f)
    return myenv, datas
