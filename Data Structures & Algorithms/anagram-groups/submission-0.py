class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hashmap to store word count
        #Key: Letters counter (list) // Value: strings
        store = defaultdict(list) #Creates new key if it doesnt exist
        for st in strs:
            counter = [0] * 26 #covers a-z alphabet
            for s in st:
                counter[ord(s)-ord('a')] += 1
            store[tuple(counter)].append(st)
        return list(store.values())