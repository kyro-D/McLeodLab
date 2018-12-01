#McLeod Lab Printer Software 
#Written by Kyle Rose for Python 2


#imports
import nidaqmx.system
from time import sleep

import os
from ctypes import *
from scipy import misc

import XPS_Q8_drivers
import sys

def main():
    print "Welcome"
    numOfSteps = 200;


if __name__ == '__main__':
    main()


#TODO make deconstructor, and Main printing function that calls all the subclasses
class Print:
    #This is the main class that will handle all of the printing
    def __init__(self, exposeTime, waitTime, numberOfSteps, numberOfImages):
        self.exptime = exposeTime
        self.numOfSteps = numberOfSteps
        self.numOfImgs = numberOfImages
        self.wait = waitTime


    def generateActuatorPositions(self, numberOfSteps, actuator1Position, \
        actuator2OffPosition, actuator2OnPosition, actuator3OffPosition, actuator3OnPosition, \
        actuator3StepSize, actuator4Position, actuator5Position, actuator6Postion, actuator7Position):
        #This function generates an array to map the actuator positions during each step of the print
        #make sure the arguments given are in units of micro meters

        act1Pos = actuator1Position
        act2OffPos = actuator2OffPosition
        act2OnPos = actuator2OnPosition
        act3OffStart = actuator3OffPosition
        act3OnStart = actuator3OnPosition
        act3Step = actuator3StepSize
        act4Pos = actuator4Position
        act5Pos = actuator5Position
        act6Pos = actuator6Postion
        act7Pos = actuator7Position

        #the 2D array to be populated with actuator positions
        actuatorPositions = []
        #array that has the following elements and is inserted into actuatorPositions at each iteration of loop
        stepList = []

        for step in range(numberOfSteps):
            #step list will have the following form at the end of the loop
            #act1pos, act2pos, act3pos, act4pos, act5pos, act6pos, act7pos
            
            #clear the list so it is empty at begininng of each loop
            stepList.clear()


            stepList.append(act1Pos)
            if(step % 2) == 0:
                #Even step number
                stepList.append(act2OnPos)
                stepList.append(act3OnStart - ((step-1)/2)*act3Step)
            else :
                #Odd number steps
                stepList.append(act2OffPos)
                stepList.append(act3OffStart-((step-1)/2)*act3Step)
            #insert the rest of the elements
            stepList.append(act4Pos)
            stepList.append(act5Pos)
            stepList.append(act6Pos)
            stepList.append(act7Pos)

            #insert stepList into actuatorPositions
            actuatorPositions.append(stepList)


        #return the 2d array
        return actuatorPositions


class SLMSequencer:
    #This class will handle all of the image storage and processing 

class XPSController:
    #This class will handle all of the actuator operations

    def __init__(self, numberOfSteps, numberOfImages):
        self.numSteps = numberOfSteps
        self.numImgs = numberOfImages
        self.myxps = XPS_Q8_drivers.XPS()



    def displayErrorAndClose (self, socketId, errorCode, APIName): 
        if (errorCode != -2) and (errorCode != -108):
            [errorCode2, errorString] = self.myxps.ErrorStringGet(socketId,errorCode)
            if(errorCode2 != 0):
                print APIName + ': ERROR ' + str(errorCode)
            else:
                print APIName + ': ' + errorString
        else:
            if (errorCode == -2):
                print APIName + ': TCP timeout'
            if (errorCode == -108):
               print APIName + ': The TCP/IP connection was closed by an administrator'

        self.myxps.TCP_CloseSocket(socketId)
        return
    

    def connectToXPS(self, ipAddress):
        # Connect to the XPS
        socketId = self.myxps.TCP_ConnectToServer(ipAddress, 5001, 20)
        print("Socket Id: ", socketId)
        # Check connection passed
        if (socketId == -1):
            print 'Connection to XPS failed, check IP & Port'
            sys.exit ()
        return

    #MUST CALL THIS METHOD AFTER MAKING CONNECTION TO XPS via connectToXPS() method
    #groupName must be of the form 'GROUP(1-7)'
    def initalizeActuatorGroup(self, groupName):
        group = groupName






class LEDController:
    #This class will handle all of the LED operations
    def __init__(self):


    def expose(self, exposeTime):
        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
            'Dev1/port1/line3',
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)

            try:
                task.write(True, auto_start=True)

            except nidaqmx.DaqError as e:
                print 'error ' , e

            sleep(exposeTime)

            try:
                task.write(False, auto_start=True)

            except nidaqmx.DaqError as e:
                print 'error ' , e


            return

    def __del__(self):
        #turn off the laser when the instance is deleted
        with nidaqmx.Task() as task:
            task.do_channels.add_do_chan(
            'Dev1/port1/line3',
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES)


        try:
            task.write(False, auto_start=True)

        except nidaqmx.DaqError as e:
            print 'error ' , e





class SLMController:
    #This class will handle all of the slm operations and utiliizes the class SLMSequencer










