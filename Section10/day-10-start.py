
def my_function():
    result = 3 * 2
    return result

output = my_function()
print(output)

#Functions with Outputs
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("JOHN", "tomas")
print(formatted_string)


def format_name(f_name, l_name):
    #Docstrings can do multi-line commenting and also for expaining the purpose of the function
    """Take a first and last name and format it
    to return the titla case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
