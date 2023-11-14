# 1 - Write a program to reverse a string in place.
# naive way
def reverse_string_in_place(text):
    for i in range(len(text)):
        text = text[:i] + text[-1] + text[i:-1]
    return text


# def reverse_string_in_place_fast(text):
#     # text = reversed(text)
#     text = text[::-1]
#     return text


if __name__ == '__main__':
    txt = "asd"
    txt = reverse_string_in_place(txt)
    print(txt)


