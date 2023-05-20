var openModalBtn = document.getElementById('openModalBtn');
var modal = document.getElementById('modal');
var modalContent = document.querySelector('.modal-content');

openModalBtn.addEventListener('click', function() {
  modal.style.display = 'block';
  chatBox.style.display = 'none';
});

modal.addEventListener('click', function(event) {
  if (event.target === modal || event.target === modalContent) {
    modal.style.display = 'none';
  }
});

const chatButton = document.getElementById('chatButton');
const chatBox = document.getElementById('chatBox');
const closeBtn = document.getElementById('close-btn');

chatButton.addEventListener('click', () => {
  chatBox.style.display = 'block';
  modal.style.display = 'none';
});

closeBtn.addEventListener('click', () => {
  chatBox.style.display = 'none';
});