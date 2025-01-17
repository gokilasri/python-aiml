# #write a py program  take list of space - sepreate integer and print the 2 largest element
n = input(" enter the list"). split()
n.sort(reverse = True)
print(n)
print(n[1])


#another version
nums = list(map(int,input().split(" ")))
# n.sort(reverse = True)
large = nums[0]
sec_large=nums[-1]
for num in nums:
    if num>large:
        sec_large = large
        large=num
    elif large == sec_large:
        sec_large = num
    elif num> sec_large:
        sec_large=num
    else:
        continue
print(sec_large)

