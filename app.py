from flask import Flask, request, jsonify
from models.task import Task

# __name__ = __main__
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

# Create tasks
@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control ,title=data["title"], description=data.get("description",""))
  task_id_control += 1
  tasks.append(new_task)
  print(tasks)
  return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
  
  task_list = [task.to_dict() for task in tasks]
  output = {
    "tasks": task_list,
    "total_tasks": len(tasks)
  }
  
  return jsonify(output)

# Get task by ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
  
  for t in tasks:
    if t.id == id:
      return jsonify(t.to_dict())
    
  return jsonify({'message': 'Essa tarefa nao existe!'}), 404

# Update task by ID
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
  
  task = None
  data = request.get_json()
  for t in tasks:
    if t.id == id:
      task = t
      break
      
    
  if task == None:
    return jsonify({'message': 'Nao foi possivel encontrar atividade'}), 404
    
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  
  return jsonify({'message': 'Tarefa atualizada com sucesso'})

# Delete task by ID
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
  
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break
  
  if not task:
    return jsonify({'message': 'Nao foi possivel encontrar atividade'}), 404

  tasks.remove(task)
  return jsonify({"message": "Tarefa deletada com sucesso"})


if __name__ == "__main__":
  app.run(debug=True)