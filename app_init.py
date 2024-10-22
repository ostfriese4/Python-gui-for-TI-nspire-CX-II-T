def ImportToKernel(k):
  apps=[]
  apps.append("system_search_gui")
  apps.append("calculator_app")
  apps.append("tictactoe_app")
  apps.append("test_apps")
  apps.append("settings_app")
  apps.append("graphs_app")
  apps.append("pse_app")
  apps.append("ships_app")
  apps.append("clocks_app")
  apps.append("apple_theme")
  apps.append("propaganda_app")
  apps.append("screensaver")
  apps.append("extra_characters_gui")
  apps.append("system_search_gui")

  w=k.get("gui").window(title="starting")
  l=k.get("widgets").Label(w,text="")
  def code():
    name=apps.pop()
    l.set_text(name)
    k.get(name)
    if apps==[]:
      w.close()
      proc.delete()
  proc=k.get("kernel").process(k,name="init",code=code)
