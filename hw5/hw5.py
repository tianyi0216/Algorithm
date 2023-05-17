import sys

def count_sort(nums):
    if len(nums) == 1:
        return (nums, 0)
    mid = len(nums) // 2
    nums1, c1 = count_sort(nums[:mid])
    nums2, c2 = count_sort(nums[mid:])
    result, c = merge_count(nums1, nums2)
    return (result, c+c1+c2)

def merge_count(left, right):
    s = []
    c = 0
    # left and right pointer
    left_idx = 0
    right_idx = 0

    # merge by comapring left and right
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            s.append(left[left_idx])
            left_idx += 1
        else:
            s.append(right[right_idx])
            right_idx += 1
            c += len(left) - left_idx
    
    # add the result of list of 1 part to the result, it should be greater than all elements in result and in order
    s += left[left_idx:]
    s += right[right_idx:]

    return (s, c)

if __name__ == '__main__':
    num_instance = int(sys.stdin.readline())
    result = []

    for i in range(num_instance):
        list_size = int(sys.stdin.readline())
        numbers = list(map(int, sys.stdin.readline().strip().split()))
        result.append(count_sort(numbers))
    
    for res in result:
        sys.stdout.write(str(res[1]) + '\n')