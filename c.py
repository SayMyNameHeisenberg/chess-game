'''input
2
1 1
1 1
'''
import sys
n = int(sys.stdin.readline())
arr = [0]*n
for i in range(n):
	temp = list(map(int,sys.stdin.readline().split(' ')))
	temp = temp[1:]
	temp.sort()
	arr[i] = temp
for i in range(n):
	ans = "YES"
	for j in range(n):
		if i!=j:
			# print(len(arr[i]),len(arr[j]))
			if (len(arr[i])>=len(arr[j])):
				if (arr[i]==arr[j]):
					ans = "NO"
					break
				else:
					count=0
					# print(arr[i],arr[j])
					for p in arr[j]:
						if p in arr[i]:
							count+=1
					if count==len(arr[j]):
						ans="NO"
						break
	print(ans)