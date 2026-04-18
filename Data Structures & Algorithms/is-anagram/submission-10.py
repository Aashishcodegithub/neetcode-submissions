class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s)==sorted(t)
        return Counter(s)== Counter(t)
        s.split()
        t.split()
        freq1={}
        freq2={}
        for i in s:
            if i in s:
                freq1[i]+=1
            else:
                freq1[i]=1
        for j in t:
            if j in t:
                freq2[j]+=1
            else:
                freq2[j]=1
        return freq1==freq2
    