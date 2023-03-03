import random 

passlen = int(input("Enter the length of desired password \n"))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ0123456789!@#$%&*?"
p = "".join(random.sample(s,passlen ))
print(p)