
def DecToBinary(n1,n2):
    
    i=n1
    dict={}
    while i<=n2:
        
        list=[]
        temp=i
        while i>=1:
            r=i%2
            list.append(r)
            i=i//2
        i=temp
        length=len(list)
        j=0
        while j<length:
            if j==(length-1):
                dict.update({i:'False'})
                break
            elif list[j]==1 and list[j+1]==1:
                dict.update({i:'True'})
                break
            else:
                j=j+1
        i=i+1
        
    return dict

