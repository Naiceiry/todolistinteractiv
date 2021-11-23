from flask import Flask
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
  return flask.jsonify(todos)

# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=3245, debug=True)