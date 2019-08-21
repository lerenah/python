def find_happy_number(num):
  # TODO: Write your code here
  output = []
  copy_num = num
  digits = []
  while copy_num != 1:
    old_num = copy_num
    while old_num > 0:
      right_num = old_num % 10
      digits.append(right_num)
      old_num -= right_num
      digits.append(old_num // 10)
      old_num //= 10
    while len(digits):
      new_num = 0
      new_num += digits.pop()**2
      if new_num in output:
        return False
      output.append(new_num)
    copy_num = new_num


  return True
