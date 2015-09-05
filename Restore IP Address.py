class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        IP_lists =  self.my_restoreIPAddresses(s,4)
        
        
        
        result_str = []
        
        for lst in IP_lists:
            if len(lst)==0:
                return []
            tmpstr = str(lst[0])+"."+str(lst[1])+"."+str(lst[2])+"."+str(lst[3])
            result_str.append(tmpstr)
        
        return result_str
    
    def my_restoreIPAddresses(self, s, n0):    
        length = len(s)
        if (length > n0 * 3) or (length == 0) :
            return [[]]
            
        if (n0 == 1):
            number = int(s)
            if (number > 255):
                return [[]]
            elif (s[0]=="0") and (length>1):
                return [[]]
            else:
                return [[number]]
        
        if (length ==n0):
            result = []
            for i in range(n0):
                result.append(int(s[i]))
            return [result]
        
        first_digit = int(s[0])
        first2digits = int(s[0:2])
        first3digits = int(s[0:3])
        
        result = []
        str1 = s[1:length]
        for lst in self.my_restoreIPAddresses(str1, n0 -1):
            if (len(lst)>0):
                lst.insert(0,first_digit)
                result.append(lst)
        
        if (first_digit>0):
            str2 = s[2:length]
            for lst in self.my_restoreIPAddresses(str2, n0-1):
                if (len(lst)>0):
                    lst.insert(0,first2digits)
                    result.append(lst)
            
        if (first3digits <= 255) and (first2digits>=10):
            str3 = s[3:length]
            for lst in self.my_restoreIPAddresses(str3, n0-1):
                if (len(lst)>0):
                    lst.insert(0,first3digits)
                    result.append(lst)
        
        return result
