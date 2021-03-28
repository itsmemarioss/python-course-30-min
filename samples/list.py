numbers = [0,1,2,3,4]
numbersPart2 = [5,6,7,8,9]

print(numbers[-1]) # 4
print(numbers[:]) # entire list
print(numbers[1:3]) # from 1 to 2, 3 not included

print(numbers + numbersPart2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#search
print( 1 in numbers ) #true
print( 1 in numbersPart2 ) #false
print( 'g' in 'python' ) #false

#length
len = len(numbersPart2)
min = min(numbersPart2)
max = max(numbersPart2)

print(len)
print(min)
print(max)

wordList = list("python")
print(wordList)

numbers[2:] = numbersPart2
print(numbers) #[0, 1, 5, 6, 7, 8, 9]

numbers[2:] = []
print(numbers) #[0, 1]
