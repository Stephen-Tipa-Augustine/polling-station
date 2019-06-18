function openForm() {

    document.getElementById("popForm").style.display="block";
}

function closeForm() {

    document.getElementById("popForm").style.display="none";
}

function actionButton() {
    let myDropdown = document.getElementById("action-button");
    if (myDropdown.style.display === 'block') {
        myDropdown.style.display = "none";
    } else {
        myDropdown.style.display = "block";
    }
}

function alertNotice() {
    alert("Thanks for Your Feedback, We have received it with thanks")
}

function voteDetails(clickedId) {
        let myView = document.getElementById(clickedId)
        if(myView.style.display === 'block')
        {
            myView.style.display = 'none'
        }
        else
        {
            myView.style.display = 'block'
        }
}