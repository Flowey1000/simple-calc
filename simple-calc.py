def simple_calculator(expression):
  try:
    result = eval(expression)
    return result
  except Exception as e:
    return f"Error: {e}"

expression = input("")
answer = simple_calculator(expression)
print(f"The answer to '{expression}' is: {answer}")
