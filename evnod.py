a=range(51,100)
print [x**2 if not x%2 else x**3 for x in a if x%3]
