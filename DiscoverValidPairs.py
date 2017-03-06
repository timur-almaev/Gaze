
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

import sys
import os

from ProcessRecording import ProcessRecording

def main():
    os.system('clear')
    os.system('rm *.csv')

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
            print ' >> %02d. Looking into: \"%s\" ... ' % (counter, folder, )
            ProcessRecording(folderPath)

if __name__ == "__main__":
    main()
