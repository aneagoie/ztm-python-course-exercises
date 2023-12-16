def do_stuff(num=0):
  try:
    if num: # try to test for when input is 0. How can you fix this?
      return int(num) + 5
    else:
      return 'please enter number'
  except ValueError as err:
    return err