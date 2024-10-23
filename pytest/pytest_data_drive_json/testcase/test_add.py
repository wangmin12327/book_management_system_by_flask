# 测试my_add方法的测试用例
import pytest
import json
from pytest_data_drive_json.func.operation import my_add


# 用到json文件中的数据时，就需要读取出来
def get_json():
    # 读取json文件内容
    with open("../data/params.json", 'r') as f:
        data = json.loads(f.read())  # 将json文件加载成python对象:[[],[],[]]
        return list(data.values())


class TestWithJSON:
    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
