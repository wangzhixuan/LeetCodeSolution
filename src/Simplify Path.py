class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        
        p = []
        new_input = False
        one_dot = False
        two_dots = False
        path += "/"
        for letter in path:
            if letter not in (".", "/"):
                if new_input:
                    new_name += letter
                elif one_dot:
                    new_input = True
                    new_name = "." + letter
                elif two_dots:
                    new_input = True
                    new_name = ".."+letter
                else:
                    new_input = True
                    new_name = letter
            elif letter == "/":
                if new_input:
                    new_input = False
                    p.append(new_name)
                elif one_dot:
                    pass
                elif two_dots:
                    if len(p)>0:
                        p.pop()
                one_dot = False
                two_dots = False
            elif letter == ".":
                if one_dot:
                    two_dots = True
                    one_dot = False
                elif two_dots:
                    two_dots = False
                    new_input = True
                    new_name = "..."
                elif new_input:
                    new_name += "."
                else:
                    one_dot = True
        
        #if new_input:
        #    p.append(new_name)
        
        
        result = "/"
        while len(p)>0:
            result += p.pop(0)
            if len(p)>0:
                result += "/"
            else:
                break
        
        return result
            