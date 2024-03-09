str = input("Введіть рядок - ")
rev_str = ""
for i in range(len(str), 0, -1):
  rev_str += str[i]
print(rev_str)