from bottle import route, run, template, error

@route('/')
def index():
    return template('Hello {{ title }} page!!', title='top')

@route('/hello')
def hello():
    return "Hello Python!"

@route('/add')
def add():
    return template('add.html', title='Hello Python!!', flag=True)

@error(404)
def error404(error):
    return '<h1>404 Page Not found'


run(host='localhost', port=8080, debug=True, reloader=True)
