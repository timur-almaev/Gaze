
import sys
import os
import csv
import glob
import numpy as np

def ProcessFrames( folderPath ):

    # Compose path to sensor readings csv
    csvPath = os.path.join(folderPath, 'sensor.csv')

    # Check if sensor readings file exist, return error otherwise
    if not os.path.isfile(csvPath):
        print ' >> ERROR - Sensor readings not found'
        return

    # Read CSV sensor readings file into numpy matrix
    csvRows = np.genfromtxt(csvPath, delimiter=',')

    # Remove first headers row
    csvRows = np.delete(csvRows, (0), axis=0)

    # Compose output filename
    outputPath = os.path.basename(folderPath) + '.csv'

    return

    statistics = np.asarray([])

    # What we need here is for every frame find the difference as below, however take it further and save the filename along with the corresponding csv row (picked by index) and the value of difference to the output csv

    # Make sure when you load csv and then save it nothing there changes

    # You can make it easier to yourself if you define the columns of the csv that you need

    nGoodFrames = 0
    frames = np.asarray(glob.glob(os.path.join(folderPath, '*.png')))
    for frame in frames:
        frameTimeStamp = long(os.path.basename(frame).split('-')[1])
        diff = np.zeros((len(csvTimeStamps), 2))
        diff[:,0] = np.arange(0, len(csvTimeStamps), 1)
        diff[:,1] = np.absolute(csvTimeStamps - frameTimeStamp)
        diff = diff[diff[:, 1].argsort()]

        diff[0,1]

        if statistics.size == 0:
            statistics = np.asarray([folder, str(nFrames), str(nSensorReadings), str(nGoodFrames)])
        else:
            statistics = np.vstack((statistics, [folder, str(nFrames), str(nSensorReadings), str(nGoodFrames)]))

    np.savetxt(outputPath, statistics, delimiter=",", fmt="%s")

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> Partition path required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition path: \"' + partitionPath + '\"'

    folders = os.listdir(partitionPath)
    counter = 0
    for folder in folders:
        folderPath = os.path.join(partitionPath, folder)
        if os.path.isdir(folderPath):
            counter += 1
            print '\n >> ' + str(counter) + '. Looking into: \"' + folder + '\" ... '
            ProcessFrames(folderPath)

    print

if __name__ == "__main__":
    main()
