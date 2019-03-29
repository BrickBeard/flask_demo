var modal = document.getElementById('api_modal')
var btn_users = document.getElementById('users_')
var btn_user = document.getElementById('user_')
var btn_companies = document.getElementById('companies_')
var display = document.getElementById('display')
var close_ = document.getElementsByClassName('close')[0];

btn_users.onclick = () => {
    fetch('http://127.0.0.1:5000/api/users')
    .then(response => response.json())
    .then(jsonRes => {
        const data = jsonRes;
        console.log('Testing jsonRes' + jsonRes);
        display.innerHTML = JSON.stringify(data, null, 4);
        modal.style.display = 'block';
    }); 
}

btn_user.onclick = function() {
    fetch('http://127.0.0.1:5000/api/users/2')
    .then(response => response.json())
    .then(jsonRes => {
        const data = jsonRes;
        console.log('Testing jsonRes' + jsonRes);
        display.innerHTML = JSON.stringify(data, null, 4);
        modal.style.display = 'block';
    }); 
}

btn_companies.onclick = function() {
    fetch('http://127.0.0.1:5000/api/companies')
    .then(response => response.json())
    .then(jsonRes => {
        const data = jsonRes;
        console.log('Testing jsonRes' + jsonRes);
        display.innerHTML = JSON.stringify(data, null, 4);
        modal.style.display = 'block';
    }); 
}

close_.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}