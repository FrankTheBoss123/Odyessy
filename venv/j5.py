def reward(scores):
    min = []
    max = []
    #these if statements cover the corner cases of the array
    if scores[0]>scores[1]:
        max.append(0)
    elif scores[0]<scores[1]:
        min.append(0)
    if scores[-1]>scores[-2]:
        max.append(len(scores)-1)
    elif scores[-1]<scores[-2]:
        min.append(len(scores)-1)
    #used to find the peak and valleys of the array
    for num in range(1,len(scores)-2):
        if scores[num]<scores[num+1] and scores[num+1]>scores[num+2]:
            max.append(num+1)
        elif scores[num]>scores[num+1] and scores[num+1]<scores[num+2]:
            min.append(num+1)
    ans = [0]*len(scores)
    min.sort()
    max.sort()
    print(min)
    print(max)
    list = []
    for x in range(len(min)):
        for thing in range(max[x])
    for num in range(len(ans)):
        if num not in min:
            ans[num]+=1
    print(ans)


reward([8,4,2,1,3,6,7,9,5,6,7,8,9,10,3,2,5,6,1])
