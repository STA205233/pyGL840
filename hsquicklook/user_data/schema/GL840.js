HSQuickLook.main.schema =
  [
    // {
    //   "collection": "GL840",
    //   "directory": "GL840",
    //   "document": "GL840",
    //   "period": 1,
    //   "section": "GL840",
    //   "contents": {
    //     "Time": { "type": "string" },
    //     "Temperature_1": { "type": "int" },
    //     "Ch2": { "type": "int" },
    //     "Ch3": { "type": "int", "conversion": conversion_MPT200AR },
    //     "Ch4": { "type": "int" },
    //     "Ch5": { "type": "int" },
    //     "Ch6": { "type": "int" },
    //     "Ch7": { "type": "int" },
    //     "Ch8": { "type": "int" },
    //     "Ch9": { "type": "int" },
    //     "Ch10": { "type": "int" },
    //     "Ch11": { "type": "int" },
    //     "Ch12": { "type": "int" },
    //     "Ch13": { "type": "int" },
    //     "Ch14": { "type": "int" },
    //     "Ch15": { "type": "int" },
    //     "Ch16": { "type": "int" },
    //     "Ch17": { "type": "int" },
    //     "Ch18": { "type": "int" },
    //     "Ch19": { "type": "int" },
    //     "Ch20": { "type": "int" },
    //   },
    // },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "tableName": "GL840",
      "contents": {
        "Temperature_1": { "source": "Temperature_1", "type": "string" },
        "Ch2": { "type": "string" },
        "Ch3": { "type": "string", "conversion": conversion_MPT200AR },
        "Ch4": { "type": "string" },
        "Ch5": { "type": "string" },
        "Ch6": { "type": "string" },
        "Ch7": { "type": "string" },
        "Ch8": { "type": "string" },
        "Ch9": { "type": "string" },
        "Ch10": { "type": "string" },
        "Ch11": { "type": "string" },
        "Ch12": { "type": "string" },
        "Ch13": { "type": "string" },
        "Ch14": { "type": "string" },
        "Ch15": { "type": "string" },
        "Ch16": { "type": "string" },
        "Ch17": { "type": "string" },
        "Ch18": { "type": "string" },
        "Ch19": { "type": "string" },
        "Ch20": { "type": "string" },
      }
    },
  ];

function check_invalid_value(v) {
  if (v == "BURNOUT" || v == "******") {
    return false
  }
  return true
}

function conversion_MPT200AR(v) {
  if (check_invalid_value(v)) {
    value = Number(v)
    return 10 ** (1.667 * value - 11.33)
  }
  return v
}