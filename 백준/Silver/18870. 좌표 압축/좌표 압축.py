N = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(set(arr))
dict = {}
for i, coordinate in enumerate(sorted_arr):
  dict[coordinate] = i

print(' '.join(str(dict[x]) for x in arr))