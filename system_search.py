def ImportToKernel(k):
  kernel=k.get("kernel")
  modules = []
  class Item:
    def __init__(self, name="item", description="description", code=kernel.empty):
      self.code=code
      self.name=name
      self.description=description
  class Module:
    def __init__(self, name):
      modules.append(self)
    def search(self,term):
      return []
  def search_modules(term):
    items=[]
    for modul in modules:
      new=k.run_code(lambda:modul.search(term))
      if new:
        items += new
    return items
  output=kernel.lib()
  output.modul=Module
  output.search=search_modules
  output.item=Item
  output.modules=modules
  return output
