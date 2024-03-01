person = {
    'name': "Prithwish",
    'age': 27
}

#  loop through a dictionary
for key in person:
    print(person[key])
    

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

for key in travel_log:
    travel_log[key] = {
        "visited_cites": travel_log[key]
    } 

print(travel_log)

# python does not have block scope like javascript
if 1 == 1:
    apple = "my apple, I want to eat that"
    
def eat_apple():
    global apple
    apple = "Now I am eating the apple"

eat_apple()

print(apple)    