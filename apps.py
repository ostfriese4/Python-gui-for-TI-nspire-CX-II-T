def ImportToKernel(k):
  k.get("gui")
  menu=k.lib["gui"]["Appmenu"]
  apps=[]
  _ = k.get("translations").translate
  class app:
    def __init__(self,name="App",categories=[],startcode=k.lib["system"]["empty"],initcode=k.lib["system"]["empty"], description="",keywords=""):
      apps.append(self)
      self._name=name
      self._description=description
      self._categories = categories
      self._start=startcode
      self._keywords=keywords
      self._init=initcode
      self._categories=categories
      self.rename()
      k.get("translations").changed.connect(self.rename)
    def rename(self):
      categories = self._categories
      if categories==[]:
        categories.append(_("Other"))
      for categorie in categories:
        path=categorie
        path=path.split("/")
        parent=menu.items # Dict of the app-menu
        for sub in path:
          if not _(sub) in parent:
            parent[_(sub)]={}
          parent=parent[_(sub)]
        parent[_(self._name)]=self.run
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
