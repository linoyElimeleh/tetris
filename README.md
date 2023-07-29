

## Creator Details:

Linoy Elimeleh 

0532808388

lino1998y@gmail.com


---


## How to run?
 `python main.py < input.txt`
you will see the output file on /output_files by the date

---

## Requirements:
**target**:  Simplified Tetris engine.
**input**: Text file of lines each representing a sequence of pieces entering the grid.
**output**:  For each line of the input file, your program should output the resulting height of the remaining blocks within the grid by Tetris engine.


**tetris engine:**
The engine should model a grid in that pieces enter from the top and come to rest at the bottom as if pulled down by gravity. Each piece is made up of four unit squares. No two unit squares can occupy the same space in the grid at the same time. The pieces are rigid, and come to rest as soon as any part of a piece contacts the bottom of the grid or any resting block. As in Tetris, whenever an entire row of the grid is filled, it disappears, and any higher rows drop into the vacated space without any change to the internal pattern of blocks in any row.


**about the input file:**
•	The input file called "input.txt" denotes the different possible shapes by letter. 
•	Q, Z, S, T, I, L, and J are the letters used.
•	 The shapes of the pieces they represent are shown in the diagram.
•	 Each line of the input file is a comma-separated list. 
•	Each entry in the list is a single letter (from the set above) and a single-digit integer.
•	 The integer represents the leftmost column of the grid that the shape occupies, starting from zero. 


**About the board:**
•	The grid of the game space is 10 units wide.
•	For each line of the file, the grid’s initial state is empty.


**Exclusions**:
1.	Your program does not need to validate the file format and can assume that there will be no illegal inputs in the file.
2.	 You do not have to account for shape rotation in your model. The pieces will always have the orientations shown.
3.	 Your program need not detect whether any sequence of pieces will exceed any particular height, but you may assume that no test case will result in a height greater than 100.
4.	 Your program should preferably be invoked from a command line, taking its input from STDIN and writing its output to STDOUT. For instance: $ ./tetris < input.txt > output.txt


**For example**, if the input file consisted of the line “Q0” the corresponding line in the output file would
be “2”, since the block will drop to the bottom of the initially empty grid and has height two.


**Steps:** 
1.	Process the text file.
2.	 Read the input file line by line.
3.	For each line, initialize an empty 10*10 grid. 
4.	For each entry in the line, extract the shape letter and leftmost column position.
5.	Determine the height of the piece based on its shape letter.
6.	Calculate the final position of the piece by adding its height to the grid's bottom row and subtracting the leftmost column position from the grid's width.
7.	Update the grid by placing the piece at its final position, filling the corresponding cells with the piece's shape letter.
8.	Check if any rows in the grid are filled completely and need to be cleared.
9.	If a row is filled, remove it and shift all rows above it one position down.
10.	Repeat steps 4-9 for each entry in the line.
11.	Calculate and output the resulting height of the remaining blocks within the grid.
12.	Repeat steps 3-11 for each line in the input file.


**Shape:** 
1.	Type
2.	Height 
3.	Width
4.	Metrix

**Board:** 
1.	Grid
2.	Height_array
3.	Current_height

---
