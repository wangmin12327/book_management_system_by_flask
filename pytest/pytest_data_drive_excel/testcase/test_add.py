# 测试my_add方法的测试用例
import openpyxl
import pytest

from pytest_data_drive_excel.func.operation import my_add


# 用到excel文件中的数据时，就需要读取出来
def get_excel():
    # 获取工作薄
    book = openpyxl.load_workbook("../data/params.xlsx")
    # 获取活动行（非空白的）
    sheet = book.active
    # 提取数据，格式：[[1,2,3],[3,6,9],[100,200,300]]
    values = []
    for row in sheet:  # 遍历行
        line = []
        for cell in row:  # 遍历列
            line.append(cell.value)
        values.append(line)
    return values           # [[1,1,2],[3,6,9],[100,200,300]]


class TestWithEXCEL:
    @pytest.mark.parametrize('x, y, expected', get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
