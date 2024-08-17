# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())
bools = []

for i in range(n):
    b = set(map(int, input().split()))
    if a.issuperset(b) and len(a) > len(b):
        bools.append(True)
    else:
        bools.append(False)
        
if False not in bools:
    print(True)
else:
    print(False)
