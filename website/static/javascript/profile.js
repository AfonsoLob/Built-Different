let submit_btn = document.getElementById('get-weight');
let navLinks = document.getElementsByClassName('nav-link');
let linksArray = Array.from(navLinks);

submit_btn.addEventListener('click', function(){
    let weight = document.getElementById('weight').value;
    document.getElementById('graph').innerHTML = weight;
})
linksArray.forEach(link => {
    if(link.id != 'settings'){ // link is not settings
        link.addEventListener('click', function(){
            if(!link.classList.contains('active')){
                document.querySelector('.nav-link.active').classList.toggle('active');
                link.classList.toggle('active');
                let target = link.getAttribute('data-target');
                document.querySelector('.content.is-selected').classList.toggle('is-selected');
                let elTarget = document.getElementById(target);
                elTarget.classList.toggle('is-selected');
            }
        })
    }
    else{ // link is settings
        let settingsLinks = document.getElementsByClassName('dropdown-item');
        let settingsArray = Array.from(settingsLinks);
        settingsArray.forEach(link => {
            link.addEventListener('click', function(){
                document.querySelector('.nav-link.active').classList.toggle('active');
                document.getElementById('settings').classList.toggle('active');
                let target = link.getAttribute('data-target');
                document.querySelector('.content.is-selected').classList.toggle('is-selected');
                let elTarget = document.getElementById(target);
                elTarget.classList.toggle('is-selected');
            })
        })
    }
});