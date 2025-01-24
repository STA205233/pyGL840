HSQuickLook.main.schema =
  [
    // {
    //   "collection": "event",
    //   "directory": "event",
    //   "document": "event",
    //   "period": 1,
    //   "section": "count_rate",
    //   "tableName": "Countrate",
    //   "contents": {
    //     "FEC0_Count_circle_like_noise": { "source": "Count_circle_like_noise_0", "type": "int" },
    //     "FEC0_Rate_circle_like_noise": { "source": "Rate_circle_like_noise_0", "type": "float", "format": "%.2f Hz" },
    //     "FEC0_Count_rnd_like_noise": { "source": "Count_rnd_like_noise_0", "type": "int" },
    //     "FEC0_Rate_rnd_like_noise": { "source": "Rate_rnd_like_noise_0", "type": "float", "format": "%.2f Hz" },
    //     "FEC0_Count_gamma_ray": { "source": "Count_gamma_ray_0", "type": "int" },
    //     "FEC0_Rate_gamma_ray": { "source": "Rate_gamma_ray_0", "type": "float", "format": "%.2f Hz" },
    //     "FEC1_Count_circle_like_noise": { "source": "Count_circle_like_noise_1", "type": "int" },
    //     "FEC1_Rate_circle_like_noise": { "source": "Rate_circle_like_noise_1", "type": "float", "format": "%.2f Hz" },
    //     "FEC1_Count_rnd_like_noise": { "source": "Count_rnd_like_noise_1", "type": "int" },
    //     "FEC1_Rate_rnd_like_noise": { "source": "Rate_rnd_like_noise_1", "type": "float", "format": "%.2f Hz" },
    //     "FEC1_Count_gamma_ray": { "source": "Count_gamma_ray_1", "type": "int" },
    //     "FEC1_Rate_gamma_ray": { "source": "Rate_gamma_ray_1", "type": "float", "format": "%.2f Hz" },
    //     "FEC2_Count_circle_like_noise": { "source": "Count_circle_like_noise_2", "type": "int" },
    //     "FEC2_Rate_circle_like_noise": { "source": "Rate_circle_like_noise_2", "type": "float", "format": "%.2f Hz" },
    //     "FEC2_Count_rnd_like_noise": { "source": "Count_rnd_like_noise_2", "type": "int" },
    //     "FEC2_Rate_rnd_like_noise": { "source": "Rate_rnd_like_noise_2", "type": "float", "format": "%.2f Hz" },
    //     "FEC2_Count_gamma_ray": { "source": "Count_gamma_ray_2", "type": "int" },
    //     "FEC2_Rate_gamma_ray": { "source": "Rate_gamma_ray_2", "type": "float", "format": "%.2f Hz" },
    //     "Total_gamma_count": { "source": "Total_gamma_count", "type": "int" },
    //   }
    // },

    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "FEC0_Count",
      "contents": {
        "Count_circle_noise_0": { "source": "Count_circle_like_noise_0", "type": "int" },
        "Count_rnd_noise_0": { "source": "Count_rnd_like_noise_0", "type": "int" },
        "Count_gamma_0": { "source": "Count_gamma_ray_0", "type": "int" },
      }
    },
    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "FEC0_Rate",
      "contents": {
        "Rate_circle_noise_0": { "source": "Rate_circle_like_noise_0", "type": "float", "format": "%.2f Hz" },
        "Rate_rnd_noise_0": { "source": "Rate_rnd_like_noise_0", "type": "float", "format": "%.2f Hz" },
        "Rate_gamma_0": { "source": "Rate_gamma_ray_0", "type": "float", "format": "%.2f Hz" }
      }
    },
    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "FEC1_Count",
      "contents": {
        "Rate_circle_noise_1": { "source": "Count_circle_like_noise_1", "type": "int" },
        "Rate_rnd_noise_1": { "source": "Count_rnd_like_noise_1", "type": "int" },
        "Rate_gamma_1": { "source": "Count_gamma_ray_1", "type": "int" },
      }
    },
    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "FEC1_Rate",
      "contents": {
        "Rate_circle_noise_1": { "source": "Rate_circle_like_noise_1", "type": "float", "format": "%.2f Hz" },
        "Rate_rnd_noise_1": { "source": "Rate_rnd_like_noise_1", "type": "float", "format": "%.2f Hz" },
        "Rate_gamma_1": { "source": "Rate_gamma_ray_1", "type": "float", "format": "%.2f Hz" }
      }
    },
    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "FEC2_Count",
      "contents": {
        "Count_circle_noise_2": { "source": "Count_circle_like_noise_2", "type": "int" },
        "Count_rnd_noise_2": { "source": "Count_rnd_like_noise_2", "type": "int" },
        "Count_gamma_2": { "source": "Count_gamma_ray_2", "type": "int" },
      }
    },
    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "FEC2_Rate",
      "contents": {
        "Rate_circle_noise": { "source": "Rate_circle_like_noise_2", "type": "float", "format": "%.2f Hz" },
        "Rate_rnd_noise": { "source": "Rate_rnd_like_noise_2", "type": "float", "format": "%.2f Hz" },
        "Rate_gamma": { "source": "Rate_gamma_ray_2", "type": "float", "format": "%.2f Hz" }
      }
    },

    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "CountRateGraph",
      "contents": {
        "FEC0": {
          "type": "trend-graph",
          "group": [
            { "source": "Rate_circle_like_noise_0", "options": { "legend": "Circle", "color": "cyan" } },
            { "source": "Rate_rnd_like_noise_0", "options": { "legend": "Random", "color": "green" } },
            { "source": "Rate_gamma_ray_0", "options": { "legend": "Gammaray", "color": "red" } },
            // {"source": ""}
          ],
          "options": {
            "xWidth": 1000,
            "frame": {
              "width": 480,
              "height": 270
            }
          },
        },
        "FEC1": {
          "type": "trend-graph",
          "group": [
            { "source": "Rate_circle_like_noise_1", "options": { "legend": "Circle", "color": "cyan" } },
            { "source": "Rate_rnd_like_noise_1", "options": { "legend": "Random", "color": "green" } },
            { "source": "Rate_gamma_ray_1", "options": { "legend": "Gammaray", "color": "red" } },
            // {"source": ""}
          ],
          "options": {
            "xWidth": 1000,
            "frame": {
              "width": 480,
              "height": 270
            }
          },
        },
        "FEC2": {
          "type": "trend-graph",
          "group": [
            { "source": "Rate_circle_like_noise_2", "options": { "legend": "Circle", "color": "cyan" } },
            { "source": "Rate_rnd_like_noise_2", "options": { "legend": "Random", "color": "green" } },
            { "source": "Rate_gamma_ray_2", "options": { "legend": "Gammaray", "color": "red" } },
            // {"source": ""}
          ],
          "options": {
            "xWidth": 1000,
            "frame": {
              "width": 480,
              "height": 270
            }
          },
        },
      }
    },

    // {
    //   "collection": "event",
    //   "directory": "event",
    //   "document": "event",
    //   "period": 1,
    //   "section": "count_rate",
    //   "tableName": "CountRateGraph_FEC0",
    //   "contents": {
    //     "Rate": {
    //       "type": "trend-graph",
    //       "group": [
    //         { "source": "Rate_circle_like_noise_0", "options": { "legend": "Circle", "color": "cyan" } },
    //         { "source": "Rate_rnd_like_noise_0", "options": { "legend": "Random", "color": "green" } },
    //         { "source": "Rate_gamma_ray_0", "options": { "legend": "Gammaray", "color": "red" } },
    //         // {"source": ""}
    //       ],
    //       "options": {
    //         "xWidth": 100,
    //         "frame": {
    //           "width": 480,
    //           "height": 270
    //         }
    //       },
    //     }
    //   }
    // },

    // {
    //   "collection": "event",
    //   "directory": "event",
    //   "document": "event",
    //   "period": 1,
    //   "section": "count_rate",
    //   "tableName": "CountRateGraph_FEC1",
    //   "contents": {
    //     "Rate": {
    //       "type": "trend-graph",
    //       "group": [
    //         { "source": "Rate_circle_like_noise_1", "options": { "legend": "Circle", "color": "cyan" } },
    //         { "source": "Rate_rnd_like_noise_1", "options": { "legend": "Random", "color": "green" } },
    //         { "source": "Rate_gamma_ray_1", "options": { "legend": "Gammaray", "color": "red" } },
    //         // {"source": ""}
    //       ],
    //       "options": {
    //         "xWidth": 100,
    //         "frame": {
    //           "width": 480,
    //           "height": 270
    //         }
    //       },
    //     }
    //   }
    // },

    // {
    //   "collection": "event",
    //   "directory": "event",
    //   "document": "event",
    //   "period": 1,
    //   "section": "count_rate",
    //   "tableName": "CountRateGraph_FEC2",
    //   "contents": {
    //     "Rate": {
    //       "type": "trend-graph",
    //       "group": [
    //         { "source": "Rate_circle_like_noise_2", "options": { "legend": "Circle", "color": "cyan" } },
    //         { "source": "Rate_rnd_like_noise_2", "options": { "legend": "Random", "color": "green" } },
    //         { "source": "Rate_gamma_ray_2", "options": { "legend": "Gammaray", "color": "red" } },
    //         // {"source": ""}
    //       ],
    //       "options": {
    //         "xWidth": 100,
    //         "frame": {
    //           "width": 480,
    //           "height": 270
    //         }
    //       },
    //     }
    //   }
    // },


    // {
    //   "collection": "GroupingFECData",
    //   "directory": "event",
    //   "document": "event",
    //   "period": 1,
    //   "section": "GroupingFECData",
    //   "tableName": "HitDistribution",
    //   "contents": {
    //     "GroupingFECData": { "source": "GroupingFECData", "type": "image", "options": { "frame": { "width": 30, "height": 35 } } }
    //   },
    // },
    {
      "collection": "electron_image0",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "electron_image0",
      "tableName": "EventImageOneFEC0",
      "contents": {
        "electron_0": { "source": "electron_image0", "type": "image", "options": { "width": 60, "height": 65 } },
      }
    },
    {
      "collection": "electron_image1",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "electron_image1",
      "tableName": "EventImageFEC1",
      "contents": {
        "electron_1": { "source": "electron_image1", "type": "image", "options": { "width": 60, "height": 65 } },
      }
    },
    {
      "collection": "electron_image2",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "electron_image2",
      "tableName": "EventImageFEC2",
      "contents": {
        "electron_2": { "source": "electron_image2", "type": "image", "options": { "width": 60, "height": 65 } },
      }
    },
    // {
    //   "collection": "electron_4FEC_image",
    //   "directory": "event",
    //   "document": "event",
    //   "period": 1,
    //   "section": "electron_4FEC_image",
    //   "tableName": "electron_4FEC_image",
    //   "contents": {
    //     "electron_4FEC_image": { "source": "electron_4FEC_image", "type": "image", "options": { "width": 60, "height": 65 } },
    //   }
    // },

    {
      "collection": "GammaSpectrum",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "GammaSpectrum",
      "tableName": "GammaSpectrum",
      "contents": {
        "GammaSpectrum": {
          "type": "image",
          "source": "GammaSpectrum",
          "options": {
            "frame": {
              "width": 300,
              "height": 365
            }
          }
        }
      }
    }

  ];
