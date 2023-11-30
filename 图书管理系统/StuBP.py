#蓝图配置
from flask import *
from pymysql import *


# 1. 蓝图的声明
stuBP = Blueprint(name="stu", import_name=__name__)
# 连接数据库
db_connect = Connect(host="127.0.0.1", port=3306, user="root", password="123456", database="bms", charset="utf8")


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
    sql_str = ''' select * from book; '''
    cursor.execute(sql_str)
    data = cursor.fetchall()
    datas = []
    for item in data:
        s = {}
        s["bid"] = item[0]
        s["name"] = item[1]
        s["price"] = item[2]
        s["summary"] = item[3]
        s["quantity"] = item[4]

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
        bid = request.values.get("bid")
        name = request.values.get("name")
        price = request.values.get("price")
        summary = request.values.get("summary")
        quantity = request.values.get("quantity")

        sql_str = ''' insert into book (bid, name, price, summary, quantity) values(%s,%s,%s,%s,%s) '''
        cursor = db_connect.cursor()
        cursor.execute(sql_str, [bid, name, price, summary, quantity])
        # 提交更改操作，不提交不生效
        db_connect.commit()
        cursor.close()
        return redirect("/")

# 修改数据接口
@stuBP.route("/change/<bid>", methods=["GET", "POST"])
def change(bid):
    # 根据请求方式区别不同的操作
    if request.method == "GET":
        return render_template("change.html")
    else:
        # 将数据库中的数据找出来修改后再保存到数据库中
        # 将添加提交过来的数据保存到数据库中
        name = request.values.get("name")
        price = request.values.get("price")
        summary = request.values.get("summary")
        quantity = request.values.get("quantity")

        sql_str = ''' update book set name=%s, price=%s, summary=%s, quantity=%s where bid = %s '''
        cursor = db_connect.cursor()
        cursor.execute(sql_str, [bid, name, price, summary, quantity])
        # 提交更改操作，不提交不生效
        db_connect.commit()
        cursor.close()
        return redirect("/")


# 用来返回修改信息时的回显数据
@stuBP.route("/changeData/<bid>")
def changeData(bid):
    cursor = db_connect.cursor()
    sql = '''select * from book where bid = ''' + bid
    cursor.execute(sql)
    item = cursor.fetchone()
    data = {}
    data["bid"] = item[0]
    data["name"] = item[1]
    data["price"] = item[2]
    data["summary"] = item[3]
    data["quantity"] = item[4]

    cursor.close()
    return data


# 删除信息接口
@stuBP.route("/delete/<bid>")
def delete(bid):
    curosr = db_connect.cursor()
    sql = ''' delete from book where bid = %s '''
    curosr.execute(sql, [bid])
    db_connect.commit()
    curosr.close()
    return redirect("/")
