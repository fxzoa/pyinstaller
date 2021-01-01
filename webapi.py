from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False #ソートをそのまま

@app.route('/')
def hello_get():
    name = request.args.get('name')
    return render_template('hello.html', title='flask test', name=name)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', title='flask test', name=name) 

@app.route('/hello', methods=['POST']) #Methodを明示する必要あり
def hello_post():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name."
    return render_template('hello.html', title='flask test', name=name) 

@app.route('/good')
def good():
    members = [
        { "name": "山田", "email": "yamada@gmail.com" },
        { "name": "渡辺", "email": "watanabe@yahoo.co.jp" }
    ]
    return  render_template('good.html', title='good test', members=members)

@app.route('/json')
def json():
    data = [
        {"name":"山田"},
        {"age":30}
    ]
    return jsonify({
            'status':'OK',
            'data':data
        })

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
