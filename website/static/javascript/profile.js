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

let macro_event = () => {
    const idade = document.getElementById('idade-input').value;
    const altura = (document.getElementById('altura-input').value);
    const peso = document.getElementById('peso-input').value;
    let genero = document.getElementsByClassName('gender is-selected')[0]; // There should be only 1 element with this class (Masculino or Feminino)
    let objetivo = document.getElementsByClassName('objective is-selected')[0];; // There should be only 1 element with this class (Cut, Maintain or Bulk)
    const activity = document.getElementById('activity-level').value;
    if(idade > 0 && altura > 0 && peso > 0 && activity > 0 && genero && objetivo){
        // For men: 10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) + 5 (kcal / day)
        // For women: 10 x weight (kg) + 6.25 x height (cm) – 5 x age (y) -161 (kcal / day)
        // Multiplication: Sedentario (1) = 1.2 ; Atividade Leve (2) = 1.375 ; Atividade Moderada (3) = 1.550 ; Muito Ativo (4) = 1.725 ; Extremamente Ativo (5) = 1.9
        // Weight loss: Reduce by 10-20% ; Weight gain: Add 500 calories ; Weight maintenance: Unchanged
        genero = genero.innerText;
        objetivo = objetivo.innerText;
        let bmr;
        if(genero == 'Masculino'){
            bmr = 10 * peso + 6.25 * altura  - 5 * idade + 5;
        }
        else if(genero == 'Feminino'){
            bmr = 10 * peso + 6.25 * altura  - 5 * idade - 161;
        }
        bmr = bmr * activity;
        if(objetivo == 'Cut'){
            // Reduce by 10%-20%"
            bmr *= 0.9;
        }   
        else if(objetivo == 'Bulk'){
            // Add 500 Calories
            bmr += 500;
        }
        // If objetivo == 'Maintain' the result remains unchanged

        bmr = bmr.toFixed(0);
        const proteinas = ((bmr * 0.3)/4).toFixed(0); // 1g Proteina = 4 Calorias
        const hidratos = ((bmr * 0.4)/4).toFixed(0); // 1g Hidratos = 4 Calorias
        const gorduras = ((bmr * 0.3)/9).toFixed(0); // 1g Gordura = 9 Calorias

        document.getElementById('macrosP-input').value = proteinas + "g"; // Proteinas
        document.getElementById('macrosH-input').value = hidratos + "g"; // Hidratos
        document.getElementById('macrosG-input').value = gorduras + "g"; // Gorduras
    }
}

window.addEventListener('load', () => {
    bmi_event();
    macro_event();
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
        if(option_family == "gender"){
            macro_event();
            const gender = option.innerText;
            const email = $( "#email-input" ).val();
            $.ajax({
                type: "POST",
                url: "/profile",
                data: {
                    'op': '1',
                    'email': email,
                    'gender': gender,
                },
                error: function(request) {
                    if (request.status === 404) {
                        alert("Não foi possível alterar o seu género.")
                    }
                }  
            });
        }
        else if(option_family == "objective"){
            macro_event();
            const objective = option.innerText;
            const email = $( "#email-input" ).val();
            $.ajax({
                type: "POST",
                url: "/profile",
                data: {
                    'op': '2',
                    'email': email,
                    'objective': objective,
                },
                error: function(request) {
                    if (request.status === 404) {
                        alert("Não foi possível alterar o seu objetivo.")
                    }
                }  
            });
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
        inputField.addEventListener('focusout', () => {bmi_event(); macro_event(); inputField.disabled = true});
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
            'op': '0',
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


let activity_level = document.getElementById('activity-level');
let activity_options = Array.from(document.getElementById('activity-level').children)
activity_level.addEventListener('change', () => {
    macro_event();
    const activity_value = $( "#activity-level" ).val();
    const email = $( "#email-input" ).val();

    $.ajax({
        type: "POST",
        url: "/profile",
        data: {
            'email': email,
            'op': '3',
            'activity': activity_value,
        },
        error: function(request) {
            if (request.status === 404) {
                alert("Não foi possível alterar a sua atividade.")
            }
        }  
    });
})