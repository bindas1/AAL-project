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
2. ```python main.py –m2 -n100 -bw5 -bl10 >out.txt``` - this way we can generate input for our program. N is the number of boxes in our set. Bw and bl mean how many boxes should on average fit in base's width and length respectively. 
3. ```python main.py –m3 -n1000 -k30 -step500 -r10``` - this way we can generate many instances of the problem and return the average score for given n and time that the method takes. N is the primary number of boxes in our set. The rest of the flags are explained below.

Execution parameters (optional arguments):
*  -h, --help            show this help message and exit
*  --mode MODE, -m MODE  Execution mode
*  --number_of_boxes NUMBER_OF_BOXES, -n NUMBER_OF_BOXES
                        Number of boxes to be inserted
*  --number_of_problems NUMBER_OF_PROBLEMS, -k NUMBER_OF_PROBLEMS
                        Number of problems that should be executed
*  --step STEP, -step STEP
                        How many boxes are added for the next problem
*  --samples SAMPLES, -r SAMPLES
                        How many times do we simulate a problem
*  --avg_number_boxes_width AVG_NUMBER_BOXES_WIDTH, -bw AVG_NUMBER_BOXES_WIDTH
                        Average number of boxes that fit in width
*  --avg_number_boxes_length AVG_NUMBER_BOXES_LENGTH, -bl AVG_NUMBER_BOXES_LENGTH
                        Average number of boxes that fit by length

Additionaly we can use ```generate.py``` to generate specific data for standard input and use it as pipeline with method 1.
```python generate.py –n100 -bw5 -bl10 | python main.py –m1```

## Input and output
Input should be a text file (any format that can be used for stdin) and be structured like in the example below:
```20,10,10
50,30,20
10,20,5
...```
All edges should be separated by commas and each cuboid should be written in new line.
