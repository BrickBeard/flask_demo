var modal = document.getElementById('delete_modal');
var display = document.getElementById('show_name');
var modal_btn = document.getElementById('del_btn');
var close_ = document.getElementsByClassName('close')[0];

function delete_user (id_, name_) {
    modal_btn.href = "/users/delete/"+id_
    display.innerHTML = name_ ;
    modal.style.display = 'block';

    close_.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
};