document.querySelectorAll('.update-cart').forEach(element => {
    element.addEventListener('click', () => {
        console.log(user + ' wants to ' + element.dataset.action + " " + element.dataset.product);
        if (user === 'AnonymousUser') {
            console.log('Not logged in: ' + user);
        } else {
            updateCart(element.dataset.product, element.dataset.action);
        }
    });
});

function updateCart(id, action) {
    const csrftoken = Cookies.get('csrftoken');

    console.log('sending payload ... ');
    const payload = {
        pid: id,
        action: action
    };

    fetch('http://127.0.0.1:8000/update_item/', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            'Content-Type' : 'application/json; charset=UTF-8',
            'X-CSRFToken' : csrftoken,
        }
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
        location.reload();
    });
}