
deleteBtn = document.querySelector("#delete")

deleteBtn.onclick = function(e) {
    const personId = e.target.dataset['id'];
    confirmation = confirm("Are you sure you want to delete?");
    if(confirmation) {
        fetch('/person/' + personId, {
            method: 'DELETE',
        }).then(function(response) {
            document.location.href = '/';
        });
    } else {
        document.location.href = '/';
    }   
}
