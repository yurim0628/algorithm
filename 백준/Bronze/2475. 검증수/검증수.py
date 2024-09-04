nums = map(int, input().split())
print(sum(num * num for num in nums) % 10)