from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_name():
    value_list = ['hihi','hihi1','hoho2']
    return render_template('8_for.html',values = value_list)


if __name__ == "__main__":
    app.run(debug=True)