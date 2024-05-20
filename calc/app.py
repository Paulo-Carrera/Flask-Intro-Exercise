#   Put your app in here .
from flask import Flask , request
from operations import add , sub , mult , div

app = Flask(__name__)

# @app.route('/add')
# def addition():
#     a = int(request.args.get('a',0))
#     b = int(request.args.get('b',0))
#     result = add(a,b)
#     return str(result)

# @app.route('/sub')
# def subtraction():
#     a = int(request.args.get('a',0))
#     b = int(request.args.get('b',0))
#     result = sub(a,b)
#     return str(result)

# @app.route('/mult')
# def multiplication():
#     a = int(request.args.get('a',0))
#     b = int(request.args.get('b',0))
#     result = mult(a,b)
#     return str(result)

# @app.route('/div')
# def division():
#     a = int(request.args.get('a',0))
#     b = int(request.args.get('b',0))
#     result = div(a,b)
#     return str(result)






operations = {
    'add' : add ,
    'sub' : sub ,
    'mult' : mult ,
    'div' : div
}

@app.route('/<operation>')
def math_operation(operation):
    a = int(request.args.get('a',0))
    b = int(request.args.get('b',0))
    if operation in operations:
        result = operations[operation](a,b)
        return str(result)
    else:
        return "Error: Invalid Operation", 400