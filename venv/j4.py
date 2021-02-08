import copy

a = 6
list = [5,4,3,2,1]

ans = 0


def foo(current,left):
    print(current)
    print(left)
    print("---------------")
    if sum(current) >= a:
        return len(current)
    curans = 0
    for x in range(len(left)):
        newcur = copy.deepcopy(current)
        newleft = copy.deepcopy(left)
        val = newleft.pop(x)
        newcur.append(val)
        val2 = foo(newcur,newleft)
        curans = max(curans,val2)
    return curans

print(foo([],list))
