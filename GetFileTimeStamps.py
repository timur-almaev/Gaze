
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import glob
import os
import numpy as np

def GetFileTimeStamps(folderPath):

    # Establish frame files pattern
    pattern = os.path.join(folderPath, '*.png')

    # Query frames
    listing = glob.glob(pattern)
    
    # Display total number of frames
    print '\n\t >> #Frames: ' + str(len(listing))

    timestamps = []
    for element in listing:
        timestamp = os.path.basename(element).split('-')[1]
        timestamps.append(timestamp)

    timestamps = list(set(timestamps))
    timestamps = np.asarray(timestamps, dtype=float)

    return timestamps
