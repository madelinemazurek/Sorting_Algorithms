#Author: Madeline Mazurek
#Date: Nov 8th 2021

#This is a program that uses the graphics.py library 
# to display a visual representation of various sorting 
# algorithms

#Note: https://www.programiz.com was used as a learning 
# resource for the various sorting algorithms used in this 
# code

import random # used to randomize list
import time # used to create pauses for animantion
from graphics import * # used to create data visualization

# window and list global functions
win = GraphWin("MySort", 1035, 500)
list = []

def main():
    # iterate through all types of sorts
    win.getMouse() # Pause before sorting
    bubbleSort()
    insertionSort()
    selectionSort()
    cocktailSort()
    win.getMouse() # Pause before closing
    win.close()    # Close window when done

# creates a randomized list of 50 elements 
# ranging from 0 to 250 for rgb values
def randomList():
    list.clear()
    for i in range(50):
        list.append(i*5)
    random.shuffle(list)

#initializes screen to hold random output and algorithm name
def setScreen(title):
    # fill screen black
    r = Rectangle(Point(0, 0), Point(1034, 499))
    r.setOutline("black")
    r.setFill("black")
    r.draw(win)
    
    # write name of sort
    t = Text(Point(515, 80), title)
    t.setFill("white")
    t.setSize(30)
    t.setStyle("bold")
    t.draw(win)
    
    #draw 50 rectangles on screen
    populate()

# draw all rectangles in list
def populate():
    for i in range(50):
        drawRect(i)

# draw a single element based on index in list
def drawRect(index):
    xOffset = 20 + (index * 20) # find x location
    r = Rectangle(Point(xOffset,150), Point(15+xOffset,450))
    #creates a blue-red gradient based on index values
    r.setFill(color_rgb(list[index], 100, 255- list[index]))
    r.draw(win)

# draw updated values for two elements and pause
def updateswap(rec1, rec2):
    drawRect(rec1)
    drawRect(rec2)
    time.sleep(0.001)
    
# draw updated values for one element and pause
def update(rec):
    drawRect(rec)
    time.sleep(0.001)
        
def bubbleSort():
    randomList()
    setScreen("BUBBLE SORTER")
    time.sleep(1) #pause before sorting
    
    #iteratre through all elements
    for i in range(len(list)): 
        #on each element, compare up to sorted section        
        for j in range(0, len(list) - i - 1): 
            #compare with neighbour, switch if in wrong order
            if (list[j] > list[j + 1]): 
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                updateswap(j, j+1) #display change
                
    time.sleep(1) # pause before next sort
    
def insertionSort():
    randomList()
    setScreen("INSERTION SORTER")
    time.sleep(1) #pause before sorting
    
    #iterate through all elements
    for i in range(1, len(list)):
        curr = list[i] 
        j = i - 1
        
        # search for correct spot of curr in sorted portion
        # stop when an element smaller than curr is found
        while j >= 0 and curr < list[j]:
            list[j + 1] = list[j]
            updateswap(j, j + 1) #display changes of shifting values
            j = j - 1
        
        # Place key at after the element just smaller than it.
        list[j + 1] = curr
        update(j + 1)
       
    time.sleep(1) # pause before next sort
    
def selectionSort():
    randomList()
    setScreen("SELECTION SORTER")
    time.sleep(1) #pause before sorting
    
    #iterate through all elements
    for i in range(len(list)):
        #initialize smallest as first element
        smallest = i

        #in remaining unsorted section find smallest value 
        # element and assign to smallest
        for j in range(i + 1, len(list)):
            time.sleep(0.001) #delay for each comparison
            if list[j] < list[smallest]:
                smallest = j
         
        # put min at beginning of unsorted section
        temp = list[i]
        list[i] = list[smallest]
        list[smallest] = temp
        updateswap(i, smallest)
                
    time.sleep(1) # pause before next sort

def cocktailSort():
    randomList()
    setScreen("COCKTAIL SORTER")
    time.sleep(1) #pause before sorting

    flag = True
    start = 0
    end = len(list) - 1
    while (flag==True):
        # assume list is not yet sorted
        flag = False
        # left to right
        for i in range (start, end):
            if (list[i] > list[i+1]): # move greatest element to end
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                updateswap(i, i + 1)
                flag=True
        # if no swap takes place array is sorted
        if (flag==False):
            break
        # otherwise, reset the flag and move endpoint
        # (last item must be sorted)
        flag = False
        end -= 1
        # right to left
        for i in range(end-1, start-1,-1):
            if (list[i] > list[i+1]): # move smallest element to front
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                updateswap(i, i + 1)
                flag = True
        # move startpoint (first item is sorted)
        start += 1
        
    time.sleep(1) # pause before next sort
        
main()