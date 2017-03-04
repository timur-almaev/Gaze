
import sys
import os
import csv
import glob
import numpy as np

def ProcessFolder( folderPath ):

    # Compose path to sensor readings csv
    csvPath = os.path.join(folderPath, 'sensor.csv')

    # Check if sensor readings file exist, return error otherwise
    if not os.path.isfile(csvPath):
        print '\n\t >> ERROR - Sensor readings not found \n'
        return

    # Read CSV sensor readings file into numpy matrix
    csvRows = np.genfromtxt(csvPath, delimiter=',')

    # Get the last column of readings with timestamps
    csvTimeStamps = csvRows[:,-1]

    # Remove first header row
    csvTimeStamps = np.delete(csvTimeStamps, 0)

    # Query all right camera frames
    listing = np.asarray(glob.glob(os.path.join(folderPath, '*.png')))

    lFrameMissing = 0
    rFrameMissing = 0

    frames = np.asarray(['filename', 'ftimestamp', 'stimestamp', 'mindiff', 'sindex'])
    for element in listing:

        # Extract filebase
        filebase = os.path.basename(element).split('-')[0] + '-' + os.path.basename(element).split('-')[1]

        # Compose left camera filename
        lfilename = os.path.join(folderPath, filebase + '-left.png')

        # Make sure left frame is present as well
        if not os.path.isfile(lfilename):
            lFrameMissing += 1
            continue

        # Compose right camera filename
        rfilename = os.path.join(folderPath, filebase + '-right.png')

        # Make sure left frame is present as well
        if not os.path.isfile(rfilename):
            rFrameMissing += 1
            continue

        # Extract timestamp from the filename
        timeStamp = long(os.path.basename(element).split('-')[1])

        # Compute difference between the timestamp and every sensor reading
        diff = np.absolute(csvTimeStamps - timeStamp)

        # Find the minimum difference
        mindiff = diff.min()

        # Find the indexes of the minimum difference
        indexes = np.where(diff == mindiff)
        index = indexes[0]

        # You might want to make sure that if you take the first minimum
        # it's actually the best possible value

        # If there is more than one minimum complain and skip
        if len(index) > 1:
            index = index[0]

        # Compose CSV line with the filename, frame timestamp, the closest sensor
        # timestamp, the value of the difference between the two and the corresponind
        # sensor reading index.
        content = [os.path.basename(element), str(timeStamp), str(long(csvTimeStamps[index])), str(int(mindiff)), str(int(index))]

        # Add frame to the list
        frames = np.vstack((frames, content))

    print '\n\t >> Missing left  frames: ' + str(lFrameMissing)
    print '\t >> Missing right frames: ' + str(rFrameMissing) + '\n'

    # Compose output filename
    outputPath = os.path.basename(folderPath) + '.csv'

    # Save the result
    np.savetxt(outputPath, frames, delimiter=",", fmt="%s")

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> ERROR - Partition path required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition path: \"' + partitionPath + '\" \n'

    folders = os.listdir(partitionPath)
    counter = 0
    for folder in folders:
        folderPath = os.path.join(partitionPath, folder)
        if os.path.isdir(folderPath):
            counter += 1
            print ' >> %02d. Looking into: \"%s\" ... ' % (counter,folder,)
            ProcessFolder(folderPath)

    print

if __name__ == "__main__":
    main()
