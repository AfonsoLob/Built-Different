const playButton1 = document.getElementById('playButton1');
const videoPlayer1 = document.getElementById('videoPlayer1');
const playButton2 = document.getElementById('playButton2');
const videoPlayer2 = document.getElementById('videoPlayer2');
const playButton3 = document.getElementById('playButton3');
const videoPlayer3 = document.getElementById('videoPlayer3');

playButton1.addEventListener('click', function() {
videoPlayer1.setAttribute('allowfullscreen', '');

    // Depending on the Web Browser
    if (videoPlayer1.requestFullscreen) {
        videoPlayer1.requestFullscreen();
    } else if (videoPlayer1.mozRequestFullScreen) {
        videoPlayer1.mozRequestFullScreen();
    } else if (videoPlayer1.webkitRequestFullscreen) {
        videoPlayer1.webkitRequestFullscreen();
    } else if (videoPlayer1.msRequestFullscreen) {
        videoPlayer1.msRequestFullscreen();
    }
});

playButton2.addEventListener('click', function() {
    videoPlayer2.setAttribute('allowfullscreen', '');
    
        // Depending on the Web Browser
        if (videoPlayer2.requestFullscreen) {
            videoPlayer2.requestFullscreen();
        } else if (videoPlayer2.mozRequestFullScreen) {
            videoPlayer2.mozRequestFullScreen();
        } else if (videoPlayer2.webkitRequestFullscreen) {
            videoPlayer2.webkitRequestFullscreen();
        } else if (videoPlayer2.msRequestFullscreen) {
            videoPlayer2.msRequestFullscreen();
        }
});

playButton3.addEventListener('click', function() {
    videoPlayer3.setAttribute('allowfullscreen', '');
    
        // Depending on the Web Browser
        if (videoPlayer3.requestFullscreen) {
            videoPlayer3.requestFullscreen();
        } else if (videoPlayer3.mozRequestFullScreen) {
            videoPlayer3.mozRequestFullScreen();
        } else if (videoPlayer3.webkitRequestFullscreen) {
            videoPlayer3.webkitRequestFullscreen();
        } else if (videoPlayer3.msRequestFullscreen) {
            videoPlayer3.msRequestFullscreen();
        }
});