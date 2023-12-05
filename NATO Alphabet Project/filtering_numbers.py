numbers = input("Enter numbers in this format (3, 4, 23): ").split(",")

even_nums = [num for num in numbers if int(num) % 2 == 0]
odd_nums = [num for num in numbers if int(num) % 2 != 0]

print(even_nums, odd_nums)