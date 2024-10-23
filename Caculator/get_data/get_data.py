import yaml


class GetData:
    """
    获取数据类： 用于获取测试数据的函数
              get_add_data()：静态方法，获取用于测试add()函数的测试数据
              get_div_data()：静态方法，获取用于测试div()函数的测试数据
    """

    @staticmethod
    def get_add_data():
        """
        获取用于测试add()函数的测试数据
        :return: 返回正常的测试数据：[[1,1,2]]
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/add_data.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_add_data_range_in():
        """
        获取用于测试的数据范围边界内的参数
        :return: 返回数据范围边界内的参数
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/add_data_range_in.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_div_data_range_in():
        """
        获取用于测试的数据范围边界内的参数
        :return: 返回数据范围边界内的参数
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/div_data_range_in.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_data_range_out():
        """
        获取用于测试的超出数据范围的参数
        :return: 返回超出数据范围的参数
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/data_range_out.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_data_type_error():
        """
        获取用于测试的错误数据类型参数
        :return: 返回错误的数据类型参数
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/data_type_error.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_div_data():
        """
        获取用于测试div()函数的测试数据
        :return: 返回正常的测试数据：[[10,5,2]]
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/div_data.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data

    @staticmethod
    def get_zero_division_error():
        """
        获取用于测试div()函数在除数为0的情况下，异常提示ZeroDivisionError,并输出异常提示：除数不能为0
        :return: 返回异常提示ZeroDivisionError,并输出异常提示：除数不能为0
        """
        # 如果yaml文件中有中文，需要加上encoding = "utf-8"
        with open('../data/zero_division_error.yaml', 'r', encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data


