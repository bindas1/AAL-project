About us
---------
We are third year Computer Science students at Warsaw University of Technology. 
This is our project for the course called Analysis of algorithms. 
We are both interested in the fields of Computer Science especially data science and algorithmic thinking. 
You can find us on LinkedIn: [Aleksandra Kukawka](https://www.linkedin.com/in/aleksandrakukawka/) and [Bartłomiej Binda](https://www.linkedin.com/in/bart%C5%82omiej-binda-936915147/).

## The subject of the project
Given the set of cuboids a1,. . . , an and a cuboid area with two sides not smaller than the largest of the sides of the cuboids in the set. It is necessary to determine, using various heuristic methods, as well as a systematic search, the shortest length of the third side of the area allowing for the orthogonal arrangement of the collision of the set in the area. Compare the calculation times and results of the different methods.

## How to run our project
There are 3 ways (methods) to run our project:
1. ```python main.py –m1 <in.txt >out.txt``` - this way we can use a file a standard input and the output of the program will be saved in out.txt. If out.txt isn't specified the results will be returned in terminal.
2. ```python main.py –m2 -n100 -w5 -l10 >out.txt``` - this way we can generate input for our program. N is the number of boxes in our set. Bw and bl mean how many boxes should on average fit in base's width and length respectively. 
3. ```python main.py –m3 -n1000 -k30 -s500 -r10``` - this way we can generate many instances of the problem and return the average score for given n and time that the method takes. N is the primary number of boxes in our set. The rest of the flags are explained below.

Execution parameters (optional arguments):
*  -h, --help            show this help message and exit
*  --mode MODE, -m MODE  Execution mode
*  --number_of_boxes NUMBER_OF_BOXES, -n NUMBER_OF_BOXES
                        Number of boxes to be inserted
*  --number_of_problems NUMBER_OF_PROBLEMS, -k NUMBER_OF_PROBLEMS
                        Number of problems that should be executed
*  --step STEP, -s STEP
                        How many boxes are added for the next problem
*  --samples SAMPLES, -r SAMPLES
                        How many times do we simulate a problem
*  --avg_number_boxes_width AVG_NUMBER_BOXES_WIDTH, -w AVG_NUMBER_BOXES_WIDTH
                        Average number of boxes that fit in width
*  --avg_number_boxes_length AVG_NUMBER_BOXES_LENGTH, -l AVG_NUMBER_BOXES_LENGTH
                        Average number of boxes that fit by length

Please note that 3 parameters

Additionaly we can use ```generate.py``` to generate specific data for standard input and use it as pipeline with method 1.
```python generate.py –n100 -w5 -l10 | python main.py –m1```

## Input and output
Input should be a text file (any format that can be used for stdin) and be structured like in the example below:
```
20,10,10
50,30,20
10,20,5
...
```
All edges should be separated by commas and each cuboid should be written in new line.
The **output** differs depending on the mode that we're using:
- for mode 1 and 2 for each of the algorithms we get the final height of the cuboid. Example:
```
The final height for naive with sort is 19.748150306420225
The final height for naive without sort is 19.74815030642023
The final height for systematic search is 7.43837254612423
The final height for search with layers is 11.378883254225343
The final height for search with tree is 8.808003603782272
```
- for mode 3 we obtain a table with 3 columns. First column is the number of boxes, second column is the time in miliseconds that it takes given algorithm to run, third column is the coefficient q calculated from the formula:
![Image](/images/formula.png)
Example output for one of the algorithms:
```
Method with layers
50       0.09560000000001789     3.0611276660041913
100      0.17939999999996292     1.4938785220082287
150      0.26610000000000245     1.0
200      0.33520000000000216     0.7144748576432071
```

