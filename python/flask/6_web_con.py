from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_html():
    return render_template('6_simple.html')


if __name__ == "__main__":
    app.run(debug=True) 