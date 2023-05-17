import sys

def count_line(top, bot):
    """
    get the count of intersection between two set of points
    param: top - the top set of points, bot- the bot set of points
    return: the number of inversion count
    """
    _,sort_bot = get_bot(top, bot) # O(nlogn)
    _,get_count = count_intersect(sort_bot) #O(nlogn)
    return get_count

def get_bot(top, bot):
    """
    function get the sorted bot list based on top list
    """
    if len(top) == 1 or len(bot) == 1:
        return top, bot
    
    ## divide in half and then merge together
    mid = len(top) // 2
    leftt, leftb= get_bot(top[:mid], bot[:mid])
    rightt, rightb = get_bot(top[mid:], bot[mid:])
    topm, botm= merge_list(leftt, leftb, rightt, rightb)
    return topm, botm

def merge_list(leftt, leftb, rightt, rightb):
    """
    function that merges the top list and merge bot list based on top list
    """
    stop = []
    sbot = []
    left_idx = 0
    right_idx = 0

    ## merge sort two list
    while left_idx < len(leftt) and right_idx < len(rightt):
        if leftt[left_idx] <= rightt[right_idx]:
            stop.append(leftt[left_idx])
            sbot.append(leftb[left_idx])
            left_idx += 1
        else:
            stop.append(rightt[right_idx])
            sbot.append(rightb[right_idx])
            right_idx += 1

    stop += leftt[left_idx:]
    sbot += leftb[left_idx:]
    stop += rightt[right_idx:]
    sbot += rightb[right_idx:]
    
    return stop, sbot

def count_intersect(bot):
    """
    function get the number of intersection based on order of bot list
    """
    if len(bot) == 1:
        return bot, 0
    
    mid = len(bot) // 2
    left, c1 = count_intersect(bot[:mid])
    right, c2 = count_intersect(bot[mid:])
    result, c = merge_count(left, right)
    return result, c+c1+c2

def merge_count(left, right):
    """
    count the number of intersection.
    """
    s = []
    count = 0
    left_idx = 0
    right_idx = 0

    ## similar to count inversion.
    ## if the insert is from second half, it must intersect with two in front as it is sorted based on top.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            s.append(left[left_idx])
            left_idx += 1
        else:
            s.append(right[right_idx])
            right_idx += 1
            count += len(left) - left_idx

    s += left[left_idx:]
    s += right[right_idx:]
    return s, count

if __name__ == '__main__':
    num_instance = int(sys.stdin.readline())
    result = []

    for i in range(num_instance):
        size = int(sys.stdin.readline())
        top = []
        bot = []
        for i in range(size):
            top.append(int(sys.stdin.readline()))
        for i in range(size):
            bot.append(int(sys.stdin.readline()))
        result.append(count_line(top, bot))
    
    for res in result:
        sys.stdout.write(str(res) + '\n')