# 测试my_add方法的测试用例
import pytest
import yaml
from pytest_data_drive_yaml.func.operation import my_add


# 用到yaml文件中的数据时，就需要读取出来

def get_data():
    # 如果yaml文件中有中文，需加上encoding="utf-8
    with open("../data/data.yaml", 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)  # 将yaml文件加载成python对象:[[],[],[]]
    return data


class TestWithYAML:
    @pytest.mark.parametrize('x,y,expected', get_data())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
