var Bottom_tempareture = 0.0;
var SiPM_tempareture = 0.0;
var Above_tempareture = 0.0;
var Below_tempareture = 0.0;
var TPC_tempareture = 0.0;
var Top_tempareture = 0.0;
var dewpoint = 0.0;


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
        "Inner_Pressure": { "source": "Ch3", "type": "float", "format": "%.3f Bar", "status": function (v) { return status_func("Ch3", v); } },
        "LAr_Level": { "source": "Ch4", "type": "float", "format": "%.2f cm", "status": function (v) { return status_func("Ch4", v); } },
        "Oxygen": { "source": "Ch5", "conversion": conversion_OX600, "type": "float", "format": "%-5.1f &#037;", "status": function (v) { return status_func("Ch5", v); } },
        "Room_Tempareture": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", },
        "Humidity": { "source": "Ch22", "type": "float", "format": "%.3f ％" },
        "Dew_Point": { "source": "Ch23", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { dewpoint = v; return v; } },
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
        "Top_Baffle": { "source": "Ch16", "type": "float", "format": "%.3f &#8451;", "status": function (v) { Top_tempareture = v; return status_func_temp("Ch16", v); } },
        "TPC_Baffle": { "source": "Ch15", "type": "float", "format": "%.3f &#8451;", "status": function (v) { TPC_tempareture = v; return status_func_temp("Ch15", v); } },
        "Above_Anode": { "source": "Ch14", "type": "float", "format": "%.3f &#8451;", "status": function (v) { Above_tempareture = v; return status_func_temp("Ch14", v); } },
        "Below_Anode": { "source": "Ch13", "type": "float", "format": "%.3f &#8451;", "status": function (v) { Below_tempareture = v; return status_func_temp("Ch13", v); } },
        "SiPM": { "source": "Ch12", "type": "float", "format": "%.3f &#8451;", "status": function (v) { SiPM_tempareture = v; return status_func_temp("Ch12", v); } },
        "Bottom_Heater": { "source": "Ch11", "type": "float", "format": "%.3f &#8451;", "status": function (v) { Bottom_tempareture = v; return status_func_temp("Ch11", v); } },
      }
    },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 1,
      "section": "GL840",
      "tableName": "Tempareture-DewPoint",
      "contents": {
        "TopBaffleT-DewPoint": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { return Top_tempareture - dewpoint; }, "status": function (v) { return status_func("tempareture_warning", Top_tempareture - dewpoint) } },
        "TPCBaffleT-DewPoint": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { return TPC_tempareture - dewpoint; }, "status": function (v) { return status_func("tempareture_warning", TPC_tempareture - dewpoint) } },
        "AboveAnodeT-DewPoint": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { return Above_tempareture - dewpoint; }, "status": function (v) { return status_func("tempareture_warning", Above_tempareture - dewpoint) } },
        "BelowAnodeT-DewPoint": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { return Below_tempareture - dewpoint; }, "status": function (v) { return status_func("tempareture_warning", Below_tempareture - dewpoint) } },
        "SiPMT-DewPoint": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { return SiPM_tempareture - dewpoint; }, "status": function (v) { return status_func("tempareture_warning", SiPM_tempareture - dewpoint) } },
        "BottomT-DewPoint": { "source": "Ch21", "type": "float", "format": "%.3f &#8451", "conversion": function (v) { return Bottom_tempareture - dewpoint; }, "status": function (v) { return status_func("tempareture_warning", Bottom_tempareture - dewpoint) } }
      }
    },

    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 60,
      "tableName": "Trend_graph",
      "section": "GL840",
      "contents": {
        "Oxygen": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch5", "conversion": conversion_OX600, "options": { "legend": "O2", "color": "red" } }
          ],
          "options": {
            "xWidth": 1000, "yRange": [0.0, 30], "frame": { "height": 270, "width": 480 }
          },
        },
        "Temperature": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch21", "options": { "legend": "room", "color": "orange" } },
            { "source": "Ch16", "options": { "legend": "Baffle", "color": "cyan" } },
            { "source": "Ch15", "options": { "legend": "TPCTop", "color": "black" } },
            { "source": "Ch14", "options": { "legend": "FEC", "color": "brown" } },
            { "source": "Ch13", "options": { "legend": "Anode", "color": "green" } },
            { "source": "Ch12", "options": { "legend": "SiPM", "color": "blue" } },
            { "source": "Ch11", "options": { "legend": "Bottom", "color": "red" } },
          ],
          "options": { "xWidth": 1000, "yRange": [-200, 30], "frame": { "height": 270, "width": 480 } }
        },
        "Temperature_refill": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch14", "options": { "legend": "FEC", "color": "brown" } },
            { "source": "Ch13", "options": { "legend": "Anode", "color": "green" } },
            { "source": "Ch12", "options": { "legend": "SiPM", "color": "blue" } },
            { "source": "Ch11", "options": { "legend": "Bottom", "color": "red" } },
          ],
          "options": { "xWidth": 100, "yRange": [-195, -160], "frame": { "height": 270, "width": 480 } }
        },
        "LAr_Level": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch4", "options": { "legend": "level", "color": "red" } },
          ],
          "options": { "xWidth": 1000, "yRange": [-1, 70], "frame": { "height": 270, "width": 480 } }
        },
      }
    },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 60,
      "tableName": "Presssure",
      "section": "GL840",
      "contents": {
        "Outer_Vacuum": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch1", "conversion": conversion_PKR251, "options": { "legend": "Outer", "color": "red" } },
          ],
          "options": { "xWidth": 1000, "yRange": [0, 0.05], "frame": { "height": 270, "width": 480 } }
        },
        "Inner_Vacuum": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch2", "conversion": conversion_MPT200AR, "options": { "legend": "Inner", "color": "blue" } },
          ],
          "options": { "xWidth": 1000, "yRange": [0, 10.0], "frame": { "height": 270, "width": 480 } }
        },
        "Inner_Pressure": {
          "type": "trend-graph",
          "group": [
            { "source": "Ch3", "options": { "legend": "Inner_APR", "color": "green" } },
          ],
          "options": { "xWidth": 1000, "yRange": [0.5, 3.0], "frame": { "height": 270, "width": 480 } }
        }
      }
    },
  ];




function conversion_MPT200AR(v) {
  return 10 ** (1.667 * v - 9.333);
}

function conversion_PKR251(v) {
  return 10 ** (1.667 * v - 9.333);
}

function conversion_APR262(v) {
  return 20000 * (v - 1.0) / 0.8;
}

function conversion_OX600(v) {
  R = 151.6;
  I = 1000.0 * v / R;
  return 25.0 * (I - 4.0) / (20.0 - 4.0);
}

function conversion_PKR251_log(v) {
  return 1.667 * v - 9.333;
}
function conversion_MPT200AR_log(v) {
  return 1.667 * v - 9.333;
}

var status_configuration = {
  "Ch1": { "safe_range": [0, 0.001], "warning_range": [0, 0.01] },
  "Ch2": { "safe_range": [0, 1e+6], "warning_range": [1, 50] },
  "Ch3": { "safe_range": [0, 1.3], "warning_range": [0, 2.0] },
  "Ch4": { "safe_range": [-1, 20], "warning_range": [-1, 25] },
  "Ch5": { "safe_range": [20.6, 22], "warning_range": [20.3, 20.6] },
  "Ch11": { "LAr_temp": [-189, -185] },
  "Ch12": { "LAr_temp": [-189, -185] },
  "Ch13": { "LAr_temp": [-189, -185] },
  "Ch14": { "LAr_temp": [-189, -185] },
  "Ch15": { "LAr_temp": [-189, -185] },
  "Ch16": { "LAr_temp": [-189, -185] },
  "tempareture_warning": { "safe_range": [5, 50], "warning_range": [0, 5] }
};

function status_func(name, v) {
  if ((status_configuration[name]["safe_range"][0] <= v) && (status_configuration[name]["safe_range"][1] >= v)) {
    return "safe";
  }
  else if ((status_configuration[name]["warning_range"][0] <= v) && (status_configuration[name]["warning_range"][1] >= v)) {
    return "warning";
  }
  else {
    return "error";
  }
}

function status_func_temp(name, v) {
  if ((status_configuration[name]["LAr_temp"][0] <= v) && (status_configuration[name]["LAr_temp"][1] >= v)) {
    return "temp";
  }
}
