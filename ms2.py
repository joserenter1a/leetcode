def greet (name, time):
    greet = "Good " + time + " " + name
    if (name == "Alice"):
        return greet
    greet = greet + "!"
    print(greet)
    return greet

banner = "Good night"
greet("Alice", "night")
print(banner)