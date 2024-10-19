from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

app.config["MONGO_URI"] = "mongodb://mongo:27017/todos"
mongo = PyMongo(app)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = mongo.db.todos.find()
    result = []
    for todo in todos:
        result.append({'_id': str(todo['_id']), 'text': todo['text']})
    return jsonify(result)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {'text': data['text']}
    result = mongo.db.todos.insert_one(new_todo)
    return jsonify({'_id': str(result.inserted_id), 'text': new_todo['text']})

@app.route('/api/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    mongo.db.todos.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Todo deleted'})
@app.route('/test',methods=['GET'])
def test():
    return jsonify({'message':'API tested successfully..'})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

