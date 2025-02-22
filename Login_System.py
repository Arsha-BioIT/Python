# User database as a dictionary where the name is the key, and username & password are values
user_base = {
    "Arsha": ["foxntales", "12345"],
    "Surekha": ["lemontarzan", "surekha2233"],
    "Ishita": ["anamika212", "ishita2001"],
    "Raghav": ["zeus444", "art@2003"],
    "Atif": ["carzanam136", "kk_5656@jaipur"]
}

# Taking user input
name = input("Enter your name: ")
user_name = input("Enter your username: ")
password = input("Enter your password: ")

# Checking if the user exists in the database
if name in user_base:
    stored_username, stored_password = user_base[name]

    if user_name == stored_username and password == stored_password:
        print(f"✅ Login Successful: {name}")
    elif user_name != stored_username:
        print("❌ Username is incorrect")
    elif password != stored_password:
        print("❌ Password is incorrect")
else:
    print("❌ User not found")
