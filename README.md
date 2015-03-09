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

You run the program similar to espresso:
```
cappuccino file.in file.out
```
Where file.in is your input file and file.out is your output file. 
This will create two files. The first file will have the same name as your input file with Espresso appended to the front. The second will be your output file. For example, if you input cappuccino ayylmao.txt nicememe.txt then the script will create an Espressoayylmao.txt alongside of your output file. 

#FAQ

**How do I run this on Mac/Linux?**
The package includes both the executable and the python script. On Windows, you can just run the executable similar to how you'd run espresso. If you are on Linux or Mac you'll have to install python first and make sure you use python 3.4. Most Debian based linux distros come prepackaged with python so you'll just have to make sure to run it as
```
python3 cappuccino.py file.in file.out
```
If you need help installing python on either platform, don't be afraid to google it. There's lots of documentation on Python, but if you still cannot figure it out then you can email me or submit an issue.

**Why does it create two files? What is Espresso[input.file]?
The output file contains what you would expect, the minimized boolean equations. The Espresso[input.file] contains the regular inputfile with your shorthand converted into a truth table so you can double check it incase there's reason to believe an error occured. It's purely for debugging purposes and your reference, feel free to ignore it if you would like. 

**Why does it output a bunch of gibberish into the command line?**
I still have a lot of debugging features in the script to make it easier to identify the cause of problems incase users have issues. The script will first echo out the SOP equation by deliminating the sum from the don't cares. Secondly, it will echo the inputs parsed into two dimensional arrays. Finally, it'll output the equations it's writing to the out file. 

**HELP IT ISN'T WORKING CORRECTLY**
Submit an issue in this repository by clicking the issues button at the top of the screen. I'll get to it as soon as possible, I promise. 

**Why are you doing all of this documentation just for a simple python script?**
Why not?

**Do you plan on adding any features to the script?**
If enough people use it, I'll add to it. One thing I was planning on adding soon that isn't a part of canonical shorthand notation was allowing users to input a range of values. For example,
```
sum(range[2,10,2],13,6)+d(18,19)
```
would be include all the values from 2 to 10 stepping by 2. So basically it'd be the same as 
```
sum(2,4,6,8,10,13,6)+d(18,19)
```
I'll probably add Product of Sums notation as well since it can get tedious inputting tons of values if you have a mostly true truth table. 
```
