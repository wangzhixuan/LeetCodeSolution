        	
	
class Solution:
    # @return a string
    def minWindow(self, S, T):
		"""
		My first idea of solving this problem.
		Turns out to be quite inefficient (passed OJ, though with 2800ms)
		"""
		
		
		def find_position(lst0, to_insert):
			"""
			insert an element into a list sorted by the first element
			return the insert position so that the new list is still sorted
			"""

			left = 0
			right = len(lst0)-1
			
			if to_insert[0] < lst0[left][0]:
				return 0
			elif to_insert[0] > lst0[right][0]:
				return right+1
			
			while (right - left) > 1:
				mid = (left+right)/2
				if to_insert[0] == lst0[mid][0]: # well, not possible in this problem
					return mid
				elif to_insert[0] < lst0[mid][0]:
					right = mid
				else:
					left = mid
				
			return right
		
        dic = {}
        m = len(T)
        for i,element in enumerate(S):
            if element in T:
                if element in dic:
                    dic[element].append(i)
                else:
                    dic[element] = [i]
        min_window = ""
        
        lst0 = []
        for element in T:
            try:
                lst0.append((dic[element].pop(0), element))
            except:
                return ""
        
        
        lst0.sort(key=lambda x:x[0])
        min_window = S[lst0[0][0]:lst0[-1][0]+1]
        
        minlength = lst0[-1][0] - lst0[0][0]
        while True:
            next = lst0.pop(0)
            element = next[1]
            if len(dic[element])==0:
                return min_window
            else:
                to_insert = (dic[element].pop(0), element)
            
            position = find_position(lst0, to_insert)
            
            lst0.insert(position, to_insert)
            
            length = lst0[-1][0] - lst0[0][0]
            if length<minlength:
                minlength = length
                min_window = S[lst0[0][0]:lst0[-1][0]+1]
				
				
	def minWindow_better(self, S, T):
		"""
		A better solution by mike3
		passed OJ with 428 ms
		"""
        dicT = {}
        
        for element in T:
            if element in dicT:
                dicT[element] -= 1
            else:
                dicT[element] = -1
        
        dicS = dict(dicT)
        
        end = 1
        n = len(S)
        m = len(T)
        
        if n<m: # not possible
            return ""
        
        # find the first window
        for end,element in enumerate(S):
            if element in dicS:
                dicS[element] += 1
            else:
                dicS[element] = 1
            
            findall = True
            for elementT in dicT:
                if dicS[elementT]<0:
                    findall = False
                    break
            
            if findall:
                break
        
        if not findall: # no such window at all
            return ""
        else:
            for start,element in enumerate(S):
                if element in T and dicS[element]==0:
                    break
                else:
                    dicS[element] -= 1
            minlength = end - start +1

        minwindow = S[start:end+1]
        element = S[start]
        dicS[element] -= 1
        
        while end < n-1:
            
            end += 1
            newelement = S[end]
            if newelement in dicS:
                dicS[newelement] += 1
            else:
                dicS[newelement] = 1
        
            if newelement == element:
#                assert(element == S[start])
                while start < end:
                    
                    start += 1
                    element = S[start]
                    dicS[element] -= 1
                    
                    if element in dicT and dicS[element] <0:
                        break
                        
                length = end - start + 1
                if length < minlength:
                    minlength = length
                    minwindow = S[start:end+1]
        
        return minwindow
