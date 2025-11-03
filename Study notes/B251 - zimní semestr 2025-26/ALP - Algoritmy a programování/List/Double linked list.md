- = obousměrný/dvousměrný spojový seznam
- každý uzel obsahuje ukazatel jak na další prvek (`next`), tak na předchozí prvek (`prev`)
- první a poslední: **`head`**/**`tail`**, `begin`/`end` . . .
---
```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoubleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	# . . .
	
	# Přidání prvku lehce složitější, potřeba změnit ukazatele obou okolních
	# prvků (pokud existují), ale celkový princip stejný.
	# Možné zjednodušit, ifs se hodně překrývají, zde rozepsáno pro názornost.
	def insert(self, node, data):
		newNode = Node(data)
		
		if node == None: # Začátek listu, totožné s add
			newNode.prev = None # Zahrnuto v konstruktoru Node
			newNode.next = self.head
			
			newNode.next.prev = newNode
			self.head = newNode
		elif node == self.tail: # Konec listu
			newNode.prev = self.tail
			newNode.next = None # Zahrnuto v konstruktoru Node
			
			newNode.prev.next = newNode
			self.tail = newNode
		else: # Prostředek listu
			newNode.prev = node
			newNode.next = node.next
			
			newNode.next.prev = newNode
			newNode.prev.next = newNode
	
	# Procházení dopředu...
	def traverseForwards(self, fromNode = None):
		if fromNode == None:
			fromNode = self.head
		while fromNode != None:
			print(fromNode.data)
			fromNode = fromNode.next
	
	# ...a dozadu
	def traverseBackwards(self, fromNode = None):
		if fromNode == None:
			fromNode = self.tail
		while fromNode != None:
			print(fromNode.data)
			fromNode = fromNode.prev
```

#B3B33ALP
