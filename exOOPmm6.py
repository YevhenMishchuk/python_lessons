import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    #print("1")
    return self.cont[index + random.randint(-2, 2)]
    
  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
#print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
