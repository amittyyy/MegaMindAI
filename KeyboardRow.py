from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            lower_word = set(word.lower() + row1)
            
            result.append(lower_word)
        return result

# Example usage
solution = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(solution.findWords(words))