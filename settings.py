def ImportToKernel(k):
  dataVAR={}
  class settings:
    def __init__(self):
      self._locale={}
    def get(self,key,alt=None):
      if key in self._locale:
        return self._locale[key]
      if key in dataVAR:
        return dataVAR[key]
      return alt
    def set(self,key,data,open=False):
      if open:
        dataVAR[key]=data
      else:
        self._locale[key]=data
  return settings
