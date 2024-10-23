import json


def get_json():
    """
     json.loads()，解析一个文本对象，并返回成字典格式
    :return: 返回字典格式
    """
    with open("data/params.json", "r", encoding="utf-8") as f:
        raw = json.loads(f.read())
        print(raw)


def dump_json():
    """
    json.dumps()， 解析一个字典格式对象，并保存为文本格式(即字符串格式)
    :return:
    """
    with open("data/params.json", "r", encoding="utf-8") as f:
        raw = json.loads(f.read())
        res = json.dumps(raw)
        print(type(res))
        print(res)
        f.close()

    with open("data/params.json", "w", encoding="utf-8") as f:
        f.write(res)
        f.close()


if __name__ == '__main__':
    # get_json()
    dump_json()
