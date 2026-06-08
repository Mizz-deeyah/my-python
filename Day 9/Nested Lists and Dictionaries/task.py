# travel_log ={
#     "Saudi Arabia": [ "Riyadh", "Jedda", "Taif"]
#
# }
# print(travel_log["Saudi Arabia"][2])

# nested_list = ["A", "B",["C", "D"]]
#
# print(nested_list[2][1])

travel_log = {
 "Saudi Arabia":{
    "cities visited": ["Riyadh", "Jedda", "Taif"],
     "total visits": 6
  },

 "Nigeria":{
     "cities visited": ["Abuja", "Niger", "Kano"],
     "total visits": 5


  }



}


print(travel_log["Nigeria"]["cities visited"][2])