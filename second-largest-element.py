nums = [10, 5, 20, 8, 15]
max=0
sec_max=0
for i in nums:
    if(i>max):
        max=i
for j in nums:
    big=0
    if(j>big and j<max):
        sec_max=j
print(sec_max)
