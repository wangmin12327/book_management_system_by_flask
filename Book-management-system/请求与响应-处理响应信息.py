#导入Flask模块
from flask import Flask
#创建Flask应用程序实例
app = Flask(__name__)
#定义接口路由和视图函数
@app.route('/text',methods=["GET"])
def re_text():
#返回文本信息类型的响应结果
    return '返回文本'
@app.route('/Tuple',methods=['GET'])
def re_Tuple():
  #返回元组信息类型的响应结果(响应结果对象/响应状态码/响应头信息)
    return '你好', 200 , {"Engineer":"wang"}
#运行app程序
if __name__ == '__main__':
    app.run()
