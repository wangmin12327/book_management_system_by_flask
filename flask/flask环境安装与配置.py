# 导入flask模块
from flask import Flask

# 通过实例化Flask类并传入__name__参数，创建一个Flask应用程序app实例,__name__是一个特殊变量，表示当前模块的名称。
app = Flask(__name__)


# 定义路由和视图函数
# 使用@app.route("/")装饰器定义路由，并指定URL路径
@app.route("/")
# 定义视图函数：用于处理指定URL路径的请求，并将函数的返回结果作为浏览器访问指定URL路径后的显示结果
def hello():
    return "Hello Flask"


if __name__ == "__main__":
    app.run()
