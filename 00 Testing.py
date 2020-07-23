

def list_sum(mylist):
   sum = 0
   for item in mylist:
      sum += item
   return sum

list = [1,2,4,5,6,1,234,5]

print(list_sum(list))