import sys

def schedule(joblist):
    """
    Function that find the number job can schedule given a list of jobs.
    Implemented using interval scheduling greedy algorithm covered in class.
    Overall complexity: O(nlog(n))
    param: joblist- a list of all the jobs consist of form [start_time, finish_time]
    return: number of job interval scheduling greedy algorithm can schedule
    """
   
    # sort joblist by finish time, O(nlog(n)) - using merge sort
    #joblist = merge_sort(joblist)
    joblist = sorted(joblist, key= lambda j: j[1])
    result = [joblist[0]]

    # loop through job and find all compatilble jobs, O(n)
    for i in range(1, len(joblist)):
        if joblist[i][0] >= result[-1][1]:
            result.append(joblist[i])

    return len(result)

if __name__ == '__main__':
    # read the input and print to std output
    num_instance = int(input())
    result = []

    for i in range(num_instance):
        jobnum = int(input())
        joblist = []
        for j in range(jobnum):
            jobtmp = input().split(' ')
            joblist.append([int(jobtmp[0]), int(jobtmp[1])])
        result.append(schedule(joblist))

    for idx in range(len(result)):
        print(result[idx])