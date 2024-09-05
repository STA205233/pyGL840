HSQuickLook.main.schema =
  [
    {
      "collection": "event",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "count_rate",
      "tableName": "Countrate",
      "contents": {
        "Count_circle_like_noise_0": { "source": "Count_circle_like_noise_0", "type": "int"},
        "Rate_circle_like_noise_0": { "source": "Rate_circle_like_noise_0", "type": "float"},
        "Count_rnd_like_noise_0": { "source": "Count_rnd_like_noise_0", "type": "int"},
        "Rate_rnd_like_noise_0": { "source": "Rate_rnd_like_noise_0", "type": "float"},
        "Count_gamma_ray_0": { "source": "Count_gamma_ray_0", "type": "int"},
        "Rate_gamma_ray_0": { "source": "Rate_gamma_ray_0", "type": "float"},
        "Total_gamma_count": { "source": "Total_gamma_count", "type": "int"},
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
        "Rate": {
          "type": "trend-graph",
          "group": [
            { "source": "Rate_circle_like_noise_0", "options": { "legend": "Circle", "color": "cyan" }},
            { "source": "Rate_rnd_like_noise_0", "options": { "legend": "Random", "color": "green" }},
            { "source": "Rate_gammaray_0", "options": { "legend": "Gammaray", "color": "red" }}
          ],
          "options": { "xWidth": 1000, "frame": { "height": 270, "width": 480 } }
        },
      }
    },
    {
      "collection": "GroupingFECData",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "GroupingFECData",
      "tableName": "HitDistribution",
      "contents": {
       "GroupingFECData": { "source": "GroupingFECData", "type": "image", "options": { "width": 120, "height": 65 } },
      }
    },
    {
      "collection": "electron_image0",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "electron_image0",
      "tableName": "EventImageOneFEC0",
      "contents": {
        "electron_image0": { "source": "electron_image0", "type": "image", "options": { "width": 120, "height": 65 }},
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
        "electron_image1": { "source": "electron_image1", "type": "image", "options": { "width": 120, "height": 65 }},
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
        "electron_image2": { "source": "electron_image2", "type": "image", "options": { "width": 120, "height": 65 }},
      }
    },
     {
      "collection": "electron_4FEC_image",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "electron_4FEC_image",
      "tableName": "electron_4FEC_image",
      "contents": {
        "electron_4FEC_image": { "source": "electron_4FEC_image", "type": "image", "options": { "width": 120, "height": 65 }},
      }
    },
    { "collection": "GammaSpectrum",
      "directory": "event",
      "document": "event",
      "period": 1,
      "section": "GammaSpectrum",
      "tableName":"GammaSpectrum",
      "contents": {
        "GammaSpectrum": { "source": "GammaSpectrum", "type": "image", "options": { "width": 120, "height": 65 }},
      }}
  ];
