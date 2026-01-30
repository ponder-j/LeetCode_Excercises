# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hash_dic = {}
#         for word in strs:
#             hashit = generate_key(word)
#             if hashit not in hash_dic:
#                 hash_dic[hashit] = []
#             hash_dic[hashit].append(word)
#         ans = []
#         for key in hash_dic:
#             ans.append(hash_dic[key])
#         return ans
    
def generate_key(word):
    count = [0 for i in range(26)]
    for letter in word:
        count[ord(letter)-97] += 1
    hashstr = ""
    for i in range(26):
        if count[i] != 0:
            hashstr += chr(i+97) + str(count[i])
    return hashstr
# print(generate_key("tea"))

# def groupAnagrams(strs):
#     hash_dic = {}
#     for word in strs:
#         hashit = generate_key(word)
#         if hashit not in hash_dic:
#             hash_dic[hashit] = []
#         hash_dic[hashit].append(word)
#     ans = []
#     for key in hash_dic:
#         ans.append(hash_dic[key])
#     return ans
    
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))