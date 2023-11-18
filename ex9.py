# 1 - Write a program to check if a given number is even or odd using bit manipulation.
# odd - the rightmost bit should be 1
# even - the rightmost bit should be 0
def bit_check_even_odd(num: int):
    bin_num = bin(num)[2:]
    # if the number is odd, when we do Xor with 1 we got (num - 1), when it is even we got (num + 1)
    xor_res = num ^ 1
    if xor_res + 1 == num:
        return "odd"
    return "even"

    # if num & 1 == 1:
    #     return "odd"
    # return "even"


# 2 - Write a program to find the number of set bits in a given integer using bit manipulation.
def count_set_bits(num: int):
    ones_count = 0
    
    while num > 0:
        ones_count += (num & 1)
        num >>= 1
    return ones_count


if __name__ == '__main__':
    # Question 1
    # 101
    odd_num = 5
    print(f"Check odd or even for number {odd_num} using bit manipulation: " + bit_check_even_odd(odd_num))
    # 110
    even_num = 6
    print(f"Check odd or even for number {even_num} using bit manipulation: " + bit_check_even_odd(even_num))
    
    # Question 2
    set_num = 53
    print(f"the Count of Set Bits in number {set_num}: " + str(count_set_bits(set_num)))
    