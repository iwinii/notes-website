function deleteNote(noteId, that){
    console.log(that);
    $("[data-id='" + noteId +"']").hide();
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        _res.json().then(function(data) {
        console.log(data);
//        alert(data.message);
        });
//        window.location.href = "/";
    });
}