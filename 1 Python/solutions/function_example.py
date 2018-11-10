def say_hello(first_name, last_name): # this is a function definition
	# first_name and last_name are parameters
	# they are temp variables that you can use throughout the function block
    print('Hello ' + first_name + ' ' + last_name)

fn = input('what is your first name? ')
ln = input('what is your last name? ')

# function call with positional arguments
say_hello(fn, ln)

# with keyword arguments (kwargs)
say_hello(last_name=ln, first_name=fn)