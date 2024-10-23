import pytest
import os

import yaml


# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
# 在conftest.py配置里写方法可以实现数据共享，不需要import导入，可以跨文件共享

# 重写hook函数，修改默认编码unicode格式的测试用例，改为支持中文格式的unicode-escape
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


def pytest_configure(config):
    config.addinivalue_line("markers",
                            "test_normal: mark test functions that test data type errors")
    config.addinivalue_line("markers",
                            "test_data_type_error: mark test functions that test data type errors")
    config.addinivalue_line("markers",
                            "test_data_range: mark test functions that test data type errors")
    config.addinivalue_line("markers",
                            "test_zero_division_error: mark test functions that test data type errors")


# 通过@pytest.fixture实现测试装置以及参数化
@pytest.fixture(scope="session", autouse=True)
def open_caculator():
    print("\n打开计算器app操作")
    yield
    close_caculator()


def close_caculator():
    print("\n关闭计算器app操作")


# 通过pytest_addoption函数实现为第三方插件pytest新增命令行参数 --show, 用于查看测试用例的测试数据
def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    """
    定义第三方插件pytest新增命令行参数 --show，用于查看指定测试用例的测试数据
    :param parser:  命令行组
    :param pluginmanager: 插件管理器
    :return:
    """
    mygroup = parser.getgroup("showtestdatas")  # 通过getgroup函数获取某一组命令
    mygroup.addoption("--show",
                      default="add_data",  # 默认为查看add_data测试用例的测试数据
                      dest="show",
                      help="show the test data of a specified test case")


# 通过@fixture拿到获取到的参数
@pytest.fixture(scope="session")
def cmd_option(request):
    """
    查看指定测试用例的测试数据
    :param request:  参数化
    :return:
    """
    global data_path
    my_file_path = request.config.getoption("--show", default="add_data")
    if my_file_path == "add_data":
        data_path = "../data/add_data.yaml"
    elif my_file_path == "range_in_add_data":
        data_path = "../data/add_data_range_in.yaml"
    elif my_file_path == "range_out_data":
        data_path = "../data/data_range_out.yaml"
    elif my_file_path == "type_error_data":
        data_path = "../data/data_type_error.yaml"
    elif my_file_path == "div_data":
        data_path = "../data/div_data.yaml"
    elif my_file_path == "rang_in_div_data":
        data_path = "../data/div_data_rang_in.yaml"
    elif my_file_path == "zero_division_error":
        data_path = "../data/zero_division_error.yaml"

    with open(data_path, "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)

    return my_file_path, datas
