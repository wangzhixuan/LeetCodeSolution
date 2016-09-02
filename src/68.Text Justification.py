"""
LeetCode OJ time: 40ms
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
       
        current_line_length = 0
        spacesThisLine = []
        wordsThisLine = []
        
        result = []
        
        def generateNewLine(lastLine = False):
            newline = ''
            print wordsThisLine

            if len(wordsThisLine) > 1 and not lastLine:
                extraSpaces = maxWidth - current_line_length
                extraSpacePerPosition = extraSpaces / (len(wordsThisLine)-1)
                extraExtraSpaces = extraSpaces % (len(wordsThisLine)-1)
                    
                for i, space in enumerate(spacesThisLine[1:]):
                    spacesThisLine[i+1] += extraSpacePerPosition
                    if i<extraExtraSpaces:
                        spacesThisLine[i+1] += 1
                    
                for word,space in zip(wordsThisLine, spacesThisLine):
                    newline += ' '*space
                    newline += word
            else:
                for word,space in zip(wordsThisLine, spacesThisLine):
                    newline += ' '*space
                    newline += word
                extraSpaces = maxWidth - len(newline)
                newline += ' '*extraSpaces
            return newline
        
        for i,word in enumerate(words):
            if current_line_length ==0:
                wordsThisLine.append(word)
                spacesThisLine.append(0)
                current_line_length += len(word)
            elif current_line_length + len(word) + 1 <=maxWidth:
                wordsThisLine.append(word)
                spacesThisLine.append(1)
                current_line_length += len(word) +1                
            else:
                newline = generateNewLine()
                result.append(newline)
                current_line_length = len(word)
                spacesThisLine = [0]
                wordsThisLine = [word]
                
        result.append(generateNewLine(lastLine=True))
        return result            

