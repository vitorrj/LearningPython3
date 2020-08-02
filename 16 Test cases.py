# | ------------------ |
# | --- TEST CASES --- |
# | ------------------ |

### Assert
def square(x):
    return x*x

assert square(3), 9

### try and except
mylist = [1,2]
try:
    print(mylist[2])            # IndexError: list index out of range
    y = 10 / 0                  # ZeroDivisionError: can't divide by 0
except:
    print("I skipped the error!")

