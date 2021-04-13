myDict={
    1:3,
    "name":"amisha",
}

# print(myDict.keys())
# print(myDict.items())
updateDict={
    "update": "value",
    "name":"coder",
}
myDict.update(updateDict) #update the dictionary by using update
print(myDict)
# interview question
# what is mydict.get("name")= this will print none if value is not present in the dictionary
print(myDict["nae"]) #gives error
print(myDict.get("nam")) #return none id key/value is not present
