def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

first_name = input("Input your first name here: ")
last_name = input("Input your last name here: ")
print(format_name(first_name, last_name))


# ------------OR---------------
# def format_name(f_name, l_name):
#     full_name = f_name.title() + ' ' + l_name.title()
#     return full_name

# first_name = input("Input your first name here: ")
# last_name = input("Input your last name here: ")
# formated_string = format_name(first_name, last_name)
# print(formated_string)