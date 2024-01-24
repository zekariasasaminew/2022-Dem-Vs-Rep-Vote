# Dem Vs Rep Gerrymandering Detection

This program analyzes the voting in the state entered by the user for a particular election
whose data is stored in a file. The program displays voting data from that state by district
in a stacked bar chart, displays the statistics by district used to determine gerrymandering,
and computes whether there was gerrymandering in this election in favor of the Democrats or Republicans.

## Installation and Usage

1. Ensure Dependencies:
   - Install graphics2 module
2. File Preparation:
   - Ensure that the 'districts.txt' file exists and contains the necessary voting data.
The format of the file appears to be comma-separated values with the state name,
district, Democratic votes, and Republican votes.
3. Ensure python ide is installed
4. Run the Program:
   - Open a terminal or command prompt.
   - Navigate to the directory where your Python file is located.
   - Run the script by entering the following command
5. Input State:
   - The program will prompt you to enter the state you want to look up. Enter the state name and press Enter.
  
*** Make sure you have Python installed on your system, and the 'graphics2' module is available. 
If any errors occur during execution, check the console output for error messages, and ensure that 
the required dependencies are met.

## Overview

### Constants
```python
MIN_NUM_DISTRICTS = 2
EFFICIENCY_GAP_LIMIT = 8
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750
DEFAULT_BAR_HEIGHT = 20
SPACE_BETWEEN = 5
surplus_d_sum = 0
surplus_r_sum = 0
total_vote_sum = 0
space = 0
```


First the file is opened. 

```python
file = open(FILE_NAME, 'r')
```

Then it iterates across te data by splitting it in commas and the first element of the list is the state and the
following are district, democratic vote, republic vote respectively.

```python
for line in file:
        file_list = line.split(',')
        if state == file_list[0]:
            state_list = file_list[1:]
```

After window is created and bars are calculated for states that have a lot of districts with the formula

```python
new_bar_height = ((WINDOW_HEIGHT - SPACE_BETWEEN) - (SPACE_BETWEEN * num_district)) / (num_district)
```

Then, gerrymandering is determined by using the diffrence between the two party's vote then the bars are drawn.

```python
#draw the blue bar (Democrats)
upperLeft = Point(0, ((space + 1) * SPACE_BETWEEN) + (space * new_bar_height))
lowerRight = Point(width_democrats, (SPACE_BETWEEN * (space + 1)) + ((space + 1) * new_bar_height))
bar_d = Rectangle(upperLeft, lowerRight)
bar_d.setFill('blue')
bar_d.draw(window)

#draw the red bar (Republicans)
upperLeft = Point(width_democrats, ((space + 1) * SPACE_BETWEEN) + (space * new_bar_height))
lowerRight = Point(WINDOW_WIDTH, (SPACE_BETWEEN * (space + 1)) + ((space + 1) * new_bar_height))
bar_r = Rectangle(upperLeft, lowerRight)
bar_r.setFill('red')
bar_r.draw(window)
space = space + 1
```

## Contribution
Professor Diane Mueller 
