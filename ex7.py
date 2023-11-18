# 1 - Write a program to calculate the factorial of a number using recursion.
def factorial(num: int):
    if num == 1 or num == 0:
        return 1
    if num == 2:
        return 2
    
    return num * factorial(num - 1)


# 2 - Write a program to generate all permutations of a string using recursion.
def generate_permutations(text: str):
    # if the string combined from just one letter, so it is the only permutation that exists
    if len(text) == 1:
        return [text]
    
    perms = []
    # we iterate over all the letters of the string to take all the possibilities
    for i in range(len(text)):
        # run the function again (recursively) without the i'th letter
        for perm in generate_permutations(text[:i] + text[i + 1:]):
            # add the i'th letter to the current permutation
            perms.append(text[i] + perm)
    return perms


if __name__ == '__main__':
    # Question 1
    num = 5
    print(f"Factorial of {num}: " + str(factorial(num)))
    print()
    
    # Question 2
    text = "abc"
    print(f"All Permutations of \"{text}\": " + str(generate_permutations(text)))
