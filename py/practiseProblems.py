def removeDuplicates(l):
    newL = []
    for i in l:
        if i not in newL:
            newL.append(i)
    return newL

def findMaxMinAndAverage(t):
    max =  float('-inf')
    min =  float('inf')
    avg = 0
    for ele in t:
        avg += ele
        if ele > max:
            max = ele
        elif ele < min:
            min = ele
    avg /= len(t)
    return (min, max, avg)

def countFrequencies(l):
    d = {}
    for ele in l:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    return d

print(removeDuplicates([1, 1, 2, 3, 4, 5, 6, 1, 2]))
print(findMaxMinAndAverage((2, 43, 1, 4, 65, 32)))
print(countFrequencies([1, 1, 1, 1, 4, 4, 4, 2, 3, 5]))
