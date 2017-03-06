
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import numpy as np

def ProcessPair(timestamp, sTimeStamps):

    # Compute difference between the timestamp and every sensor reading
    diff = np.absolute(sTimeStamps - timestamp) # pylint: disable=I0011,E1101

    # Find the minimum difference
    mindiff = diff.min()

    # Find the indexes of the minimum difference
    indexes = np.where(diff == mindiff)
    index = indexes[0]

    # If there is more than one minimum complain and skip
    if len(index) > 1:
        print '\t >> WARNING - Multiple minimum found'
        index = index[0]

    basename = 'webcamera-' + str(long(timestamp))
    stimestamp = sTimeStamps[index]
    content = [basename, str(long(stimestamp)), str(int(mindiff)), str(int(index))]

    return content
