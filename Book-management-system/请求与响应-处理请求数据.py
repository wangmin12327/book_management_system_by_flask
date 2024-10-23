from flask import Flask,request
from werkzeug.utils import secure_filename

#创建Flask应用程序实例
app = Flask(__name__)

@app.route('/user')
def get_user():
    #获取URL中的请求参数
    url_param = request.args
    print(url_param)
    #查看获取到的请求参数类型
    print(type(url_param))
    #获取请求参数中的 username 对应的值
    username = url_param.get('username')
    return f'Hello, {username}!'

@app.route('/user/post',methods = ["POST"])
#创建视图函数
def post_user():
#获取post请求方法中的json数据，并解析成字典格式
    dict_data = request.json
#打印解析后的数据类型
    print(dict_data)
#获取指定键username和pwd对应的值
    username = dict_data.get('username')
    pwd = dict_data.get('pwd')
#视图函数处理完数据后的返回值
    return f'username:{username},pwd:{pwd}'

@app.route('/user/put',methods=["PUT"])
#创建视图函数
def put_user():
    dict_data = request.json
    # 打印解析后的数据类型
    print(dict_data)
    # 获取指定键username和pwd对应的值
    username = dict_data.get('username')
    pwd = dict_data.get('pwd')
    # 视图函数处理完数据后的返回值
    return f'username:{username},pwd:{pwd}'

@app.route('/user/login',methods=['POST'])
def post_form_user():
#解析表单数据
    form_data = request.form
#打印request.form的返回值类型
    print(form_data)
#获取form表单中指定字段的值
    username = form_data.get('username')
    password = form_data.get('password')
#返回视图函数处理完请求数据后最终的值
    return f"welcome: {username},{password}!"

#定义接口路由和视图函数
@app.route('/user/upload_files',methods=['POST'])
def post_upload_files():
#解析上传的文件对象数据
    files_data = request.files
#通过指定的键，获取客户端上传文件中的指定文件对象
    file = files_data.get(files_data)
#通过save()方法，将指定文件对象保存在后台服务器的指定路径下，并带上secure_filename()函数
    file.save('./uploads/'+secure_filename(file.filename))
#返回视图函数处理完请求数据后最终的结果
    return f"File {file.filename} has been saved!"

@app.route('/user/upload',methods=['GET','POST'])
def upload_file():
    #获取请求URL
    r_url = request.url
    #获取请求域名
    r_host = request.host
    #获取请求头信息
    r_headers = request.headers
    #获取请求方法
    r_method = request.method
    print(r_url,r_host,r_headers,r_method)
    #获取文件请求体
    r_file = request.files
    #判断请求方法为POST
    if r_method == 'POST':
        #判断请求头中包含Mys-Header字段并且值为Hogwarts
        if r_headers.get('My-Header') == "Hogwarts":
            #保存文件
            f = r_file.get("file")
            f.save('./uploads/'+secure_filename(f.filename))
            return f'File{f.filename} is saved! URL is {r_url},host is {r_host}'
        return f"My-Header is missing!"
    return f"Method is wrong!"

# 运行应用程序
if __name__ == '__main__':
    app.run(debug=True, port=8888)