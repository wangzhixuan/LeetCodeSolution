class Solution:
    # @param s, a string
    # @return a boolean
	def isNumber(self, s):
		"""
		A cheat for the problem  OJ time: 328ms
		"""
        try:
            float(s)
            return True
        except:
            return False
            
	
	
    def isNumber(self, s):
		"""
		A solution considers all the corner cases  
		OJ time: 320ms
		Honestly I don't understand why "3." or "46.e2" is a valid number...
		But that's what OJ thinks
		"""
        start = False
        end = False
        has_dot = False
        has_e = False
        
        after_e = False
        after_dot = False
        before_dot = False
        
        has_sign = False
        after_sign = False
        
        for letter in s:
            if after_sign:
                if letter in ".0123456789":
                    after_sign = False
                else:#	"-a"
                    return False

            if letter == ' ':
                if start:
                    end = True
                continue
            else:
                if end:	# "1 2"
                    return False
            
            if after_dot:
                if letter in "0123456789": #"1.2" or "1.e2"
                    after_dot = False
                elif letter == 'e':
                    if before_dot:
                        after_dot = False
                    else:
                        return False
                else: # "1.a"
                    return False
            

            
            if after_e:
                if letter in "0123456789": # "1e3"
                    after_e = False
                elif letter in "+-": #"1e+3", handle it later
                    pass
                else: # "1ea" 
                    return False
            
            
            if letter in "+-":
                if (start or has_sign) and (not after_e):
                    return False
                    after_e = False
                else:
                    has_sign = True
                    after_sign = True
            
            elif letter == '.':
                if has_dot or has_e: # "1.2.3" or "1e2.3"
                    return False
                elif (not start): # ".2"
                    #return False
                    has_dot = True
                    after_dot = True
                    before_dot = False
                    start = True
                else:
                    has_dot = True
                    after_dot = True
                    before_dot = True
            elif letter == 'e':
                if has_e :	# "1e2e3"
                    return False
                elif (not start): # "e5"
                    return False
                else:
                    has_e = True
                    after_e = True
            elif letter not in "0123456789": # abcde
                return False
            else:
                if not start:
                    start = True
                    
        if after_e or (not start): # " 1e" or " " or " -" (sign does not start the expression)
            return False
        if after_dot and (not before_dot): # "." vs "3."
            return False
        
        return True