#McLeod Lab Printer Software 
#Written by Kyle Rose for Python 2


def main():
    print "Welcome"
    numOfSteps = 200;


if __name__ == '__main__':
    main()



class Print:
    #This is the main class that will handle all of the printing
    def __init__(self, exposeTime, waitTime, numberOfSteps, numberOfImages):
        exptime = exposeTime
        numOfSteps = numberOfSteps
        numOfImgs = numberOfImages
        wait = waitTime


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




        




