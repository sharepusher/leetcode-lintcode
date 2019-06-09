## Reference
# https://www.lintcode.com/problem/text-justification/description

## Hard - Linkedin/Airbnb/Facebook

## Description
# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth
# characters and is fully(left and right) justsified/aligned.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned
# more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.
# NOTE: A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guarantteed to be greater than 0 and NOT exceed maxWidth.
# The input array words contains at least one word.

## Example
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ] 

# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
#Explanation: Note that the last line is "shall be    " instead of "shall     be",
#             because the last line must be left-justified instead of fully-justified.
#             Note that the second line is also left-justified becase it contains only one word.

#Input:
#words = ["Science","is","what","we","understand","well","enough","to","explain",
#         "to","a","computer.","Art","is","everything","else","we","do"]
#maxWidth = 20
#Output:
#[
#  "Science  is  what we",
#  "understand      well",
#  "enough to explain to",
#  "a  computer.  Art is",
#  "everything  else  we",
#  "do                  "
#]

## Analysis
# 1. left-justified == left-aligned
# 2. two cases:
#    1) normal line: fully justified(left and right aligned) extra spaces between words should be distributed as evenly as possible
#      if do not evely between words, the empty slots on the left will be assigned more spaces than the slots on the right.
#    2) last line: left aligned and no extra spaces inserted between words.
# 

## Solution
# two parts: 
# 1) split the words into lines according to the max_width, and pay attention to the absence between words.
#    How? if total words length(including space between words, counted by len(line)) <= max_width: line.append(word); else: 
# 2) format the line properly when appending them to result.

class Solution(object):
    # justify words of line
    #  
    def lineShaping(self, line, max_width, is_last_line=False):
        if not line:
            return ""
        N = len(line)
        if N == 1:
            return line[0]+" "*(max_width-len(line[0]))
        if is_last_line:
            sentence = " ".join(line)
            return sentence + " "*(max_width-len(sentence))

        # not last line
        total_words = sum(map(len, line))
        spaces = max_width-total_words
        word_space = spaces//(len(line)-1)
        extra_space = spaces % (len(line)-1)
        for i in xrange(len(line)-1):
            if extra_space != 0:
                line[i] = line[i]+" "*(word_space+1)
                extra_space -= 1
            else:
                line[i] = line[i]+" "*word_space
        return "".join(line)


    def fullJustify(self, words, maxWidth):
        if not words or maxWidth <= 0:
            return []
        # line: temp list to store words splited
        # words_length: total length of words of line
        line, result, words_length =[], [], 0
        for word in words:
            if words_length+len(word)+len(line) <= maxWidth:
                line.append(word)
                words_length += len(word)
            else:
                result.append(self.lineShaping(line, maxWidth))
                line = [word]
                words_length = len(word)
        if line:
            result.append(self.lineShaping(line, maxWidth, is_last_line=True))
        return result


if __name__ == "__main__":
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    result1 = [
   "This    is    an",
   "example  of text",
   "justification.  "]
    sol = Solution()
    print(sol.fullJustify(words1, maxWidth1) == result1)

    words2 = ["What","must","be","acknowledgment","shall","be"]
    result2 = ["What   must   be", "acknowledgment  ","shall be        "]
    print(sol.fullJustify(words2, maxWidth1) == result2)

    words3 = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
    result3 = ["Science  is  what we","understand      well","enough to explain to",
    "a  computer.  Art is","everything  else  we","do                  "]
    maxWidth3 = 20
    print(sol.fullJustify(words3, maxWidth3) == result3)










