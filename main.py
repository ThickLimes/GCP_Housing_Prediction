from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
