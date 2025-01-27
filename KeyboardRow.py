from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        for word in words:
            lower_word = set(word.lower())
            
            # AT. 01262024 the <= operator is used to check if the left-hand side set is a subset of the right-hand side set. 
            # It returns True if all elements of the left-hand side set are contained within the right-hand side set, otherwise it returns False.
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                result.append(word)
        return result

# Example usage
solution = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(solution.findWords(words))