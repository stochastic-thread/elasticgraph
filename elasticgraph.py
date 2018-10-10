
class Triplet(object):
  def __init__(self, a, relation, b):
    self.origin = a
    self.path = relation
    self.terminus = b
  def format_triplet(self):
    if isinstance(self.origin, str) and isinstance(self.terminus, str):
      return('('+self.origin+'=->'+self.path+'=->'+self.terminus+')')
    else:
      return "Wrong format, look at the code"
x = Triplet('amelia', 'is friends with', 'barty')
print(x.format_triplet())

