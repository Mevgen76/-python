nums = [5,7,2,4,5,1,False, 'Brother',4.6436]

nums[0] = 155

print(nums)

change = str(input('Меняем бул на True? - да/нет'))
if change == 'да':
    nums[6] = True
    print(nums)
elif change == 'нет':
    print(nums)


