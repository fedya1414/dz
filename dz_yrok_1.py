def palindrome(predl):
    return predl[::-1] == predl
while True:
    print(palindrome(input('Введите слово: ')))