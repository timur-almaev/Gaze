
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import os
import numpy as np

def GetSensorReadings(folderPath):

    # Compose path to sensor readings csv
    csvPath = os.path.join(folderPath, 'sensor.csv')

    # Check if sensor readings file exist, return error otherwise
    if not os.path.isfile(csvPath):
        print '\n\t >> ERROR - Sensor readings not found \n'
        return

    # Read CSV sensor readings file into numpy matrix
    csvReadings = np.genfromtxt(csvPath, delimiter=',')

    # Remove first header row
    csvReadings = np.delete(csvReadings, (0), axis=0)

    # Print total number of sensor readings
    print '\t >> #Sensor readings: ' + str(csvReadings.shape[0])

    return csvReadings
