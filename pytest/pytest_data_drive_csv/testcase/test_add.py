import pytest
import csv
from pytest_data_drive_csv.func.operation import my_add


# 从data模块中读取csv文件数据
def get_csv():
    """

    :return: 格式： [[1,1,2],[3,6,9],[100,200,300]]
    """
    # 读取csv文件，如果文件内容有中文，需要加上encoding = "utf-8"
    with open("../data/params.csv", 'r', encoding="utf-8") as f:
        raw = csv.reader(f)  # 读取csv格式的文件数据,f表示文件或列表对象，返回迭代器raw；raw为列表类型，可迭代，每次迭代返回的数据类型也是列表
        data = []  # 定义空列表，用于存放读出来的数据
        for line in raw:
            # raw列表中的每一个元素，代表csv文件中的每一行数据，循环读出数据
            data.append(line)

        return data  # [[],[],[]]


# pytest结合数据驱动加载csv文件
class TestWithCsv:
    """
    测试类： 测试pytest结合数据驱动加载csv文件
    """

    @pytest.mark.parametrize("a,b,expected", get_csv())
    def test_my_add(self, a, b, expected):
        assert my_add(int(a), int(b)) == int(expected)
