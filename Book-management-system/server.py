#Flask服务器配置
from BookBP import *
from flask_cors import CORS   #支持跨域访问

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 注册蓝图
app.register_blueprint(bookBP)
app.run(debug=True,port=8888)



#bms数据库建库、建表语句
# 创建数据库
# create database bms charset=utf8;
# 切换数据库
# use bms
# 查看数据库中有哪些数据表
# show tables;
# 创建数据表（字段根据需求去创建）
# create table book(bid int primary key auto_increment, name char(50), price float, summary varchar(50), quantity int);
# 插入数据
# insert into book values("python", 23, "", 12),(5,"Alice",26,"female");