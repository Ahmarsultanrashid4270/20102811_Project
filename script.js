const url = "http://127.0.0.1:5000/animals";
let animals = [];
let editId = 0;

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
    
     if(editId == 0){

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
            alert("Animal added successfully!");

        });

    }
    else{

        fetch(url + "/" + editId,{
            method:"PUT",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(animal)
        })
        .then(function(){

            editId = 0;

            document.getElementById("saveBtn").innerHTML = "Add Animal";

            clearData();
            showAnimals();
            alert("Animal updated successfully!");

        });

    }


    
}

showAnimals();

function showAnimals() {

    fetch(url)
    .then(res => res.json())
    .then(data => {

        animals = data;

        let rows = "";

        data.forEach(function(animal){

            rows += `
            <tr>
                <td>${animal.id}</td>
                <td>${animal.animal_id}</td>
                <td>${animal.name}</td>
                <td>${animal.species}</td>
                <td>${animal.breed}</td>
                <td>${animal.age}</td>
                <td>${animal.gender}</td>
                <td>${animal.status}</td>
                <td>
                    <button onclick="editAnimal(${animal.id})">Edit</button>

                    <button onclick="deleteAnimal(${animal.id})">Delete</button>
                </td>
            </tr>
            `;

        });

        document.getElementById("animals").innerHTML = rows;

    });

}

function editAnimal(id){

    editId = id;

    let animal = animals.find(function(a){
        return a.id == id;
    });

    document.getElementById("animal_id").value = animal.animal_id;
    document.getElementById("name").value = animal.name;
    document.getElementById("species").value = animal.species;
    document.getElementById("breed").value = animal.breed;
    document.getElementById("age").value = animal.age;
    document.getElementById("gender").value = animal.gender;
    document.getElementById("status").value = animal.status;

    document.getElementById("saveBtn").innerHTML = "Update Animal";

}

function deleteAnimal(id){

    fetch(url + "/" + id,{
        method:"DELETE"
    })
    .then(function(){

        showAnimals();
        clearData();
        alert("Animal deleted successfully!");

    });

}

function clearData(){

    document.getElementById("animal_id").value = "";
    document.getElementById("name").value = "";
    document.getElementById("species").value = "";
    document.getElementById("breed").value = "";
    document.getElementById("age").value = "";
    document.getElementById("gender").value = "";
    document.getElementById("status").value = "";

}


