from flask import Flask, request
import Jump

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        jump_time = request.form['Time']
        Jump.jump(jump_time)
    else:
        Jump.screencap()
    with open('./index.html','r') as f:
        index = f.read()
    return index

@app.route('/screen.png')
def downScreenshot() :
    with open('./screen.png','rb') as f:
        img = f.read()
    return img

#用request获取form信息，form表单使用一个单行文本输入框并绑定一个滑动条

if (__name__ == "__Jump__") :
    app.run()