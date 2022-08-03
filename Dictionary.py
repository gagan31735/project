bad_guys = {
    "daredevil": " king",
    "x-men": "app ",
    "bat man": " bat"
}

print(bad_guys)
bad_guys["bat man"] #we can call the dictionary objects
print(bad_guys["bat man"])
#we can add the data into the dictionary
bad_guys["gagan"] = "good boy "
print(bad_guys)
# we can update  the entry in the dictionary
bad_guys["bat man"] = "bad boy "
print(bad_guys)
# we can delet the entry which we can entered in the dictionary
del bad_guys["gagan"]
print(bad_guys)
print(len(bad_guys))# we can find the length of the dictionary means these
# would be equal to the number of items of the dictionary
gagan = bad_guys.copy()
print(gagan)
dist = {}
dist['one']="these is one"
dist[2]="these is 2"
print(dist)
tinydict = {"name":"john","code":6745,"dept":"sals"}
print(tinydict.keys())