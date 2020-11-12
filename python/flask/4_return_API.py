from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/json_test')
def hello_json():
    data = {'name' : 'Aaron', 'family' : 'Byun'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = {'server_name' : '127.0.0.1', 'server_port' : '5500'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host = "127.0.0.1" , port="5500")