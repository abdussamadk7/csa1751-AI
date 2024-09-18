import itertools
# Helper function to check if a solution is valid
def is_valid_solution(letters, values, words):
    letter_to_digit = dict(zip(letters, values)) 
    # Check if the first letter of any word is assigned a zero
    for word in words:
        if letter_to_digit[word[0]] == 0:
            return False
    # Convert words to their numerical equivalents
    nums = [sum(letter_to_digit[letter] * (10 ** i) for i, letter in enumerate(word[::-1])) for word in words] 
    # Check if the sum of the first n-1 numbers equals the last number
    return sum(nums[:-1]) == nums[-1] 
# Solve cryptarithmetic puzzle
def solve_cryptarithmetic(words):
    # Extract unique letters
    letters = set(''.join(words))
    if len(letters) > 10:
        print("Too many letters for unique digits!")
        return
    letters = list(letters) 
    # Generate all permutations of 10 digits
    for perm in itertools.permutations(range(10), len(letters)):
        if is_valid_solution(letters, perm, words):
            letter_to_digit = dict(zip(letters, perm))
            print("Solution found!")
            for word in words:
                print(f"{word}: {''.join(str(letter_to_digit[letter]) for letter in word)}")
            return letter_to_digit
    print("No solution found.")
    return None
# Example usage with the SEND + MORE = MONEY puzzle
words = ['SEND', 'MORE', 'MONEY']
solve_cryptarithmetic(words)
