states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
"Connecticut", "Massachusetts", "Maryland", "South Carolina", 
"New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
"Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
"Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California",
"Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", 
"Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
"Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
"Alaska", "Hawaii"]

print(states_of_america[-1]) ## -1 starts from the end of the list

# states_of_america.append("Puerto Rico") ## adds to the list

# states_of_america.extend(["John's Funhouse", "Jackie Land"])

print(states_of_america)

# dirty_dozen = ["Strawberries", "Spinich", "Kale", "Nectarines", "Apples",
# "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches",
"Cherries", "Pears"]

vegetables = ["Spinich", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # This is a nested list

print(dirty_dozen)

print(dirty_dozen[1])