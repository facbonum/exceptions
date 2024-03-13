class SomeError(Exception):
  pass

x = 2
try:
  raise SomeError("This is not a cool error.")
  # raise Exception("I'm a custom exception!") # generic exception
  # print(x/0)
  # if not type(x) is str:
  #   raise TypeError("Only strings are allowed.") # built-in Python error
except NameError:
  print('NameError means something is probably undefined.')
except ZeroDivisionError:
  print('Please do not divide by zero.')
except Exception as error:
  print(error)
else: # only if there are no exceptions
  print('No errors.')
finally: # always, whether or not there are exceptions
  print("I'm going to print with or without an error.")