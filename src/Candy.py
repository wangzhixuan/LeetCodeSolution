class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n = len(ratings)
        sum = 0
        
        if n ==1:
            return 1
        
        previous_peak = False

        for index in range(n):
            if index>0:
                previous_diff = diff
                if previous_diff>0:
                    height+=1
                else:
                    height=1
            else:
                height = 1

            sum+= height

            if index<(n-1):
                diff = ratings[index+1] - ratings[index]

            if index==0:            
                peak = (diff<0)
                bottom = (diff>=0)
            elif index == n-1:
                peak = (previous_diff>=0)
                bottom = (previous_diff<=0)
            else:
                peak = (previous_diff>=0) and (diff<0)
                bottom = (previous_diff<=0) and (diff>=0)
            
            if peak:
                previous_peak = True
                previous_peak_position = index
                previous_peak_height = height
            
            if bottom:
                if previous_peak == True:
                    length = index - previous_peak_position
                    sum += (length-1)*length/2  # add the triangle area
                    if length+1> previous_peak_height:
                        sum += (length+1-previous_peak_height) # whether the peak also need to be higher
            
                    previous_peak = False

            
        return sum
            
            