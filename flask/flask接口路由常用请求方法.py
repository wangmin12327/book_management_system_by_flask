from flask import Flask

# 创建Flask实例
app = Flask('__NAME__')


# 定义接口路由GET请求方法
@app.route('/',methods=['GET'])
def get():
    return f"Method is GET."

@app.route('/get')
def get_1():
    return f"Method is GET."
# 定义接口路由POST请求方法

@app.route('/post',methods=['POST'])
def POST():
    return f"Method is POST."

@app.route('/put',methods=['PUT'])
def PUT():
    return f"Method is PUT."

@app.route('/delete',methods=['DELETE'])
def delete():
    return f"Method is DELETE."

if __name__ == '__main__':
    app.run()


