import json 

# open json
with open('Python-task.json', 'r') as f:
    data = json.load(f)

#make dict from json file 
hotels = {}

for hotel in data["assignment_results"][0]["shown_price"]:    
    hotels[hotel] = float(data["assignment_results"][0]["shown_price"][hotel])

#sort rooms by prices
srt = dict(sorted(hotels.items(), key=lambda item: item[1]))

#  task a. Find and return the cheapest (lowest) shown price
#  little funny solution but tried to do something interesting without min function, calling 0 element after sorting
lowest_shown_price = list(srt.items())


# task b. Find and return the room type, number of guest with the cheapest price
# not sure, in json only 1 string with guests number

#task c. Print the total price (Net price + taxes) for all rooms along with the room type

#get taxes json from origin json
taxes_raw = data["assignment_results"][0]["ext_data"]["taxes"]
taxes = json.loads(taxes_raw)

#calculate sum of 2 taxes
tax = 0
for value in taxes:
    tax = float(taxes[value]) + tax

#add taxes to our room cost
total_price = {}
for hotel in hotels:
    total_price[hotel] = round(float(data["assignment_results"][0]["net_price"][hotel]) + tax, 5)

# task d. Output

#write results in json format
result = {
    'lowest price' : lowest_shown_price[0][1],
    'cheapest room with guests number' : {
        'room type' : lowest_shown_price[0][0],
        'price' : lowest_shown_price[0][1],
        'guests' : data["assignment_results"][0]["number_of_guests"]
    },
    'prices with taxes' : total_price
}

#final output 
json_output = json.dumps(result)

with open("output.json", "w") as output:
    output.write(json_output)

#we are happy here