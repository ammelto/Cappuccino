# Cappuccino
Python script to make espresso easier to use. Allows input files to have shorthand canonical SOP equations rather than truth tables

#How to use
Create your espresso input file as normal, but rather than putting the PLA as a truth table, input it as a canonical SOP equation. Each new line represents a new output in the order you list them at the top of the espresso input file. 
For example: 
```
.i 6
.o 4
.ilb a2 a1 a0 b2 b1 b0
.ob za zb zc zd
 
sum(0,1,3,5,42)+d(2,4)
sum(0,5,6,14,32)+d(2,4)
sum(3,4,2)+d(40,14,3,6)
sum(4,5,6)+d(2)

.e
```
is the same as:

![SOP notation](http://i.imgur.com/MSLMYO1.png)

Make sure that the .i and .o corresspond to the correct number of inputs and outputs listed, otherwise the program will not work correctly.
