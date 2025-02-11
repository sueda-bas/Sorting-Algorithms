import sys

# Sorting the list with bubble sort
def bubble_sort (L):
    count=0 #Count is used for pass numbers
    stringb="" #
    for element in range (len(L)-1):

        if element!=0 and isSwatched==True:
            count=count+1
            
            M = " ".join(str(i) for i in L)
           
            stringb+=("Pass "+str(count)+": "+str(M)+"\n") 
        isSwatched=False   
        for element in range (len(L)-element-1):
            
            while L[element+1]<L[element]:
                sublist=L[element:element+2] #Two element is selected to change their position
                L.pop(element+1)
                L.insert(element,sublist[1])
                isSwatched=True
    return stringb

#Sorting the list with insertion sort
def insertion_sort(L):
    stringi=""
    count=0
    for element in range (0,len(L)-1):
        if element!=0:
            M = " ".join(str(i) for i in L)
            
            stringi+=("Pass "+str(count)+": "+str(M)+"\n") 
        while L[element+1]<L[element] and element>=0:
            sublist=L[element:element+2]
            L.pop(element+1)
            L.insert(element,sublist[1])
            
            element=element-1
        count=count+1
    stringi+=("Pass "+str(count)+": "+str(M)+"\n")
    return stringi

#Checking if the input list is sorted or not
def isSorted (L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            return False
        else:
            return True


def main():
    input_file=open(sys.argv[1],"r")
    data=input_file.read().split(" ")
    data_integer=[int(string) for string in data]
    input_file.close
    
    outputb=open(sys.argv[2],"w")
    outputi=open(sys.argv[3],"w")

    if isSorted(data_integer)==True:
        
        outputi.write("Already sorted!")
        outputb.write("Already sorted!")
        
    else:
        bubbleresult=bubble_sort(data_integer)
        insertionresult=insertion_sort(data_integer)
        outputi.write(bubbleresult)
        outputb.write(insertionresult)
    outputb.close
    outputi.close
if __name__=="__main__":
    main()


