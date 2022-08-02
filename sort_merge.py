number = [16,21,11,8,12,22]


def merge_sort(number):
    
    if len(number)>1:
        left_array = number[:len(number)//2]
        right_array = number[len(number)//2:]
        
        merge_sort(left_array)
        merge_sort(right_array)
        
        i=0
        j=0
        k=0 
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                number[k] = left_array[i]
                i+=1
            else:
                number[k] = right_array[j]
                j+=1
            k+=1
            
        while i < len(left_array):
            number[k] = left_array[i]
            i+=1
            k+=1
        
        while j < len(right_array):
            j+=1
            k+=1
        
merge_sort(number)
print(number)