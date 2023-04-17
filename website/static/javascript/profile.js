let submit_btn = document.getElementById('get-weight');
let navLinks = document.getElementsByClassName('nav-link');
let linksArray = Array.from(navLinks);

// submit_btn.addEventListener('click', function(){
//     let weight = document.getElementById('weight').value;
//     document.getElementById('graph').innerHTML = weight;
// })

linksArray.forEach(link => {
    link.addEventListener('click', function(){
        if(!link.classList.contains('active') && link.id != 'settings'){
            document.querySelector('.nav-link.active').classList.toggle('active');
            link.classList.toggle('active');
        }
    })
});