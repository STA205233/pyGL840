HSQuickLook.main.schema =
  [
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "contents": {
        "Time": { "type": "string" },
        "Temperature_1": { "type": "int" },
        "ch2": { "type": "int" },
        "ch3": { "type": "int", "conversion": conversion_MPT200AR },
        "ch4": { "type": "int" },
        "ch5": { "type": "int" },
        "ch6": { "type": "int" },
        "ch7": { "type": "int" },
        "ch8": { "type": "int" },
        "ch9": { "type": "int" },
        "ch10": { "type": "int" },
        "ch11": { "type": "int" },
        "ch12": { "type": "int" },
        "ch13": { "type": "int" },
        "ch14": { "type": "int" },
        "ch15": { "type": "int" },
        "ch16": { "type": "int" },
        "ch17": { "type": "int" },
        "ch18": { "type": "int" },
        "ch19": { "type": "int" },
        "ch20": { "type": "int" },
      }
    },
  ];


function conversion_MPT200AR(v) {
  return 10 ** (1.667 * v - 11.33)
}