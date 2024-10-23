import requests

def test_file():
    url = "http://127.0.0.1:8888/user/upload_files"
    file = {'file':open(r"D:\开发项目\flask\uploads\license.txt")}
    r = requests.post(url, files=file)
    assert r.status_code == 200
