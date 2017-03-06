
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import os
import numpy as np

def GetSensorTimeStamps(folderPath):

    # Compose path to sensor readings csv
    csvPath = os.path.join(folderPath, 'sensor.csv')

    # Check if sensor readings file exist, return error otherwise
    if not os.path.isfile(csvPath):
        print '\n\t >> ERROR - Sensor readings not found \n'
        return

    # Read CSV sensor readings file into numpy matrix
    csvReading = np.genfromtxt(csvPath, delimiter=',')

    # Get the last column of readings with timestamps
    csvTimeStamps = csvReading[:, -1]

    # Remove first header row
    csvTimeStamps = np.delete(csvTimeStamps, 0)

    # Print total number of sensor readings
    print '\t >> Number of sensor readings: ' + str(len(csvTimeStamps))

    return csvTimeStamps
