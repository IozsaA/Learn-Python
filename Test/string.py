s = '12ab7u7uuacd405'
result = ''.join([i for i in s if not i.isdigit()])
print(result)