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
        "Temperature_1": {
          "source": "Temperature_1", "conversion": convert_string, "type": "string", "format": "%-5.3e &#8451;"
},
        "Ch2": { "type": "string", "conversion": convert_string, "format": "%.3f &#8451;" },
        "Ch3": { "type": "string", "conversion": conversion_MPT200AR, "format": "%.3f hPa" },
        "Ch4": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch5": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch6": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch7": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch8": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch9": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch10": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch11": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch12": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch13": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch14": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch15": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch16": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch17": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch18": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch19": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
        "Ch20": { "type": "string", "conversion": convert_string, "format": "%.3f V" },
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
        "Temperature_1": { "source": "Temperature_1", "conversion": show_status, "type": "string", "status": status_color },
        "Temperature_2": { "source": "Ch2", "type": "string", "conversion": show_status, "status": status_color },
        "Ch3": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch4": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch5": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch6": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch7": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch8": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch9": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch10": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch11": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch12": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch13": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch14": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch15": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch16": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch17": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch18": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch19": { "type": "string", "conversion": show_status, "status": status_color },
        "Ch20": { "type": "string", "conversion": show_status, "status": status_color },
      }
    },
  ];

function check_invalid_value(v) {
  if (v == "BURNOUT" || v == "+++++++" || v == "Off" || v == "Disabled") {
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

function status_color(v) {
  if (v == "Off") {
    return ""
  }
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
  return NaN
}