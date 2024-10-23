import openpyxl


def get_excel():
    book = openpyxl.load_workbook("data/params.xlsx")
    sheet = book.active
    # 获取单元格第A列,第1行中的数据
    a_1 = [sheet['A1'].value]
    print(a_1)
    # 获取单元格第C列,第3行中的数据
    c_3 = [sheet['C3'].value]
    print(c_3)
    c_3 = [sheet.cell(column=3, row=3).value]
    print(c_3)

    # 获取单元格从第A列,第1行起，至第C列,第3行止范围内的所有数据
    cells = sheet['A1':'C3']
    # ( (<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>),
    # (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>),
    # (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>) )

    values = []  # 定义一个空列表，用于存放获取出来的文件类容[[],[],[]]
    for row in cells:  # 循环遍历cells元组
        data = []  # 定义一个空列表，用于存放cells元组中每个元素的值
        for cell in row:  # 循环遍历每个元素
            data.append(cell.value)  # 将每个元素中的值存放到data列表中
        values.append(data)  # 将每个data列表存放到values中
    print(values)


if __name__ == "__main__":
    get_excel()
