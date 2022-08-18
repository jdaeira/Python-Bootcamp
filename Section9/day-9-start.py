programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    "Loop": "The action of doing something over and over again",
} 

#Retreiving items from the dictionary.
print(programming_dictionary["Bug"])

#Adding new items to the dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#Create new empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary) #dictionay is empty now

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop throug a dictionary.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#####################################################################  

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a List in a Dictionary
travel_log_dic = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting a Dictionary in a Dictionary
travel_log_nest_dic = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Portugal": {"cities_visited": ["Cascais", "Sintra", "Estoril"], "total_visits": 20},
}

#Nesting a Dictionary in a List
travel_log_nest_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Portugal", 
        "cities_visited": ["Cascais", "Sintra", "Estoril"],
        "total_visits": 20
    },
]


