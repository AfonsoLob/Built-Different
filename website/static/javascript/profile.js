let navLinks = document.getElementsByClassName('nav-link');
let linksArray = Array.from(navLinks);

let bmi_event = () => {
            const altura = (document.getElementById('altura-input').value)/100;
            const peso = document.getElementById('peso-input').value;
            if(altura > 0 && peso > 0){
                const bmi_input = document.getElementById('bmi-input');
                bmi_input.value = (peso/(altura*altura)).toFixed(1);
                Array.from(document.getElementsByClassName('bmi-category')).forEach(element => {
                    element.classList.remove('active');
                });
                let bmi_category;
                if(bmi_input.value < 18.5){
                    bmi_category = document.getElementById('bmi-underweight');
                }
                else if(bmi_input.value < 25){
                    bmi_category = document.getElementById('bmi-normal');
                }
                else if(bmi_input.value < 30){
                    bmi_category = document.getElementById('bmi-overweight');
                }
                else{
                    bmi_category = document.getElementById('bmi-obese');
                }
                bmi_category.classList.add('active');
            }
    }

window.addEventListener('load', bmi_event)

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

const statsFields = document.getElementsByClassName('stats-value');
const array_statsFields = Array.from(statsFields);


array_statsFields.forEach(statField => {
    if(statField.children.length == 2){
        const inputField = statField.children[0];
        const pencilIcon = statField.children[1];
        pencilIcon.addEventListener('click', () => {
            inputField.disabled = false;
            inputField.select();
        });
        inputField.addEventListener('focusout', bmi_event);
        inputField.addEventListener('focusout', () => {inputField.disabled = true});
    }
});

let stats = document.querySelectorAll('.pstat');

let stat_event = () => {
    const idade = $( "#idade-input" ).val();
    const altura = $( "#altura-input" ).val();
    const peso = $( "#peso-input" ).val();
    const email = $( "#email-input" ).val();
    $.ajax({
        type: "POST",
        url: "/profile",
        data: {
            "email": email,
            "idade": idade,
            "altura": altura,
            "peso": peso,
        },
        error: function(request) {
            if (request.status === 404) {
                alert("Não foi possível alterar os seus dados.")
            }
        }  
    });
};

stats.forEach(element => {
    element.addEventListener('focusout', stat_event);
});