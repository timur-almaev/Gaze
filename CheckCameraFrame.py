
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import os

def CheckCameraFrame(folderPath, timestamp, suffix):

    # Compose camera filename
    filename = os.path.join(folderPath, 'webcamera-' + str(long(timestamp)) + suffix)

    # Make sure left frame is present as well
    if not os.path.isfile(filename):
        return False

    return True
