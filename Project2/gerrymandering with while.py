"""
Name: Zekarias Asaminew
Date: 10/08/2023
CSC 201
Project 2-Gerrymandering

This programs analyzes the voting in the state entered by the user for a particular election
whose data is stored in a file. It also analyzes wheater a valid state name was entered or not and
also if nothing is entered or not; and uses while loop to prompt the user again for a valid state name
The program displays that voting data from that state by district in a stacked bar chart, displays
the statistics by district used to determine gerrymandering, and computes whether there was
gerrymandering in this election in favor of the Democrats or Republicans.


Document Assistance: I neither gave nor recieved any assistance to anyone. 



"""

from graphics2 import *

FILE_NAME = 'districts.txt'
MIN_NUM_DISTRICTS = 2
EFFICIENCY_GAP_LIMIT = 8

#constants for the window created
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750
DEFAULT_BAR_HEIGHT = 20
SPACE_BETWEEN = 5

def main():
    #open the file that is going to be read
    file = open(FILE_NAME, 'r')
    getStateFile = open(FILE_NAME, 'r')
    state = input('Which state do you want to look up? ')
    print()
    state = state.title()
    
    #initialize constants for surplus computation
    surplus_d_sum = 0
    surplus_r_sum = 0
    total_vote_sum = 0
    
    #initialize constant for the loop of drawing the bar
    space = 0
    
    while state == '':
        print("You didn't enter anything! Please enter a valid state. ")
        state = input('Which state do you want to look up? ')
        print()
        state = state.title()
    states = []
    for lines in getStateFile:
        file_lists = lines.split(',')
        states.append(file_lists[0])
        
    while state not in states:
        print('Invalid state name. Enter state name again.')
        state = input('Which state do you want to look up? ')
        print()
        state = state.title()
        while state == '':
            print("You didn't enter anything! Please enter a valid state. ")
            state = input('Which state do you want to look up? ')
            print()
            state = state.title()
    
    #read each line of the file
    for line in file:
        file_list = line.split(',')
        if state == file_list[0]:
            state_list = file_list[1:]
            num_district = len(state_list) / 3
            print(f'District   Democratic Votes   Republican Votes   Surplus Democrat   Surplus Republican')
            
            #create a window
            window = GraphWin(f'District Overview for {state}', WINDOW_WIDTH, WINDOW_HEIGHT)
            window.setBackground('white')
            
            #draw a line at the center of the window
            upperLeft = Point(250, 0)
            lowerRight = Point(250, 750)
            bar_d = Line(upperLeft, lowerRight)
            bar_d.setFill('black')
            bar_d.draw(window)
            
            
            #decrase the bar height if the bars do not fit in the window
            if ((SPACE_BETWEEN * num_district) + (DEFAULT_BAR_HEIGHT * num_district)) > WINDOW_HEIGHT - SPACE_BETWEEN:
                new_bar_height = ((WINDOW_HEIGHT - SPACE_BETWEEN) - (SPACE_BETWEEN * num_district)) / (num_district)
            else:
                new_bar_height = DEFAULT_BAR_HEIGHT
                
            #loop through all the district to compute surplus and also draw the bar in the window
            for num in range(0, len(state_list), 3):
                district = state_list[num]
                
                #compute party votes, majority and surplus votes
                democratic_vote = int(state_list[num + 1])
                republican_vote = int(state_list[num + 2])
                total_vote = democratic_vote + republican_vote
                total_vote_sum = total_vote_sum + total_vote
                majority = int(((democratic_vote + republican_vote)/2) + 1)
                surplus_d = int(democratic_vote - majority)
                surplus_r = int(republican_vote - majority)
                
                #conditions for computing surplus votes
                if democratic_vote > republican_vote:
                    surplus_r = republican_vote
                elif democratic_vote + republican_vote == 0:
                    surplus_r = 0
                    surplus_d = 0
                else:
                    surplus_d = democratic_vote
                
                #sum of all the surplus votes of Democrats and Republicans 
                surplus_d_sum = surplus_d_sum + surplus_d
                surplus_r_sum = surplus_r_sum + surplus_r
                
                #computation of gerrymandering
                diffrence_democratic = surplus_d_sum - surplus_r_sum
                diffrence_republican = surplus_r_sum - surplus_d_sum
                gerrymandering_d = round((diffrence_democratic / total_vote_sum) * 100, 2)
                gerrymandering_r = round((diffrence_republican / total_vote_sum) * 100, 2)
                
                #condition for districts that have zero vote from both party
                if democratic_vote + republican_vote != 0:
                    width_democrats = (democratic_vote / total_vote) * WINDOW_WIDTH
                    
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
                
                #print party votes and surplus votes properly aligned 
                print(f'{district:>4}   {democratic_vote:16,}{republican_vote:19,}{surplus_d:19,}{surplus_r:19,}')
            print()
            
            #print each party's total surplus vote
            print(f'Total surplus Democratic votes: {surplus_d_sum:,}')
            print(f'Total surplus Republican votes: {surplus_r_sum:,}')
            
            #condition for determining and computing gerrymandeing
            if num_district <= MIN_NUM_DISTRICTS:
                print('Gerrymandering computation only valid when more than 2 districts.')
            elif gerrymandering_d >= EFFICIENCY_GAP_LIMIT:
                seat = round((gerrymandering_d / (100 / num_district)), 2)
                print(f'Gerrymandering in {state} favoring Republicans worth {seat} congressional seats.')
            elif gerrymandering_r >= EFFICIENCY_GAP_LIMIT:
                seat = round((gerrymandering_r / (100 / num_district)), 2)
                print(f'Gerrymandering in {state} favoring Democrats worth {seat} congressional seats.')
            else:
                print('No evidence of gerrymandering in', state + '.')


    #close file      
    file.close()        
main()