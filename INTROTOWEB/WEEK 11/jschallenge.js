// Convert the string into an array, removing the + characters in the process. Save the result in a variable called myArray.
// Store the length of the array in a variable called arrayLength.
// Store the last item in the array in a variable called lastItem.


// PROBLEM 2: 

let myString = 'Ryu+Ken+Chun-Li+Cammy+Guile+Sakura+Sagat+Juri';
myList=myString.split("+")
console.log(myList)
lengthofmylist=myList.length
console.log(lengthofmylist)
lastitem=myList[lengthofmylist-1]
console.log(lastitem)


// PROBLEM 4:
const birds = [ "Parrots", "Falcons", "Eagles", "Emus", "Caracaras", "Egrets" ];
let newlist=[]
const eaglesindex=birds.indexOf("Eagles")
birds.splice(eaglesindex,1)
console.log(birds)
for (const bird of birds){
    if (bird.startsWith('E')){
        newlist.push(bird);
    }
}
console.log(newlist)
