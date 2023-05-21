const conversas = document.getElementById("conversas");
const createChat = (name) => {
    const content = `
    <div class="text">
        <span>
            <strong style="color: #00A86B;">${name}</strong>
        </span>
    </div>
    `;
    conversas.innerHTML += content;
};