print("starting")
from kernel import*
k=kernel()
def log(delete=False):
  k.print_log(delete)
try:
  k.get("ti_system").clear_history()
#  k.print=True;log(True)
  k.get("input").key("esc").pressed.connect(k.stop)
#  k.get("files")
#  k.get("shell")
  k.get("app_init")
  k.get("gui").start()
  k.start()
except Exception as err:
  k.errors+=1
  k.log("<ERROR>")
  k.log(err)
if k.errors>0:
  print(str(k.errors)+" Error(s) occured. Type log() for more information")
