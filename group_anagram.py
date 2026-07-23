class Solution(object):
    def groupAnagrams(self, strs):
        result={}
        for i in strs:
            key="".join (sorted(i))
            if key not in result:
                result[key]=[]
            result[key].append(i)
        return list(result.values())