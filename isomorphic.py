
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s.keys():
                dict_s[s[i]] = t[i]
            elif dict_s[s[i]] != t[i]:
                return False
            if t[i] not in dict_t.keys():
                dict_t[s[i]] = s[i]
            elif dict_t[t[i]] != s[i]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    s = "egg"
    t = "add"
    print(sol.isIsomorphic(s,t))
