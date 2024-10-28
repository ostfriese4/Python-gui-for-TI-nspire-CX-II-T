def ImportToKernel(k):
  backend=k.get("system_search")
  apps = backend.modul("Apps")
  def app_search(term):
    apps=k.lib["apps"]
    term=term.lower()
    items=[]
    for app in apps:
      if term in app._name.lower() or term in app._description.lower() or term in app._keywords.lower():
        items.append(backend.item(app._name,app._description,app.run))
    return items
  apps.search=app_search

  theme=backend.modul("Theme")
  def theme_search(term):
    items=[]
    for i in k.lib["gui"]["themes"]:
      if term in i.name.lower():
        items.append(backend.item("Design: "+i.name, "Design aktivieren", i.enable))
    return items
  theme.search=theme_search
