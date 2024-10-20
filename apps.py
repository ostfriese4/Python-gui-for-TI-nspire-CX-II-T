def ImportToKernel(k):
  k.get("gui")
  menu=k.lib["gui"]["Appmenu"]
  apps=[]
  class app:
    def __init__(self,name="App",categories=[],startcode=k.lib["system"]["empty"],initcode=k.lib["system"]["empty"], description="",keywords=""):
      apps.append(self)
      self._name=name
      self._description=description
      self._start=startcode
      self._keywords=keywords
      self._init=initcode
      self._categories=categories
      if categories==[]:
        categories.append("unsorted")
      for categorie in categories:
        path=categorie
        path=path.split("/")
        parent=menu.items
        for sub in path:
          if not sub in parent:
            parent[sub]={}
          parent=parent[sub]
        parent[name]=self.run
      self.init()
    def init(self):
      k.run_code(self._init)
    def run(self):
      k.run_code(self._start)
    def delete(self):
      pass
  k.lib["app"]=app
  k.lib["apps"]=apps
  return app
