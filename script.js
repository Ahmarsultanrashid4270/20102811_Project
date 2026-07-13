const url = "http://127.0.0.1:5000/animals";

function addAnimal() {

    let animal= { 
        
        animal_id: document.getElementById("animal_id").value,
        name: document.getElementById("name").value,
        species: document.getElementById("species").value,
        breed: document.getElementById("breed").value,
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        status: document.getElementById("status").value

    };
     fetch(url,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(animal)
        })
        .then(function(){

            clearData();
            showAnimals();

        });

    
}


