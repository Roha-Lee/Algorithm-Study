string = list(input().strip())
numbers = [int(num) for num in string if num.isdigit()]
letters = sorted([letter for letter in string if letter.isalpha()])
letters.append(str(sum(numbers)))
print(''.join(letters))
