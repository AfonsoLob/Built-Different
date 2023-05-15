let navLinks = document.getElementsByClassName('nav-link');
let linksArray = Array.from(navLinks);

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


let el_options = document.getElementsByClassName('option');
let array_options = Array.from(el_options);

array_options.forEach(option => {
    option.addEventListener('click', function(){
        let option_family = option.classList[1]
        let familiar_options = document.getElementsByClassName(option_family)
        for(let i=0; i<familiar_options.length; i++){
            if(familiar_options[i] == option){
                familiar_options[i].classList.add('is-selected');
            }
            else{
                familiar_options[i].classList.remove('is-selected');
            }
        }

    })
});