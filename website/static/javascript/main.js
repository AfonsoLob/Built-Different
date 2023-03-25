let emailError = document.getElementById('email-error')
let email = document.getElementById('email')
let passwordError = document.getElementById('password1-error')
let password = document.getElementById('password1')
let confPass = document.getElementById('password2')
let confPassErr = document.getElementById('password2-error')

email.addEventListener("keyup", function(){
    if(!email.value.match(/^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)){
        emailError.innerHTML = "Please enter a valid email.";
        email.style.borderColor = "red"
    }
    else{
        email.style.borderColor = "green"
        emailError.innerHTML = ""
    }
})

password.addEventListener('keyup', function(){
    if(password.value.length < 8 && password.value.length > 0){
        passwordError.innerHTML = "Password must be over 7 characters.";
        password.style.borderColor = "red";
        confPass.style.borderColor = "red";
    }
    else{
        passwordError.innerHTML = "";
    }

    if(password.value.length == 0){

    }
})
confPass.addEventListener('keyup', function(){
    if(password.value == confPass.value && password.value.length > 7){
        password.style.borderColor = "green";
        confPass.style.borderColor = "green";
    }
})