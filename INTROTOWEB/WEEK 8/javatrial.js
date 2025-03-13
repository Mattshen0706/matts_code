
function updateName(){
     const name = prompt("Enter a new name!")
     buttonformat.textContent='Player 1 :${name}'
}

const buttonformat = document.querySelector("button")
buttonformat.addEventListener("click",updateName);