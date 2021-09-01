import pyautogui as pg
import random
import time

#y = pg.size()
#x = pg.position()

#print ("size")
#print (y)
#print (x)

while True:
    
    #width = random.randint(0, 1600)
    #height = random.randint(0, 900)
    #print (width)
    #print (height)
    
    # here type a x and y position in addition of number of seconds that you wish the mouse cursor move to that spesific location
    #pg.moveTo(x,y,time in seconds)
 
    pg.moveTo(87,706,4)
    pg.click()

    #here 60 refer to 60 seconds to hold up and then move the mouse cursor to a new location

    time.sleep(60)
    pg.moveTo(88,825,4)
    pg.click()
    time.sleep(60)
    
    
     
