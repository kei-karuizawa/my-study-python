from flask import Flask, request

# 固定写法
app = Flask(__name__)

# 一个接口，没有任何参数
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/hello')
# def hello_world2():
#     return 'Hello World2!'
#
#
# @app.route('/hello/<username>')
# def hello_world3(username):
#     print(username)
#     return 'Hello World3' + username


@app.route('/hello/args/<username>')
def hello_world4(username):
    print(username)
    key = request.args.get('key')
    value = request.args.get('value')
    print(key)
    print(value)
    return 'Hello World4' + ':::' + key + ':::' + value


if __name__ == "__main__":
    app.run()