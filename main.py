import json
import os

filename = input("Name of the file to load from data folder: ")

basePath = os.path.dirname(__file__)
relativePath = "data/" + filename + ".json"
fullPath = os.path.join(basePath, relativePath)

print(fullPath)

with open(fullPath, 'r') as f:
	dataDictionary = json.load(f)

print(dataDictionary)

thresh = float(input("Enter the minimum value to highlight: "))

while True:
	searchKey = input("Enter Pattern Number (\"END\" to end): ")
	if searchKey == "END":
		break
	else:
		try:
			searchKey = int(searchKey)
		except:
			print("Input was not a pattern number, please try again")
			continue
		result = dataDictionary.get(str(searchKey))
		if result == None:
			print("...")
		else:
			print(result)
			try:
				result = float(result)
			except:
				continue
			else:
				if result >= thresh:
					print("""\
                                                           
                            ,--.                ,----..    
    ,---,.    ,---,       ,--.'|  ,----..      /   /   \   
  ,'  .'  \,`--.' |   ,--,:  : | /   /   \    /   .     :  
,---.' .' ||   :  :,`--.'`|  ' :|   :     :  .   /   ;.  \ 
|   |  |: |:   |  '|   :  :  | |.   |  ;. / .   ;   /  ` ; 
:   :  :  /|   :  |:   |   \ | :.   ; /--`  ;   |  ; \ ; | 
:   |    ; '   '  ;|   : '  '; |;   | ;  __ |   :  | ; | ' 
|   :     \|   |  |'   ' ;.    ;|   : |.' .'.   |  ' ' ' : 
|   |   . |'   :  ;|   | | \   |.   | '_.' :'   ;  \; /  | 
'   :  '; ||   |  ''   : |  ; .''   ; : \  | \   \  ',  /  
|   |  | ; '   :  ||   | '`--'  '   | '/  .'  ;   :    /   
|   :   /  ;   |.' '   : |      |   :    /     \   \ .'    
|   | ,'   '---'   ;   |.'       \   \ .'       `---`      
`----'             '---'          `---`                    
                                                           
						""")


print("GOODBYE...")