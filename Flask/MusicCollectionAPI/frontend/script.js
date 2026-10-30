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
            song.innerHTML = `<div>Song Name: ${data[i].song_name}</div>`
            let singer = document.createElement('div');
            singer.innerHTML = `<div>Singer Name: ${data[i].singer_name}</div>`
            let card = document.createElement("div")
            card.classList.add("card");
            card.append(id)
            card.append(song)
            card.append(singer)
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
    <div class="dialog-title">${operation} Song</div>
    <form class="song=form">
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
    document.body.appendChild(dia);
    return dia;
}
const add = document.querySelector("#addSong")
add.addEventListener("click", async () => {
    add.disabled = true;
    try{
        let data = await getSongs()
        const addDialog = dialogBox("Add")
        
        if(addDialog.isConnected){
            addDialog.showModal();
        }else{
            console.log("Dialog box cannot be loaded!");
        }
        document.querySelector(".submit-btn").addEventListener("submit", (e) => {
            e.preventDefault();
            const song_name = document.querySelector("#song-name").value;
            const singer_name = document.querySelector("#singer-name").value;

            let new_song = {
                "song_name":song_name,
                "singer_name":singer_name
            }
            addDialog.close();
        })
        
    }catch(e){
        console.log(e.message);
    }finally{
        add.disabled = false;
    }
})
