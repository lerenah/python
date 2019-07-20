def balancedBrackets(string):
	q1 = []
	for el in string:
		if el == '{':
			q1.append(el)
		elif el == '[':
			q1.append(el)
		elif el == '(':
			q1.append(el)
		elif el == '}':
			if not len(q1) or q1.pop() != '{':
				return False
		elif el == ']':
			if not len(q1) or q1.pop() != '[':
				return False
		elif el == ')':
			if not len(q1) or q1.pop() != '(':
				return False

	return len(q1) == 0
