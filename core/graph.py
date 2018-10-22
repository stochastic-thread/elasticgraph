class Graph():
  def __init__(self):
    self.vertices = {} # maps (vk) -> dict, which contains properties
    self.edges    = {} # maps (vk1, vk2) -> dict, which may contain any
                       # number of prop label to prop value pairs
  def __str__(self):
    retval = ""
    for index, label in enumerate(self.vertices):
      retval += ("{0}\n\t".format(label))
      if self.vertices[label] == None:
        self.vertices[label] = {}
      props = self.vertices[label]
      pks = props.keys()
      pksl = len(pks)
      for index,key in enumerate(pks):
        retval += ("{0} : {1}".format(key,props[key]))
        if index != pksl-1:
          retval += ";\n\t"
        else:
          retval += "\n"
    retval += "\n"
    for neighbors in self.edges:
        (v1, v2) = neighbors
        retval += "({0})===({1})===({2})\n".format(v1,self.edges[neighbors],v2)
    return retval

  def add_vertex(self, label, value):
    vs = self.vertices
    retval = False
    if label not in vs.keys():
      vs[label] = value
      retval = True
    else:
      if vs[label] != value:
        print("Updating {0}:{1} to {0}:{2}".format(label, vs[label], value))
        vs[label] = value
        retval = True
      else:
        print("Identical vertex already exists")
        print("key:{0}, value:{1}".format(label, vs[label]))
    return retval

  def add_edge(self, vl1, vl2, edge_info):
      vs = self.vertices
      vsk = vs.keys()
      if vl1 not in vsk:
        self.add_vertex(vl1, None)
      if vl2 not in vsk:
        self.add_vertex(vl2, None)
      self.edges[(vl1, vl2)] = edge_info

def main():
    g = Graph()
    g.add_vertex('A', {'full name': 'Arthur Maroufi Colle', 'birthday': {'year':1992,'month':2,'date':18}, 'alma mater': 'University of Maryland, College Park'})
    g.add_vertex('S', {'full name': 'Sophie Mireille-Anastasia Colle', 'birthday': {'year':1996,'month':10,'date':9}, 'alma mater': 'Virginia Polytechnic Institute and State University'})
    g.add_vertex('J', {'full name': 'Jasmine Hazelnut', 'birthday': {'year':1994,'month':4,'date':8}, 'alma mater': 'UMiami'})
    g.add_edge('A', 'S', {'relationship':'family', 'details': 'siblings', 'subdetails': 'brother-sister', 'roles': {'brother':'A', 'sister': 'S'}})
    g.add_edge('A', 'J', {'relationship':'none', 'details': 'old flame', 'subdetails': 'exbf-exgf', 'roles': {'exbf':'A', 'exgf':'J'}})
    g.add_edge('A', 'R', {'relationship': 'family', 'details': 'family', 'subdetails': 'father-son', 'roles': {'father': 'R', 'son': 'A'}})
    graph_representation = str(g)
    print(graph_representation)

if __name__ == "__main__":
    main()
