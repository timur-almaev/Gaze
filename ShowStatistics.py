
import sys
import os
import csv

def ProcessFolder(folderPath):
    print ' >> Loading \"sensor.csv\" ... '
    csvPath = os.path.join(folderPath, 'sensor.csv')
    with open(csvPath, 'rb') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')

        # Each csvRow is a list of 17 entries
        # Make sure every row has 17 entries
        # Each frame is named as "webcamera-<timestamp>-[left|right].png"
        # Each frame must exist
        # The number of frames must be equal to the number of csv rows
        for csvRow in csvReader:

            timestamp = csvRow[-1]
            continue

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> Partition path is required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition path: \"' + partitionPath + '\"'

    # Get list of folders within partition
    folders = os.listdir(partitionPath)
    for folder in folders:
        folderPath = os.path.join(partitionPath, folder)
        if os.path.isdir(folderPath):
            print '\n >> Looking into: \"' + folder + '\" ... '
            ProcessFolder(folderPath)

    print

if __name__ == "__main__":
    main()
