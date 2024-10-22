def ImportToKernel(k):
  translations = k.get("translations")

  data={
      "Yes":"Ja",
      "No":"Nein",
      "Utilities":"Zubehör",
      "Time":"Zeit"
      }

  translations.getLanguage("de").sets.append(data)
