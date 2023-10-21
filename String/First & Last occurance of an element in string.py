def find_occurrence(string, index, element):
    global first, last  # Using globals for first and last
    if index == len(string):
        print(first)
        print(last)
        return

    curr_char = string[index]
    if curr_char == element:
        if first == -1:
            first = index
        else:
            last = index
    find_occurrence(string, index + 1, element)
first = -1
last = -1
str = "abaacdaefaah"
find_occurrence(str, 0, 'a')


# Output: 0
#         10



