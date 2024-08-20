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
        "Outer_Vacuum": { "source": "Ch1", "conversion": conversion_PKR251, "type": "float", "format": "%-5.2e Pa", "status": function (v) { return status_func("Ch1", v); } },
        "Pressure_inner_MPT200": { "source": "Ch2", "conversion": conversion_MPT200AR, "type": "float", "format": "%-5.2e Pa", "status": function (v) { return status_func("Ch2", v); } },
        "Inner_Pressure": { "source": "Ch3", "type": "float", "format": "%.3f Bar", "status": function (v) { return status_func("Ch3", v); } },
        "LAr_Level": { "source": "Ch4", "type": "float", "format": "%.2f cm", "status": function (v) { return status_func("Ch4", v); } },
        "Oxygen": { "source": "Ch5", "conversion": conversion_OX600, "type": "float", "format": "%-5.1f &#037;", "status": function (v) { return status_func("Ch5", v); } },

        // "Ch6": { "source": "Ch6","type": "string", "conversion": convert_string, "format": "%.3f V" },
        // "Ch7": { "source": "Ch7","type": "string", "conversion": convert_string, "format": "%.3f V" },
        // "Ch8": { "source": "Ch8", "type": "string", "conversion": convert_string, "format": "%.3f V" },
        // "Ch9": { "source": "Ch9","type": "string", "conversion": convert_string, "format": "%.3f V" },
        // "Ch10": { "source": "Ch10","type": "string", "conversion": convert_string, "format": "%.3f V" },
        // "Bottom_temp": { "source": "Ch11", "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func("Ch11",v); } },
        // "TPB_temp": { "source": "Ch12",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func("Ch12",v); }},
        // "z15cm_temp": { "source": "Ch13",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func("Ch13",v); }},
        // "z16_5cm_temp": { "source": "Ch14",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func("Ch14",v); }},
        // "upper_Baffle_Bottom_temp": { "source": "Ch15", "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func("Ch15",v); }},
        // "Temperature_16": { "source": "Ch16",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return "test"}},
        // "Temperature_17": { "source": "Ch17", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
        // "Temperature_18": { "source": "Ch18", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
        // "Temperature_19": { "source": "Ch19", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
        // "Temperature_20": { "source": "Ch20", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
      }
    },

    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "tableName": "Tempareture",
      "contents": {
        "CH17_duwer": { "source": "Ch17", "type": "float", "format": "%.3f &#8451;", "status": function (v) { return status_func_temp("Ch16", v); } },
        "CH18_Back": { "source": "Ch18", "type": "float", "format": "%.3f &#8451;", "status": function (v) { return status_func_temp("Ch16", v); } },
        "CH19_front": { "source": "Ch19", "type": "float", "format": "%.3f &#8451;", "status": function (v) { return status_func_temp("Ch16", v); } },
      },
    },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "tableName": "Trend_graph1",
      "contents": {
        "Temperature": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch17", "options": { "legend": "duwar", "color": "orange" } },
            { "source": "Ch18", "options": { "legend": "back", "color": "blue" } },
            { "source": "Ch19", "options": { "legend": "front", "color": "green" } }
          ],
        }
      }
    }
  ];



// function check_invalid_value(v) {
//   if (v == "BURNOUT" || v == "+++++++" || v == "Off" || v == "Disabled") {
//     return false
//   }
//   return true
// }

// function convert_string(v) {
//   if (check_invalid_value(v)) {
//     return Number(v)
//   }
//   return NaN
// }

// function show_status(v) {
//   if (check_invalid_value(v)) {
//     return "OK"
//   }
//   else {
//     return v
//   }
// }

// function status_color(v) {
//   if (v == "Off") {
//     return ""
//   }
//   if (check_invalid_value(v)) {
//     return "safe"
//   }
//   else {
//     return "error"
//   }
// }

function conversion_MPT200AR(v) {
  return 10 ** (1.667 * v - 9.333)
}

function conversion_PKR251(v) {
  return 10 ** (1.667 * v - 9.333)
}

function conversion_APR262(v) {
  return 20000 * (v - 1.0) / 0.8
}

function conversion_OX600(v) {
  R = 151.6
  I = 1000.0 * v / R
  return 25.0 * (I - 4.0) / (20.0 - 4.0)
}

function conversion_PKR251_log(v) {
  return 1.667 * v - 9.333
}
function conversion_MPT200AR_log(v) {
  return 1.667 * v - 9.333
}

var status_configuration = {
  "Ch1": { "safe_range": [0, 0.001], "warning_range": [0, 0.01] },
  "Ch2": { "safe_range": [0, 1e+6], "warning_range": [1, 50] },
  "Ch3": { "safe_range": [0, 1.3], "warning_range": [0, 2.0] },
  "Ch4": { "safe_range": [-1, 20], "warning_range": [-1, 25] },
  "Ch5": { "safe_range": [20.6, 22], "warning_range": [20.3, 20.6] },
  "Ch7": { "warning_range": [-1e6, -0.05] },
  "Ch11": { "LAr_temp": [-189, -183] },
  "Ch12": { "LAr_temp": [-189, -183] },
  "Ch13": { "LAr_temp": [-189, -183] },
  "Ch14": { "LAr_temp": [-189, -183] },
  "Ch15": { "LAr_temp": [-189, -183] },
  "Ch16": { "LAr_temp": [-189, -183] },
  "Ch20": { "safe_range": [-1e+6, 50], "warning_range": [25, 50] },
  "tempareture_warning": { "safe_range": [5, 50], "warning_range": [0, 5] },
}

function status_func(name, v) {
  if ((status_configuration[name]["safe_range"][0] <= v) && (status_configuration[name]["safe_range"][1] >= v)) {
    return "safe"
  }
  else if ((status_configuration[name]["warning_range"][0] <= v) && (status_configuration[name]["warning_range"][1] >= v)) {
    return "warning"
  }
  else {
    return "error"
  }
}

function status_func_temp(name, v) {
  if ((status_configuration[name]["LAr_temp"][0] <= v) && (status_configuration[name]["LAr_temp"][1] >= v)) {
    return "temp"
  }
}