import string
import random


def read_file(path):
	"""
	(data)->(list)
	Read the information from the file and return the list with "1" and "0"
	instead of "X" and "0"
	"""
	lst = []
	with open(path, "r") as f:
		for i in f:
			lst1 = []
			for j in i:
				if j == "X":
					lst1.append(1)
				if j == "0":
					lst1.append(0)
			lst.append(lst1)

	return lst


print(read_file("file.txt"))


def has_ship(lst, coordinate):
	"""
	(list,list)->(bool)
	Check whether there is a ship on this coordinates
	"""
	letters = list(string.ascii_uppercase)
	if lst[coordinate[1]][letters.index(coordinate[0])] == 1:
		return True
	else:
		return False
print(has_ship(read_file("file.txt"),["A",1]))


def ships(lst):
	"""
	(list)->(list)
	Return the list of coordinates, on which there are ships
	"""
	alp = [i for i in string.ascii_uppercase]
	lst1 = []
	for line in lst:
		for cells in line:
			if cells == 1:
				lst_1 = [alp[line.index(cells)], lst.index(line) + 1]
				line[line.index(cells)] = 0
				lst1.append(lst_1)
	return lst1


def ship_size(coordinate):
	"""
	(list)->(int)
	Check which size the ship has
	"""
	lst = read_file("file.txt")
	letters = list(string.ascii_uppercase)
	ship = has_ship(lst, coordinate)

	if ship == True:
		count = 1
		i = lst[coordinate[1]]
		j = i[letters.index(coordinate[0])]
		g = i.index(j)
		if i[g + 1] == 1:
			count += 1
			if i[g + 2] == 1:
				count += 1
				if i[g + 2] != i[-1]:
					if i[g + 3] == 1:
						count += 1
		elif i[g - 1] == 1:
			count += 1
			if i[g - 2] == 1:
				count += 1
				if i[g - 2] != i[-1]:
					if i[g - 3] == 1:
						count += 1
		return count
	else:
		return 0


def is_valid(lst):
	"""
	(list)->(bool)
	Check whether the field size is appropriate for the game
	"""
	if len(lst) == 10:
		if all(len(i) == 10 for i in lst):
			return True
		else:
			return False
	else:
		return False


def field_to_str(lst):
	"""
	(list)->(str)
	return the field as a string
	"""
	return "\n".join(str(i) for i in lst)


def generate_field():
	"""
	(None)->(list)
	Randomly field generating
	"""
	board = []
	for i in range(10):
		lst = []
		for j in range(10):
			lst.append(0)
		board.append(lst)
	for i in range(4):
		a = random.randint(0, 9)
		b = random.randint(0, 9)
		board[a][b] = 1
	for i in range(3):
		a = random.randint(0, 8)
		b = random.randint(0, 8)
		board[a][b] = 1
		board[a + 1][b + 1] = 1
	for i in range(2):
		a = random.randint(0, 7)
		b = random.randint(0, 7)
		board[a][b] = 1
		board[a + 1][b + 1] = 1
		board[a + 2][b + 2] = 1
	for i in range(1):
		a = random.randint(0, 6)
		b = random.randint(0, 6)
		board[a][b] = 1
		board[a + 1][b + 1] = 1
		board[a + 2][b + 2] = 1
		board[a + 3][b + 3] = 1
	return board
