city_list = ["Mumbai", "Bangalore", "Kolkata", "Chennai", "Hyderabad", "Pune", "Ahmedabad", "Jaipur"]
states = ["Uttar Pradesh", "Maharashtra", "Bihar", "West Bengal", "Madhya Pradesh", "Tamil Nadu", "Rajasthan", "Karnataka", "Gujarat", "Andhra Pradesh"]


try:
    print(city_list[-2])
except IndexError:
    print("Index is out of range. Please provide a valid index.")
    
dirty_list = [city_list, states] 

print(dirty_list)
   

        