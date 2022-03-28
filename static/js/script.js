// dismiss alert messages after 5 seconds
let messages = document.getElementsByClassName('alert');

setTimeout(function () {
    for (let message of messages) {
        let alert = new bootstrap.Alert(message);
        alert.close();
    }
}, 5000);