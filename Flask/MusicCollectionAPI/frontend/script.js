console.log(">Music Collection API");

const url = "http://127.0.0.1:5000/songs"
const content = document.querySelector(".content");

async function getSongs(){
    const response = await fetch(url)
    if(!response.ok){
        throw new Error();
    }
    const data = await response.json()
    return data;
}

const load = document.querySelector("#loadSongs")
load.addEventListener("click" , async () => {
    load.disabled = true;
    try{
        let data = await getSongs();
        let ids = Object.keys(data)
        content.innerHTML = ""
        ids.forEach(i => {
            let id = document.createElement('div');
            id.classList.add("id");
            id.innerHTML = `<div data-song-id=${i}>Song ID: ${i}</div>`
            let song = document.createElement('div');
            song.textContent = `Song Name: ${data[i].song_name}`
            let singer = document.createElement('div');
            singer.textContent = `Singer Name: ${data[i].singer_name}`
            let card = document.createElement("div")
            card.classList.add("card");
            card.append(id,song,singer)
            content.append(card)
        });
    }catch(e){
        console.log(e.message);
    }finally{
        load.disabled = false;
    }
})
function dialogBox(operation) {
    const dia = document.createElement("dialog");
    dia.classList.add("dialogBox");
    dia.innerHTML = `
    <button class="close-btn"> X </button>
    <div class="dialog-title">${operation} Song</div>
    <form class="song-form">
    <div class="id-div"></div>
    <div>
        <label for="song-name">Song Name:</label>
        <input type="text" name="song-name" id="song-name" placeholder="Song Name is...">
        </div>
        <div>
        <label for="singer-name">Singer Name:</label>
        <input type="text" name="singer-name" id="singer-name" placeholder="Singer Name is...">
        </div>
        <button type="submit" class="btn submit-btn">${operation}  song</button>
        </form>
        `
    dia.querySelector(".close-btn").addEventListener("click", () => {
        dia.remove();
    })
    return dia;
}
const add = document.querySelector("#addSong")
add.addEventListener("click", async () => {
    add.disabled = true;
    try{
        let data = await getSongs();

        const addDialog = dialogBox("Add")
        addDialog.querySelector(".id-div").innerHTML = `
            <label for="song-id">Song ID:</label>
            <label for="song-id">${(Math.max(...Object.keys(data).map(Number) , 0) + 1 )}</label>
        `
        addDialog.querySelector("#singer-name").required = true;
        addDialog.querySelector("#song-name").required = true;
        document.body.appendChild(addDialog);
        
        if(addDialog && addDialog.isConnected){
            addDialog.showModal();
        }else{
            console.log("Dialog box cannot be loaded!");
        }
        addDialog.querySelector(".song-form").addEventListener("submit", async (e) => {
            e.preventDefault();
            const song_name = addDialog.querySelector("#song-name").value;
            const singer_name = addDialog.querySelector("#singer-name").value;

            if (!song_name || !singer_name) {
                console.log("Both fields are required!");
                return;
            }
            const new_song = {
                "song_name":song_name,
                "singer_name":singer_name
            }
            const response = await fetch("http://127.0.0.1:5000/songs", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(new_song)
            });
            if(!response.ok){
                throw new Error("Something went wrong! Song cannot be added.");
            }
            let result = await response.json();
            console.log(result);
            addDialog.remove();
            load.click();
        })
    }catch(e){
        console.log(e.message);
    }finally{
        add.disabled = false;
    }
})

load.click()