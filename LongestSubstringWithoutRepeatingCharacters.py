class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_len = -1
        current_subst_dct = dict()
        start_subst: int = 0
        subst_unique = dict()
        len_previous_subst = 1
        for i in range(len(s)):
            if s[i] in current_subst_dct:
                # current_subst_dct.clear()
                len_previous_subst = i - start_subst
                if len_previous_subst not in subst_unique:
                    subst_unique[len_previous_subst] = []
                    subst_unique[len_previous_subst].append((start_subst, i - 1))
                else:
                    subst_unique[len_previous_subst].append((start_subst, i - 1))
                if current_subst_dct[s[i]] + 1 == i:
                    start_subst = current_subst_dct[s[i]] + 1
                    current_subst_dct.clear()
                else:
                    prev_start_subst = start_subst
                    start_subst = current_subst_dct[s[i]] + 1
                    for j in range(prev_start_subst, current_subst_dct[s[i]]):
                        current_subst_dct.pop(s[j])
                current_subst_dct[s[i]] = i
            else:
                current_subst_dct[s[i]] = i

        len_previous_subst = len(s) - start_subst
        if len_previous_subst not in subst_unique:
            subst_unique[len_previous_subst] = []
            subst_unique[len_previous_subst].append((start_subst, len(s) - 1))
        else:
            subst_unique[len_previous_subst].append((start_subst, len(s) - 1))

        max_len = max(subst_unique.keys())
        return max_len



# s = "abcabcbb"
# s ="wobgrovw"
s = "bbbbb"
# s = "pwwkew"
# s = "aaa"
# s = "au"
# s = "dvdf"
# s ="abba"
print(Solution.lengthOfLongestSubstring(s))
