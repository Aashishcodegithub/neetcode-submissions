class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cres=defaultdict(list)#to map the charcount
        for i in strs:
            count=[0]*26# this will return 26 zeros help us to map the current value to these
            for j in i:
                count[ord(j)-ord('a')]+=1
            cres[tuple(count)].append(i)
        return list(cres.values())


  