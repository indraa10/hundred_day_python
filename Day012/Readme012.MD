#Day012 : 
concept of Namespace : 

local scope : when you created new variable or new function within another function then those variables or function will only be available within the function .

global scope : function or variable created not within any other function then
that function / variable will be available to all the other functions

now if you want to create a variable like below : 

game_level = 3

enemies = ["skeleton", "Zombie", "Alien"]
if game_level < 5 :
	new_enemy = enemies[0]

print(new_enemy)

in the above case variable is indented within a block of code but not inside any function then this will be available to all the code but as soon as the code comes under a function then the variable will not be accessible outside .

#modify a global variable : 

same name variable present within a function ( local scope ) and outside of the function ( global scope ) then both the variable will be considered two different variable .

if you execute a function and same name variable present within and outside the function then if function return the variable then the variable will be of local scope.
but if you want to mention the global variable within the function where same name variable present then use the keyword global . this will ensure that python will treate both the variable as same variable . example : 








