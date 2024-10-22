def ImportToKernel(k):
  _ = k.get("translations").translate
  elements = []

  class element:
    def __init__(self, short, name, position = (1,1)):
      self.name = name
      self.short = short
      self.position = position
      elements.append(self)

  def app():
    widgets = k.get("widgets")
    width = 1/18
    height = 1/7
    window = k.get("gui").window(title = _("Periodic System"))
    window.maximize()

    for element in elements:
      x,y = element.position
      x = (x-1)*width
      y = (y-1)*height
      button = widgets.Button(window, text = element.short, x=x, y=y, width = width, height = height) # Create entry in the table
  def showElement(element):
    pass
  def runner(term):
    return []

  k.get("apps")(name = "Periodic table", categories = ["Education"], startcode = app) # Create App


  search = k.get("system_search")
  modul = search.modul("PSE") # Create search-modul
  modul.search = runner


  element("H", "Hydrogen", (1,1))
  element("He", "Helium", (18,1))
  element("Li", "Lithium", (1,2))
  element("Be", "Beryllium", (2,2))
  element("B", "Boron", (13,2))
  element("C", "Carbon", (14,2))
  element("N", "Nitrogen", (15,2))
  element("O", "Oxygen", (16,2))
  element("F", "Fluorine", (17,2))
  element("Ne", "Neon", (18,2))
  element("Na", "Sodium", (1,3))
  element("Mg", "Magnesium", (2,3))
  element("Al", "Aluminium", (13,3))
  element("Si", "Silicon", (14,3))
  element("P", "Phosphorus", (15,3))
  element("S", "Sulfur", (16,3))
  element("Cl", "Chlorine", (17,3))
  element("Ar", "Argon", (18,3))
  element("K", "Potassium", (1,4))
  element("Ca", "Calcium", (2,4))
  element("Sc", "Scandium", (3,4))
  element("Ti", "Titanium", (4,4))
  element("V", "Vanadium", (5,4))
  element("Cr", "Chromium", (6,4))
  element("Mn", "Manganese", (7,4))
  element("Fe", "Iron", (8,4))
  element("Co", "Cobalt", (9,4))
  element("Ni", "Nickel", (10,4))
  element("Cu", "Copper", (11,4))
  element("Zn", "Zinc", (12,4))
  element("Ga", "Gallium", (13,4))
  element("Ge", "Germanium", (14,4))
  element("As", "Arsenic", (15,4))
  element("Se", "Selenium", (16,4))
  element("Br", "Bromine", (17,4))
  element("Kr", "Krypton", (18,4))
  element("Rb", "Rubidium", (1,5))
  element("Sr", "Strontium", (2,5))
  element("Y", "Yttrium", (3,5))
  element("Zr", "Zirconium", (4,5))
  element("Nb", "Niobium", (5,5))
  element("Mo", "Molybdenum", (6,5))
  element("Tc", "Technetium", (7,5))
  element("Ru", "Ruthenium", (8,5))
  element("Rh", "Rhodium", (9,5))
  element("Pd", "Palladium", (10,5))
  element("Ag", "Silver", (11,5))
  element("Cd", "Cadmium", (12,5))
  element("In", "Indium", (13,5))
  element("Sn", "Tin", (14,5))
  element("Sb", "Antimony", (15,5))
  element("Te", "Tellurium", (16,5))
  element("I", "Iodine", (17,5))
  element("Xe", "Xenon", (18,5))
  element("Cs", "Caesium", (1,6))
  element("Ba", "Barium", (2,6))
  element("La", "Lanthanum", (3,6))
  element("Hf", "Hafnium", (4,6))
  element("Ta", "Tantalum", (5,6))
  element("W", "Tungsten", (6,6))
  element("Re", "Rhenium", (7,6))
  element("Os", "Osmium", (8,6))
  element("Ir", "Iridium", (9,6))
  element("Pt", "Platinum", (10,6))
  element("Au", "Gold", (11,6))
  element("Hg", "Mercury", (12,6))
  element("Tl", "Thallium", (13,6))
  element("Pb", "Lead", (14,6))
  element("Bi", "Bismuth", (15,6))
  element("Po", "Polonium", (16,6))
  element("At", "Astatine", (17,6))
  element("Rn", "Radon", (18,6))
  element("Fr", "Francium", (1,7))
  element("Ra", "Radium", (2,7))
  element("Ac", "Actinium", (3,7))
  element("Rf", "Rutherfordium", (4,7))
  element("Db", "Dubnium", (5,7))
  element("Sg", "Seaborgium", (6,7))
  element("Bh", "Bohrium", (7,7))
  element("Hs", "Hassium", (8,7))
  element("Mt", "Meitnerium", (9,7))
  element("Ds", "Darmstadtium", (10,7))
  element("Rg", "Roentgenium", (11,7))
  element("Cn", "Copernicium", (12,7))
  element("Nh", "Nihonium", (13,7))
  element("Fl", "Flerovium", (14,7))
  element("Mc", "Moscovium", (15,7))
  element("Lv", "Livermorium", (16,7))
  element("Ts", "Tennessine", (17,7))
  element("Og", "Oganesson", (18,7))
