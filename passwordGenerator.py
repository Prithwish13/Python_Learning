import random

pass_len = int(input("How many letters would you like in your password?\n"))
symbol_num = int(input("How many symbols would you like?\n"))
numbers_len = int(input("How many numbers would you like?\n"))

letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
numbers = [chr(i) for i in range(48, 58)]
symbols = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]

# picked_letters = random.sample(letters, pass_len)
# picked_symbols = random.sample(symbols, symbol_num)
# picked_nums = random.sample(numbers, numbers_len)



# probable_pass_arr = picked_letters + picked_symbols + picked_nums


# random.shuffle(probable_pass_arr)


# final_password = "".join(str(elm) for elm in probable_pass_arr)

# print(final_password)


# Alternative way to doing the same

password = ''

for elm in range(0, pass_len):
    password += random.choice(letters)
    
for elm in range(0, symbol_num):
    password += random.choice(symbols)
    
for elm in range(0, numbers_len):
    password += random.choice(numbers)    
    
    
prob_pass  = list(password)
random.shuffle(prob_pass)
final_pass = "".join(prob_pass)
print(final_pass)


