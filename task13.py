def sum_rec(l, res, i=0):
    if i == len(l):
        return res
    else:
        res += l[i]
        i += 1
        return sum_rec(l, res, i)


l = [x for x in range(10)]
print(sum_rec(l, 0))
