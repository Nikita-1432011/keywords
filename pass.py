for a in range(25):
  if a % 20 == 0:
    print("twist")
  elif a % 15 == 0:
    print("fizz")
  elif a % 5 == 0:
    pass
  elif a % 3 == 0:
    print("buzz")
  else:
    print(a)