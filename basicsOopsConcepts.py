#while loop
    
is_failed=True
i=1

while is_failed:
    if  i%2!=0:
        i = i+1
        continue
    print( f"attempt {i}")
    i = i+1
    if i>100:
        break
    



 
    