
# pylint: disable=I0011,C0103
# pylint: disable=I0011,C0303
# pylint: disable=I0011,C0111

# This function can compute the boundaries of each class
# given screen resolution. Currently it is 1920x1080, which
# make the size of a segment 480x360.

screenDimX = 1920
screenDimY = 1080

def Coordinates2EyeClasses(i, j):
    label = 0

    segmentX = screenDimX / 4
    segmentY = screenDimY / 3



    if i <= 0 or j <= 0:
        return 0

    if i > screenDimX or j > screenDimY:
        return 0



    if i <= segmentX and j <= segmentY:
        label = 1
    
    if i > segmentX and i <= (segmentX * 2) and j <= segmentY:
        label = 2
    
    if i > (segmentX * 2) and i <= (segmentX * 3) and j <= segmentY:
        label = 3
    
    if i > (segmentX * 3) and j <= segmentY:
        label = 4
    


    if i <= segmentX and j > segmentY and j <= (segmentY * 2):
        label = 5
    
    if i > segmentX and i <= (segmentX * 2) and j > segmentY and j <= (segmentY * 2):
        label = 6
    
    if i > (segmentX * 2) and i <= (segmentX * 3) and j > segmentY and j <= (segmentY * 2):
        label = 7
    
    if i > (segmentX * 3) and j > segmentY and j <= (segmentY * 2):
        label = 8
    


    if i <= segmentX and j > (segmentY * 2):
        label = 9
    
    if i > segmentX and i <= (segmentX * 2) and j > (segmentY * 2):
        label = 10

    if i > (segmentX * 2) and i <= (segmentX * 3) and j > (segmentY * 2):
        label = 11

    if i > (segmentX * 3) and j > (segmentY * 2):
        label = 12



    return label
