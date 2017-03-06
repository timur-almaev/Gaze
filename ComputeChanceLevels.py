
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import sys
import os 
import glob
import numpy as np

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> Partition path required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition path: \"' + partitionPath + '\" \n'

    pattern = os.path.join(partitionPath, '*.csv')
    listing = glob.glob(pattern)

    lEyeHistogram = np.empty((len(listing), 13))
    rEyeHistogram = np.empty((len(listing), 13))

    hCounter = 0
    for element in listing:
        print ' >> Checking ' + os.path.basename(element) + ' ... '

        data = np.genfromtxt(element, delimiter=',')
        data = np.delete(data, (0), axis=0)

        lEyeClasses = data[:, 6]
        rEyeClasses = data[:, 9]

        lEyeHistogram[hCounter, :] = np.histogram(lEyeClasses, bins=range(14))[0]
        rEyeHistogram[hCounter, :] = np.histogram(rEyeClasses, bins=range(14))[0]

        hCounter += 1

    lEyeHistogram = lEyeHistogram.sum(axis=0)
    rEyeHistogram = rEyeHistogram.sum(axis=0)

    lEyeHistogram = lEyeHistogram[1:]
    rEyeHistogram = rEyeHistogram[1:]

    lEyeHistogram = lEyeHistogram / lEyeHistogram.sum()
    rEyeHistogram = rEyeHistogram / rEyeHistogram.sum()

    # Normalise histograms
    lEyeHistogram = (lEyeHistogram - lEyeHistogram.min()) / (lEyeHistogram.max() - lEyeHistogram.min())
    rEyeHistogram = (rEyeHistogram - rEyeHistogram.min()) / (rEyeHistogram.max() - rEyeHistogram.min())

    print lEyeHistogram
    print rEyeHistogram

if __name__ == "__main__":
    main()
