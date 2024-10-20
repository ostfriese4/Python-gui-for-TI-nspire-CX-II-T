descriptions={}

descriptions["∑"]="n-stellige Summe"
descriptions["·"]="Mittelpunkt; Multiplikationszeichen"
descriptions["?"]="Fragezeichen"
descriptions["!"]="Ausrufezeichen"
descriptions["☺"]="weißer Smiley"
descriptions["ß"]="scharfes s; sz"
descriptions[";"]="Semikolon"
descriptions[":"]="Doppelpunkt"
descriptions["#"]="Hashtag; Nummernzeichen"
descriptions["_"]="Unterstrich"
descriptions[" "]="Leerzeichen"
descriptions["\\"]="Umgekehrter Schrägstrich; Backslash"
descriptions["%"]="Prozentzeichen"
descriptions["π"]="Kleines griechisches pi"
descriptions["©"]="Copyright-Zeichen"
descriptions[" "]="Schmales Leerzeichen"
descriptions[" "]="Geschütztes Leerzeichen"
descriptions["—"]="Gevierstrich"
descriptions["¨"]="Trema"
descriptions["§"]="Paragraph-Zeichen"
descriptions["¶"]="Absatzendemarke"
descriptions["–"]="Halbgevierstrich"
descriptions["­"]="bedingter Trennstrich"
descriptions["®"]="Registrierte Marke"
descriptions["™"]="Markenzeichen"
descriptions["←"]="Pfeil nach links"
descriptions["↑"]="Pfeil nach oben"
descriptions["→"]="Pfeil nach rechts; sto Operator"
descriptions["↓"]="Pfeil nach unten"
descriptions["↔"]="Pfeil nach links-rechts"
descriptions["↕"]="Pfeil nach unten-oben"
descriptions["↦"]="Pfeil nach rechts von Leiste"
descriptions["↵"]="Pfeil nach unten-links"
descriptions["⇐"]="Doppelpfeil nach links"
descriptions["⇒"]="Doppelpfeil nach rechts"
descriptions["⇔"]="Doppelpfeil links-rechts"
descriptions["⇥"]="Pfeil nach rechts zu Leiste"
descriptions["⇧"]="Weißer Pfeil nach oben"
descriptions[""]="TI-Schritt"
descriptions["★"]="Schwarzer Stern"
descriptions["✓"]="Häckchen"
descriptions["∴"]="folglich"
descriptions["∵"]="weil"
descriptions["≃"]="Asymptotisch gleich"
descriptions["≅"]="kongruent"
descriptions["≈"]="Fast gleich"
descriptions["≟"]="Vielleicht gleich"
descriptions["≡"]="Identisch"
descriptions["≢"]="Nicht Identisch"
descriptions["⊂"]="Teilmenge"
descriptions["⊆"]="Teilmenge oder gleich"
descriptions["∝"]="Proportional zu"
descriptions["∓"]="Minus-/Pluszeichen"
descriptions["∣"]="Teilt"
descriptions["∤"]="Teilt nicht"
descriptions["∥"]="Parallel"
descriptions["∦"]="Nicht parallel"
descriptions["∎"]="Ende des Beweises"
descriptions["¯"]="Überstrich"
descriptions["Þ"]="Großes lateinisches Thorn"
descriptions["þ"]="Kleines lateinisches Thorn"
descriptions["※"]="Verweismarke; Vierpunktkreuz"
descriptions["℉"]="Grad Fahrenheit"
descriptions["℃"]="Grad Celsius"
descriptions["‰"]="Promille"
descriptions["⑪"]="Eingekreiste Zahl elf (11)"
descriptions["⑫"]="Eingekreiste Zahl zwölf (12)"
descriptions["⑬"]="Eingekreiste Zahl dreizehn (13)"
descriptions["⑭"]="Eingekreiste Zahl vierzehn (14)"
descriptions["⑮"]="Eingekreiste Zahl fünfzehn (15)"
descriptions["⑯"]="Eingekreiste Zahl sechzehn (16)"
descriptions["("]="Klammer auf"
descriptions[")"]="Klammer zu"
descriptions["["]="Eckige Klammer auf"
descriptions["]"]="Eckige Klammer zu"
descriptions["{"]="Geschweifte Klammer auf"
descriptions["}"]="Geschweifte Klammer zu"
descriptions[""]="Katalog"
for i in "abcdefghijklmnopqrstuvwxyz":
  descriptions[i]="Kleines lateinisches "+i
  descriptions[i.upper()]="Großes lateinisches "+i.upper()
for i in "0123456789":
  descriptions[i]="Ziffer "+i
j=0
for i in "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ":
  k=["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
  descriptions[i]="Großes griechisches "+k[j]
  j+=1
j=0
for i in "αβγδεζηθικλμνξοπρστυφχψω":
  k=["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
  descriptions[i]="Kleines griechisches "+k[j]
  j+=1
del i
del j
del k

string="[]{}()<≤≠=≥>?!&$°'^*/+-%:;,._\\#πE∞θ→▶∠-·×÷±√∏∑∫©@|Σμσχ²₁₂₃ŷ∆µΩΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρστυφχψω←↑→↓↔↕↦↵⇐⇒⇔⇥⇧⊿▪▫▲△▴▶▸▼▾◀◂◆☺★✓⫽$¢£€¥¤∀∃∄∅∆∇∈∉∊∋∌∍∎∂∓∘∙∝∟∠∡∣∤∥∦∧∨∩∪∴∵≃≅≈≟≡≢⊂⊆⊙⊥¼½¾¿¬ℂℕℙℚℝℤℎ0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſǺǻǼǽǾǿ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁽⁾ªⁱⁿº₀₁₂₃₄₅₆₇₈₉₊₋₍₎•‣…~ ¡¦§¨`­®™¯´¶¸«»‹› –—‘’“”‚„ǍǎǐǒǔǖǘǚǜǸǹɐɑɔəɛɡɪɵʃʊʌʒˈˌː‰※℃℉−∷∼∽≌⑪⑫⑬⑭⑮⑯ⓐⓑⓒⓓⓔ■●"
list=list(string)
