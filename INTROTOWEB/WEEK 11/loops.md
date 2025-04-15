# LOOPS 

### EXAMPLE 1: GENERATE CIRCLES

RANDOMISE CIRCLE CODE

>const btn = document.querySelector("button");
>
>const canvas = document.querySelector("canvas");
>
>const ctx = canvas.getContext("2d");
>
initiates the varaible which will be used in the bigger code 

>document.addEventListener("DOMContentLoaded", () => {
  canvas.width = document.documentElement.clientWidth;
  canvas.height = document.documentElement.clientHeight;
});

Command for when the page loads. Gets the document width and height based on the display

>function random(number) {
>
  >return Math.floor(Math.random() * number);
>
>}

Takes from the javascript built in math library, function will return a random number given a range of (number). 

>function draw() {
>
  >ctx.clearRect(0, 0, canvas.width, canvas.height);
>
  >for (let i = 0; i < 100; i++) {
  >  
  >  ctx.beginPath();
    ctx.fillStyle = "rgb(255 0 0 / 50%)";
    ctx.arc(
      random(canvas.width),
      random(canvas.height),
      random(50), 
      0,
      2 * Math.PI,
 >   );
 >
>  ctx.fill();
 > }

Function calls for a random which initaites a for loop to draw 100 circles. The position of the circle uses a random number generated within the height and width of the display. The size of the circle is a random integer wihtin 50. 

arc(x, y, radius, startAngle, endAngle, counterclockwise)


>btn.addEventListener("click", draw);

Initiates the drae function based on when btn is clicked. 

### EXAMPLE 2: LOOPING THROUGH LIST:

>let names=["leo","draco","beatrice","joker"]
>
> for (const name in names){
>
>console.log(name)
>
>};

>leo, draco, beatrice, joker

## STANDARD CONSTRUCTION OF A FOR LOOP

>for (initializer; condition; final-expression) {
>
 > // code to run
 >
>}

### USING MAPS

>function toUpper(string) {
>
>  return string.toUpperCase();
>
>}
>
>const cats = ["Leopard", "Serval", "Jaguar", "Tiger", 
> "Caracal", "Lion"];
>
>const upperCats = cats.map(toUpper);
>
>console.log(upperCats);
// [ "LEOPARD", "SERVAL", "JAGUAR", "TIGER", "CARACAL", "LION" ]

The function above leverages the .map  command. The .map command allows you to iterate through each element in a list and modify them, in this case the map allows user to call the function to upper. which chanegs all the characters to upper. 

### USING FILTER

>const cats = ["Leopard", "Serval", "Jaguar", "Tiger", 
> "Caracal", "Lion"];
>
>const filtered = cats.filter((cat) => cat.startsWith("L"));
>console.log(filtered);

Filter allows you to filter through a list and add a condition (filter is a way to iterate through the entire list wihtout the need for an explicit for loop)

### EXAMPLE 3
>const cats = ["Pete", "Biggles", "Jasmine"];
>
>let myFavoriteCats = "My cats are called ";
>
>for (let i = 0; i < cats.length; i++) {
    >
 > if (i === cats.length - 1) {
    >
 >   // We are at the end of the array
 >
  >  myFavoriteCats += `and ${cats[i]}.`;
  >
  >} else {
    >
   > myFavoriteCats += `${cats[i]}, `;
 > }
 >
>}
>
>console.log(myFavoriteCats);

The if clause within the for loop allows you to modify the last element within the list so that it formats differently. When the iteration fullfills i===catss.lenght -1, it will add the and to the clause to finish the string. 

### USING BREAK

  >for (const contact of contacts) {
    >
  >  const splitContact = contact.split(":");
  >
  >  if (splitContact[0].toLowerCase() === searchName) {
    >
   >   para.textContent = `${splitContact[0]}'s number is $
   >
   >{splitContact[1]}.`;
   >
   >   break;
   >
   > }
 > }

When the if condition is met the loop will end and the code will skip the remaining of the for loop


### USING CONTINUE

When the if condition is met the loop will skip the iteration and move on the next iteration without completely the full code. 

### WHILE LOOPS vs DO WHILE LOOPS

FORMAT FOR WHILE LOOPS

>while (condition) {
>
  >// code to run
  >
  >final-expression
  >
>}

traditional while loop starts with while followed by conditions and brackets

>do {
    >
  >if (i === cats.length - 1) {
    >
  >  myFavoriteCats += `and ${cats[i]}.`;
  >} else {
    >
  >  myFavoriteCats += `${cats[i]}, `;
  >}
  >
  >i++;
  >
>} while (i < cats.length);

Do while loops begin with a do clause followed by brackets and the fucntion within it. It is closed off with a while and the range of the loop


## TEST YOU LOOP SKILLS:


LOOP EXERCISE 1: ----------------------------------------------

In our first looping task we want you to start by creating a simple loop that goes through all the items in the provided myArray and prints them out on the screen inside list items (i.e., <li> elements), which are appended to the provided list.



for(const elements of myArray){
  const listItemElement = document.createElement('li');
  listItemElement.textContent = elements;
  list.appendChild(listItemElement);
}


LOOP EXERCISE 2: ----------------------------------------------

In this next task, we want you to write a simple program that, given a name, searches an array of objects containing names and phone numbers (phonebook) and, if it finds the name, outputs the name and phone number into the paragraph (para) and then exits the loop before it has run its course.

If you haven't read about objects yet, don't worry! For now, all you need to know is how to access a member-value pair. You can read up on objects in the JavaScript object basics tutorial.

You are given three variables to begin with:

name — contains a name to search for
para — contains a reference to a paragraph, which will be used to report the results
phonebook - contains the phonebook entries to search.
You should use a type of loop that you've not used in the previous task.


for(i=0;i<phonebook.length;i++){
  if (name==phonebook[i].name){
    para.textContent = phonebook[i].name + " " +phonebook[i].number;
    section.appendChild(para)
  }
}


LOOP EXERCISE 3: ----------------------------------------------

In this final task, you are provided with the following:

i — starts off with a value of 500; intended to be used as an iterator.
para — contains a reference to a paragraph, which will be used to report the results.
isPrime() — a function that, when passed a number, returns true if the number is a prime number, and false if not.
You need to use a loop to go through the numbers 2 to 500 backwards (1 is not counted as a prime number), and run the provided isPrime() function on them. For each number that isn't a prime number, continue on to the next loop iteration. For each one that is a prime number, add it to the paragraph's textContent along with some kind of separator.

You should use a type of loop that you've not used in the previous two tasks.


while (i>=2){

    if (isPrime(i)){
newtext+=i
newtext+=" "
    }
    i--
}



