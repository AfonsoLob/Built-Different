import random
from string import ascii_uppercase
from flask import request, session, render_template, redirect, url_for, Blueprint
from flask_socketio import join_room, leave_room, send
from .databaseChat import get_chat_id, add_conversation, conversation_exists, get_duplicate_key
from .databaseMessages import get_messages, add_message

socketio_functions = Blueprint('socket', __name__)

def generate_random_code():
    code = ""
    while True:
        for i in range(8):
            code += random.choice(ascii_uppercase)
        if not conversation_exists(code):
            return code
        
@socketio_functions.route("/team", methods=["POST"])
def chat():
    if request.method == "POST":
        email = session.get("user")["email"]
        username = session.get("user")["username"]
        join = request.form.get('join', False)
        receiver = "algo@gmail.com"                 #TODO: Switch this, giving instant username
        
        if join != False and not get_duplicate_key(email, receiver):
            room = generate_random_code()
            add_conversation(room, email)
            add_conversation(room, receiver)
            add_message(room, username, "Created this chat")
        room = get_duplicate_key(email, receiver)

        session["room"] = room
        return render_template("team.html", messages=message_conversion(room))
    
@socketio_functions.route("/conversations", methods=["POST"])
def conversations():
    if request.method == "POST":
        username = session.get("user")["username"]
        return render_template("team.html", conversas=[username])

def message(data):
    room = session.get("room")
    if not conversation_exists(room):
        return 
    
    content = {
        "name": session.get("user")["username"],
        "message": data["data"]
    }

    sender = session.get("user")["username"]

    add_message(room, sender, data["data"])
    send(content, to=room)

def connect(auth):
    room = session.get("room")
    email = session.get("user")["email"]
    if not room or not email:
        return
    if not conversation_exists(room):
        leave_room(room)
        return
    
    join_room(room)
    if not (room in chat_id_conversion(email)):
        add_conversation(room, email)

def disconnect():
    room = session.get("room")
    leave_room(room)
    if not is_any_user_in_room(room):
        del(room)                       # performance reasons


def message_conversion(room):
    dataMessages = get_messages(room)
    messages = []                       # list of dictionaries with message and sender

    for i in dataMessages:
        content = {}
        content["name"] = i[0]                  # username
        content["message"] = i[1]               # message
        messages.append(content)
    return messages

def chat_id_conversion(email):
    dataChats = get_chat_id(email)
    chats = []                          # list of dictionaries with message and sender

    for i in dataChats:
        chats.append(i[0])
    return chats

def is_any_user_in_room(room):
    from app import socketio                                # Lazy import to avoid circular imports
    clients = socketio.server.manager.rooms.get(room)
    return bool(clients)