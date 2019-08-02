class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if value < self.value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)

		if value >= self.value:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)

        return self

    def contains(self, value):
        # Write your code here.
		if value == self.value:
			return True
		elif value < self.value:
			if self.left:
				return self.left.contains(value)
		else:
			if self.right:
				return self.right.contains(value)
		return False

	def get_successor(self):
		if self.left:
			self.left.get_successor()
		return self.left

	def removeNode(self, data):
		if not self:
			return self
		if data < self.value:
			self.left = self.left.removeNode(data)
		elif data > self.value:
			self.right = self.right.removeNode(data)
		else:
			if not self.left and not self.right:
				del self
				return None
			if not self.left:
				temp = self.right
				del self
				return temp
			elif not self.right:
				temp = self.left
				del self
				return temp
			temp = self.right.get_successor()
			self.value = temp.value
			self.right = self.right.removeNode(temp.value)
		return self


    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		if not self:
			return self
		if self is not None:
			self = self.removeNode(value)

        return self
