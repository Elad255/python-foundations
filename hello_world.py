def say_hello(name: str) -> str:
    return f"Hello, {name}! Welcome to your developer journey."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(say_hello(user))
