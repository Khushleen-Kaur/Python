const put = document.querySelector("#updateSong");
put.addEventListener("click", async () => {
    put.disabled = true;
    try{
        let data = await getSongs();
        const putDialog = dialogBox("Update");
        putDialog.querySelector(".id-div").innerHTML = `
        <label for="song-id">Song ID:</label>
        <input type="text" name="song-id" id="song-id" placeholder="Song ID is...">
        `
        putDialog.querySelector("#song-id").required = true;
        putDialog.querySelector("#singer-name").required = true;
        putDialog.querySelector("#song-name").required = true;
        
        document.body.appendChild(putDialog);
        putDialog.showModal();
        
        putDialog.querySelector(".song-form").addEventListener("submit", async (e) => {
            e.preventDefault();
            let id = putDialog.querySelector("#song-id").value;
            let song = putDialog.querySelector("#song-name").value;
            let singer = putDialog.querySelector("#singer-name").value;
            if (!Object.hasOwn(data,id)){
                console.log("ID not found!");
                alert("Please, Enter a valid ID!")
                return;
            }
            if( !song || !singer){
                console.log("Both fields are required!");
                return;
            }
            let update_data = {
                "song_name" : song,
                "singer_name" : singer
            }
            response = await fetch( `${url}/${id}`, {
                method: "PUT",
                headers: {
                    "Content-Type" : "application/json"
                },
                body: JSON.stringify(update_data)
            })
            if(!response.ok){
                console.log("Something went wrong! Response is not ok!");
                throw new Error(`PUT failed (${response.status}) : ${errorText}`);
            }
            let result = await response.json();
            console.log(result);
            putDialog.remove();
            load.click();
        })
        
        
    }finally{
        put.disabled = false;
    }
})