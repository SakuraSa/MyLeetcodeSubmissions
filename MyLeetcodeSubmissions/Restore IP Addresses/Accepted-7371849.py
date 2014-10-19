#Author     : sakura_kyon@hotmail.com
#Question   : Restore IP Addresses
#Link       : https://oj.leetcode.com/problems/restore-ip-addresses/
#Language   : python
#Status     : Accepted
#Run Time   : 208 ms
#Description: 
#Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#For example:
#Given `"25525511135"`,
#return `["255.255.11.135", "255.255.111.35"]`. (Order does not matter)

#Code       : 
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        an = list()
        self.tr(s, 0, 0, list(), an)
        return an
    
    def tr(self, s, f , c , st, an):
        #print s, f, c, st, an
        if c >= 4:
            if f == len(s):
                an.append(".".join(st))
            return
        for i in range(1, 4):
            r = self.get(s, f, i)
            if r:
                st.append(r)
                self.tr(s, f + i, c + 1, st, an)
                st.pop()
            else:
                break
        
    
    def get(self, s, f, l):
        if f + l > len(s):
            return None
        st = s[f:f + l]
        n = int(st)
        if n > 255 or str(n) != st:
            return None
        return st