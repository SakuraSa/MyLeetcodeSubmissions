#Author     : sakura_kyon@hotmail.com
#Question   : Text Justification
#Link       : https://oj.leetcode.com/problems/text-justification/
#Language   : python
#Status     : Accepted
#Run Time   : 168 ms
#Description: 
#Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
#You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly L characters.
#Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#For the last line of text, it should be left justified and no extra space is inserted between words.
#For example,
####words###: `["This", "is", "an", "example", "of", "text", "justification."]`
####L###: `16`.
#Return the formatted lines as:
#```
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]
#```
####Note:### Each word is guaranteed not to exceed L in length.
#[click to show corner cases.](#)
####Corner Cases:###
#* A line other than the last line might contain only one word. What should you do in this case?
#In this case, that line should be left-justified.

#Code       : 
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L, space_char=" ", end_char="."):
        ret = []
        buf = []
        length = 0
        words = words[::-1]
    
        def can_join(w):
            return length + len(w) + len(buf) <= L
    
        def write_line():
            if len(buf) == 0:
                ret.append(space_char * L)
                return
            elif len(buf) == 1:
                ret.append(buf[0].ljust(L, space_char))
                return
            elif not words:
                ret.append(space_char.join(buf).ljust(L, space_char))
                return
            space_length = L - length
            tab_length = space_length / (len(buf) - 1)
            all_count = len(buf) - 1
            extra_count = space_length % (len(buf) - 1)
            line = []
            for w in buf:
                line.append(w)
                if all_count:
                    if extra_count:
                        line.append(space_char * (tab_length + 1))
                        extra_count -= 1
                    else:
                        line.append(space_char * tab_length)
                    all_count -= 1
            ret.append("".join(line))
    
        while words:
            if can_join(words[-1]):
                w = words.pop()
                buf.append(w)
                length += len(w)
            else:
                write_line()
                buf = []
                length = 0
        if buf:
            write_line()
            buf = []
            length = 0
    
        return ret