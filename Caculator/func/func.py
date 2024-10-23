def setup_module():
    """
    调用func模块的前置条件
    :return:
    """
    pass


class Caculator:
    """
    待测源码:
        计算器类：实现计算器的加法、除法运算
    """
    def __init__(self, a, b):
        """
        初始化实例参数
        :param a: 参与运算的数据a
        :param b: 参与运算的数据b
        """
        self.a = a
        self.b = b

    def setup_class(self):
        """
        调用Caculator模块的前置条件
        :return:
        """
        pass

    def add(self):

        if self.a > 99 or self.a < -99 or self.b > 99 or self.b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return self.a + self.b

    def div(self):
        if self.a > 99 or self.a < -99 or self.b > 99 or self.b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return self.a / self.b

    def teardown_class(self):
        """
        调用Caculator模块结束后的数据清理操作
        :return:
        """
        pass


def teardown_module():
    """
    调用func模块结束后的数据清理操作
    :return:
    """
    pass
