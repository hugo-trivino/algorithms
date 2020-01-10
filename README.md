# Welcome to a sample of a project in Algorithms

**Author:**		Hugo Trivino

**Folder:**		Final Project

**Subfolders:**	solutions; instances 

**Files:**		report.pdf (This is the report with time analysis and pseudocode) 
		project.py (this is the python greedy and local implementations
			    for the posted problem)

`Input:	The input instances have to be dropped in the folder named instances`

`Output: The output will be saved in the solutions folder and returned to
	the function`

## running the program:
### 	From terminal:
		Open the terminal from this folder and open the python terminal.
		type the following to load the file
		>from projects import greedy
		after that you can give the number of instance to the greedy
		 function, for example if the instance number is 43, type:
		>greedy(43)
		and then check your solution folder. Your solution would be
		 there.
		if you want to check several solutions at once you can write:
		>for x in range(23,47):
	      ...	greedy(x)
		>
		This will check all instances from 23 to 46 (excluding 47).
### 	From another file:
		you can write a python file within the current folder and 
		import the function by writing:
		"from project import greedy" at the top of the file. And then
		 just use the greedy function


By the way, the implementation of a local optimum is also there, you can 
running by changing "greedy" to "local" in the previous instruction. However,
the official version and reports are made for the greedy solution.
I made the local solution to gain a better handle on the problem.
