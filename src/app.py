from flask import Flask, request, jsonify , json
app = Flask(__name__)

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"

todos = [
  { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#   request_body = request.data
#   print("Incoming request with the following body", request_body)
#   return 'Response for the POST todo'

@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.data
  decoded_object = json.loads(request_body)
  todos.append(decoded_object)
  json_text = jsonify(todos)
  return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  todos.pop(position)
  json_text = jsonify(todos)
  return json_text
# # # Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
