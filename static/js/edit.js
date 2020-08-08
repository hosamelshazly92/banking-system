const depositBtns = document.querySelectorAll("#deposit");
const withdrawBtns = document.querySelectorAll("#withdraw");
const submitBtns = document.querySelectorAll("#submit");



for(let i = 0; i < submitBtns.length; i++) {
    const submitBtn = submitBtns[i];
    const depositBtn = depositBtns[i];
    const withdrawBtn = withdrawBtns[i];

    submitBtn.onclick = function(e) {
        const accountId = e.target.dataset['id'];
        // console.log("==========> ID: " + accountId);
        // console.log("==========> Deposit: " + depositBtn.value);
        // console.log("==========> Withdraw: " + withdrawBtn.value);

        fetch('/transaction/' + accountId, {
            method: 'POST',
            body: JSON.stringify({
                'deposit': depositBtn.value,
                'withdraw': withdrawBtn.value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function(res) {
            return res.json();
        }).then(function(jsonRes) {
            document.location.reload();
        });
    }
}
