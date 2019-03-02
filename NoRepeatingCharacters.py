#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

def lls(s):
    L = len(s)
    if L > 1:
        db = [s[0]]
        num = 1
        maxnum = 1
        for i in range(1, L):
            if s[i] in db:
                di = db.index(s[i])
                db.append(s[i])
                db = db[di + 1:]
                num -= di
            else:
                db.append(s[i])
                num += 1
                if num > maxnum:
                    maxnum = num
    else:
        maxnum = L
    return maxnum