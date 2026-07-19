const API = "http://127.0.0.1:8000/tasks";

async function loadTasks() {

    const response = await fetch(API);

    const tasks = await response.json();

    const list = document.getElementById("taskList");

    list.innerHTML = "";

    tasks.forEach(task => {

        const li = document.createElement("li");

        if(task.completed){
            li.classList.add("completed");
        }

        li.innerHTML = `
            <span>${task.title}</span>

            <div>

                <button onclick="toggleTask(${task.id}, '${task.title}', ${task.completed})">
                    ${task.completed ? "Undo" : "Done"}
                </button>

                <button onclick="deleteTask(${task.id})">
                    Delete
                </button>

            </div>
        `;

        list.appendChild(li);

    });

}

async function addTask(){

    const input = document.getElementById("taskInput");

    const title = input.value.trim();

    if(title===""){
        return;
    }

    await fetch(API,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            title:title
        })
    });

    input.value="";

    loadTasks();

}

async function deleteTask(id){

    await fetch(`${API}/${id}`,{
        method:"DELETE"
    });

    loadTasks();

}

async function toggleTask(id,title,currentStatus){

    await fetch(`${API}/${id}`,{
        method:"PUT",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            title:title,
            completed:!currentStatus
        })
    });

    loadTasks();

}

loadTasks();