print("=========== Task 7 ===========\n")

#list of squares (1 to 10)
square_list = [x**2 for x in range(1,11)]
print("List of Squares (Using List): ", square_list)

#map each number to its cube
cubes_map = {x:x**3 for x in range(1,11)}
print("Cubes of each number Using Dictionary: ", cubes_map)


#set of even numbers
even_nos = {x for x in range(1,11) if x%2 == 0}
print("Set of even numbers (Using Set Comprehension): ", even_nos)
