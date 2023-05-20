var socketio = io();
          
const messages = document.getElementById("messages");
const createMessage = (name, msg) => {
    const content = `
    <div class="text">
        <span>
            <strong style="color: #00A86B;">${name}</strong>: ${msg}
        </span>
    </div>
    `;
    messages.innerHTML += content;
};

socketio.on("message", (data) => {
    createMessage(data.name, data.message);
});

const sendMessage = () => {
    const message = document.getElementById("message");
    if (message.value == "") return;
    socketio.emit("message", { data: message.value });
    message.value = "";
};

document.getElementById('message').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});