def ImportToKernel(k):
  _ = k.get("translations").translate
  elements = []

  class element:
    def __init__(self, short, name, position=(1, 1), melting_point=None, boiling_point=None, electronegativity=None, classification=None, weight=None, atomic_number=None):
      self.name = name
      self.short = short
      self.position = position
      self.melting_point = melting_point
      self.boiling_point = boiling_point
      self.electronegativity = electronegativity
      self.classification = classification
      self.atomic_number = atomic_number
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
      button = widgets.Button(window, text = element.short, x=x, y=y, width = width, height = height, crop = False) # Create entry in the table
      button.clicked.info["element"]=element
      button.clicked.connect(show)
  def show(info):
      showElement(info["element"])
  def showElement(element):
    w=k.get("gui").window(title = _(element.name))
    text = "Name: "+_(element.name)+"\nSymbol: "+element.short+"\n"
    if element.melting_point:
      text += _("Melting point")+": "+str(element.melting_point)+" °C\n"
    if element.boiling_point:
      text += _("Boiling point")+": "+str(element.boiling_point)+" °C\n"
    if element.electronegativity:
      text += _("Electronegativity")+": "+str(element.electronegativity)+"\n"
    if element.classification:
      text += _("classification")+": "+str(element.classification)+"\n"
    if element.atomic_number:
      text += _("Atomic number")+": "+str(element.atomic_number)+"\n"
    k.get("widgets").Label(w,text=text)
  def runner(term):
    items = []
    term = term.lower()
    for element in elements:
      if term == element.short.lower():
        short = element # For correct element in lambda
        items.append(search.item(element.short + " - " + _(element.name), _("Periodic table"), lambda: showElement(short))) # Add reult to results
    return items

  k.get("apps")(name = "Periodic table", categories = ["Education"], startcode = app) # Create App


  search = k.get("system_search")
  modul = search.modul("PSE") # Create search-modul
  modul.search = runner


  element("H", "Hydrogen", (1,1), melting_point=-259.1, boiling_point=-252.9, electronegativity=2.2, classification="Nonmetal", weight=1.008, atomic_number=1)
  element("He", "Helium", (18,1), melting_point=-272.1, boiling_point=-268.9, electronegativity=None, classification="Noble gas", weight=4.0026, atomic_number=2)
  element("Li", "Lithium", (1,2), melting_point=180.5, boiling_point=1342, electronegativity=0.98, classification="Alkali metal", weight=6.94, atomic_number=3)
  element("Be", "Beryllium", (2,2), melting_point=1287, boiling_point=2970, electronegativity=1.57, classification="Alkaline earth metal", weight=9.0122, atomic_number=4)
  element("B", "Boron", (13,2), melting_point=2076, boiling_point=3927, electronegativity=2.04, classification="Metalloid", weight=10.81, atomic_number=5)
  element("C", "Carbon", (14,2), melting_point=3550, boiling_point=4827, electronegativity=2.55, classification="Nonmetal", weight=12.011, atomic_number=6)
  element("N", "Nitrogen", (15,2), melting_point=-210.0, boiling_point=-195.8, electronegativity=3.04, classification="Nonmetal", weight=14.007, atomic_number=7)
  element("O", "Oxygen", (16,2), melting_point=-218.8, boiling_point=-183.0, electronegativity=3.44, classification="Nonmetal", weight=15.999, atomic_number=8)
  element("F", "Fluorine", (17,2), melting_point=-219.6, boiling_point=-188.1, electronegativity=3.98, classification="Halogen", weight=18.998, atomic_number=9)
  element("Ne", "Neon", (18,2), melting_point=-248.6, boiling_point=-246.1, electronegativity=None, classification="Noble gas", weight=20.18, atomic_number=10)
  element("Na", "Sodium", (1,3), melting_point=97.8, boiling_point=883, electronegativity=0.93, classification="Alkali metal", weight=22.99, atomic_number=11)
  element("Mg", "Magnesium", (2,3), melting_point=650, boiling_point=1090, electronegativity=1.31, classification="Alkaline earth metal", weight=24.305, atomic_number=12)
  element("Al", "Aluminum", (13,3), melting_point=660.3, boiling_point=2470, electronegativity=1.61, classification="Metal", weight=26.982, atomic_number=13)
  element("Si", "Silicon", (14,3), melting_point=1414, boiling_point=3265, electronegativity=1.9, classification="Metalloid", weight=28.085, atomic_number=14)
  element("P", "Phosphorus", (15,3), melting_point=44.1, boiling_point=280.5, electronegativity=2.19, classification="Nonmetal", weight=30.974, atomic_number=15)
  element("S", "Sulfur", (16,3), melting_point=115.2, boiling_point=444.6, electronegativity=2.58, classification="Nonmetal", weight=32.06, atomic_number=16)
  element("Cl", "Chlorine", (17,3), melting_point=-101.5, boiling_point=-34.0, electronegativity=3.16, classification="Halogen", weight=35.45, atomic_number=17)
  element("Ar", "Argon", (18,3), melting_point=-189.3, boiling_point=-185.9, electronegativity=None, classification="Noble gas", weight=39.948, atomic_number=18)
  element("K", "Potassium", (1,4), melting_point=63.5, boiling_point=759, electronegativity=0.82, classification="Alkali metal", weight=39.098, atomic_number=19)
  element("Ca", "Calcium", (2,4), melting_point=842, boiling_point=1484, electronegativity=1.00, classification="Alkaline earth metal", weight=40.078, atomic_number=20)
  element("Sc", "Scandium", (3,4), melting_point=1541, boiling_point=2836, electronegativity=1.36, classification="Transition metal", weight=44.956, atomic_number=21)
  element("Ti", "Titanium", (4,4), melting_point=1668, boiling_point=3287, electronegativity=1.54, classification="Transition metal", weight=47.867, atomic_number=22)
  element("V", "Vanadium", (5,4), melting_point=1910, boiling_point=3407, electronegativity=1.63, classification="Transition metal", weight=50.942, atomic_number=23)
  element("Cr", "Chromium", (6,4), melting_point=1907, boiling_point=2671, electronegativity=1.66, classification="Transition metal", weight=51.996, atomic_number=24)
  element("Mn", "Manganese", (7,4), melting_point=1246, boiling_point=2061, electronegativity=1.55, classification="Transition metal", weight=54.938, atomic_number=25)
  element("Fe", "Iron", (8,4), melting_point=1538, boiling_point=2862, electronegativity=1.83, classification="Transition metal", weight=55.845, atomic_number=26)
  element("Co", "Cobalt", (9,4), melting_point=1495, boiling_point=2927, electronegativity=1.88, classification="Transition metal", weight=58.933, atomic_number=27)
  element("Ni", "Nickel", (10,4), melting_point=1455, boiling_point=2730, electronegativity=1.91, classification="Transition metal", weight=58.693, atomic_number=28)
  element("Cu", "Copper", (11,4), melting_point=1084.62, boiling_point=2562, electronegativity=1.90, classification="Transition metal", weight=63.546, atomic_number=29)
  element("Zn", "Zinc", (12,4), melting_point=419.5, boiling_point=907, electronegativity=1.65, classification="Transition metal", weight=65.38, atomic_number=30)
  element("Ga", "Gallium", (13, 4), melting_point=29.76, boiling_point=2204, electronegativity=1.81, classification="Metal", weight=69.723, atomic_number=31)
  element("Ge", "Germanium", (14, 4), melting_point=938.25, boiling_point=2833, electronegativity=2.01, classification="Metalloid", weight=72.63, atomic_number=32)
  element("As", "Arsenic", (15, 4), melting_point=817, boiling_point=614, electronegativity=2.18, classification="Metalloid", weight=74.922, atomic_number=33)
  element("Se", "Selenium", (16, 4), melting_point=221, boiling_point=685, electronegativity=2.55, classification="Nonmetal", weight=78.971, atomic_number=34)
  element("Br", "Bromine", (17, 4), melting_point=-7.2, boiling_point=58.8, electronegativity=2.96, classification="Halogen", weight=79.904, atomic_number=35)
  element("Kr", "Krypton", (18, 4), melting_point=-157.4, boiling_point=-153.4, electronegativity=3.00, classification="Noble gas", weight=83.798, atomic_number=36)
  element("Rb", "Rubidium", (1, 5), melting_point=39.31, boiling_point=688, electronegativity=0.82, classification="Alkalimetall", weight=85.468, atomic_number=37)
  element("Sr", "Strontium", (2, 5), melting_point=777, boiling_point=1382, electronegativity=0.95, classification="Erdalkalimetall", weight=87.62, atomic_number=38)
  element("Y", "Yttrium", (3, 5), melting_point=1526, boiling_point=3336, electronegativity=1.22, classification="Übergangsmetall", weight=88.906, atomic_number=39)
  element("Zr", "Zirconium", (4, 5), melting_point=1855, boiling_point=4409, electronegativity=1.33, classification="Übergangsmetall", weight=91.224, atomic_number=40)
  element("Nb", "Niob", (5, 5), melting_point=2477, boiling_point=4744, electronegativity=1.6, classification="Übergangsmetall", weight=92.906, atomic_number=41)
  element("Mo", "Molybdän", (6, 5), melting_point=2623, boiling_point=4639, electronegativity=2.16, classification="Übergangsmetall", weight=95.95, atomic_number=42)
  element("Tc", "Technetium", (7, 5), melting_point=2157, boiling_point=4265, electronegativity=1.9, classification="Übergangsmetall", weight=98, atomic_number=43)
  element("Ru", "Ruthenium", (8, 5), melting_point=2334, boiling_point=4150, electronegativity=2.2, classification="Übergangsmetall", weight=101.07, atomic_number=44)
  element("Rh", "Rhodium", (9, 5), melting_point=1964, boiling_point=3695, electronegativity=2.28, classification="Übergangsmetall", weight=102.91, atomic_number=45)
  element("Pd", "Palladium", (10, 5), melting_point=1554.9, boiling_point=2963, electronegativity=2.2, classification="Übergangsmetall", weight=106.42, atomic_number=46)
  element("Ag", "Silber", (11, 5), melting_point=961.78, boiling_point=2162, electronegativity=1.93, classification="Übergangsmetall", weight=107.87, atomic_number=47)
  element("Cd", "Cadmium", (12, 5), melting_point=321.07, boiling_point=767, electronegativity=1.69, classification="Übergangsmetall", weight=112.41, atomic_number=48)
  element("In", "Indium", (13, 5), melting_point=156.6, boiling_point=2072, electronegativity=1.78, classification="Metall", weight=114.82, atomic_number=49)
  element("Sn", "Zinn", (14, 5), melting_point=231.93, boiling_point=2602, electronegativity=1.96, classification="Metall", weight=118.71, atomic_number=50)
  element("Sb", "Antimon", (15, 5), melting_point=630.63, boiling_point=1587, electronegativity=2.05, classification="Halbmetall", weight=121.76, atomic_number=51)
  element("Te", "Tellur", (16, 5), melting_point=449.51, boiling_point=988, electronegativity=2.1, classification="Halbmetall", weight=127.6, atomic_number=52)
  element("I", "Iod", (17, 5), melting_point=113.7, boiling_point=184.3, electronegativity=2.66, classification="Halogen", weight=126.9, atomic_number=53)
  element("Xe", "Xenon", (18, 5), melting_point=-111.8, boiling_point=-108.1, electronegativity=2.6, classification="Edelgas", weight=131.29, atomic_number=54)
  element("Cs", "Caesium", (1, 6), melting_point=28.44, boiling_point=671, electronegativity=0.79, classification="Alkalimetall", weight=132.91, atomic_number=55)
  element("Ba", "Barium", (2, 6), melting_point=727, boiling_point=1897, electronegativity=0.89, classification="Erdalkalimetall", weight=137.33, atomic_number=56)
  element("La", "Lanthan", (3, 6), melting_point=920, boiling_point=3464, electronegativity=1.10, classification="Lanthanoid", weight=138.91, atomic_number=57)
  element("Hf", "Hafnium", (4, 6), melting_point=2233, boiling_point=4602, electronegativity=1.3, classification="Übergangsmetall", weight=178.49, atomic_number=72)
  element("Ta", "Tantal", (5, 6), melting_point=3017, boiling_point=5458, electronegativity=1.5, classification="Übergangsmetall", weight=180.95, atomic_number=73)
  element("W", "Wolfram", (6, 6), melting_point=3422, boiling_point=5555, electronegativity=2.36, classification="Übergangsmetall", weight=183.84, atomic_number=74)
  element("Re", "Rhenium", (7, 6), melting_point=3186, boiling_point=5630, electronegativity=1.9, classification="Übergangsmetall", weight=186.21, atomic_number=75)
  element("Os", "Osmium", (8, 6), melting_point=3033, boiling_point=5012, electronegativity=2.2, classification="Übergangsmetall", weight=190.23, atomic_number=76)
  element("Ir", "Iridium", (9, 6), melting_point=2446, boiling_point=4428, electronegativity=2.2, classification="Übergangsmetall", weight=192.22, atomic_number=77)
  element("Pt", "Platin", (10, 6), melting_point=1768.3, boiling_point=3825, electronegativity=2.28, classification="Übergangsmetall", weight=195.08, atomic_number=78)
  element("Au", "Gold", (11, 6), melting_point=1064.18, boiling_point=2856, electronegativity=2.54, classification="Übergangsmetall", weight=196.97, atomic_number=79)
  element("Hg", "Quecksilber", (12, 6), melting_point=-38.83, boiling_point=356.73, electronegativity=2.00, classification="Übergangsmetall", weight=200.59, atomic_number=80)
  element("Tl", "Thallium", (13, 6), melting_point=304, boiling_point=1473, electronegativity=1.62, classification="Metall", weight=204.38, atomic_number=81)
  element("Pb", "Blei", (14, 6), melting_point=327.46, boiling_point=1749, electronegativity=2.33, classification="Metall", weight=207.2, atomic_number=82)
  element("Bi", "Bismut", (15, 6), melting_point=271.3, boiling_point=1564, electronegativity=2.02, classification="Metall", weight=208.98, atomic_number=83)
  element("Po", "Polonium", (16, 6), melting_point=254, boiling_point=962, electronegativity=2.0, classification="Metall", weight=209, atomic_number=84)
  element("At", "Astat", (17, 6), melting_point=302, boiling_point=337, electronegativity=2.2, classification="Halogen", weight=210, atomic_number=85)
  element("Rn", "Radon", (18, 6), melting_point=-71, boiling_point=-61.7, electronegativity=2.2, classification="Edelgas", weight=222, atomic_number=86)
  element("Fr", "Francium", (1, 7), melting_point=27, boiling_point=677, electronegativity=0.7, classification="Alkalimetall", weight=223, atomic_number=87)
  element("Ra", "Radium", (2, 7), melting_point=700, boiling_point=1737, electronegativity=0.9, classification="Erdalkalimetall", weight=226, atomic_number=88)
  element("Ac", "Actinium", (3, 7), melting_point=1050, boiling_point=3200, electronegativity=1.1, classification="Actinoid", weight=227, atomic_number=89)
  element("Rf", "Rutherfordium", (4, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=267, atomic_number=104)
  element("Db", "Dubnium", (5, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=268, atomic_number=105)
  element("Sg", "Seaborgium", (6, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=271, atomic_number=106)
  element("Bh", "Bohrium", (7, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=270, atomic_number=107)
  element("Hs", "Hassium", (8, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=277, atomic_number=108)
  element("Mt", "Meitnerium", (9, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=278, atomic_number=109)
  element("Ds", "Darmstadtium", (10, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=281, atomic_number=110)
  element("Rg", "Roentgenium", (11, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=282, atomic_number=111)
  element("Cn", "Copernicium", (12, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Übergangsmetall", weight=285, atomic_number=112)
  element("Nh", "Nihonium", (13, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Metall", weight=286, atomic_number=113)
  element("Fl", "Flerovium", (14, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Metall", weight=289, atomic_number=114)
  element("Mc", "Moscovium", (15, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Metall", weight=290, atomic_number=115)
  element("Lv", "Livermorium", (16, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Metall", weight=293, atomic_number=116)
  element("Ts", "Tenness", (17, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Halogen", weight=294, atomic_number=117)
  element("Og", "Oganesson", (18, 7), melting_point=None, boiling_point=None, electronegativity=None, classification="Edelgas", weight=294, atomic_number=118)
