
###### my permutation method ####
###### leetcode time: 364ms

# insert "app" number of "number" into "list0":
def insert_permute(number, app, list0):
    l = len(list0)
    
    num_pos = l+1
    
    list_of_lists = []
    tmpnumber = [ ] 
    index = range(app)  
    
    totalnumber = pow(num_pos,app)
    for i in range(app):
        tmpnumber.append(pow(num_pos,i) )
      
    
    for i in range(totalnumber):
		#create index  
        index[0] = i % num_pos
        flag = False 
        for i1 in range(1,app-1):
            index[i1] = (i % tmpnumber[i1+1]) / tmpnumber[i1]
            flag = (index[i1]>index[i1-1])
            if flag:
                break
        # new insertion position should be smaller than the old ones (avoid duplicates)
        if flag:                
            continue
                
        if(app>  1):
            index[app-1] = i / tmpnumber[app-1]        
            if (index[app-1]>index[app-2]):
                continue

        tmplist = list(list0)
        for i1 in range(app):
            tmplist.insert(index[i1],number)
            
        list_of_lists += [tmplist]
        
    return list_of_lists


def create_permute(dictionary):
    l = len(dictionary)
    if l == 0:
        return [[]]
    elif l==1:
        for number in dictionary:
            list0 = [number] * dictionary[number]
            return [list0]
    elif l==2:
        keys = dictionary.keys()
        values = dictionary.values()
        
        p0 = pow(values[0]+1,values[1])
        p1 = pow(values[1]+1,values[0])
        
        if p0<=p1:
            i0=0
            i1=1
        else:
            i1=0
            i0=1
            
        list0=[keys[i0]] * values[i0]
        return insert_permute(keys[i1],values[i1],list0)
    
    
    list_of_lists = []
       

    dict0 = dict(dictionary)
    number = dict0.keys()[0]
    appearance = dictionary[number]
    dict0.pop(number)
        
    tmplist = create_permute(dict0)
    for list0 in tmplist:
        tmplist2 = insert_permute(number,appearance,list0)
        list_of_lists += tmplist2
        
    return list_of_lists

def my_permute2(num):
    n = len(num)
    
    if n==1:
        return [num]
    
    dictionary = {}
    
    for number in num:
        if dictionary.has_key(number):
            dictionary[number] += 1
        else:
            dictionary[number] = 1
            
    tmpitems = sorted(dictionary.items(),key=lambda x: x[1])
    print tmpitems
    
    dict0={}
    for item in tmpitems:
        dict0[item[0]]=item[1]
    
    
    list_of_lists = create_permute(dict0)
    
    return list_of_lists


####another permutation method#####
#### leetcode time: 428ms
class Solution:
    def permuteUnique(self, num):
        self.perms=[]
        self.permute(0,num)
        return self.perms

    def permute(self,start,num):
        if start==len(num)-1: 
            self.perms.append(num[:])
            return
        used=[num[start]]
        self.permute(start+1,num)
        for i in range(start,len(num)):
            if num[i] in used: continue
            self.swap(start,i,num)
            self.permute(start+1,num)
            self.swap(start,i,num)
            used.append(num[i])

    def swap(self,i,j,num):
        tmp=num[i]
        num[i]=num[j]
        num[j]=tmp
    

