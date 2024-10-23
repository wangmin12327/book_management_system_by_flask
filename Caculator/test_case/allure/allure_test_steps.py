import allure


# 使用@allure.step封装测试步骤:  "输入数据a、b, 调用add()方法；"
@allure.step
def step1(a, b, expected):
    print(f"测试步骤：输入数据{a}、{b},调用add()方法；预期结果为{expected}")


# 使用@allure.step封装测试步骤:  "输入数据a、b, 调用div()方法；"
@allure.step
def step2(a, b, expected):
    print(f"测试步骤：输入数据{a}、{b},调用div()方法；预期结果为{expected}")


# 使用@allure.step封装测试步骤:  "输入数据a、b, a、b为除int整型、float浮点型、double浮点型以外的其他数据类型,调用add()方法；"
@allure.step
def step3(a, b, expected):
    print(f"测试步骤：输入数据{a}、{b}, {a}、{b}为除int整型、float浮点型、double浮点型以外的其他数据类型,调用add()方法；预期结果为{expected}")
    assert False


# 使用@allure.step封装测试步骤:  "输入数据a、b, a、b为除int整型、float浮点型、double浮点型以外的其他数据类型,调用div()方法；"
@allure.step
def step4(a, b, expected):
    print(f"测试步骤：输入数据{a}、{b}, {a}、{b}为除int整型、float浮点型、double浮点型以外的其他数据类型,调用div()方法；预期结果为{expected}")
    assert False


# 使用@allure.step封装测试步骤:  "输入数据a、b, b=0，调用div()方法；"
@allure.step
def step5(a, b, expected):
    print(f"测试步骤：输入数据{a}、{b}, {b}=0, 调用div()方法；预期结果为{expected}")
    assert False
