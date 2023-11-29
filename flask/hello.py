#1、导入Flask模块
from flask import Flask

#2、创建Flask应用程序实例
app=Flask(__name__)#实例化传参__name__==__main__,app是flask的一个实例化对象

#添加路由
#https://ceshiren.com/search?q=appium
#https---协议
#ceshiren.com---host域名
#search---路由
#?q=appium-----请求参数
@app.route("/")#"/"表示定义的路由地址为根路径，通过路由地址给后端服务发送请求，后端服务会将请求映射到对应的业务逻辑（函数方法），业务逻辑执行完成后会有一个返回结果，并显示到浏览器上
def hello_world():
	return"<p>Hello,World!</p>"

@app.route("/demo")#"/"表示定义的路由地址为根路径，通过路由地址给后端服务发送请求，后端服务会将请求映射到对应的业务逻辑（函数方法），业务逻辑执行完成后会有一个返回结果，并显示到浏览器上
def keepmoving():
	return"<p>keepmoving!</p>"

@app.route("/测试开发")#"/"表示定义的路由地址为根路径，通过路由地址给后端服务发送请求，后端服务会将请求映射到对应的业务逻辑（函数方法），业务逻辑执行完成后会有一个返回结果，并显示到浏览器上
def test():
	return"<p>测试开发</p>"
#代码调用
if __name__=='__main__':
	app.run()
#在本地开发服务器上运行应用程序,flask服务启动起来
#轮询等待的方式,等待浏览器发来请求
#会一直接受请求，直到程序停止