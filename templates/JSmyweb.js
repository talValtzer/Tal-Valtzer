const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});

const loadDiv = document.getElementById("try1");
const sentDiv = document.getElementById("sent");
const btn = document.getElementById("btn1");
btn.onclick = function () {

    loadDiv.style.display = "block";
    let myVar = setInterval(displayload ,5000);
  
};
function displayload()
{
    loadDiv.style.display = "none";
    sentDiv.style.display="block";
}

