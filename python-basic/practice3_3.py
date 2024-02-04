python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자 여부
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

# find 에서는 원하는 값이 없으면 -1
# index 에서는 원하는 값이 없으면 에러 발생

print(python.count("n")) # n이 총 몇번 있는지