def minEditDistance(s1,s2):
    m= {}
    len1 = len(s1)
    len2 = len(s2)
    maxlen = max(len1,len2)

    m = [None] * (len2 + 1)

    for i in range(len2 + 1):
        m[i] = [0] * (len1+1)

    for j in range(1, len1+1):
        m[0][j] = j

    for i in range(1, len2+1):
        m[i][0] = i

    for i in range(1,len2+1):
        for j in range(1, len1+1):
            cost = 1
            if s1[j-1] == s2[i-1]: cost = 0
            replaceCost = m[i-1][j-1] + cost
            removeCost = m[i-1][j] +1
            addCost = m[i][j-1] + 1
            m[i][j] = min(replaceCost,removeCost,addCost)

    print(m)
    return  m[len2][len1]

minEditDistance("test","tests")