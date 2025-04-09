def avg(nums):
  return sum(nums) / len(nums) if nums else 0
scores = [80, 90, 75, 85]
average = avg(scores)
print(f"Average: {average}")
