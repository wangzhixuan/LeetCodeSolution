class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        
        result = ""
        
        if num1=="0" or num2=="0":
            return "0"
        
        number = 0
        for digit in range(l1 + l2 - 1):
            number = number / 10
            for digit1 in range(digit + 1):
                digit2 = digit - digit1
                if (digit1 >=l1) or (digit2 >= l2):
                    continue
                number1 = int(num1[-digit1-1])
                number2 = int(num2[-digit2-1])
                number += number1 * number2
            result = str(number % 10) + result
        
        if number >= 10:
            result = str(number / 10) + result
        
        return result     