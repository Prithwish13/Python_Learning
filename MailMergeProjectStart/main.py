#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
def read_name(file_path):
    with open(file_path, mode="r") as file:
        names = file.readlines()
    names = [ name.strip() for name in names]
    return names

def read_template(file_path):
    with open(file_path, mode='r') as file:
        template = file.read()
    return template

def generate_personalize_email(template, name):
    return template.replace("[name]", name)

def save_email(name, content, path):
    file_name = f"{name}.txt"
    file_path = f"{path}/{file_name}"
    with open(file_path, mode="w") as file:
        file.write(content)
    
names = read_name("./Input/Names/invited_names.txt")
template = read_template("./Input/Letters/starting_letter.txt")

for name in names:
    email = generate_personalize_email(template, name)
    save_email(name, email, "./Output/ReadyToSend")