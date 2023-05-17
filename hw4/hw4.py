from collections import deque

def cache(cache_size, req_size, requests):
    fault = 0
    cache = set()
    c_dict = {}
    
    # build c dict - track indices
    for idx in range(req_size):
        if requests[idx] not in c_dict:
            c_dict[requests[idx]] = deque([idx])
        else:
            c_dict[requests[idx]].append(idx) # can assume sorted

    for i in range(req_size):
        # remove current indices
        c_dict[requests[i]].popleft()
        if requests[i] in cache:
            # hit, continue
            continue
        else:
            fault += 1
            if len(cache) < cache_size:
                cache.add(requests[i])
            else:
                # find furthest in future. Should be max of first index for each item or item with 0 index left
                furthest = 0
                evicted = None
                for item in cache:
                    if len(c_dict[item]) == 0:
                        evicted = item
                        break
                    else:
                        if c_dict[item][0] > furthest or evicted == None:
                            evicted = item
                            furthest = c_dict[item][0]
                cache.remove(evicted)
                cache.add(requests[i])
    return fault

if __name__ == '__main__':
    num_instance = int(input())
    result = []

    for i in range(num_instance):
        cache_size = int(input())
        req_size = int(input())
        requests = input()
        if requests[-1] == ' ':
            requests = requests[0:len(requests)-1]
        requests = requests.split(' ')
        result.append(cache(cache_size, req_size, [int(j) for j in requests]))
    
    for res in result:
        print(res)
