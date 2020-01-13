def BinarySearch(list_search, number):
    height = len(list_search)-1
    low = 0
    mid = int(height/2)
    while(low<=height):
        if d[mid] == number:
            return True
        elif d[mid]>number:
            height = mid-1
            mid = int(height/2)
        elif d[mid]<number:
            low = mid+1
            mid = int((height-low)/2)+low
    return False




