def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el
    return min_number  # <--- ЗАМЕНИЛИ print НА return

nums1 = [5, 1, 7, 4, 1, 5, 7, 23]
min1 = minimal(nums1)  # Теперь внутри min1 запишется 1

nums2 = [5.1, 7.4, 1.5, 7.23]
min2 = minimal(nums2)  # Теперь внутри min2 запишется 1.5

# Теперь сравнение сработает отлично:
if min1 < min2:
    print("Самое маленькое число из двух списков:", min1)
else:
    print("Самое маленькое число из двух списков:", min2)
