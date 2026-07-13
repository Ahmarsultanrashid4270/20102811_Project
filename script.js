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

           alert("Animal Added Successfully");
            

        });

    
}

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


