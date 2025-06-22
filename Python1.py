def clean_string(text):
  
  # Add a single-line docstring
  """Swap spaces to underscores and convert text to lowercase."""
  
  no_spaces = text.replace(" ", "_")
  clean_text = no_spaces.lower()
  return clean_text

# Access the docstring
print(clean_string.__doc__)

# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
  # Add a multi-line docstring
  """
  Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
  	data (list, tuple, or set): Converted data structure.
    
  """
  if data_type == "tuple":
    data = tuple(data)
  elif data_type == "set":
    data = set(data)
  else:
    data = list(data)
  return data

print(help(convert_data_structure))

# * converts to a single iterable (tuple)
# **kwargs - arbitray keyword argument


#it expects arbitrary keyword arguments and
#stores them in a dictionary called kwarg
# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))


def concat(**kwarg):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for value in kwarg.values():
    result += " " + value
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x* 1.2)(sale_price))

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Create the updated list, sales_plus_tax
sales_plus_tax = list(add_taxes)

# Print the new list with updated values
print(sales_plus_tax)


## use try and except for error handling
def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")


## using raise
def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")


# Loop through the dictionary's keys and values
for key, value in courses.items():
  
  # Check if the value is "AI"
  if value  == "AI":
    print(key, "is an AI course")
  
  # Check if the value is "Programming"
  elif value == "Programming":
    print(key, "is a Programming course")
  
  # Otherwise, print that it is a "Data Engineering" course
  else:
    print(key, "is a Data Engineering course")

    # Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity +1):
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")

# Check the number of beds
if num_beds < min_num_beds:
  print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
  print("Too small")

  
# Check the rent
elif rent > max_rent:
  print("Too expensive")

  
# If all conditions met
else:
  print("This looks promising!")
# Create review_one
review_one = """ 
I really enjoy the courses,
and they are easy to fit into my busy schedule. 
I wish I had started using your platform sooner.
I'll be recommending you to my friends!!
"""

# Create review_two
review_two = """
One year ago, I was unsure of how to make progress in my career. 
Now, I work as a Prompt Engineer, and I can't thank you enough! 
Keep up the great work."""

# Print the two reviews individually
print(review_one)
print(review_two)

"""Create a while loop to run while tickets_sold is less than max_capacity.
Inside the loop, increment tickets_sold by 1, representing an increase for each ticket sold.
Outside of the loop, print tickets_sold."""


tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")


"""Create a while loop based on current_date being less than or equal to release_date.
Check if current_date is less than or equal to 24 and, if so, print "Purchase before the 25th for early access"
Otherwise, check if current_date is equal to 25, printing "Coming soon!".
After all checks, increment current_date by one for each day that passes."""


release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")
  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon!")
  else:
    print("Available now!")
  
  # Increment current_date by one
  current_date += 1

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
  # Check for values less than 25
  if value < 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)

"""Previously, you worked with a dictionary containing information about authors and the number of books that they have written.

In this exercise, data about the same authors has been aggregated to create a new dictionary called genre_sales, where the keys are the genre and the values are the average sales for that genre among the 20 most popular authors.

Your job is to find the most and least popular genres among these authors, along with their average sales revenue.

Instructions
100 XP
Check if average_sale is equal to the largest sales revenue (5166000000) in genre_sales.
Print the genre with the largest average sales.
Next, check whether average_sale is equal to the smallest sales revenue (80000000).
Lastly, print the genre with the smallest average sales."""



for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
      
      # Print the genre
      print("Most popular genre: ", genre)
      print("Average sales: ", average_sale)
    
    # Filter for the minimum sales value
    elif average_sale == 80000000:
      
      # Print the genre
      print("Least popular genre: ", genre)
      print("Average sales: ", average_sale)


# Loop through the dictionary
for genre, sale in genre_sales.items():
  
  # Check if genre is Horror or Mystery
  if genre == "Horror" or genre == "Mystery":
    print(genre, sale)
  
  # Check if genre is Thriller and sale is at least 3 million
  elif genre == "Thriller" and sale >= 3000000:
    print(genre, sale)


  # Use as many cells as you need
from python_functions import validate_name, validate_email, validate_password
def validate_user(name, email, password):
    if validate_name(name) == False:
        raise ValueError("The name should only contain string.")
    if validate_email(email) == False:
        raise ValueError("The email should only contain string.")
    if validate_password(password) == False:
        raise ValueError("The password should only contain string.")
    return True
  

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except:
        return False

    user = {"name": name, "email": email, "password": password}

    return user


# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for item in flash:
    print(item)


# Create an iterator for flash: superhero
superhero = iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))


# Create a range object: values
values = range(10, 21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for i in range(3):
    print(i)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10**100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

      
