def Beer_Song():
    num_of_bottles = 99
    for i in range (99,0,-1): # gives a range in the reverse order where -1 is the step
        if i == 2:
            print(f'''
                    {i} bottles of beer on the wall, {i} bottles of beer.
                    Take one down and pass it around, {i-1} bottle of beer on the wall.
                     ''') # Added in order to put the singular format of bottles into consideration
        if i ==1:
            print(f'''
                  {i} bottle of beer on the wall, {i} bottle of beer.
                  Take one down and pass it around, no more bottles of beer on the wall.
                  ''')
        while i>2 :
            print(f'''
                  {i} bottles of beer on the wall, {i} bottles of beer. 
                  Take one down and pass it around, {i-1} bottles of beer on the wall.
                  ''')
            break # Stops the loop
    print(f'''
          No more bottles of beer on the wall, no more bottles of beer.
          Go to the store and buy some more, {num_of_bottles} bottles of beer on the wall
          ''')   
        
        
        
Beer_Song() # Calls the function
