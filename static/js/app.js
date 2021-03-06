if (user != 'AnonymousUser') {
    document.getElementById("loginBtn").children[0].style.display = "none";
} else {
    document.getElementById("cartdisplay").children[0].style.display = "none";
    document.getElementById("dashboard").children[0].style.display = "none";
    document.getElementById("logoutBtn").children[0].style.display = "none";
    document.getElementById("userdisplay").children[0].style.display = "none";
}

document.querySelectorAll('.update-cart').forEach(element => {
    element.addEventListener('click', () => {
        if (user != 'AnonymousUser') {
            document.getElementById("signout").addEventListener("click", (e) => { document.getElementById("logout-action").submit(); });
            updateCart(element.dataset.product, element.dataset.action);
        }
    });
});

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
        console.log(json);
        location.reload();
    });
}