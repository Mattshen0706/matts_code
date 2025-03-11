# DIVS

HOW TO CREATE MULTIPLE COLOUMS

display: 
    float:allows you to put elements side by side
    flex: allows yout o make more felxible side to side containers 
    grid (grid-template-colums: 33%, 33%, 33%)
}



# CLASS

CLASS



# IMAGE FORMATTING
Make the div 100% outside the box so it aligns with the division dimensions

object-fit: cover (COVERS THE ENTIRE BOX)

object-fit: contain (FIT WITHIN THE DIMENSIONS OF THE BOX)

>  ">*"  means everything which is contained in the class will be applied with the same CSS. 


Padding: Distance between image and border
Margin: Distance between edge of photo and container


> target="_blank" to open up a new window from a link

> transform: translate(x-translation, y translation) (Takes the centre of the text as referecen)

>class:hover - Allows you to do functions when hovering over 

>class:hover.claas{
    modifications will be made to the .class when hovering over
}

>translate:rotate{rotatation function

>translate:scale(default scale is 1)}

>translate:skew(direction x, direction y) (creates the feeling of 3 dmiensional sheering)

>translate:matrix(takes in all the measurements for transform)

>translate:rotateX (3 dimensional rotation)

>translate:rotateZ (3 dimensional rotation)

# TRANSITIONS WITH DURATION:
USE A "TRANSITION" within a class and reference that in hover"

example:
.hover3D:
width:0;
position:relative;
transition: width 2s, transform 2s:

.hover3D:hover:
width:200%;
translate:rotateX(50%);

