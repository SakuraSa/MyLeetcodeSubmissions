#Author     : sakura_kyon@hotmail.com
#Question   : String to Integer (atoi)
#Link       : https://oj.leetcode.com/problems/string-to-integer-atoi/
#Language   : python
#Status     : Accepted
#Run Time   : 272 ms
#Description: 
#Implement atoi to convert a string to an integer.
####Hint:### Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
####Notes:### 
#It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front. 
#[spoilers alert... click to show requirements for atoi.](#)
####Requirements for atoi:###
#The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

#Code       : 
class Solution:
    # @return an integer
    def atoi(self, str):
        numlst = list()
        sing = 1
        singFlag = False
        numFlag = False
        for c in str:
            if c == " " and not singFlag and not numFlag:
                continue
            if not singFlag and not numFlag:
                if c == "+":
                    sing = 1
                    singFlag = True
                    continue
                if c == "-":
                    sing = -1
                    singFlag = True
                    continue
            if "0" <= c <= "9":
                numFlag = True
                numlst.append(c)
            else:
                break
        sum = 0;l = 1
        for c in numlst[::-1]:
            sum += l * (ord(c) - 48)
            l *= 10
        sum *= sing
        sum = min(sum, 2147483647)
        sum = max(sum, -2147483648)
        return sum