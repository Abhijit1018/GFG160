def minRemoval(intervals):
    cnt = 0

    # Sort by minimum ending point
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]

    for i in range(1, len(intervals)):

        # if there is an overlap increase the count
        if intervals[i][0] < end:
            cnt += 1

        # else increment the ending point
        else:
            end = intervals[i][1]

    # return the count
    return cnt

if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 5], [1, 4]]
    print(minRemoval(intervals))
