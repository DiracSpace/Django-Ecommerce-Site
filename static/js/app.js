if (user != 'AnonymousUser') { 
    document.getElementById("loginBtn").children[0].style.display = "none";
} else {
    document.getElementById("userdisplay").children[0].style.display = "none";
}

document.querySelectorAll('.update-cart').forEach(element => {
    element.addEventListener('click', () => {
        if (user === 'AnonymousUser') {
            addCookieItem(element.dataset.product, element.dataset.action);
        } else {
            document.getElementById("signout").addEventListener("click", (e) => { document.getElementById("logout-action").submit(); });
            updateCart(element.dataset.product, element.dataset.action);
        }
    });
});

function addCookieItem(id, action) {
    console.log('unauthenticated user is ' + action + ' product ' + id);
    if (action == 'add') {
        if (cart[id] == undefined) {
            cart[id] = {'quantity' : 1};
        } else {
            cart[id] += 1;
        }
    }
    
    if (action == 'remove') {
        cart[id]['quantity'] -= 1;
        if (cart[id]['quantity'] <= 0) {
            console.log('removing');
            delete cart[id];
        }
    }
    console.log('cart', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
}

function updateCart(id, action) {
    const csrftoken = Cookies.get('csrftoken');

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
    .then((response) => response.json())
    .then((json) => {
        location.reload();
    });
}