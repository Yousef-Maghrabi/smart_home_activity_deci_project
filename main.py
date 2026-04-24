p_title = "welcome to smart home".title() 

print("*"*len(p_title))
print(p_title) 
print("*"*len(p_title))
print("\n")

has_id = True
is_student = True
temperature = 22
system_active = True
security_code = 404
is_night_mode = False
 
# Temperature Checker
print("Checking Temp...\n")
if temperature > 35:
    print("it's hot today, turn on the AC.")
elif temperature < 10:
    print("it's cold today, turn on the Heater")
else:
    print("it's cool today,")
print("\n")

# Door System
if security_code % 2 == 0:
    print("It's safe, code is even")
else:
    print("It's not safe, code is odd")

if system_active and not is_night_mode:
    if is_student:
        if has_id:
            print("Permission Granted ✅")
        else:
            print("Permission Denied ❌", "Missing Id Error")
    else:
        print("Permission Denied ❌", "Not A Student Error")
else:
    print("System Inactive ❌", "it's inactive or night")

print("\n")
print("Thanks for using our program,")
