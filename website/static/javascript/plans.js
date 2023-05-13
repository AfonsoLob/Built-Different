// select the buttons and lists
const trainingPlanButton = document.getElementById('btn-trainings');
const personalTrainerButton = document.getElementById('btn-personal-trainers');
const trainingPlanList = document.getElementById('training-plans');
const personalTrainerList = document.getElementById('personal-trainers');

// add event listeners to the buttons
trainingPlanButton.addEventListener('click', () => {
    // Toggle is selected
    if(!trainingPlanButton.classList.contains('is-selected')){
        trainingPlanButton.classList.toggle('is-selected');
        trainingPlanList.classList.toggle('is-selected');
        personalTrainerButton.classList.toggle('is-selected');
        personalTrainerList.classList.toggle('is-selected');
    }
});

personalTrainerButton.addEventListener('click', () => {
    // Toggle is selected
    if(!personalTrainerButton.classList.contains('is-selected')){
        trainingPlanButton.classList.toggle('is-selected');
        trainingPlanList.classList.toggle('is-selected');
        personalTrainerButton.classList.toggle('is-selected');
        personalTrainerList.classList.toggle('is-selected');
    }
});
