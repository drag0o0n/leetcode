
#https://leetcode.com/problems/valid-anagram/
#O(S+T) for memory and speed 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT ={},{}
        for i in range(len(s)):
            countS[s[i]] = 1 +countS.get(s[i],0) #counting how many times each char exist
            #the function get is used to get the key the same as the right side 
            #of the equality. 0 is the default value for the function get
            
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
            
            
# the second solution :
# return Counter(s) == Counter(t)
#better in time and space complexity
#third solution:
#We can sorted before then use (==)
#the complexity depends on the sorting algorithm time and space complexity
#return sorted(s) == sorted(t)
