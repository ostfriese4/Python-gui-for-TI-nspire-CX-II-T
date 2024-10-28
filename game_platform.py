def ImportToKernel(k):
  _ = k.get("translations").translate
  class user:
    def __init__(self,name):
      self.name=name
      self.score=0
  class platform:
    def __init__(self):
      self.user1=None
      self.user2=None
    def reset(self):
      self.user1=None
      self.user2=None
      self.resetApp.delete()
    def init(self,app):
      if self.user1 is None or self.user2 is None:
        gui=k.get("gui")
        w=gui.window(title="Games")
        widgets=k.get("widgets")
        l=widgets.Label(w,text=_("Please enter your names:"),x=0,y=0,width=100,height=0.25)
        n1=widgets.TextEdit(w,text="",x=0,y=0.27,width=0.48,height=0.45)
        n2=widgets.TextEdit(w,text="",x=0.52,y=0.27,width=0.48,height=0.45)
        b=widgets.Button(w,text=_("Next"),x=0,y=0.75,width=1,height=0.25,text_align="center")
        def ready():
          self.user1=user(n1.get_text())
          self.user2=user(n2.get_text())
          w.close()
          self.resetApp=k.get("apps")(name="Reset Games",categories=["Games"],startcode=self.reset)
          app()
        b.clicked.connect(ready)
      else:
        app()
  return platform()
