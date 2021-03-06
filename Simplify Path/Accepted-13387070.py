#Author     : sakura_kyon@hotmail.com
#Question   : Simplify Path
#Link       : https://oj.leetcode.com/problems/simplify-path/
#Language   : python
#Status     : Accepted
#Run Time   : 188 ms
#Description: 
#Given an absolute path for a file (Unix-style), simplify it.
#For example,
####path### = `"/home/"`, => `"/home"`
####path### = `"/a/./b/../../c/"`, => `"/c"`
#[click to show corner cases.](#)
####Corner Cases:###
#* Did you consider the case where ###path### = `"/../"`?
#In this case, you should return `"/"`.
#* Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.
#In this case, you should ignore redundant slashes and return `"/home/foo"`.

#Code       : 
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        for op in path.split("/"):
            if op:
                if op == ".":
                    continue
                elif op == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(op)
        return "/" + "/".join(stack)