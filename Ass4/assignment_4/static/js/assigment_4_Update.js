const button = document.getElementById('updateBtn');

button.addEventListener('click', updateButton);

function updateButton() {
  document.getElementById('emailupdate').value=document.getElementById('useremail')
}
