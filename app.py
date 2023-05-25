#step one create a virtual enviroment using python -m venv env
#Step two create a flask setup to host the to do list
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
tasks = []


@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == "POST":
    #     task = request.form['task']
    #     tasks.append(task)
    #     return redirect('/')
    if request.method == "POST":
        task = request.form['task']
        if 'remove_task' in request.form:
                task_to_remove = request.form['remove-task']
                tasks.remove(task_to_remove)
        else:
            tasks.append(task)
        return redirect('/')
        

    # if request.method == "POST['complete']":
    #     task = request.form['complete_task']
    #     tasks.remove(task)
    #     return redirect('/')
    return render_template('index.html',tasks=tasks)

# @app.route('/remove', methods=['POST'])
# def remove():
#     task = request.form['task']
#     if task in tasks:
#         tasks.remove(task)
#     return redirect('/')
# @socketio.on('connect')
# def handel_connect():
#     print('Client has connected')
#     send_updates()

# @socketio.on('disconnect')
# def handel_disconnect():
#     print('Client has disconnected')


# @socketio.on('request_updates')
# def handel_request_updates():
#     send_updates()


# @socketio.on('update')
# def handel_updates():
#     send_updates()

# def send_updates():
#     emit('update')

if __name__ == '__main__':
    # socketio.run(app)
    app.run(debug=True)