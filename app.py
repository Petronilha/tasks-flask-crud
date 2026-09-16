from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD 
# Create, Read, Update e Delete

tasks = []
task_id_control = 1

# Create a task
@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message": "Nova tarefa criada com sucesso"})

# Get all tasks 
@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]
  output = {
    "tasks": task_list,
    "total_tasks": len(tasks )
  }
  return jsonify(output)

# Get a specific task  
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())
  return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

if __name__ == "__main__":
  app.run(debug=True)