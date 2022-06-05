
# demop th uise of a for loop
def foo( n: int ):
  count=0
  for i in range(n):
  # for i in range(50, n, 2):
    print(i, "Hello world!")
    count += 1
  
  return(count)
  
# call the foo() function
lines=foo(100)
print("Printed "+ str(lines) + " times")