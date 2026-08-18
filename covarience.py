def mean(a):
    return sum(a) / len(a)
def covarience(a,b):
    n = len(a)
    ma = mean(a)
    mb = mean(b)
    sum = 0
    for i in range(n):
        sum = sum + (a[i]-ma)*(b[i]-mb)
    return sum/n
def coverience_matrix(a,b):
    cm = [[0,0],
          [0,0]]
    cm[0][0] = covarience(a,a)
    cm[0][1] = covarience(a,b)
    cm[1][0] = covarience(b,a)
    cm[1][1] = covarience(b,b)
    for row in cm:
        print(row)

a = [4.0, 4.2, 3.9, 4.3, 4.1]
b = [2.0, 2.1, 2.0, 2.1, 2.2]
coverience_matrix(a,b)