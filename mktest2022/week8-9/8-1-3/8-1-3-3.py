from flask import Flask, request

# 固定写法，获取 Flask 对象
app= Flask(__name__)

@app.route('/', methods=['POST'])
def mypost():
    return 'my post request'


@app.route('/mypost', methods=['POST'])
def mypost2():
    return 'my post request 222'


@app.route('/mypost3/<username>', methods=['POST'])
def mypost3(username):
    print(username)
    return 'mypost3' + ':' + username


@app.route('/mypost4/<username>', methods=['POST'])
def mypost4(username):
    print(username)
    name = request.form['name']
    age = request.form['age']
    print(name)
    print(age)
    return 'mypost4' + ':' + name + ':' + age


@app.route('/mypost5/<username>', methods=['POST'])
def mypost5(username):
    print(username)
    request_data = request.get_json()
    print(request_data)
    print(type(request_data))
    return 'mypost5' + ':' + request_data['name'] + ':' + str(request_data['age'])


if __name__ == '__main__':
    app.run()
