const patch = document.querySelector("#patchSong");
patch.addEventListener("click", async () => {
    const patchDialog = dialogBox("Patch");
    const choice = document.createElement("div");
    const choice_song = document.createElement("button");
    choice_song.textContent = "Update Song Name";
    choice_song.classList.add("btn");
    const choice_singer = document.createElement("button");
    choice_singer.textContent = "Update Singer Name";
    choice_singer.classList.add("btn");

    let selected_choice = "song_name";

    choice_singer.addEventListener("click" ,()=>{
        console.log("Singer_name");
        selected_choice = "singer_name";
    })
    choice_song.addEventListener("click" ,()=>{
        console.log("Spmg_name");
        selected_choice = "song_name";
    })

    choice.append(choice_song, choice_singer);
    
    
    patchDialog.querySelector(".dialog-title").insertAdjacentElement("afterend",choice );
    patchDialog.querySelector(".id-div").innerHTML = `
    <label for="song-id">Song ID:</label>
    <input type="text" name="song-id" id="song-id" placeholder="Song ID is...">
    `
    const singer_div = patchDialog.querySelector(".singer-div");
    const song_div = patchDialog.querySelector(".song-div");
    
    singer_div.classList.add("display_patch");
    
    choice_song.disabled = true;
    choice_singer.addEventListener("click", () => {
        choice_singer.disabled = true;
        choice_song.disabled = false;
        singer_div.classList.remove("display_patch");
        song_div.classList.add("display_patch");
    })
    choice_song.addEventListener("click", () => {
        choice_singer.disabled = false;
        choice_song.disabled = true;
        singer_div.classList.add("display_patch");
        song_div.classList.remove("display_patch");
    })
    document.body.appendChild(patchDialog);
    patchDialog.showModal();
    
    patchDialog.querySelector(".song-form").addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = await getSongs();
        const id = patchDialog.querySelector("#song-id").value;
        if(!Object.hasOwn(data, id)){
            alert("Please, Enter a valid ID!");
            throw new Error("ID doest not Exit!");
        }
        let new_data = {};
        if(selected_choice == "song_name"){
            const song_name = patchDialog.querySelector("#song-name").value;
            if (!song_name) {
                alert("Please, Enter a Song name!");
                throw new Error("Song name cannot be empty!");
            }
            new_data[selected_choice] = song_name;
        }
        else if(selected_choice == "singer_name"){
            const singer_name = patchDialog.querySelector("#singer-name").value;
            if (!singer_name) {
                alert("Please, Enter a Singer name!");
                throw new Error("Singer name cannot be empty!");
            }
            new_data[selected_choice] = singer_name;
        }
        const response = await fetch( `${url}/${id}` , {
            method: "PATCH",
            headers : {
                "Content-Type" : "application/json"
            },
            body: JSON.stringify(new_data)
        });
        if(!response.ok){
            throw new Error("Something went wrong! Response error!");
        }
        const response_data = await response.json();
        console.log("Response : " , response_data);
        patchDialog.remove();
        load.click();

    })
    
})