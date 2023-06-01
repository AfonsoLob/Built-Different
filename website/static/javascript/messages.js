const socketio = io();

const messages = $("#messages");
const createMessage = (name, msg) => {
    const content = `
    <div class="text">
        <span>
            <strong style="color: #00A86B;">${name}</strong>: ${msg}
        </span>
    </div>
    `;
    messages.append(content);
};

socketio.on("message", (data) => {
    createMessage(data.name, data.message);
});

const sendMessage = () => {
    const message = $("#message");
    if (message.val() === "") return;
    socketio.emit("message", { data: message.val() });
    message.val("");
};

$("#message").on("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
