$(document).ready(function() {
  const openModalBtn = $('#openModalBtn');
  const modal = $('#modal');
  const chatBox = $('#chatBox');
  const closeBtn = $('#close-btn');
  const allChatButton = $('#chatStickyBtn');
  const allChat = $('#allChat');
  const allCloseBtn = $('#close-btn-all');

  openModalBtn.on('click', function() {
    modal.css('display', 'block');
  });

  modal.on('click', function(event) {
    if (event.target === modal[0]) {
      modal.css('display', 'none');
    }
  });

  $(document).on('click', '.chatButton', function() {
    chatBox.css('display', 'block');
    allChat.css('display', 'none');
    modal.css('display', 'none');
  });

  closeBtn.on('click', function() {
    chatBox.css('display', 'none');
  });

  allChatButton.on('click', function() {
    allChat.css('display', 'block');
  });

  allCloseBtn.on('click', function() {
    allChat.css('display', 'none');
  });

  // Handle the form submission event for chatForm
  $(document).on('click', '.chatForm', function(event) {
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
        $('#messages').empty();
        var messages = response.messages;
        for (var i = 0; i < messages.length; i++) {
          var message = messages[i];
          var html = `
            <div>
              <span>
                <strong style="color: #00A86B;"> ${message.name} </strong>: ${message.message} 
              </span>
            </div>`;
          $('#messages').append(html);
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
        $('#conversas').empty();
        var conversations = response.conversations;
        var names = response.names;
        for (var i = 0; i < conversations.length; i++) {
          var conversation = conversations[i];
          var name = names[i];
          var html = `
            <form method="post" action="/team" class="chatForm">
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
