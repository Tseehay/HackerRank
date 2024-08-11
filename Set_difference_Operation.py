# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
e=list(map(int,input().split()))
m=int(input())
f=list(map(int,input().split()))

count=0
for en in e:
    if en not in f:
        count+=1
print(count)