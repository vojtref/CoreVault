from re import split as re_split

in_string = input()

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def bracket_priority(self):
		if isinstance(self.value, int):
			return 0
		elif isinstance(self.value, str):
			if self.value == "**":
				return 1
			elif self.value == "*" or self.value == "/":
				return 2
			elif self.value == "+" or self.value == "-":
				return 3

	def __str__(self):
		return f"{self.value}"

# Splitneme string podle regexu na operatory (rozliseni * a ** vyzaduje negative lookahead), a vyradime prazdne tokeny (workaround, asi spatne napsany regex)
tokens = [t for t in re_split(r"(\+{1}|\-{1}|\*{1}(?!\*)|\/{1}|\*{2})|\s+", in_string) if t != None and len(t) > 0]
OPERATORS = ("+", "-", "*", "/", "**")

def operator_tree(tokens):
	if len(tokens) == 0:
		print("ERROR")
		quit()

	token = tokens.pop(0) # Evalvujeme zleva
	if token not in OPERATORS: # Pokud token neni operator, predpokladame, ze je cislo
		token = int(token)

	node = Node(token)

	if token in OPERATORS:
		# Podstromy na kazde strane
		node.left = operator_tree(tokens)
		node.right = operator_tree(tokens)
	else:
		node = Node(token)

	return node

def print_tree(node, level=0):
	if node is not None:
		print_tree(node.right, level + 1)
		print('\t' * level + str(node.value))
		print_tree(node.left, level + 1)

root = operator_tree(tokens)
if len(tokens) > 0:
	print("ERROR")
	quit()

print_tree(root)