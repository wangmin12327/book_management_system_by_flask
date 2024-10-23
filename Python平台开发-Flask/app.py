#Flask环境安装与配置
from flask import Flask

#创建Flask应用程序实例
app = Flask(__name__)

#定义路由和视图函数
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello Flask!'

#接口路由技术
#路由规则
#基本路由
@app.route('/about')
def about():
    return 'About Page'

@app.route('/hogwarts/')
def hello_hogwarts():
    return 'Hello Hogwarts'

#动态路由
@app.route('/user/<username>')
def user():
    return ''
#限定类型路由


if __name__ == '__main__':
    app.run()

