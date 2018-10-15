##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a point
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: Andrea Alatorre - aa449@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import modules
import sys, os, arcpy

# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

# Open the ARGOS data file for reading
inputFileObj = open(inputFile, 'r')

# Get the first line of data so we can use a while loop
lineString = inputFileObj.readline()
while lineString:

    #So that it doesn't include the very first line, use "Date :" instead of "Date"
    if "Date :" in lineString:

    # Split the lineString into a list. Split() defaults to a space.
        lineList = lineString.split()

        # Get attributes from first line
        tagID = lineList[0]
        break
    
    #Get the next line
    lineString = inputFileObj.readline()