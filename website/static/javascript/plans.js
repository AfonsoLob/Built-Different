let inputTreino = document.getElementById('inputSelectTreino');
let inputSets, button_post;
if(inputTreino){
    inputTreino.addEventListener('click', inputTreinoEvent);

    inputSets = document.getElementById('inputSelectSets');
    inputSets.addEventListener('click', inputSetsEvent);

    button_post = document.getElementById('post-plan');
    button_post.addEventListener('click', postPlan);
}

let array_savePlans = Array.from(document.getElementsByClassName('guardar-plano'));
array_savePlans.forEach(savePlan_btn => {
    savePlan_btn.addEventListener('click', savePlan)
});



// Functions
function inputTreinoEvent() {
    let treino = document.getElementById('inputSelectTreino');

    // Validate Training Category
    if(Number.isInteger(parseInt(treino.value))) {
        const treino_value = treino.value;
        treino = treino.textContent.replace(/[\n\r]+|[\s]{2,}/g, ' ').trim().split('  ');
        treino = treino[parseInt(treino_value)].slice(10).toLowerCase();
        
        // All Exercises Selectores
        let exercises_options = Array.from(document.getElementsByClassName('select-exercicio'));
        
        exercises_options.forEach(exercise_selector => {
            let options = Array.from(exercise_selector.children);
            options.forEach(children => {
                if(children.classList.contains(`ex-${treino}`) == false)
                    children.hidden = true;
                else
                    children.hidden = false;
            });
        });
    }
}
function inputSetsEvent() {
    let value = inputSets.value;
    let inputGroup = document.getElementById('inputGroupSetsReps');
    inputGroup.innerHTML = ``

    for (let i = 0; i < value; i++) {
        inputGroup.innerHTML += `
        <span class="input-group-text" id="repSet${i+1}">S${i+1}</span>
        <input type="text" class="form-control set-rep" placeholder="Rep Qty" title="Repetition Quantity" aria-label="Exercise Repetitions" aria-describedby="repSet${i+1}">
        `
    }
}

function postPlan() {
    let valid_treino, valid_number_of_sets, valid_exercises;
    let exercises_list = []
    let descansos_list = []
    let sets_reps = []

    let treino = document.getElementById('inputSelectTreino');
    let number_of_sets = document.getElementById('inputSelectSets');
    let tipo = document.getElementById('inputSelectTipo').textContent.replace(/[\r]+|[\s]{2,}/g, ' ').trim().split(' ');
    let dificuldade = document.getElementById('inputSelectDificuldade').textContent.replace(/[\r]+|[\s]{2,}/g, ' ').trim().split(' ');
    const tipo_value = document.getElementById('inputSelectTipo').value;
    const dificuldade_value = document.getElementById('inputSelectDificuldade').value;
    tipo = tipo[parseInt(tipo_value)-1];
    dificuldade = dificuldade[parseInt(dificuldade_value)-1];

    // Validate Training Category
    if(Number.isInteger(parseInt(treino.value))) {
        const treino_value = treino.value;
        treino = treino.textContent.replace(/[\n\r]+|[\s]{2,}/g, ' ').trim().split('  ');
        treino = treino[parseInt(treino_value)];
        valid_treino = true;
    }
    // Validate Number of Sets (and number of reps per set)
    if(Number.isInteger(parseInt(number_of_sets.value))) {
        valid_number_of_sets = true;
        let sets = document.getElementById('inputGroupSetsReps').getElementsByClassName('set-rep');
        for (let i = 0; i < number_of_sets.value; i++) {
            if(Number.isInteger(parseInt(sets[i].value))){
                sets_reps.push(sets[i].value);
            }
            else{ 
                valid_number_of_sets = false;
            }
        }
        number_of_sets = number_of_sets.value;
    } 
    // Validate Exercises
    const array_exercises = Array.from(document.getElementsByClassName('group-exercise'));
    array_exercises.forEach(exercise_group => {
        let exercise = exercise_group.getElementsByTagName('select')[0].textContent.replace(/[\n\r]+|[\s]{2,}/g, ' ').trim().split('  ').slice(1); 
        const exercise_value = exercise_group.getElementsByTagName('select')[0].value; 
        let descanso = exercise_group.getElementsByTagName('select')[1].textContent.replace(/[\n\r]+|[\s]{2,}/g, ' ').trim().split('  ').slice(1);
        const descanso_value = exercise_group.getElementsByTagName('select')[1].value;

        if(Number.isInteger(parseInt(exercise_value)) && Number.isInteger(parseInt(descanso_value)) ){
            exercise = exercise[exercise_value-1];
            descanso = descanso[descanso_value-1];
            exercises_list.push(exercise);
            descansos_list.push(descanso)
            valid_exercises = true;
        }
    });
    if(valid_treino && valid_number_of_sets && valid_exercises){
        $.ajax({
            type: "POST",
            url: "/plans",
            data: {
                "op": '0',
                "treino": treino,
                "tipo": tipo,
                "dificuldade": dificuldade,
                "number_of_sets": number_of_sets,
                "sets_reps": JSON.stringify(sets_reps),
                "exercises": JSON.stringify(exercises_list),
                "descansos": JSON.stringify(descansos_list),
            },
            error: function(request) {
                if (request.status === 404) {
                    alert("Não foi possível postar o plano.")
                }
            } 
        });
    }
    else{
        console.log("NO POST")
    }
}

function savePlan() {
    const planId = this.id;
    if(Number.isInteger(parseInt(planId))){
        $.ajax({
            type: "POST",
            url: "/plans",
            data: {
                'op': 1,
                'planId': planId,
            },
            success: function (response) {
                
            }
        });
    }
    else{
        alert('Não foi possível guardar este plano')
    }
}