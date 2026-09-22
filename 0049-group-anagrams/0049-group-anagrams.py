class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = defaultdict(list)
        for s in strs:
            caunt = [0]*26
            for char in s:
                caunt[ord(char) - ord('a')] += 1
            anagrams_map[tuple(caunt)].append(s)
        return list(anagrams_map.values())

          