let signUp = document.getElementById('sign-up')

$('#email').on("focusout", function(){
    let emailError = document.getElementById('email-error')
    let email = document.getElementById('email')
    if(!email.value.match(/^[A-Za-z\._\-0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)){
        emailError.innerHTML = "Please enter a valid email.";
        email.style.borderColor = "red"
    }

    else{
        email.style.borderColor = "green"
        emailError.innerHTML = ""
    }
})

$('#password1').on('keyup', function(){
    let passwordError = document.getElementById('password1-error')
    let password = document.getElementById('password1') 
    let confPass = document.getElementById('password2')
    if((password.value.length < 8 && password.value.length > 0)){
        passwordError.innerHTML = "Password must be over 7 characters.";
        password.style.borderColor = "red";
        confPass.style.borderColor = "red";
    }
    else{
        passwordError.innerHTML = "";
    }
    if(password.value != confPass.value){
        password.style.borderColor = "red";
        confPass.style.borderColor = "red";
    }

    if(password.value.length == 0){

    }
})
$('#password2').on('keyup', function(){
    let password = document.getElementById('password1') 
    let confPass = document.getElementById('password2')
    let confPassErr = document.getElementById('password2-error')
    if(password.value == confPass.value && password.value.length > 7){
        password.style.borderColor = "green";
        confPass.style.borderColor = "green";
        confPassErr.innerHTML = "";
    }
    else{
        password.style.borderColor = "red";
        confPass.style.borderColor = "red";
        confPassErr.innerHTML = "";
    }
})