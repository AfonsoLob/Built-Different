import random
from string import ascii_uppercase
from flask import request, session, render_template, redirect, url_for, Blueprint, jsonify
from flask_socketio import join_room, leave_room, send
from .database import get_username
from .databaseChat import get_chat_id, add_conversation, conversation_exists, get_duplicate_key, get_users
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
        receiver = request.form['receiver_value']
        
        if not get_duplicate_key(email, receiver):
            room = generate_random_code()
            add_conversation(room, email)
            add_conversation(room, receiver)
            add_message(room, username, "Created this chat")
        room = get_duplicate_key(email, receiver)

        session["room"] = room
        return jsonify({'messages': message_conversion(room)})
    
@socketio_functions.route("/conversations", methods=["POST"])
def conversations():
    if request.method == "POST":
        conversations = get_all_conversations()
        return jsonify({'conversations': conversations, 'names': emails_names_conversion(conversations)})

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
    messages = []                 

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

def get_all_conversations():
    email = session.get("user")["email"]
    conversations_id = get_chat_id(email)
    conversations = []
    for conversation_id in conversations_id:
        users_involved = get_users(conversation_id[0])
        for user in users_involved:
            if user[0] != email:
                conversations.append(user[0])
    return conversations

def emails_names_conversion(conversations):
    names = []
    for email in conversations:
        names.append(get_username(email))
    return names
    
