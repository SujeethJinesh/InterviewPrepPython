def k_string_generator(string, k):
    """
    link: https://www.geeksforgeeks.org/reorder-the-given-string-to-form-a-k-concatenated-string/
    :return: string that is k divisible or not possible.
    """
    num_characters = {}
    for character in string:
        if character in num_characters.keys():
            num_characters[character] += 1
        else:
            num_characters[character] = 1

    repeat_string = ""

    for key in num_characters:
        value = num_characters[key]
        if value % k == 0:
            repeat_string += str(key) * int(
                value / k)  # don't need to put float here because the if guarantees it's divisble
        else:
            return "Not Possible"

    to_return = ""

    for i in range(k):
        to_return += repeat_string

    return to_return

if __name__ == '__main__':
    print(k_string_generator("gkeekgee", 2))
    print(k_string_generator("abcd", 2))
