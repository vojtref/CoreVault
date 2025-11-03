- = (lineární) spojový seznam/list
- v každém uzlu ukazatel na následující uzel
---
- uzel
```python
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
```
- ručně sestavený linked list:
```python
n1 = Node("a")
n2 = Node("b")
n3 = Node("c")

n1.next = n2
n2.next = n3
```
- první prvek označovaný jako **head**, begin, first...
```python
head = n1
```
- skrz první prvek lze projít celým seznamem
```python
tmp = head
while tmp != None:
	print(tmp.data)
	tmp = tmp.next
```
- seznam jako objekt
```python
class LinkedList:
	def __init__(self):
		self.head = None
	
	# Přidá další data na začátek seznamu
	def add(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode
	
	# Přidá data do seznamu za zadaný uzel
	def insert(self, data, node):
		newNode = Node(data)
		newNode.next = node.next
		node.next = newNode
	
	# Vrátí data prvního uzlu a odebere uzel ze seznamu
	def pop(self):
		data = self.head.data
		self.head = self.head.next
		return data
	
	# Vrátí první uzel s danými daty (nebo `None` pokud takový uzel neexistuje)
	def find(self, data):
		tmp = self.head
		while tmp != None:
			if tmp == data:
				return tmp
			tmp = tmp.next
		return None
```  

#B3B33ALP
