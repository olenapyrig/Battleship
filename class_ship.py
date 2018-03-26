import string


class Ship():

	def __init__(self, player_field, coordinate):
		self.player_field = player_field
		self.coordinate = coordinate

	def has_ship(self):
		"""
		(self)->(bool)
		Check whether there is a ship on this coordinates
		"""
		letters = list(string.ascii_uppercase)
		if self.player_field[self.coordinate[1]][
			letters.index(self.coordinate[0])] == 1:
			return True
		else:
			return False


class Field():
	def __init__(self):
		self.field1 = "file1.txt"
		self.field2 = "file2.txt"
		self.lst_player1 = []
		self.lst_player2 = []

	def player1_field(self):
		"""
		(data)->(list)
		Read the information from the file and return the list with "1" and "0"
		instead of "X" and "0"
		"""
		with open(self.field1, "r") as f:
			for i in f:
				lst1 = []
				for j in i:
					if j == "X":
						lst1.append(1)
					if j == "0":
						lst1.append(0)
				self.lst_player1.append(lst1)

		return self.lst_player1

	def player2_field(self):
		"""
		(data)->(list)
		Read the information from the file and return the list with "1" and "0"
		instead of "X" and "0"
		"""
		with open(self.field2, "r") as f:
			for i in f:
				lst1 = []
				for j in i:
					if j == "X":
						lst1.append(1)
					if j == "0":
						lst1.append(0)
				self.lst_player2.append(lst1)
		return self.lst_player2


class Game():
	def __init__(self):
		self.player1 = input(
			"Enter your name(player1): ")
		self.player2 = input(
			"Enter your name(player2): ")
		self.player1_field = Field().player1_field()
		self.player2_field = Field().player2_field()
		self.step = 1

	def game(self):
		"""
		(self)->(str)
		Run the game,return the winner
		"""
		count_1 = 0
		count_2 = 0
		while not count_1 == 20 or count_2 == 20:

			if self.step % 2 != 0:
				print("{}'s turn".format(self.player1))
				print("Choose the coordinate you want to shoot at")
				row = int(input("Enter row: ")) - 1
				col = input("Enter column: ").upper()
				coordinate = [col, row]
				a = Ship(self.player2_field, coordinate).has_ship()
				self.step += 1
				if a == True:
					print("You hit me")
					count_1 += 1
					print("Your count: {}".format(count_1))

				else:
					print("You miss")

			elif self.step % 2 == 0:
				print("{}'s turn".format(self.player2))
				print("Choose the coordinate you want to shoot at")
				row = int(input("Enter row: ")) - 1
				col = input("Enter column: ").upper()
				coordinate = [col, row]
				b = Ship(self.player1_field, coordinate).has_ship()
				self.step += 1
				if b == True:
					print("You hit me")
					count_2 += 1
					print("Your count: {}".format(count_1))

				else:
					print("You miss")
		else:
			if count_1 == 2:
				print("{} win".format(self.player1))
			else:
				print("{} win".format(self.player2))


Game().game()
