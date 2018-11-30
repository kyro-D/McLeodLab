# --------- Python program: XPS controller demonstration --------
#
import XPS_Q8_drivers

import sys
# Display error function: simplify error print out and closes  socket
def displayErrorAndClose (socketId, errorCode, APIName): 
    if (errorCode != -2) and (errorCode != -108):
        [errorCode2, errorString] = myxps.ErrorStringGet(socketId,errorCode)
        if(errorCode2 != 0):
            print APIName + ': ERROR ' + str(errorCode)
        else:
            print APIName + ': ' + errorString
    else:
        if (errorCode == -2):
            print APIName + ': TCP timeout'
        if (errorCode == -108):
           print APIName + ': The TCP/IP connection was closed by an administrator'

    myxps.TCP_CloseSocket(socketId)
    return
    
# Instantiate the class
myxps = XPS_Q8_drivers.XPS()

# Connect to the XPS
socketId = myxps.TCP_ConnectToServer('128.138.189.69', 5001, 20)
print("Socket Id: ", socketId)
# Check connection passed
if (socketId == -1):
    print 'Connection to XPS failed, check IP & Port'
    sys.exit ()
# Add here your personal codes, below for example:
# Define the positioner
print "Made it 0.0"
group = 'GROUP7'
positioner = group + '.POSITIONER'
print"Made it 0.1"


# Kill the group
[errorCode, returnString] = myxps.GroupKill(socketId, group)
if (errorCode != 0):
    displayErrorAndClose (socketId, errorCode, 'GroupKill')
    sys.exit ()
print "Made it 0.2"
#initalize the group
[errorCode, returnString] = myxps.GroupInitialize(socketId, group)
if (errorCode != 0):
    displayErrorAndClose (socketId, errorCode, 'GroupKill')
    sys.exit ()
print "Made it .3"

# Home Search IE move it back to 0
[errorCode, returnString] = myxps.GroupHomeSearch(socketId, group)
if(errorCode !=0):
    displayErrorAndClose(socketId, errorCode, 'GroupHomeSearch')
    sys.exit()





#MAKe some MOVES BABY
[errorCode, returnString] = myxps.GroupMoveAbsolute(socketId, positioner, [10.0])
if(errorCode != 0):
    displayErrorAndClose (socketId, errorCode, 'GroupMoveAbsolute')
    sys.exit

[errorCode, returnString] = myxps.GroupMoveRelative(socketId, positioner, [-10.0])
if(errorCode != 0):
    displayErrorAndClose (socketId, errorCode, 'GroupMoveAbsolute')
    sys.exit





# Close connection
myxps.TCP_CloseSocket(socketId)
print "FINISHED TEST"
#----------- End of the demo program ----------#
