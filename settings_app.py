def ImportToKernel(k):
  def app():
    gui=k.get("gui")
    widgets=k.get("widgets")
    window=gui.window(title="Einstellungen")
    settings=k.get("settings")()


    def set_theme():
      themes=k.lib["gui"]["themes"]
      title=theme.get_var()
      for i in themes:
        if i.name==title:
          i.enable()
          return

    def set_screensaver():
      settings.set("Screensaver_timeout",int(screensaverInput.get_text()),True)

    screensaverLabel=widgets.Label(window,height=0.45,width=0.5,text="Bildschirmshonerzeit:")
    screensaverInput=widgets.TextEdit(window,x=0.55,height=0.45,width=0.45,text=str(settings.get("Screensaver_timeout")))
    screensaverInput.updated.connect(set_screensaver)
    themes=[]
    for i in k.lib["gui"]["themes"]:
      themes.append(i.name)
    themeLabel=widgets.Label(window,y=0.5,width=0.5,height=0.5,text="Design:")
    theme=widgets.ComboBox(window,x=0.55,width=0.45,y=0.5,height=0.5,options=themes)
    def update_theme():
      theme.set_var(k.lib["gui"]["enabled theme"].theme.name)
    update_theme()
    k.lib["gui"]["theme changed"].connect(update_theme)
    theme.text_updated.connect(set_theme)

  k.get("apps")(name="Einstellungen",categories=["System","Zubehör"],startcode=app)
