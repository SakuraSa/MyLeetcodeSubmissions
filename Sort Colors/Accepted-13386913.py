#Author     : sakura_kyon@hotmail.com
#Question   : Sort Colors
#Link       : https://oj.leetcode.com/problems/sort-colors/
#Language   : python
#Status     : Accepted
#Run Time   : 300 ms
#Description: 
#Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
####Note:###
#You are not suppose to use the library's sort function for this problem.
#[click to show follow up.](#)
####Follow up:###
#A rather straight forward solution is a two-pass algorithm using counting sort.
#First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#Could you come up with an one-pass algorithm using only constant space?

#Code       : 
def quickSort(array, from_index=None, to_index=None, key_func=None, cmp_func=None):
    from_index = from_index or 0
    to_index = to_index or (len(array) - 1)
    key_func = lambda x: x
    cmp_func = lambda a, b: a < b
    pointer_head = from_index
    pointer_tail = to_index
    move_flag = True
    while pointer_head < pointer_tail:
        if not cmp_func(
            key_func(array[pointer_head]),
            key_func(array[pointer_tail])):
            array[pointer_head], array[pointer_tail] = array[pointer_tail], array[pointer_head]
        if move_flag:
            pointer_head += 1
        else:
            pointer_tail -= 1
    if from_index < pointer_head - 1:
        quickSort(array, from_index, pointer_head - 1, key_func, cmp_func)
    if pointer_tail + 1 < to_index:
        quickSort(array, pointer_tail + 1, to_index, key_func, cmp_func)
    return array

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        quickSort(A)