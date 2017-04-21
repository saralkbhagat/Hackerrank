n=int(input())
arr = []


for i in range (n):
    s = input()
    cmd = s.split()

    if cmd[0] == "insert":
        arr.insert(int(cmd[1]), int (cmd[2]))
    if cmd[0] == "print":
        print(arr)
    if cmd[0] == "remove":
        arr.remove(int(cmd[1]))
    if cmd[0] == "append":
        arr.append(int(cmd[1]))
    if cmd[0] == "sort": arr.sort()
    if cmd[0] == "reverse":arr.reverse()
    if cmd[0] == "pop": arr.pop()










