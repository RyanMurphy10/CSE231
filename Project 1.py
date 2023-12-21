inputOfNumRods=input("Input rods: ")

inputRodsInFloat=float(inputOfNumRods)

print("You input " + str(round(inputRodsInFloat,3))+" rods.")

valueOfMeters=inputRodsInFloat*5.0292
valueOfMiles=valueOfMeters/1609.34
valueOfFeets=valueOfMeters/0.3048
valueOfFurlongs=inputRodsInFloat/40
valueOfMinutesToWalk=(valueOfMiles/3.1)*60

print("\nConversions")
print("Meters:",round(valueOfMeters,3))
print("Feet:",round(valueOfFeets,3))
print("Miles:",round(valueOfMiles,3))
print("Furlongs:",round(valueOfFurlongs,3))
print("Minutes to walk "+str(round(inputRodsInFloat,3))+" rods:",round(valueOfMinutesToWalk,3))