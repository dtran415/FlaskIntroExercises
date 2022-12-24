from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a, b)
    return str(result)

@app.route('/sub')
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a, b)
    return str(result)

@app.route('/mult')
def mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a, b)
    return str(result)

@app.route('/div')
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a, b)
    return str(result)

operators = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

@app.route('/math/<operator>')
def math(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operator](a, b)
    return str(result)