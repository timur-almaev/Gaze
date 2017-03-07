
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import sys
import os 
import glob
import numpy as np

def BuildHistogram(arr, fname):

    # Get the sum of rows
    arr = arr.sum(axis=0)

    # Remove first column (class 0)
    arr = arr[1:]

    arr = arr / arr.sum()

    # Print distribution
    for element in arr:
        print element
    print

    # Save distribution
    np.savetxt(fname, arr, delimiter=",", fmt="%s")

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> Partition path required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition path: \"' + partitionPath + '\" \n'

    leftEyeDistribtionCSV = os.path.join(partitionPath, 'left-eye-distribution.csv')
    if os.path.isfile(leftEyeDistribtionCSV):
        print ' >> Found exisitng left eye distribution CSV. Removing ... '
        os.remove(leftEyeDistribtionCSV)

    rightEyeDistribtionCSV = os.path.join(partitionPath, 'right-eye-distribution.csv')
    if os.path.isfile(rightEyeDistribtionCSV):
        print ' >> Found exisitng right eye distribution CSV. Removing ... '
        os.remove(rightEyeDistribtionCSV)

    pattern = os.path.join(partitionPath, '*.csv')
    listing = glob.glob(pattern)

    lEyeHistogram = np.empty((len(listing), 13))
    rEyeHistogram = np.empty((len(listing), 13))

    hCounter = 0
    for element in listing:
        print '\n >> Checking \"' + os.path.basename(element) + '\" ... '

        data = np.genfromtxt(element, delimiter=',')
        data = np.delete(data, (0), axis=0)

        lEyeClasses = data[:, 6]
        rEyeClasses = data[:, 9]

        lEyeHistogram[hCounter, :] = np.histogram(lEyeClasses, bins=range(14))[0]
        rEyeHistogram[hCounter, :] = np.histogram(rEyeClasses, bins=range(14))[0]

        hCounter += 1

    print '\n >> Left eye distribution: \n'
    BuildHistogram(lEyeHistogram, leftEyeDistribtionCSV)

    print '\n >> Right eye distribution: \n'
    BuildHistogram(rEyeHistogram, rightEyeDistribtionCSV)

if __name__ == "__main__":
    main()
