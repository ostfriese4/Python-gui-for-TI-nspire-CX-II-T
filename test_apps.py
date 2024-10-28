def ImportToKernel(k):
  k.get("apps")
  k.get("gui")
  lib=k.lib["gui"]
  def noteTest():
    w=lib["window"](title="Notes")
    txt="Hello"
    e=lib["TextEdit"](w,text=txt)
  k.lib["app"](name="Notes",startcode=noteTest,categories=["Tests","Utilities"])
  def testcenter():
    w=lib["window"](title="Testcenter")
    l=lib["Label"](w,width=0.5,height=0.7,text="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    b=lib["Button"](w,x=0.55,width=0.45,height=0.7,text="close")
    b.clicked.connect(w.close)
    nb=lib["Button"](w,y=0.75,height=0.25,text="Notes")
    nb.clicked.connect(noteTest)
  k.lib["app"](name="Testcenter",startcode=testcenter,categories=["Tests"])
  k.lib["app"](name="Notification",categories=["Tests"],startcode=lambda:lib["notification"](app="test",text="awrxABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
