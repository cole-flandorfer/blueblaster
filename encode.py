import json
import os

filename = input("Name of the file:")

dataDictionary = {
	"foo":"bar"
}

while True:
	pattern = input("Input pattern number (input \"END\" to finish): ")
	if pattern == "END":
		break
	else:
		try:
			pattern = int(pattern)
		except:
			print("Not a valid pattern number")
			continue
	value = input("Input relevant value: ")
	try:
		value = float(value)
	except:
		print("Non-float value will be stored as a string")
	dataDictionary[pattern] = value

basePath = os.path.dirname(__file__)
relativePath = "data\\" + filename + ".json"
fullPath = os.path.join(basePath, relativePath)

print(fullPath)

with open(fullPath, 'w') as f:
	json.dump(dataDictionary, f, indent=2)

input("Press enter to close...")

print("GOODBYE...")