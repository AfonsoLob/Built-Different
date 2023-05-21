document.addEventListener('DOMContentLoaded', () => {
  const openModalBtn = document.getElementById('openModalBtn');
  const modal = document.getElementById('modal');
  const chatButton = document.getElementById('chatButton');
  const chatBox = document.getElementById('chatBox');
  const closeBtn = document.getElementById('close-btn');
  const allChatButton = document.getElementById('chatStickyBtn');
  const allChat = document.getElementById('allChat');
  const allCloseBtn = document.getElementById('close-btn-all');

  openModalBtn.addEventListener('click', function() {
    modal.style.display = 'block';
  });

  modal.addEventListener('click', function(event) {
    if (event.target === modal) {
      modal.style.display = 'none';
    }
  });

  if (chatButton) {
    chatButton.addEventListener('click', () => {
      if (chatBox) {
        chatBox.style.display = 'block';
      }
      modal.style.display = 'none';
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      if (chatBox) {
        chatBox.style.display = 'none';
      }
    });
  }

  allChatButton.addEventListener('click', () => {
    allChat.style.display = 'block';
  });

  if (allCloseBtn) {
    allCloseBtn.addEventListener('click', () => {
      if (allChat) {
        allChat.style.display = 'none';
      }
    });
  }

});
