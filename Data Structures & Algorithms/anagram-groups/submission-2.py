class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for words in strs:
            key=''.join(sorted(words))
            if key not in res:
                res[key]=[]
            res[key].append(words)
        return list(res.values())