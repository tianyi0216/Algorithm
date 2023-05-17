import sys

def schedule(joblist):
    """
    Find the maximum value from a given schedule
    param: joblist - a list of job in the form [start, end ,value] read from standard input
    return: the maximum value from the list of job it can schedule
    """
    joblist = sorted(joblist, key = lambda j: j[1])
    arr = [joblist[0][2]] # dp array

    ## bellman equation from lecture slide, populate from 1 to n
    for j in range(1, len(joblist)):
        i = find_i(j, joblist)
        # if i is -1, then no such job exists, thus only need current value at j to compare
        if i >= 0:
            arr.append(max(arr[j-1], arr[i] + joblist[j][2]))
        else:
            arr.append(max(arr[j-1], joblist[j][2]))
    return arr[len(joblist)-1]

def find_i(j, joblist):
    """
    Helper function using binary search method to find the best job i with finish time thats 
    less than start time for job at j.
    input: j - index j, joblist - list of jobs
    return: i - index where job i has the latest finish time earlier than start time of job at j.
    """
    left = 0
    right = j-1
    mid = 0
    
    # binary search algorithm, joblist is sorted by end time.
    while left <= right:
        mid = (right + left) // 2

        if joblist[mid][1] <= joblist[j][0]:
            left = mid + 1
        else:
            right = mid - 1

    # if not found, use -1 to indicate that there's no such job
    return right

if __name__ == '__main__':
    num_instance = int(sys.stdin.readline())
    result = []

    for i in range(num_instance):
        job_num = int(sys.stdin.readline())
        joblist = []
        for i in range(job_num):
            joblist.append(list(map(int, sys.stdin.readline().strip().split())))
        result.append(schedule(joblist))
    
    for res in result:
        sys.stdout.write(str(res) + '\n')