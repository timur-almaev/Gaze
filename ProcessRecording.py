
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import os
import numpy as np

from GetFileTimeStamps import GetFileTimeStamps
from GetSensorReadings import GetSensorReadings
from CheckCameraFrame  import CheckCameraFrame
from ProcessPair       import ProcessPair

def ProcessRecording(folderPath):

    fTimestamps = GetFileTimeStamps(folderPath)
    csvReadings = GetSensorReadings(folderPath)
    
    # Get the last column of readings with timestamps
    sTimeStamps = csvReadings[:, -1]

    frames = np.asarray(['filename', 'stimestamp', 'diff', 'sindex', 
                         'left-eye-i', 'left-eye-j', 'right-eye-i', 'right-eye-j'])
    for timestamp in fTimestamps:

        if not CheckCameraFrame(folderPath, timestamp, '-right.png'):
            continue

        if not CheckCameraFrame(folderPath, timestamp, '-left.png'):
            continue

        # Add frame pair to the list
        pair = ProcessPair(timestamp, sTimeStamps, csvReadings) # pylint: disable=I0011,E1121
        frames = np.vstack((frames, pair))

    # Print total number of pairs
    print '\t >> Number of pairs: ' + str(frames.shape[0] - 1) + '\n'

    # Compose output filename
    outputPath = os.path.basename(folderPath) + '.csv'

    # Save the result
    np.savetxt(outputPath, frames, delimiter=",", fmt="%s")
