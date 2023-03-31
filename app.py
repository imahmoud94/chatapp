from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name= request.form.get('name')
        code = request.form.get('code')
        join=request.form.get("join", False)
        create = request.form.get("create", False)

        if not name:
            return render_template("index.html", error="Please enter a name.")
    return render_template("index.html")


@socketio.on('connect')
def test_connect(auth):
    print('Client connected')
    emit('my response', {'data': 'Connected'})
    
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
   
 


