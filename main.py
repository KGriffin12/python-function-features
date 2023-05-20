#1 arb_args
def arb_args(*args):
  for a in args:
    print(a)


#2 inner_func
def inner_func(x, y):

  def inner_1():
    return x + y

  def inner_2():
    return x - y

  print(inner_1() + inner_2())

  #3 lunch_lady
  def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)


#4 sum_n_product
def sum_n_product(x, y):
  return x + y, x * y


#5 alias_arb_args
alias_arb_args = arb_args


#6 arb_mean
def arb_mean(*args):
  total = 0
  for a in args:
    total += a
  print(a / len(args))


#7 arb_longest_string
def arb_longest_string(*args):
  long = 0
  longest = ""
  for a in args:
    if len(a) > long:
      long = len(a)
      longest = a
  return longest


#test