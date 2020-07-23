class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont,line,other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam/hello)


class SpecialString2:
  def __init__(self, cont):
    self.cont = cont
  
  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return " Ukraine ".join([self.cont,line,other.cont])

spam2 = SpecialString2("spam")
hello2 = SpecialString2("Hello world!")
print(spam2/hello2)