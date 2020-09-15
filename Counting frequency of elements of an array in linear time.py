# Python program to count the frequency of 
# elements in a list using a dictionary 
  
def CountFrequency(my_list): 
      
   # Creating an empty dictionary  
   count = {} 
   for i in my_list: 
    count[i] = count.get(i, 0) + 1
   return count 
  
# Driver function 
if __name__ == "__main__":  
    my_list =list(map(int,input().rstrip().split())) 
    print(CountFrequency(my_list))

   
'''
get() method in python.

syntax - dictionary.get(keyname, value)
         keyname -- (Required) The keyname of the item you want to return the value from
         value -- (Optional) A value to return if the specified key does not exist. Default value None
'''
