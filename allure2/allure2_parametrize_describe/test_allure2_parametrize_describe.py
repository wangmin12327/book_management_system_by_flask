import allure
import pytest


# Demo1: allure2 报告中添加用例标题
# @allure.title("参数化用例标题: 参数一: {param1}, 参数二: {param2}")
# @pytest.mark.parametrize("param1, param2, expected", [(1, 1, 2), (0.1, 0.3, 0.4)])
# def test_with_parametrize_title(param1, param2, expected):
#     assert param1 + param2 == expected


# Demo2: allure2 报告中添加用例步骤(适用于流程性测试用例：调用数据库、连接资源等)
# 方法一： 使用装饰器定义一个测试步骤，在测试用例中使用
@allure.step
def simple_step1(step_param1, step_param2=None):
    """
    定义一个测试步骤
    :param step_param1:
    :param step_param2:
    :return:
    """
    print("连接数据库，准备测试数据")
    print(f"步骤1: 打开页面1， 参数1: {step_param1}, 参数2: {step_param2}")


# # 定义测试步骤： simple_step2

@allure.step
def simple_step2(step_param):
    """
    定义一个测试步骤
    :param step_param:
    :return:
    """
    print(f"步骤2：完成搜索 {step_param}功能")


@pytest.mark.parametrize("param1", ["pytest", "allure"], ids=["search pytest", "search allure"])
def test_parameterize_with_id(param1):
    simple_step2(param1)


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step1(param1, param2)


@pytest.mark.parametrize('param2', ['pytest', 'unittest'])
@pytest.mark.parametrize('param1,param3', [[1, 2]])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    simple_step1(param1, param3)
    simple_step2(param2)


# 方法二： 使用" with allure.step() "添加测试步骤
@allure.title("搜索用例")
def test_step_in_method():
    with allure.step("测试步骤一：打开页面"):
        print("操作 a")
        print("操作 b")

    with allure.step("测试步骤二：搜索"):
        print("搜索操作 ")

    with allure.step("测试步骤三：断言"):
        assert True


# Demo3: allure2
# 格式1：添加一个普通的link 链接
@allure.link('https://ceshiren.com/t/topic/15860')
def test_with_link():
    pass


# 格式2：添加一个普通的link 链接，添加链接名称
@allure.link('https://ceshiren.com/t/topic/15860', name='这是用例链接地址')
def test_with_named_link():
    pass


# 格式3：添加用例管理系统链接
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.testcase(TEST_CASE_LINK, '用例管理系统')
def test_with_testcase_link():
    pass


# 格式4：添加bug管理系统链接 这个装饰器在展示的时候会带 bug 图标的链接。可以在运行时通过参数 `--allure-link-pattern`
# 指定一个模板链接，以便将其与提供的问题链接类型链接模板一起使用。执行命令需要指定模板链接：`--allure-link-pattern=issue:https://ceshiren.com/t/topic/{}`
@allure.issue("15860", 'bug管理系统')
def test_with_issue():
    pass
