
#команда инпут работает с консолью, пользователь работает в консоли - интерактив
#принимает только strng, надо превращать в int

user = input("Please, enter your user name:")

# print("Hello " + user)

#or we can have the same results by
print(f"Hello, {user}")

#more examples:

user = input("Please, enter user name: ")
age = int(input("Please, enter your age: "))
print(f"Hello, {user}, your age is: {age}")

