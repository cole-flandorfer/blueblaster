class BlueNode():
	def __init__(self):
		self.children = [None] * 10
		self.isEndOfNumber = False

class BlueTrie:
	def __init__(self):
		self.root = BlueNode()

	def insert(self, number):
		pointer = self.root
		key = str(number)

		for n in key:
			index = int(n)
			if pointer.children[index] is None:
				newNode = BlueNode()
				pointer.children[index] = newNode

			pointer = pointer.children[index]

		pointer.isEndOfNumber = True

	def search(self, number):
		pointer = self.root
		key = str(number)

		for n in key:
			index = int(n)
			if pointer.children[index] is None:
				return False

			pointer = pointer.children[index]

		return pointer.isEndOfNumber

if __name__ == '__main__':
	blueData = BlueTrie()
	insertData = [490, 148, 69, 704, 567, 723, 308, 517, 674, 341, 781, 885, 904, 297, 948, 530, 990, 67, 273, 461, 96, 16, 792, 66, 695, 790, 321, 263, 772, 482, 651, 347, 159, 259, 587, 324, 843, 426, 48, 406]
	for i in insertData:
		blueData.insert(i)

	searchKey = "1"
	while int(searchKey) != 0:
		searchKey = input("Enter Pattern Number (0 to end): ")
		try:
			searchKey = int(searchKey)
			print(blueData.search(searchKey))
		except:
			print("Input was not a number, please try again")


	print("GOODBYE")