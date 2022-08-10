$(function() {
    console.log(window.location)
//twitter bootstrap script
 $("#add-note-button").click(function(event){
    event.preventDefault();

    var form_data = $('#add-note-form').serializeArray();
    console.log(JSON.stringify({note: "asd"}));
    fetch("/", {
        method: "POST",
        body: JSON.stringify({note: form_data[0].value})
    }).then((_res) => {
        console.log(_res);
        _res.json().then(function(data) {
        console.log(data);
//        alert(data.message);
        });
        window.location.href = "/";
    });
 });
});
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