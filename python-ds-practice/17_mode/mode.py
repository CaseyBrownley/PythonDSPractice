def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # counter = 0
    # num = lst[0]
    counts = {}
# Make frequency counter of num:freq
    for num in nums:
        counts[num] = counts.get(num,0) + 1

# find the highest value (the most frequent number)
    max_value = max(counts.value())


# now we need to see at which index the highest value is at

    for (num, freq) in counts.items():
        if freq == max_value:
            return num
# def most_frequent(List):
#     counter = 0
#     num = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency> counter):
#             counter = curr_frequency
#             num = i
 
#     return num
 
# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(List))