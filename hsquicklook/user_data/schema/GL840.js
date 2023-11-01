HSQuickLook.main.schema =
  [
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "tableName": "GL840",
      "contents": {
        "Temperature_1": { "source": "Temperature_1", "conversion": convert_string, "type": "string" },
        "Ch2": { "type": "string", "conversion": convert_string, "format": "%.6f &#8451;" },
        "Ch3": { "type": "string", "conversion": conversion_MPT200AR, "format": "%.3f Pa" },
        "Ch4": { "type": "string", "conversion": convert_string },
        "Ch5": { "type": "string", "conversion": convert_string },
        "Ch6": { "type": "string", "conversion": convert_string },
        "Ch7": { "type": "string", "conversion": convert_string },
        "Ch8": { "type": "string", "conversion": convert_string },
        "Ch9": { "type": "string", "conversion": convert_string },
        "Ch10": { "type": "string", "conversion": convert_string },
        "Ch11": { "type": "string", "conversion": convert_string },
        "Ch12": { "type": "string", "conversion": convert_string },
        "Ch13": { "type": "string", "conversion": convert_string },
        "Ch14": { "type": "string", "conversion": convert_string },
        "Ch15": { "type": "string", "conversion": convert_string },
        "Ch16": { "type": "string", "conversion": convert_string },
        "Ch17": { "type": "string", "conversion": convert_string },
        "Ch18": { "type": "string", "conversion": convert_string },
        "Ch19": { "type": "string", "conversion": convert_string },
        "Ch20": { "type": "string", "conversion": convert_string },
      }
    },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "tableName": "GL840Status",
      "contents": {
        "Temperature_1": { "source": "Temperature_1", "conversion": show_status, "type": "string", "status": status_func },
        "Temperature_2": { "source": "Ch2", "type": "string", "conversion": show_status, "status": status_func },
        "Ch3": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch4": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch5": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch6": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch7": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch8": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch9": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch10": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch11": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch12": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch13": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch14": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch15": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch16": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch17": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch18": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch19": { "type": "string", "conversion": show_status, "status": status_func },
        "Ch20": { "type": "string", "conversion": show_status, "status": status_func },
      }
    },
  ];

function check_invalid_value(v) {
  if (v == "BURNOUT" || v == "+++++++") {
    return false
  }
  return true
}

function convert_string(v) {
  if (check_invalid_value(v)) {
    return Number(v)
  }
  return NaN
}

function show_status(v) {
  if (check_invalid_value(v)) {
    return "OK"
  }
  else {
    return v
  }
}

function status_func(v) {
  if (check_invalid_value(v)) {
    return "safe"
  }
  else {
    return "error"
  }
}

function conversion_MPT200AR(v) {
  if (check_invalid_value(v)) {
    value = Number(v)
    return 10 ** (1.667 * value - 11.33)
  }
  return v
}