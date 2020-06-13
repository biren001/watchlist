'''
from flask import Flask,escape
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/userbiren/<name>')
def hello(name):
    #return '<h1>Welcome 肖战王一博等明星及其网红ip分享网站 作者：%s </h1><img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1592025812580&di=b31cf73c3c523a8b3e149b5cf579da75&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn10109%2F360%2Fw1200h760%2F20190912%2F09f8-iepyyhh5407999.jpg" width="1000" height="500">' % escape(name)
    #return '<h1>Welcome 肖战王一博等明星及其网红ip分享网站</h1><img src="..//xiao.jpg" width="1000" height="500">'
    return '<h1>Welcome 肖战王一博等明星及其网红ip分享网站 作者：%s' % escape(name)+'<img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1592025812580&di=b31cf73c3c523a8b3e149b5cf579da75&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn10109%2F360%2Fw1200h760%2F20190912%2F09f8-iepyyhh5407999.jpg" width="1000" height="500">' 
'''

from flask import Flask,url_for, escape

# ...
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'