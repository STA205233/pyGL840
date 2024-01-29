
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
        "Outer_Vacuum":       { "source": "Ch1", "conversion": conversion_PKR251, "type": "float", "format": "%-5.2e Pa", "status": function (v) {return status_func("Ch1",v); }},
        // "Pressure_inner_MPT200": { "source": "Ch2", "conversion": conversion_MPT200AR, "type": "float", "format": "%-5.2e Pa", "status": function (v) {return status_func("Ch2",v); }},
        "Inner_Pressure": { "source": "Ch3",  "type": "float", "format": "%.3f Bar", "status": function (v) {return status_func("Ch3",v); }},
        "LAr_Level":         { "source": "Ch4",  "type": "float", "format": "%.2f cm", "status": function (v) {return status_func("Ch4",v); }},
        "Oxygen":                 { "source": "Ch5", "conversion": conversion_OX600, "type": "float", "format": "%-5.1f &#037;", "status": function (v) {return status_func("Ch5",v); }},
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
        "RoomTemperature": { "source": "Ch16", "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch16",v); } },
        "Baffle": { "source": "Ch15", "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch15",v); }},
        "z16_5cm": { "source": "Ch14",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch14",v); }},
        "z15_0cm": { "source": "Ch13",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch13",v); }},
        "MPPC_window": { "source": "Ch12",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch12",v); }},
        "Bottom": { "source": "Ch11", "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch11",v); } },
        // "MPPC_window": { "source": "Ch12",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch12",v); }},
        // "z15cm": { "source": "Ch13",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch13",v); }},
        // "z16_5cm": { "source": "Ch14",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch14",v); }},
        // "upper_Baffle_Bottom": { "source": "Ch15", "type": "float", "format": "%.3f &#8451;", "status": function (v) {return status_func_temp("Ch15",v); }},
        // // "Temperature_16": { "source": "Ch16",  "type": "float", "format": "%.3f &#8451;", "status": function (v) {return "test"}},
        // // "Temperature_17": { "source": "Ch17", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
        // "Temperature_18": { "source": "Ch18", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
        // "Temperature_19": { "source": "Ch19", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
        // "Temperature_20": { "source": "Ch20", "conversion": convert_string, "type": "string", "format": "%.3f &#8451;"},
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
        "Oxygen": { "type": "trend-graph",
        "group": [
            {"source": "Ch5","conversion":conversion_OX600,"options":{"legend": "Oxygen","color": "red" }}
        ],
        "options":{"xWidth": 10000,"yRange":[0.0, 30],
        },
        },
          "Temperature": { "type": "trend-graph",
              "group": [
                  {"source": "Ch11", "options":{"legend": "Bottom","color": "red"}},
                  {"source": "Ch12", "options":{"legend": "TPB","color": "blue"}},
                  {"source": "Ch13", "options":{"legend": "+15cm","color": "green"}},
                  {"source": "Ch14", "options":{"legend": "+16.5cm","color": "brown"}},
                  {"source": "Ch15", "options":{"legend": "Baffle_Bottom","color": "black"}},
                  {"source": "Ch16", "options":{"legend": "RoomTemperature","color": "cyan"}},
              ],
        "options":{"xWidth": 10000,"yRange":[-200, 30]}
        },
          "LAr_Level": { "type": "trend-graph",
          "group": [
              {"source": "Ch4","options":{"legend": "level","color": "red"}},
            ],
        "options":{"xWidth": 10000,"yRange":[-1, 70]}
        },
        }    
    },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 60,
      "tableName": "Presssure_log",
      "section": "GL840",
      "contents": {
          "Outer_log": { "type": "trend-graph",
              "group": [
                  {"source": "Ch1","conversion":conversion_PKR251_log, "options":{"legend": "Outer_PKR","color": "red"}},
              ],
              "options":{"xWidth": 10000,"yRange":[-4, 5]}
          },
          // "Inner_log": { "type": "trend-graph",
          //     "group": [
          //         {"source": "Ch2", "conversion":conversion_MPT200AR_log, "options":{"legend": "Inner_MPT","color": "blue"}},
          //     ],
          //     "options":{"xWidth": 1000,"yRange":[-4, 5]}
          // },
      }
        
    },
    {
      "collection": "GL840",
      "directory": "GL840",
      "document": "GL840",
      "period": 60,
      "tableName": "Presssure_linear",
      "section": "GL840",
      "contents": {
          "Outer_Pa": { "type": "trend-graph",
              "group": [
                  {"source": "Ch1","conversion":conversion_PKR251, "options":{"legend": "Outer_PKR","color": "red"}},
              ],
              "options":{"xWidth": 10000,"yRange":[0, 0.05]}
          },
          // "Inner": { "type": "trend-graph",
          //     "group": [
          //         {"source": "Ch2", "conversion":conversion_MPT200AR, "options":{"legend": "Inner_MPT","color": "blue"}},
          //     ],
          //     "options":{"xWidth": 1000,"yRange":[0, 10.0]}
          // },
          "Inner_Bar": { "type": "trend-graph",
              "group": [
                  {"source": "Ch3", "options":{"legend": "Inner_APR","color": "green"}},
              ],
              "options":{"xWidth": 10000,"yRange":[0.5, 3.0]}
          }
      }
        
    },
    
  ];


  function conversion_MPT200AR(v) {
    return 10 ** (1.667 * v - 9.333)
}

function conversion_PKR251(v) {
    return 10 ** (1.667 * v - 9.333)
}

function conversion_APR262(v) {
     return 20000*(v-1.0)/0.8
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
    return  1.667 * v - 9.333
}

var status_configuration = {
  "Ch1": {"safe_range": [0,0.1 ], "warning_range": [0, 1.0]},
  "Ch2": {"safe_range": [0, 1e+6], "warning_range": [1, 50]},
  "Ch3": {"safe_range": [0, 1.4], "warning_range": [0, 2.0]},
  "Ch4": {"safe_range": [-1, 20], "warning_range": [-1,25]},
  "Ch5": {"safe_range": [20.7,22], "warning_range": [20.6, 22]},
  "Ch11": {"LAr_temp": [-189, -185]}, 
  "Ch12": {"LAr_temp": [-189, -185]},
  "Ch13": {"LAr_temp": [-189, -185]},
  "Ch14": {"LAr_temp": [-189, -185]},
  "Ch15": {"LAr_temp": [-189, -185]},
  "Ch16": {"LAr_temp": [10, 25]},
}

function status_func(name,v) {
  if ((status_configuration[name]["safe_range"][0] <=v)&&(status_configuration[name]["safe_range"][1] >=v)){
    return "safe"
  }
  else if ((status_configuration[name]["warning_range"][0] <=v)&&(status_configuration[name]["warning_range"][1] >=v)){
    return "warning"
  }
  else {
    return "error"
  }
}

function status_func_temp(name,v){
  if ((status_configuration[name]["LAr_temp"][0] <=v)&&(status_configuration[name]["LAr_temp"][1] >=v)){
    return "temp"
  }
}