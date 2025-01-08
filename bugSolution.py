def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Both inputs must be numbers"

result = function(5, '10')
print(result)
result2 = function(5, 'abc')
print(result2)