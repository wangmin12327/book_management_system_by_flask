import json


def get_data():
    """
    从Yaml文件中获取测试数据
    1、打开yaml文件，导出测试数据
    :return: 测试数据
    """
    with open("../data/test_data.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
        print(list(data.values()))
        return list(data.values())
