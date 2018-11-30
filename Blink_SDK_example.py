# Example usage of Blink_SDK_C.dll
# Meadowlark Optics Spatial Light Modulators
# Dec 5 2016

import os
from ctypes import *
from scipy import misc
from time import sleep

# Load the DLL
# BlinkHdmiSdk.dll, HdmiDisplay.dll, freeglut.dll and glew64/32.dll
# should all be located in the same directory as the program referencing the
# library
cdll.LoadLibrary("BlinkHdmiSdk")
slm_lib = CDLL("BlinkHdmiSdk")

# Path to this example and the files it references
# Remember to escape the backslash
path = "C:\\Program Files\\Meadowlark Optics\\Blink 1920 HDMI\\Image Files"
lut_file = "C:\\Program Files\\Meadowlark Optics\\Blink 1920 HDMI\\LUT Files\\linear.blt"
com_port = "COM1"

# Arrays for image data
mlo_image = misc.imread(os.path.join(path, "mlo.bmp"), flatten = 0, mode = 'RGB')
wedge_image = misc.imread(os.path.join(path, "half_wedge.bmp"), flatten = 0, mode = 'RGB')

# Array for LUT data
lut = (c_ushort * 256)()

# Call the Create_SDK constructor
# Returns a handle that's passed to subsequent SDK calls
sdk = slm_lib.Create_SDK()

print "Blink SDK was successfully constructed"

# Read the lookup table into memory
slm_lib.Read_lut(sdk, lut_file, lut)

# Load the lookup table to the controller
slm_lib.Load_lut(sdk, com_port, lut)

# Loop between our ramp images
for i in range(0, 10):
    slm_lib.Write_image(sdk, mlo_image.ctypes.data_as(POINTER(c_ubyte)), 0)
    sleep(0.5) # This is in seconds
    slm_lib.Write_image(sdk, wedge_image.ctypes.data_as(POINTER(c_ubyte)), 0)
    sleep(0.5) # This is in seconds

# Always call Delete_SDK before exiting
slm_lib.Delete_SDK(sdk)
