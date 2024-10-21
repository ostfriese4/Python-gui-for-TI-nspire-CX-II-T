def ImportToKernel(k):
  lib = k.get("kernel").lib()

  userLanguage = "en"

  languages = {}

  class language:
    def __init__(self, name="en"):
      self.name = name
      self.sets = []
      languages[short] = self

  def getLanguage(name):
    if name in languages:
      return languages[name]
    languages[name] = language(name)
    return languages[name]

  def translate(term, language = None):
    if language is None:
      language = userLanguage
    sets = getLanguage(language)
    for set in sets:
      if term in set:
        return set[term]
    return term

  def setLanguage(name):
    nonlocal userLanguage
    userLanguage = name

  lib.translate = translate
  lib.setLanguage = setLanguage
  lib.getLanguage = getLanguage
  lib.language = language

  return lib

