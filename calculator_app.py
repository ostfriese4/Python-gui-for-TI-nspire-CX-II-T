def ImportToKernel(k):
  backend=k.get("system_search")

  namespace={}

  def calculate(term):
    code="result="+term
    code=code.replace("^","**")
    code=code.replace("-","-")
    namespace[""]=2.718281828459
    namespace["pi"]=3.1415926535898
    namespace["π"]=3.1415926535898
    try:
      exec(code,namespace)
    except Exception as e:
      return e
    return namespace["result"]

  calc=backend.modul("Calculator")
  def calc_search(term):
    for i in term:
      if i not in "0123456789.-+-*/()^= π":
        return []
    result=calculate(term)
    if not (type(result)==int or type(result)==float):
      return []
    return [backend.item(str(result),"Calculator",lambda:start(term))]
  calc.search=calc_search

  def start(starttext=""):
    k.get("gui")
    gui=k.lib["gui"]
    window=gui["window"](title="Calculator")
    entry=gui["TextEdit"](window,height=0.6,text=starttext)
    result=gui["Label"](window,y=0.65,height=0.35,text="")
    def work(info=None):
      exercise=entry.get_text()
      result.set_text(str(calculate(exercise)))
    entry.updated.connect(work)
    entry.click()
    work()
  k.get("input").key("scratchpad").pressed.connect(start)
  app=k.get("apps")(name="calculator",categories=["Utilities"],startcode=start)
