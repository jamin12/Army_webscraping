from flask import Flask, render_template
app = Flask(__name__)

@app.route('/html_test')
def hello_html():
    return render_template('simple.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port="5500") 