from StuBP import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 注册蓝图
app.register_blueprint(stuBP)
app.run(debug=True,port=8888)



#
# @app.route("/")  #路由的根路径
# def index():
#     return "<h1>Index Page!!</h1>"
#
# @app.route("/list")
# def list():
#     return "<h1>list Page!!</h1>"
#
# @app.route("/news")
# def news():
#     return "<h1>news Page!!</h1>"
#
# #server.run()
# app.run(debug=True)   #debug模式，热启动:不需要重启服务器就可以调试






