# f"..." 
#we make variable(s)

# if we want to use something that has a variable so we use the variable instead of using 
# that thing(Maybe that thing is included 10 lines and we don't want to write that again and again...)
# so we use f , then "anything we want to write {variable} and if we want we can continue 
# writting {and again a variable} and etc..."
Greet = "Hello"
Answer = "Hi , How are you? "
x = f"I wanted to say {Greet} , But he said : {Answer}"

print(x)
# output = I wanted to say Hello , But he said : Hi , How are you? 

#Another example:
sum = 2+2
minus = 4-2
answer = "No"
print(f"The sum of 2 and 2 is {sum} , and the minus of 4 and 2 is {minus} , isn't it amazing? {answer}")
#output = The sum of 2 and 2 is 4 , and the minus of 4 and 2 is 2 , isn't it amazing? No
