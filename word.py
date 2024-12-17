#1
first_word = input("Enter the first word: ") 
second_word = input("Enter the second word: ") 
len_first = len(first_word) 
len_second = len(second_word) 

if len_first == len_second: 
    for i in range(len_first): 
        print(first_word[i] + second_word[i], end="") 
elif len_first > len_second: 
    for i in range(len_second): 
        print(first_word[i] + second_word[i], end="") 
    print(first_word[len_second:]) 
elif len_second > len_first: 
    for i in range(len_first): 
        print(first_word[i] + second_word[i], end="") 
    print(second_word[len_first:])
print()
#2
def can_place_flowers(flowerbed, n):

    count = 0
    length = len(flowerbed)    
    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True    
    return False

print(can_place_flowers([1, 0, 0, 0, 1], 1))  
print(can_place_flowers([1, 0, 0, 0, 1], 2))
