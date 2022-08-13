from app import app
from flask import render_template, url_for, request, redirect
from app.models import Task, db

@app.route('/', methods=['GET','POST'])
def index():
    tasks = Task.query.all()
    if request.method == 'POST':
        task_name = request.form['task_name']
        task = Task()
        task.name = task_name
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/')
        except:
            return "Could not create task {}".format(task)
    else:
        return render_template('index.html', tasks=tasks)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.name = request.form['task_name']  
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Could not update the task {}".format(task.id)
    else:
        return render_template('update.html', task=task)
    
@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    if task:
        try:
            db.session.delete(task)
            db.session.commit()
            return redirect('/')
        except:
            return "Could not update the task {}".format(task.id)    
    else:
        return redirect('/')

    
    
