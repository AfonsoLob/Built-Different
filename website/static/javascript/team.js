$(document).ready(function() {
  const openModalBtn = $('#openModalBtn');
  const openModalBtn2 = $('#openModalBtn2');
  const openModalBtn3 = $('#openModalBtn3');
  const modalClass = $('.modal');
  const modal = $('#modal');
  const modal2 = $('#modal2');
  const modal3 = $('#modal3');
  const chatBox = $('#chatBox');
  const closeBtn = $('#close-btn');
  const allChatButton = $('#chatStickyBtn');
  const allChat = $('#allChat');
  const allCloseBtn = $('#close-btn-all');

  openModalBtn.on('click', function() {
    modal.css('display', 'block');
  });

  openModalBtn2.on('click', function() {
    modal2.css('display', 'block');
  });

  openModalBtn3.on('click', function() {
    modal3.css('display', 'block');
  });

  modalClass.on('click', function(event) {
    if (event.target === modalClass[0] || event.target === modalClass[1] || event.target === modalClass[2]) {
      modalClass.css('display', 'none');
    }
  });

  $(document).on('click', '.chatButton', function() {
    $('#messages').text("");
    chatBox.css('display', 'block');
    allChat.css('display', 'none');
    modalClass.css('display', 'none');
  });

  closeBtn.on('click', function() {
    chatBox.css('display', 'none');
  });

  allChatButton.on('click', function() {
    $('#conversas').text("");
    allChat.css('display', 'block');
  });

  allCloseBtn.on('click', function() {
    allChat.css('display', 'none');
  });

  // Handle the form submission event for chatForm
  $(document).on('submit', '.chatForm', function(event) {
    event.preventDefault(); // Prevent default form submission
    var receiver_value = $(this).find('.chatButton').val(); 
  
    // Send the AJAX request
    $.ajax({
      type: 'POST',
      url: '/team',
      data: {
        'receiver_value':  receiver_value
      },
      success: function(response) {
        var messages = response.messages;
        for (var i = 0; i < messages.length; i++) {
          var message = messages[i];
          if (message.name == response.session_user){
            var html = `
              <div class="message_box">
                <span>
                  ${message.message} 
                </span>
              </div>`;
            $('#messages').append(html);
          }
          else {
            var html = `
              <div class="message_box_other">
                <span>
                  ${message.message} 
                </span>
              </div>`;
            $('#messages').append(html);
          }
        }
      }
    });
  });
  

  // Handle the form submission event for conversationsForm
  $(document).on('submit', '#conversationsForm', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Send the AJAX request
    $.ajax({
      type: 'POST',
      url: '/conversations',
      success: function(response) {
        var conversations = response.conversations;
        var names = response.names;
        for (var i = 0; i < conversations.length; i++) {
          var conversation = conversations[i];
          var name = names[i];
          var html = `
            <form method="post" action="/team" class="chatForm" onsubmit="initializeSocketIO()">
              <button type="submit" class="chatButton" value="${conversation}">
                <span>
                  <strong style="color: #00A86B;">${name}</strong>
                </span>
              </button>
              <hr>
            </form>`;
          $('#conversas').append(html);
        }
      }
    });
  });
});
