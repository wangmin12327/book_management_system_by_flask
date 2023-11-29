# 蓝图(类，模块，专门用来管理学生管理系统，划分越细，耦合性越低，可维护性越高)
# 是一种组织和管理应用程序路由和视图的机制。它允许开发者将相关功能的路由和视图进行分组，从而更好地组织项目结构和实现模块化开发。
# 蓝图可以极大地简化大型应用并为扩展提供集中的注册入口。
# Flask 可以通过蓝图来组织 URL 以及处理请求。如果使用蓝图，应用会在 Flask 层中进行管理，共享配置，通过注册按需改变应用对象。
# 蓝图的缺点是一旦应用被创建后，只有销毁整个应用对象才能注销蓝图。
#一个项目可以具有多个蓝图。但是一个蓝图并不是一个完整的应用，它不能独立于应用运行，而必须要注册到某一个应用中。
from flask import *
from flask import *
from pymysql import *


# 1. 蓝图的声明
stuBP = Blueprint(name="stu", import_name=__name__)
# 连接数据库
db_connect = Connect(host="127.0.0.1", port=3306, user="root", password="123123123", database="sms", charset="utf8")


# 通过蓝图来管理数据接口

# 首页接口
@stuBP.route("/")
def index():
    return render_template("index.html")

# 首页数据接口
@stuBP.route("/list")
def list():
    # 查询数据库得到所有的数据展示
    # 获取游标对象
    cursor = db_connect.cursor()
    sql_str = ''' select * from student; '''
    cursor.execute(sql_str)
    data = cursor.fetchall()
    datas = []
    for item in data:
        s = {}
        s["sid"] = item[0]
        s["name"] = item[1]
        s["age"] = item[2]
        s["gender"] = item[3]
        datas.append(s)
    cursor.close()
    return datas

# 添加页面接口，和添加数据接口
@stuBP.route("/add", methods=["GET", "POST"])
def add():
    # 根据请求方式区别不同的操作
    if request.method == "GET":
        return render_template("add.html")
    else:
        # 将添加提交过来的数据保存到数据库中
        name = request.values.get("name")
        age = request.values.get("age")
        gender = request.values.get("gender")

        sql_str = ''' insert into student (name, age, gender) values(%s,%s,%s) '''
        cursor = db_connect.cursor()
        cursor.execute(sql_str, [name, age, gender])
        # 提交更改操作，不提交不声效
        db_connect.commit()
        cursor.close()
        return redirect("/")

# 修改数据接口
@stuBP.route("/change/<sid>", methods=["GET", "POST"])
def change(sid):
    # 根据请求方式区别不同的操作
    if request.method == "GET":
        return render_template("change.html")
    else:
        # 将数据库中的数据找出来修改后再保存到数据库中
        # 将添加提交过来的数据保存到数据库中
        name = request.values.get("name")
        age = request.values.get("age")
        gender = request.values.get("gender")
        sql_str = ''' update student set name=%s, age=%s, gender=%s where sid = %s '''
        cursor = db_connect.cursor()
        cursor.execute(sql_str, [name, age, gender,sid])
        # 提交更改操作，不提交不声效
        db_connect.commit()
        cursor.close()
        return redirect("/")


# 用来返回修改信息时的回显数据
@stuBP.route("/chageData/<sid>")
def changeData(sid):
    cursor = db_connect.cursor()
    sql = '''select * from student where sid = ''' + sid
    cursor.execute(sql)
    item = cursor.fetchone()
    data = {}
    data["sid"] = item[0]
    data["name"] = item[1]
    data["age"] = item[2]
    data["gender"] = item[3]
    cursor.close()
    return data


# 删除信息接口
@stuBP.route("/delete/<sid>")
def delete(sid):
    curosr = db_connect.cursor()
    sql = ''' delete from student where sid = %s '''
    curosr.execute(sql, [sid])
    db_connect.commit()
    curosr.close()
    return redirect("/")
