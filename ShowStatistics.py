
import sys
import os

def main():
    os.system('clear')

    if len(sys.argv) < 2:
        print '\n >> Partition path is required \n'
        return

    partitionPath = sys.argv[1]
    print '\n >> Partition Path: \"' + partitionPath + '\"'

    # Get list of folders within partition
    folders = os.listdir(partitionPath)
    for folder in folders:
        folderPath = os.path.join(partitionPath, folder)
        if os.path.isdir(folderPath):
            print '\n >> Looking into: \"' + folder + '\" ... '

    print

if __name__ == "__main__":
    main()
