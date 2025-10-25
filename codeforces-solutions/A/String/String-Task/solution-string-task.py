a = input()
result = ""
for i in a:
    if i in "aoyeuiAOYEUI":
        continue
    else:
        result += "." + i.lower()
print(result)
