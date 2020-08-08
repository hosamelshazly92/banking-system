
const createBtn = document.getElementById("create");
const newBalance = document.getElementById("new_balance");
const removeBtns = document.querySelectorAll("#remove");

createBtn.onclick = function(e) {
    const personId = e.target.dataset['id'];

    fetch('/person/' + personId + '/create', {
        method: 'POST',
        body: JSON.stringify({
            'newBalance': newBalance.value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(response) {
        return response.json();
    }).then(function(jsonResponse) {
        document.location.reload();
        // console.log(jsonResponse);
    });
}

for(let i = 0; i < removeBtns.length; i++) {
    const removeBtn = removeBtns[i];

    removeBtn.onclick = function(e) {
        const accountId = e.target.dataset['id'];
        fetch('/delete/' + accountId, {
            method: 'DELETE'
        }).then(function() {
            document.location.reload();
        });
    }
}
