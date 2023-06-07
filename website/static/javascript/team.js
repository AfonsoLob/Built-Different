$(document).ready(function() {
  const openModalBtn = $('#openModalBtn');
  const openModalBtn2 = $('#openModalBtn2');
  const openModalBtn3 = $('#openModalBtn3');
  const modalClass = $('.modal');
  const modal = $('#modal');
  const modal2 = $('#modal2');
  const modal3 = $('#modal3');

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
    modalClass.css('display', 'none');
  });
});