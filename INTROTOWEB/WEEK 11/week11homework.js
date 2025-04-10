let grocerylistarray=[];
let groceryliststring;

const newgrocerysubmit=document.getElementById("newgrocerysubmit")
const grocerylist=document.getElementById("grocerylist")
const listElement = document.getElementById("myList");

function displayList() {
    grocerylistarray.forEach(item => {
        const listItem = document.createElement("li");
            listItem.textContent = item;
            listElement.appendChild(listItem);
        });
    }

newgrocerysubmit.addEventListener('click',function(){
    const newgroceryitem=document.getElementById("newgroceryitem")
    const newgroceryquantity=document.getElementById("newgroceryqty")
    const groceryinput=newgroceryitem.value;
    const groceryquantity=newgroceryquantity.value;
    grocerylistarray.push(groceryquantity + " " + groceryinput)
    newgroceryitem.value = "";
    newgroceryquantity.value = "";
    listElement.innerHTML = "";
    displayList();
});

displayList()




