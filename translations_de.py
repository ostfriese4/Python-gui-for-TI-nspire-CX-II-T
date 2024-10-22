def ImportToKernel(k):
  translations = k.get("translations")

  data={
      "Yes":"Ja",
      "No":"Nein",
      "Utilities":"Zubehör",
      "Time":"Zeit",
      "Education":"Bildung"
      }

  translations.getLanguage("de").sets.append(data)
