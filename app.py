from flask import Flask, request, json
app = Flask(__name__)


@app.route('/')
def bismillah():
    return "Bismillah Project"



@app.route('/request-methods', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def requestMethods():
    if request.method == 'POST':
        return "POST REQUEST"
    elif request.method == 'PATCH':
        return "PATCH REQUEST"
    elif request.method == 'DELETE':
        return "DELETE REQUEST"
    else:
        return "GET REQUEST"


@app.route('/something')
def something():
    return "Something"


@app.route('/form-data', methods = ['POST'])
def formData():
    return request.form['username'] + " " + request.form['password']


@app.route('/json-data', methods = ['POST'])
def jsonData():
    json_data = request.get_json()
    return json_data['username'] + " " + json_data['password']

@app.route('/json-data-to-json', methods = ['POST'])
def jsonDataToJson():
    json_data = request.get_json()
    return json.dumps(json_data)








if __name__ == '__main__':
    app.run(port=8088)