# total 6 cities dis[i][j] = distance from city i to city j and 0 is there is no route between city i and city j
city = [1, 2, 3, 4, 5, 6]

dis = [
    [   0, 2, 5, 0, 0, 0 ],
    [   2, 0, 0, 3, 0, 0 ],
    [   5, 0, 0, 0, 2, 0 ],
    [   0, 3, 0, 0, 0, 6 ],
    [   0, 0, 2, 0, 0, 1 ],
    [   0, 0, 0, 6, 1, 0 ]
]

n = len(city)

for i in range(n):
    for j in range(n):
        if i != j and dis[i][j] == 0:
            dis[i][j] = float('inf')

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dis[i][k] + dis[k][j] < dis[i][j]:
                dis[i][j] = dis[i][k] + dis[k][j]


print("cities are:", city)
a = int(input("Enter the start city: "))
b = int(input("Enter the end city: "))

if dis[a - 1][b - 1] == float('inf'):
    print(f"There is no route between city {a} and city {b}.")
else:
    print(f"The shortest distance between city {a} and city {b} is: {dis[a - 1][b - 1]}")