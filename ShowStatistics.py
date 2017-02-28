
import sys
import os
import csv
import glob

def ProcessCSVRow(csvRow):

    # Here we know that both corresponind frames exist, so we can move on to class conversion (see existing code) and building a distribution. If we know how many there are valid samples per class (144 in total), we can compute chance levels for our dataset. This only makes sense to do for the testing set, however it will also be useful to check the other partitions as well. We should only consider one webcam for now, however this does not mean that we don't want to check that all entries of CSV have two frames and vice versa - every frame has a CSV entry located by the timestamp value.

    return

def ProcessFolder(folderPath):
    # Get total number of frames
    nFrames = len(glob.glob(os.path.join(folderPath, '*.png')))

    # Analyse CSV
    csvPath = os.path.join(folderPath, 'sensor.csv')
    with open(csvPath, 'rb') as csvFile:

        nRightImages = 0
        nLeftImages = 0
        nCSVRows = 0

        csvReader = csv.reader(csvFile, delimiter=',')
        for csvRow in csvReader:
            if len(csvRow) != 17:
                print '\n >> ERROR: Invalid column number \n'
                continue

            nCSVRows += 1
            timestamp = csvRow[-1]

            rightImageName = 'webcamera-' + str(timestamp) + '-right.png'
            rightImagePath = os.path.join(folderPath, rightImageName)
            if os.path.isfile(rightImagePath):
                nRightImages += 1

            leftImageName = 'webcamera-' + str(timestamp) + '-left.png'
            leftImagePath = os.path.join(folderPath, leftImageName)
            if os.path.isfile(leftImagePath):
                nLeftImages += 1

            if os.path.isfile(rightImagePath) and os.path.isfile(leftImagePath):
                ProcessCSVRow(csvRow)

        if nCSVRows != nRightImages + nLeftImages:
            print '\n >> ERROR: Some rows point to non-existing frames:'
            print '\t >> Number of right camera frames: ' + str(nRightImages)
            print '\t >> Number of left  camera frames: ' + str(nLeftImages)
            print '\t >> Number of CSV rows: ' + str(nCSVRows)

        if nCSVRows != nFrames:
            print '\n >> ERROR: Some frames are not listed in the CSV:'
            print '\t >> Number of frames: ' + str(nFrames)
            print '\t >> Number of CSV rows: ' + str(nCSVRows)

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> Partition path is required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition path: \"' + partitionPath + '\"'

    # Get list of folders within partition
    folders = os.listdir(partitionPath)
    counter = 0
    for folder in folders:
        folderPath = os.path.join(partitionPath, folder)
        if os.path.isdir(folderPath):
            counter += 1
            print '\n >> ' + str(counter) + '. Looking into: \"' + folder + '\" ... '
            ProcessFolder(folderPath)

    print

if __name__ == "__main__":
    main()
