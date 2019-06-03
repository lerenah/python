def getNthFib(n):
    # Write your code here.
	if n <= 1:
		return 0
	if n <= 3:
		return 1
	first = 1
	second = 1
	_next = first + second
	for i in range(4, n):
		first = second
		second = _next
		_next = first + second

	return _next
