******************
*TURTLE INTERFACE*
******************

        0          1          2     
    |------------------------------|
    |                              |
0   |                              |
    |------------------------------|
    |        |            |        |
1   |ORDER   | ***********|        |
    |------------------------------|
    |        |            |        |
2   |Length  | ***********|        |
    |------------------------------|
    |        | aaaaaa     |        |
    |Pattern | cccccc     | TEXT   |
3   |        | dddddd     | TEXT   |
    |        | bbbbbb     | TEXT   |
    |        | eeeeee     | TEXT   |
    |        | ffffff     |        |
    |------------------------------|
    |                              |
4   |                              |
    |------------------------------|
    |        |            |        |
5   | Clear  |  Draw      | New    |
    |------------------------------|

* Construct the Tk window 				line 8
* Define handlers (OnClear and OnNew buttons)		line 13
* Define the execution functions for all figures	line 25
* Define the OnDraw button which executes the drawing	line 76
* Show description of a selected turtle			line 142
* Add labels for the various inputs			line 183
* Create a listbox so the users can select a figure	line 212
* Create functional buttons, clear, draw and new	line 227
		


*****************
*TURTLE FIGURES	*
*****************

Spirograph
----------
Spirograph was the first shape that I created so I used a lot of booleans and comments to debug. 
I left them in so that the progression of my abilities could clearly be seen. 
I used a while loop in this figure.

Binary Tree
-----------
This is a well known iteration and is quite straight forward.
I didn't have to do much other than edit the code so it matches the rest.

Spike
-----

This is all my own work using ratios, angles and rotations 
to create a loop effect. Effective angle was used just like 
in Circle Ception.

Fern Tree
---------
I also include code that can be uncommented for test runs. 


Snow Flake/Anti Snow Flake
--------------------------
I just had to match naming conventions in these figures 
and understand the maths.

Circle Ception
--------------
I created this because I wanted a type of slinky effect 
however I preferred how this was looking. I had different 
maths calculating the effective angle (just modulo) but when 
I plugged same into Spike it wouldn't work on some occassions 
so came up with effectiveAngle. I made use of modulo and 
floor division to calculate ideal angles that are within 
range no matter what inputs are used.

Triangle Fractal
----------------
This is a popular fractal algorithim widely available and I 
played around with it to fit with my requirements and take in 
user inputs

Poly Spiral
-----------
I began to gain confidence and wanted to play around with 
turtle so I created various loops and combos. I started 
identifying patterns and characteristics that I wanted to 
keep and I tinkered with undesirable ones and Poly Spiral was born.

Jagged Edge
-----------
This was a harsher version of Poly Spiral. 



