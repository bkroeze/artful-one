(() => {
  var __defProp = Object.defineProperty;
  var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
  var __publicField = (obj, key, value) => __defNormalProp(obj, typeof key !== "symbol" ? key + "" : key, value);

  // sketches/art/lib/chromotome.js
  var misc = [
    {
      name: "frozen-rose",
      colors: ["#29368f", "#e9697b", "#1b164d", "#f7d996"],
      background: "#f2e8e4"
    },
    {
      name: "winter-night",
      colors: ["#122438", "#dd672e", "#87c7ca", "#ebebeb"],
      background: "#ebebeb"
    },
    {
      name: "saami",
      colors: ["#eab700", "#e64818", "#2c6393", "#eecfca"],
      background: "#e7e6e4"
    },
    {
      name: "knotberry1",
      colors: ["#20342a", "#f74713", "#686d2c", "#e9b4a6"],
      background: "#e5ded8"
    },
    {
      name: "knotberry2",
      colors: ["#1d3b1a", "#eb4b11", "#e5bc00", "#f29881"],
      background: "#eae2d0"
    },
    {
      name: "tricolor",
      colors: ["#ec643b", "#56b7ab", "#f8cb57", "#1f1e43"],
      background: "#f7f2df"
    },
    {
      name: "foxshelter",
      colors: ["#ff3931", "#007861", "#311f27", "#bab9a4"],
      background: "#dddddd"
    },
    {
      name: "hermes",
      colors: ["#253852", "#51222f", "#b53435", "#ecbb51"],
      background: "#eeccc2"
    },
    {
      name: "olympia",
      colors: ["#ff3250", "#ffb33a", "#008c36", "#0085c6", "#4c4c4c"],
      stroke: "#0b0b0b",
      background: "#faf2e5"
    },
    {
      name: "byrnes",
      colors: ["#c54514", "#dca215", "#23507f"],
      stroke: "#0b0b0b",
      background: "#e8e7d4"
    },
    {
      name: "butterfly",
      colors: ["#f40104", "#f6c0b3", "#99673a", "#f0f1f4"],
      stroke: "#191e36",
      background: "#191e36"
    },
    {
      name: "floratopia",
      colors: ["#bf4a2b", "#cd902a", "#4e4973", "#f5d4bc"],
      stroke: "#1e1a43",
      background: "#1e1a43"
    },
    {
      name: "verena",
      colors: ["#f1594a", "#f5b50e", "#14a160", "#2969de", "#885fa4"],
      stroke: "#1a1a1a",
      background: "#e2e6e8"
    },
    {
      name: "florida_citrus",
      colors: ["#ea7251", "#ebf7f0", "#02aca5"],
      stroke: "#050100",
      background: "#9ae2d3"
    },
    {
      name: "lemon_citrus",
      colors: ["#e2d574", "#f1f4f7", "#69c5ab"],
      stroke: "#463231",
      background: "#f79eac"
    },
    {
      name: "yuma_punk",
      colors: ["#f05e3b", "#ebdec4", "#ffdb00"],
      stroke: "#ebdec4",
      background: "#161616"
    },
    {
      name: "yuma_punk2",
      colors: ["#f2d002", "#f7f5e1", "#ec643b"],
      stroke: "#19080e",
      background: "#f7f5e1"
    },
    {
      name: "moir",
      colors: ["#a49f4f", "#d4501e", "#f7c558", "#ebbaa6"],
      stroke: "#161716",
      background: "#f7f4ef"
    },
    {
      name: "sprague",
      colors: ["#ec2f28", "#f8cd28", "#1e95bb", "#fbaab3", "#fcefdf"],
      stroke: "#221e1f",
      background: "#fcefdf"
    },
    {
      name: "bloomberg",
      colors: ["#ff5500", "#f4c145", "#144714", "#2f04fc", "#e276af"],
      stroke: "#000",
      background: "#fff3dd"
    },
    {
      name: "revolucion",
      colors: ["#ed555d", "#fffcc9", "#41b797", "#eda126", "#7b5770"],
      stroke: "#fffcc9",
      background: "#2d1922"
    },
    {
      name: "sneaker",
      colors: ["#e8165b", "#401e38", "#66c3b4", "#ee7724", "#584098"],
      stroke: "#401e38",
      background: "#ffffff"
    },
    {
      name: "miradors",
      colors: ["#ff6936", "#fddc3f", "#0075ca", "#00bb70"],
      stroke: "#ffffff",
      background: "#020202"
    },
    {
      name: "kaffeprat",
      colors: ["#BCAA8C", "#D8CDBE", "#484A42", "#746B58", "#9A8C73"],
      stroke: "#000",
      background: "#fff"
    },
    {
      name: "jrmy",
      colors: ["#df456c", "#ea6a82", "#270b32", "#471e43"],
      stroke: "#270b32",
      background: "#ef9198"
    },
    {
      name: "animo",
      colors: ["#f6c103", "#f6f6f6", "#d1cdc7", "#e7e6e5"],
      stroke: "#010001",
      background: "#f5f5f5"
    },
    {
      name: "book",
      colors: ["#be1c24", "#d1a082", "#037b68", "#d8b1a5", "#1c2738", "#c95a3f"],
      stroke: "#0e0f27",
      background: "#f5b28a"
    },
    {
      name: "juxtapoz",
      colors: ["#20357e", "#f44242", "#ffffff"],
      stroke: "#000000",
      background: "#cfc398"
    },
    {
      name: "hurdles",
      colors: ["#e16503", "#dc9a0f", "#dfe2b4", "#66a7a6"],
      stroke: "#3c1c03",
      background: "#3c1c03"
    },
    {
      name: "ludo",
      colors: ["#df302f", "#e5a320", "#0466b3", "#0f7963"],
      stroke: "#272621",
      background: "#dedccd"
    },
    {
      name: "riff",
      colors: ["#e24724", "#c7c7c7", "#1f3e7c", "#d29294", "#010203"],
      stroke: "#010203",
      background: "#f2f2f2"
    },
    {
      name: "san ramon",
      colors: ["#4f423a", "#f6a74b", "#589286", "#f8e9e2", "#2c2825"],
      stroke: "#2c2825",
      background: "#fff"
    },
    {
      name: "one-dress",
      colors: ["#1767D2", "#FFFFFF", "#F9AB00", "#212121"],
      stroke: "#212121",
      background: "#fff"
    }
  ];
  var colourscafe = [
    {
      name: "cc239",
      colors: ["#e3dd34", "#78496b", "#f0527f", "#a7e0e2"],
      background: "#e0eff0"
    },
    {
      name: "cc234",
      colors: ["#ffce49", "#ede8dc", "#ff5736", "#ff99b4"],
      background: "#f7f4ed"
    },
    {
      name: "cc232",
      colors: ["#5c5f46", "#ff7044", "#ffce39", "#66aeaa"],
      background: "#e9ecde"
    },
    {
      name: "cc238",
      colors: ["#553c60", "#ffb0a0", "#ff6749", "#fbe090"],
      background: "#f5e9de"
    },
    {
      name: "cc242",
      colors: ["#bbd444", "#fcd744", "#fa7b53", "#423c6f"],
      background: "#faf4e4"
    },
    {
      name: "cc245",
      colors: ["#0d4a4e", "#ff947b", "#ead3a2", "#5284ab"],
      background: "#f6f4ed"
    },
    {
      name: "cc273",
      colors: ["#363d4a", "#7b8a56", "#ff9369", "#f4c172"],
      background: "#f0efe2"
    }
  ];
  var ranganath = [
    {
      name: "rag-mysore",
      colors: ["#ec6c26", "#613a53", "#e8ac52", "#639aa0"],
      background: "#d5cda1"
    },
    {
      name: "rag-gol",
      colors: ["#d3693e", "#803528", "#f1b156", "#90a798"],
      background: "#f0e0a4"
    },
    {
      name: "rag-belur",
      colors: ["#f46e26", "#68485f", "#3d273a", "#535d55"],
      background: "#dcd4a6"
    },
    {
      name: "rag-bangalore",
      colors: ["#ea720e", "#ca5130", "#e9c25a", "#52534f"],
      background: "#f9ecd3"
    },
    {
      name: "rag-taj",
      colors: ["#ce565e", "#8e1752", "#f8a100", "#3ac1a6"],
      background: "#efdea2"
    },
    {
      name: "rag-virupaksha",
      colors: ["#f5736a", "#925951", "#feba4c", "#9d9b9d"],
      background: "#eedfa2"
    }
  ];
  var roygbivs = [
    {
      name: "retro",
      colors: [
        "#69766f",
        "#9ed6cb",
        "#f7e5cc",
        "#9d8f7f",
        "#936454",
        "#bf5c32",
        "#efad57"
      ]
    },
    {
      name: "retro-washedout",
      colors: [
        "#878a87",
        "#cbdbc8",
        "#e8e0d4",
        "#b29e91",
        "#9f736c",
        "#b76254",
        "#dfa372"
      ]
    },
    {
      name: "roygbiv-warm",
      colors: [
        "#705f84",
        "#687d99",
        "#6c843e",
        "#fc9a1a",
        "#dc383a",
        "#aa3a33",
        "#9c4257"
      ]
    },
    {
      name: "roygbiv-toned",
      colors: [
        "#817c77",
        "#396c68",
        "#89e3b7",
        "#f59647",
        "#d63644",
        "#893f49",
        "#4d3240"
      ]
    },
    {
      name: "present-correct",
      colors: [
        "#fd3741",
        "#fe4f11",
        "#ff6800",
        "#ffa61a",
        "#ffc219",
        "#ffd114",
        "#fcd82e",
        "#f4d730",
        "#ced562",
        "#8ac38f",
        "#79b7a0",
        "#72b5b1",
        "#5b9bae",
        "#6ba1b7",
        "#49619d",
        "#604791",
        "#721e7f",
        "#9b2b77",
        "#ab2562",
        "#ca2847"
      ]
    }
  ];
  var tundra = [
    {
      name: "tundra1",
      colors: ["#40708c", "#8e998c", "#5d3f37", "#ed6954", "#f2e9e2"]
    },
    {
      name: "tundra2",
      colors: ["#5f9e93", "#3d3638", "#733632", "#b66239", "#b0a1a4", "#e3dad2"]
    },
    {
      name: "tundra3",
      colors: [
        "#87c3ca",
        "#7b7377",
        "#b2475d",
        "#7d3e3e",
        "#eb7f64",
        "#d9c67a",
        "#f3f2f2"
      ]
    },
    {
      name: "tundra4",
      colors: [
        "#d53939",
        "#b6754d",
        "#a88d5f",
        "#524643",
        "#3c5a53",
        "#7d8c7c",
        "#dad6cd"
      ]
    }
  ];
  var rohlfs = [
    {
      name: "rohlfs_1R",
      colors: ["#004996", "#567bae", "#ff4c48", "#ffbcb3"],
      stroke: "#004996",
      background: "#fff8e7"
    },
    {
      name: "rohlfs_1Y",
      colors: ["#004996", "#567bae", "#ffc000", "#ffdca4"],
      stroke: "#004996",
      background: "#fff8e7"
    },
    {
      name: "rohlfs_1G",
      colors: ["#004996", "#567bae", "#60bf3c", "#d2deb1"],
      stroke: "#004996",
      background: "#fff8e7"
    },
    {
      name: "rohlfs_2",
      colors: ["#4d3d9a", "#f76975", "#ffffff", "#eff0dd"],
      stroke: "#211029",
      background: "#58bdbc"
    },
    {
      name: "rohlfs_3",
      colors: ["#abdfdf", "#fde500", "#58bdbc", "#eff0dd"],
      stroke: "#211029",
      background: "#f76975"
    },
    {
      name: "rohlfs_4",
      colors: ["#fde500", "#2f2043", "#f76975", "#eff0dd"],
      stroke: "#211029",
      background: "#fbbeca"
    }
  ];
  var ducci = [
    {
      name: "ducci_jb",
      colors: ["#395e54", "#e77b4d", "#050006", "#e55486"],
      stroke: "#050006",
      background: "#efe0bc"
    },
    {
      name: "ducci_a",
      colors: ["#809498", "#d3990e", "#000000", "#ecddc5"],
      stroke: "#ecddc5",
      background: "#863f52"
    },
    {
      name: "ducci_b",
      colors: ["#ecddc5", "#79b27b", "#000000", "#ac6548"],
      stroke: "#ac6548",
      background: "#d5c08e"
    },
    {
      name: "ducci_d",
      colors: ["#f3cb4d", "#f2f5e3", "#20191b", "#67875c"],
      stroke: "#67875c",
      background: "#433d5f"
    },
    {
      name: "ducci_e",
      colors: ["#c37c2b", "#f6ecce", "#000000", "#386a7a"],
      stroke: "#386a7a",
      background: "#e3cd98"
    },
    {
      name: "ducci_f",
      colors: ["#596f7e", "#eae6c7", "#463c21", "#f4cb4c"],
      stroke: "#f4cb4c",
      background: "#e67300"
    },
    {
      name: "ducci_g",
      colors: ["#c75669", "#000000", "#11706a"],
      stroke: "#11706a",
      background: "#ecddc5"
    },
    {
      name: "ducci_h",
      colors: ["#6b5c6e", "#4a2839", "#d9574a"],
      stroke: "#d9574a",
      background: "#ffc34b"
    },
    {
      name: "ducci_i",
      colors: ["#e9dcad", "#143331", "#ffc000"],
      stroke: "#ffc000",
      background: "#a74c02"
    },
    {
      name: "ducci_j",
      colors: ["#c47c2b", "#5f5726", "#000000", "#7e8a84"],
      stroke: "#7e8a84",
      background: "#ecddc5"
    },
    {
      name: "ducci_o",
      colors: ["#c15e1f", "#e4a13a", "#000000", "#4d545a"],
      stroke: "#4d545a",
      background: "#dfc79b"
    },
    {
      name: "ducci_q",
      colors: ["#4bae8c", "#d0c1a0", "#2d3538"],
      stroke: "#2d3538",
      background: "#d06440"
    },
    {
      name: "ducci_u",
      colors: ["#f6d700", "#f2d692", "#000000", "#5d3552"],
      stroke: "#5d3552",
      background: "#ff7426"
    },
    {
      name: "ducci_v",
      colors: ["#c65f75", "#d3990e", "#000000", "#597e7a"],
      stroke: "#597e7a",
      background: "#f6eccb"
    },
    {
      name: "ducci_x",
      colors: ["#dd614a", "#f5cedb", "#1a1e4f"],
      stroke: "#1a1e4f",
      background: "#fbb900"
    }
  ];
  var judson = [
    {
      name: "jud_playground",
      colors: ["#f04924", "#fcce09", "#408ac9"],
      stroke: "#2e2925",
      background: "#ffffff"
    },
    {
      name: "jud_horizon",
      colors: ["#f8c3df", "#f2e420", "#28b3d0", "#648731", "#ef6a7d"],
      stroke: "#030305",
      background: "#f2f0e1"
    },
    {
      name: "jud_mural",
      colors: ["#ca3122", "#e5af16", "#4a93a2", "#0e7e39", "#e2b9bd"],
      stroke: "#1c1616",
      background: "#e3ded8"
    },
    {
      name: "jud_cabinet",
      colors: ["#f0afb7", "#f6bc12", "#1477bb", "#41bb9b"],
      stroke: "#020508",
      background: "#e3ded8"
    }
  ];
  var iivonen = [
    {
      name: "iiso_zeitung",
      colors: ["#ee8067", "#f3df76", "#00a9c0", "#f7ab76"],
      stroke: "#111a17",
      background: "#f5efcb"
    },
    {
      name: "iiso_curcuit",
      colors: ["#f0865c", "#f2b07b", "#6bc4d2", "#1a3643"],
      stroke: "#0f1417",
      background: "#f0f0e8"
    },
    {
      name: "iiso_airlines",
      colors: ["#fe765a", "#ffb468", "#4b588f", "#faf1e0"],
      stroke: "#1c1616",
      background: "#fae5c8"
    },
    {
      name: "iiso_daily",
      colors: ["#e76c4a", "#f0d967", "#7f8cb6", "#1daeb1", "#ef9640"],
      stroke: "#000100",
      background: "#e2ded2"
    }
  ];
  var kovecses = [
    {
      name: "kov_01",
      colors: ["#d24c23", "#7ba6bc", "#f0c667", "#ede2b3", "#672b35", "#142a36"],
      stroke: "#132a37",
      background: "#108266"
    },
    {
      name: "kov_02",
      colors: ["#e8dccc", "#e94641", "#eeaeae"],
      stroke: "#e8dccc",
      background: "#6c96be"
    },
    {
      name: "kov_03",
      colors: ["#e3937b", "#d93f1d", "#090d15", "#e6cca7"],
      stroke: "#090d15",
      background: "#558947"
    },
    {
      name: "kov_04",
      colors: ["#d03718", "#292b36", "#33762f", "#ead7c9", "#ce7028", "#689d8d"],
      stroke: "#292b36",
      background: "#deb330"
    },
    {
      name: "kov_05",
      colors: ["#de3f1a", "#de9232", "#007158", "#e6cdaf", "#869679"],
      stroke: "#010006",
      background: "#7aa5a6"
    },
    {
      name: "kov_06",
      colors: [
        "#a87c2a",
        "#bdc9b1",
        "#f14616",
        "#ecbfaf",
        "#017724",
        "#0e2733",
        "#2b9ae9"
      ],
      stroke: "#292319",
      background: "#dfd4c1"
    },
    {
      name: "kov_06b",
      colors: [
        "#d57846",
        "#dfe0cc",
        "#de442f",
        "#e7d3c5",
        "#5ec227",
        "#302f35",
        "#63bdb3"
      ],
      stroke: "#292319",
      background: "#dfd4c1"
    },
    {
      name: "kov_07",
      colors: ["#c91619", "#fdecd2", "#f4a000", "#4c2653"],
      stroke: "#111",
      background: "#89c2cd"
    }
  ];
  var tsuchimochi = [
    {
      name: "tsu_arcade",
      colors: ["#4aad8b", "#e15147", "#f3b551", "#cec8b8", "#d1af84", "#544e47"],
      stroke: "#251c12",
      background: "#cfc7b9"
    },
    {
      name: "tsu_harutan",
      colors: ["#75974a", "#c83e3c", "#f39140", "#e4ded2", "#f8c5a4", "#434f55"],
      stroke: "#251c12",
      background: "#cfc7b9"
    },
    {
      name: "tsu_akasaka",
      colors: ["#687f72", "#cc7d6c", "#dec36f", "#dec7af", "#ad8470", "#424637"],
      stroke: "#251c12",
      background: "#cfc7b9"
    }
  ];
  var duotone = [
    {
      name: "dt01",
      colors: ["#172a89", "#f7f7f3"],
      stroke: "#172a89",
      background: "#f3abb0"
    },
    {
      name: "dt02",
      colors: ["#302956", "#f3c507"],
      stroke: "#302956",
      background: "#eee3d3"
    },
    {
      name: "dt02b",
      colors: ["#eee3d3"],
      stroke: "#302956",
      background: "#f3c507"
    },
    {
      name: "dt03",
      colors: ["#000000", "#a7a7a7"],
      stroke: "#000000",
      background: "#0a5e78"
    },
    {
      name: "dt04",
      colors: ["#50978e", "#f7f0df"],
      stroke: "#000000",
      background: "#f7f0df"
    },
    {
      name: "dt05",
      colors: ["#ee5d65", "#f0e5cb"],
      stroke: "#080708",
      background: "#f0e5cb"
    },
    {
      name: "dt06",
      colors: ["#271f47", "#e7ceb5"],
      stroke: "#271f47",
      background: "#cc2b1c"
    },
    {
      name: "dt07",
      colors: ["#6a98a5", "#d24c18"],
      stroke: "#efebda",
      background: "#efebda"
    },
    {
      name: "dt08",
      colors: ["#5d9d88", "#ebb43b"],
      stroke: "#efebda",
      background: "#efebda"
    },
    {
      name: "dt09",
      colors: ["#052e57", "#de8d80"],
      stroke: "#efebda",
      background: "#efebda"
    },
    {
      name: "dt10",
      colors: ["#e5dfcf", "#151513"],
      stroke: "#151513",
      background: "#e9b500"
    },
    {
      name: "dt11",
      colors: ["#ece9e2"],
      stroke: "#221e1f",
      background: "#75c4bf"
    },
    {
      name: "dt12",
      colors: ["#f5f2d3"],
      stroke: "#073c5c",
      background: "#c0d0c3"
    },
    {
      name: "dt13",
      colors: ["#f5f2d3", "#f5f2d3", "#fbd6b8"],
      stroke: "#ec5525",
      background: "#ec5525"
    }
  ];
  var hilda = [
    {
      name: "hilda01",
      colors: ["#ec5526", "#f4ac12", "#9ebbc1", "#f7f4e2"],
      stroke: "#1e1b1e",
      background: "#e7e8d4"
    },
    {
      name: "hilda02",
      colors: ["#eb5627", "#eebb20", "#4e9eb8", "#f7f5d0"],
      stroke: "#201d13",
      background: "#77c1c0"
    },
    {
      name: "hilda03",
      colors: ["#e95145", "#f8b917", "#b8bdc1", "#ffb2a2"],
      stroke: "#010101",
      background: "#6b7752"
    },
    {
      name: "hilda04",
      colors: ["#e95145", "#f6bf7a", "#589da1", "#f5d9bc"],
      stroke: "#000001",
      background: "#f5ede1"
    },
    {
      name: "hilda05",
      colors: ["#ff6555", "#ffb58f", "#d8eecf", "#8c4b47", "#bf7f93"],
      stroke: "#2b0404",
      background: "#ffda82"
    },
    {
      name: "hilda06",
      colors: ["#f75952", "#ffce84", "#74b7b2", "#f6f6f6", "#b17d71"],
      stroke: "#0e0603",
      background: "#f6ecd4"
    }
  ];
  var spatial = [
    {
      name: "spatial01",
      colors: ["#ff5937", "#f6f6f4", "#4169ff"],
      stroke: "#ff5937",
      background: "#f6f6f4"
    },
    {
      name: "spatial02",
      colors: ["#ff5937", "#f6f6f4", "#f6f6f4"],
      stroke: "#ff5937",
      background: "#f6f6f4"
    },
    {
      name: "spatial02i",
      colors: ["#f6f6f4", "#ff5937", "#ff5937"],
      stroke: "#f6f6f4",
      background: "#ff5937"
    },
    {
      name: "spatial03",
      colors: ["#4169ff", "#f6f6f4", "#f6f6f4"],
      stroke: "#4169ff",
      background: "#f6f6f4"
    },
    {
      name: "spatial03i",
      colors: ["#f6f6f4", "#4169ff", "#4169ff"],
      stroke: "#f6f6f4",
      background: "#4169ff"
    }
  ];
  var jung = [
    {
      name: "jung_bird",
      colors: ["#fc3032", "#fed530", "#33c3fb", "#ff7bac", "#fda929"],
      stroke: "#000000",
      background: "#ffffff"
    },
    {
      name: "jung_horse",
      colors: ["#e72e81", "#f0bf36", "#3056a2"],
      stroke: "#000000",
      background: "#ffffff"
    },
    {
      name: "jung_croc",
      colors: ["#f13274", "#eed03e", "#405e7f", "#19a198"],
      stroke: "#000000",
      background: "#ffffff"
    },
    {
      name: "jung_hippo",
      colors: ["#ff7bac", "#ff921e", "#3ea8f5", "#7ac943"],
      stroke: "#000000",
      background: "#ffffff"
    },
    {
      name: "jung_wolf",
      colors: ["#e51c39", "#f1b844", "#36c4b7", "#666666"],
      stroke: "#000000",
      background: "#ffffff"
    }
  ];
  var system = [
    {
      name: "system.#01",
      colors: ["#ff4242", "#fec101", "#1841fe", "#fcbdcc", "#82e9b5"],
      stroke: "#000",
      background: "#fff"
    },
    {
      name: "system.#02",
      colors: ["#ff4242", "#ffd480", "#1e365d", "#edb14c", "#418dcd"],
      stroke: "#000",
      background: "#fff"
    },
    {
      name: "system.#03",
      colors: ["#f73f4a", "#d3e5eb", "#002c3e", "#1aa1b1", "#ec6675"],
      stroke: "#110b09",
      background: "#fff"
    },
    {
      name: "system.#04",
      colors: ["#e31f4f", "#f0ac3f", "#18acab", "#26265a", "#ea7d81", "#dcd9d0"],
      stroke: "#26265a",
      backgrund: "#dcd9d0"
    },
    {
      name: "system.#05",
      colors: ["#db4549", "#d1e1e1", "#3e6a90", "#2e3853", "#a3c9d3"],
      stroke: "#000",
      background: "#fff"
    },
    {
      name: "system.#06",
      colors: ["#e5475c", "#95b394", "#28343b", "#f7c6a3", "#eb8078"],
      stroke: "#000",
      background: "#fff"
    },
    {
      name: "system.#07",
      colors: ["#d75c49", "#f0efea", "#509da4"],
      stroke: "#000",
      background: "#fff"
    },
    {
      name: "system.#08",
      colors: ["#f6625a", "#92b29f", "#272c3f"],
      stroke: "#000",
      background: "#fff"
    }
  ];
  var flourish = [
    {
      name: "empusa",
      colors: [
        "#c92a28",
        "#e69301",
        "#1f8793",
        "#13652b",
        "#e7d8b0",
        "#48233b",
        "#e3b3ac"
      ],
      stroke: "#1a1a1a",
      background: "#f0f0f2"
    },
    {
      name: "delphi",
      colors: [
        "#475b62",
        "#7a999c",
        "#2a1f1d",
        "#fbaf3c",
        "#df4a33",
        "#f0e0c6",
        "#af592c"
      ],
      stroke: "#2a1f1d",
      background: "#f0e0c6"
    },
    {
      name: "mably",
      colors: [
        "#13477b",
        "#2f1b10",
        "#d18529",
        "#d72a25",
        "#e42184",
        "#138898",
        "#9d2787",
        "#7f311b"
      ],
      stroke: "#2a1f1d",
      background: "#dfc792"
    },
    {
      name: "nowak",
      colors: [
        "#e85b30",
        "#ef9e28",
        "#c6ac71",
        "#e0c191",
        "#3f6279",
        "#ee854e",
        "#180305"
      ],
      stroke: "#180305",
      background: "#ede4cb"
    },
    {
      name: "jupiter",
      colors: [
        "#c03a53",
        "#edd09e",
        "#aab5af",
        "#023629",
        "#eba735",
        "#8e9380",
        "#6c4127"
      ],
      stroke: "#12110f",
      background: "#e6e2d6"
    },
    {
      name: "hersche",
      colors: [
        "#df9f00",
        "#1f6f50",
        "#8e6d7f",
        "#da0607",
        "#a4a5a7",
        "#d3d1c3",
        "#42064f",
        "#25393a"
      ],
      stroke: "#0a0a0a",
      background: "#f0f5f6"
    },
    {
      name: "cherfi",
      colors: [
        "#99cb9f",
        "#cfb610",
        "#d00701",
        "#dba78d",
        "#2e2c1d",
        "#bfbea2",
        "#d2cfaf"
      ],
      stroke: "#332e22",
      background: "#e3e2c5"
    },
    {
      name: "harvest",
      colors: [
        "#313a42",
        "#9aad2e",
        "#f0ae3c",
        "#df4822",
        "#8eac9b",
        "#cc3d3f",
        "#ec8b1c",
        "#1b9268"
      ],
      stroke: "#463930",
      background: "#e5e2cf"
    },
    {
      name: "honey",
      colors: [
        "#f14d42",
        "#f4fdec",
        "#4fbe5d",
        "#265487",
        "#f6e916",
        "#f9a087",
        "#2e99d6"
      ],
      stroke: "#141414",
      background: "#f4fdec"
    },
    {
      name: "jungle",
      colors: [
        "#adb100",
        "#e5f4e9",
        "#f4650f",
        "#4d6838",
        "#cb9e00",
        "#689c7d",
        "#e2a1a8",
        "#151c2e"
      ],
      stroke: "#0e0f27",
      background: "#cecaa9"
    },
    {
      name: "skyspider",
      colors: [
        "#f4b232",
        "#f2dbbd",
        "#01799c",
        "#e93e48",
        "#0b1952",
        "#006748",
        "#ed817d"
      ],
      stroke: "#050505",
      background: "#f0dbbc"
    },
    {
      name: "atlas",
      colors: ["#5399b1", "#f4e9d5", "#de4037", "#ed942f", "#4e9e48", "#7a6e62"],
      stroke: "#3d352b",
      background: "#f0c328"
    },
    {
      name: "giftcard",
      colors: [
        "#FBF5E9",
        "#FF514E",
        "#FDBC2E",
        "#4561CC",
        "#2A303E",
        "#6CC283",
        "#A71172",
        "#238DA5",
        "#9BD7CB",
        "#231E58",
        "#4E0942"
      ],
      stroke: "#000",
      background: "#FBF5E9"
    },
    {
      name: "giftcard_sub",
      colors: [
        "#FBF5E9",
        "#FF514E",
        "#FDBC2E",
        "#4561CC",
        "#2A303E",
        "#6CC283",
        "#238DA5",
        "#9BD7CB"
      ],
      stroke: "#000",
      background: "#FBF5E9"
    }
  ];
  var dale = [
    {
      name: "dale_paddle",
      colors: [
        "#ff7a5a",
        "#765aa6",
        "#fee7bc",
        "#515e8c",
        "#ffc64a",
        "#b460a6",
        "#ffffff",
        "#4781c1"
      ],
      stroke: "#000000",
      background: "#abe9e8"
    },
    {
      name: "dale_night",
      colors: ["#ae5d9d", "#f1e8bc", "#ef8fa3", "#f7c047", "#58c9ed", "#f77150"],
      stroke: "#000000",
      background: "#00ae83"
    },
    {
      name: "dale_cat",
      colors: ["#f77656", "#f7f7f7", "#efc545", "#dfe0e2", "#3c70bd", "#66bee4"],
      stroke: "#000000",
      background: "#f6e0b8"
    }
  ];
  var cako = [
    {
      name: "cako1",
      colors: ["#000000", "#d55a3a", "#2a5c8a", "#7e7d14", "#dbdac9"],
      stroke: "#000000",
      background: "#f4e9d5"
    },
    {
      name: "cako2",
      colors: ["#dbdac9", "#d55a3a", "#2a5c8a", "#b47b8c", "#7e7d14"],
      stroke: "#000000",
      background: "#000000"
    },
    {
      name: "cako2_sub1",
      colors: ["#dbdac9", "#d55a3a", "#2a5c8a"],
      stroke: "#000000",
      background: "#000000"
    },
    {
      name: "cako2_sub2",
      colors: ["#dbdac9", "#d55a3a", "#7e7d14"],
      stroke: "#000000",
      background: "#000000"
    }
  ];
  var mayo = [
    {
      name: "mayo1",
      colors: ["#ea510e", "#ffd203", "#0255a3", "#039177", "#111111"],
      stroke: "#111111",
      background: "#fff"
    },
    {
      name: "mayo2",
      colors: ["#ea663f", "#f9cc27", "#84afd7", "#7ca994", "#f1bbc9", "#242424"],
      stroke: "#2a2a2a",
      background: "#f5f6f1"
    },
    {
      name: "mayo3",
      colors: ["#ea5b19", "#f8c9b9", "#137661", "#2a2a2a"],
      stroke: "#2a2a2a",
      background: "#f5f4f0"
    }
  ];
  var exposito = [
    {
      name: "exposito",
      colors: [
        "#8bc9c3",
        "#ffae43",
        "#ea432c",
        "#228345",
        "#d1d7d3",
        "#524e9c",
        "#9dc35e",
        "#f0a1a1"
      ],
      stroke: "#fff",
      background: "#000000"
    },
    {
      name: "exposito_sub1",
      colors: ["#8bc9c3", "#ffae43", "#ea432c", "#524e9c"],
      stroke: "#fff",
      background: "#000000"
    },
    {
      name: "exposito_sub2",
      colors: ["#8bc9c3", "#ffae43", "#ea432c", "#524e9c", "#f0a1a1", "#228345"],
      stroke: "#fff",
      background: "#000000"
    },
    {
      name: "exposito_sub3",
      colors: ["#ffae43", "#ea432c", "#524e9c", "#f0a1a1"],
      stroke: "#fff",
      background: "#000000"
    }
  ];
  var orbifold = [
    {
      name: "candy-wrap",
      colors: [
        "#f19797",
        "#f9b73e",
        "#ee5151",
        "#fb671f",
        "#6bbe3a",
        "#0c75b7",
        "#0b9e4e",
        "#763f68"
      ],
      stroke: "#302319",
      background: "#e7ded5"
    },
    {
      name: "slicks",
      colors: ["#e1decd", "#d95336", "#e6ac1d"],
      stroke: "#302319",
      background: "#e1decd"
    },
    {
      name: "circus",
      colors: ["#3eb79e", "#f4a910", "#f37377", "#207986", "#f26003", "#afce95"],
      stroke: "#302319",
      background: "#eadcb6"
    },
    {
      name: "spotlight",
      colors: ["#f34312", "#00a49e", "#ef888f", "#f5b408", "#412432"],
      stroke: "#412432",
      background: "#dfdcd5"
    },
    {
      name: "five-stars",
      colors: [
        "#f5e8c7",
        "#d9dcad",
        "#cf3933",
        "#f3f4f4",
        "#74330d",
        "#8bb896",
        "#eba824",
        "#f05c03"
      ],
      stroke: "#380c05",
      background: "#ecd598"
    },
    {
      name: "full-moon",
      colors: ["#f7e8be", "#aa879f", "#f6634e"],
      stroke: "#2a1f39",
      background: "#f7e8be"
    },
    {
      name: "sunday-stroll",
      colors: [
        "#d44c4c",
        "#e47781",
        "#f5d274",
        "#f7e8be",
        "#acbe55",
        "#6fb97a",
        "#5ba150",
        "#037750",
        "#003e5e",
        "#595373",
        "#73659e",
        "#ac879f"
      ],
      background: "#e5cbb5",
      w: 2
    },
    {
      name: "vegetable-soup",
      colors: [
        "#ec6a22",
        "#f7e9c5",
        "#399a3f",
        "#9ac764",
        "#fff7e0",
        "#ffcd6b",
        "#634754",
        "#98c195",
        "#708658"
      ],
      background: "#fff7e0",
      w: 2
    },
    {
      name: "risograph",
      colors: ["#f56f64", "#f9cb1f", "#f0eace"],
      stroke: "#295042",
      background: "#f0eace",
      w: 1
    },
    {
      name: "tote-bag",
      colors: ["#f5f5f5", "#ffc6cf", "#fd5105", "#4124b0"],
      stroke: "#231e22",
      background: "#ffc6cf",
      w: 1
    },
    {
      name: "slicks",
      colors: [
        "#ffbdd0",
        "#ff4328",
        "#e88526",
        "#21b929",
        "#2193c9",
        "#fffcea",
        "#ffcc21"
      ],
      stroke: "#fffcea",
      background: "#212121",
      w: 1
    }
  ];
  var pals = misc.concat(
    ranganath,
    roygbivs,
    tundra,
    colourscafe,
    rohlfs,
    ducci,
    judson,
    iivonen,
    kovecses,
    tsuchimochi,
    duotone,
    hilda,
    spatial,
    jung,
    system,
    flourish,
    dale,
    cako,
    mayo,
    exposito,
    orbifold
  );
  var palettes = pals.map((p) => {
    p.size = p.colors.length;
    return p;
  });
  function getRandom() {
    return palettes[Math.floor(Math.random() * palettes.length)];
  }
  function get(name) {
    if (name === void 0) return getRandom();
    return palettes.find((pal) => pal.name == name);
  }

  // sketches/art/lib/colors.js
  var RingStack = class _RingStack {
    constructor(series, options = {}) {
      this.series = series;
      this.options = options;
      this.index = -1;
    }
    burn(index = -1) {
      let burnIx = index === -1 ? this.index : index % this.series.length;
      if (burnIx === -1) {
        burnIx = 0;
      }
      const val = this.series[burnIx];
      const trimmed = [];
      this.series.forEach((c, ix) => {
        if (ix !== burnIx) {
          trimmed.push(c);
        }
      });
      this.series = trimmed;
      this.reset(index);
      return val;
    }
    burnRandom() {
      const index = Math.floor(Math.random() * this.series.length);
      return this.burn(index);
    }
    duplicate() {
      return new _RingStack(this.series);
    }
    dict(names) {
      const ret = {};
      names.forEach((c, ix) => {
        const key = names[ix];
        ret[names[ix]] = key === "bg" ? this.background() : this.next();
      });
      return ret;
    }
    get(index) {
      if (index === void 0) {
        return this.get(this.index);
      }
      return this.series[index % this.series.length];
    }
    next(count = 1) {
      this.reset(this.index + 1);
      if (count === 1) {
        return this.get(this.index);
      }
      const ret = [];
      for (let i = 0; i < count; i++) {
        ret.push(this.get(this.index + i));
      }
      return ret;
    }
    random() {
      const index = int(random(this.series.length));
      return this.series[index];
    }
    reset(ix = 0) {
      this.index = ix % this.series.length;
      return this;
    }
    shuffle() {
      this.series = shuffle(this.series);
      return this;
    }
  };
  var ColorStack = class _ColorStack extends RingStack {
    duplicate() {
      return new _ColorStack(this.series);
    }
    background() {
      if (!this.options.background) {
        this.options.background = this.burnRandom();
      }
      return this.options.background;
    }
    stroke() {
      if (!this.options.stroke) {
        this.options.stroke = this.burnRandom();
      }
      return this.options.stroke;
    }
    nextWithOpacity(opacity) {
      const val = this.next();
      const r = val.slice(1, 3);
      const g = val.slice(3, 5);
      const b = val.slice(5, 7);
      const rgba = `rgba(${unhex(r)}, ${unhex(g)}, ${unhex(b)}, ${opacity})`;
      return color(rgba);
    }
  };
  function chromatomeColors(pallette) {
    if (!pallette) {
      return new ColorStack(getRandom().colors);
    }
    const chroma = get(pallette);
    return new ColorStack(chroma.colors, chroma);
  }

  // sketches/art/lib/patterns.ts
  var PatternController = class {
    constructor() {
      __publicField(this, "x");
      __publicField(this, "y");
      __publicField(this, "w");
      __publicField(this, "h");
      __publicField(this, "colors");
      __publicField(this, "angle");
      __publicField(this, "patternFunction");
      __publicField(this, "renderTarget");
      this.x = 0;
      this.y = 0;
      this.w = 0;
      this.h = 0;
      this.colors = ["#FFFFFF", "#000000"];
      this.angle = 0;
      this.patternFunction = null;
      this.renderTarget = null;
    }
    patternAngle(_angle) {
      if (typeof _angle === "number") this.angle = _angle;
      return this.angle;
    }
    setPatternFunction(_func) {
      if (typeof _func !== "function") return false;
      this.patternFunction = _func;
      return this.patternFunction;
    }
    applyPattern(_x, _y, _w, _h, _renderTarget) {
      this._setPatternArea(_x, _y, _w, _h);
      this._setRenderTarget(_renderTarget);
      this.renderTarget = _renderTarget;
      this._drawPattern();
    }
    patternColors(_colsArr) {
      if (Array.isArray(_colsArr)) this.colors = _colsArr;
      return this.colors.slice(0, this.colors.length);
    }
    _setPatternArea(_x, _y, _w, _h) {
      this.x = _x;
      this.y = _y;
      this.w = _w;
      this.h = _h;
    }
    _setRenderTarget(_renderTarget) {
      this.renderTarget = _renderTarget;
    }
    _drawPattern() {
      const rt = this.renderTarget;
      const func = typeof this.patternFunction === "function" ? this.patternFunction : this._flatFill();
      const rotatedFunc = this._rotatedFuncGen(func, this.angle);
      const pRectMode = rt._renderer._rectMode;
      const pEllipseMode = rt._renderer._ellipseMode;
      rt.push();
      rt.drawingContext.clip();
      rt.translate(this.x, this.y);
      rotatedFunc(this.w, this.h, rt);
      rt.pop();
      rt.rectMode(pRectMode);
      rt.ellipseMode(pEllipseMode);
    }
    _rotatedFuncGen(_ptnFunc, _angle) {
      const func = function(_w, _h, _rt) {
        const p1 = _rt.createVector(-_w / 2, _h / 2).rotate(_angle);
        const p2 = _rt.createVector(_w / 2, _h / 2).rotate(_angle);
        const nw = Math.max(Math.abs(p1.x), Math.abs(p2.x)) * 2;
        const nh = Math.max(Math.abs(p1.y), Math.abs(p2.y)) * 2;
        _rt.push();
        _rt.translate(_w / 2, _h / 2);
        _rt.rotate(_angle);
        _rt.translate(-nw / 2, -nh / 2);
        _ptnFunc(nw, nh, _rt);
        _rt.pop();
      };
      return func;
    }
    _flatFill() {
      const c = this.patternColors(this.colors);
      return function(_w, _h, _rt) {
        _rt.rectMode(_rt.CORNER);
        _rt.fill(c[0]);
        _rt.noStroke();
        _rt.rect(0, 0, _w, _h);
      };
    }
  };
  var PatternVertexInfo = class {
    constructor() {
      __publicField(this, "verticies");
      __publicField(this, "isCurve");
      __publicField(this, "curveAreaMult");
      this.verticies = [];
      this.isCurve = false;
      this.curveAreaMult = 1.25;
    }
    reset() {
      this.verticies = [];
      this.isCurve = false;
    }
    addVertex(x, y) {
      this.verticies.push([x, y]);
    }
    addCurveVertex(x, y) {
      this.addVertex(x, y);
      this.isCurve = true;
    }
    addBezierVertex(x2, y2, x3, y3, x4, y4) {
      this.addVertex(x2, y2);
      this.addVertex(x3, y3);
      this.addVertex(x4, y4);
    }
    addQuadraticVertex(cx, cy, x3, y3) {
      this.addVertex(cx, cy);
      this.addVertex(x3, y3);
    }
    culclateArea() {
      let minx = this.verticies[0][0];
      let maxx = minx;
      let miny = this.verticies[0][1];
      let maxy = miny;
      for (let i = 0; i < this.verticies.length; i++) {
        let nx = this.verticies[i][0];
        let ny = this.verticies[i][1];
        minx = Math.min(minx, nx);
        maxx = Math.max(maxx, nx);
        miny = Math.min(miny, ny);
        maxy = Math.max(maxy, ny);
      }
      let w = maxx - minx;
      let h = maxy - miny;
      let cx = w / 2 + minx;
      let cy = h / 2 + miny;
      if (this.isCurve) {
        w *= this.curveAreaMult;
        h *= this.curveAreaMult;
      }
      let x = cx - w / 2;
      let y = cy - h / 2;
      const area = { x, y, w, h };
      return area;
    }
  };
  p5.prototype._patternController = new PatternController();
  p5.Graphics.prototype._patternController = new PatternController();
  p5.prototype._patternVertexInfo = new PatternVertexInfo();
  p5.Graphics.prototype._patternVertexInfo = new PatternVertexInfo();
  p5.prototype.patternAngle = function(_angle) {
    return this._patternController.patternAngle(_angle);
  };
  p5.prototype.patternColors = function(_colsArr) {
    return this._patternController.patternColors(_colsArr);
  };
  p5.prototype.pattern = function(_func) {
    return this._patternController.setPatternFunction(_func);
  };
  (function() {
    const _modeAdjust = function(a, b, c, d, mode) {
      if (mode === p5.prototype.CORNER) {
        return { x: a, y: b, w: c, h: d };
      } else if (mode === p5.prototype.CORNERS) {
        return { x: a, y: b, w: c - a, h: d - b };
      } else if (mode === p5.prototype.RAIUS) {
        return { x: a - c, y: b - d, w: 2 * c, h: 2 * d };
      } else if (mode === p5.prototype.CENTER) {
        return { x: a - c * 0.5, y: b - d * 0.5, w: c, h: d };
      }
    };
    const _disableColor = function(_renderTarget) {
      _renderTarget.noStroke();
      _renderTarget.fill(255, 0);
    };
    p5.prototype.rectPattern = function(...args) {
      _disableColor(this);
      const r = this.rect(...args);
      const val = _modeAdjust(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[3],
        this._renderer._rectMode
      );
      this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
      return r;
    };
    p5.prototype.squarePattern = function(...args) {
      _disableColor(this);
      const r = this.square(...args);
      const val = _modeAdjust(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[2],
        this._renderer._rectMode
      );
      this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
      return r;
    };
    p5.prototype.ellipsePattern = function(...args) {
      _disableColor(this);
      const r = this.ellipse(...args);
      const val = _modeAdjust(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[3],
        this._renderer._ellipseMode
      );
      this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
      return r;
    };
    p5.prototype.arcPattern = function(...args) {
      _disableColor(this);
      const r = this.arc(...args);
      const val = _modeAdjust(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[3],
        this._renderer._ellipseMode
      );
      this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
      return r;
    };
    p5.prototype.circlePattern = function(...args) {
      _disableColor(this);
      const r = this.circle(...args);
      const val = _modeAdjust(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[2],
        this._renderer._ellipseMode
      );
      this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
      return r;
    };
    p5.prototype.trianglePattern = function(...args) {
      _disableColor(this);
      const r = this.triangle(...args);
      const cx = (arguments[0] + arguments[2] + arguments[4]) / 3;
      const cy = (arguments[1] + arguments[3] + arguments[5]) / 3;
      const w = this.max([
        Math.abs(cx - arguments[0]),
        Math.abs(cx - arguments[2]),
        Math.abs(cx - arguments[4])
      ]) * 2;
      const h = this.max([
        Math.abs(cy - arguments[1]),
        Math.abs(cy - arguments[3]),
        Math.abs(cy - arguments[5])
      ]) * 2;
      this._patternController.applyPattern(cx - w / 2, cy - h / 2, w, h, this);
      return r;
    };
    p5.prototype.quadPattern = function(...args) {
      _disableColor(this);
      const r = this.quad(...args);
      const minX = this.min([
        arguments[0],
        arguments[2],
        arguments[4],
        arguments[6]
      ]);
      const maxX = this.max([
        arguments[0],
        arguments[2],
        arguments[4],
        arguments[6]
      ]);
      const minY = this.min([
        arguments[1],
        arguments[3],
        arguments[5],
        arguments[7]
      ]);
      const maxY = this.max([
        arguments[1],
        arguments[3],
        arguments[5],
        arguments[7]
      ]);
      this._patternController.applyPattern(
        minX,
        minY,
        maxX - minX,
        maxY - minY,
        this
      );
      return r;
    };
    p5.prototype.beginShapePattern = function(...args) {
      const r = this.beginShape(...args);
      this._patternVertexInfo.reset();
      return r;
    };
    p5.prototype.beginContourPattern = function(...args) {
      return this.beginContour(...args);
    };
    p5.prototype.vertexPattern = function(...args) {
      const r = this.vertex(...args);
      this._patternVertexInfo.addVertex(arguments[0], arguments[1]);
      return r;
    };
    p5.prototype.curveVertexPattern = function(...args) {
      const r = this.curveVertex(...args);
      this._patternVertexInfo.addCurveVertex(arguments[0], arguments[1]);
      return r;
    };
    p5.prototype.bezierVertexPattern = function(...args) {
      const r = this.bezierVertex(...args);
      this._patternVertexInfo.addBezierVertex(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[3],
        arguments[4],
        arguments[5]
      );
      return r;
    };
    p5.prototype.quadraticVertexPattern = function(...args) {
      const r = this.quadraticVertex(...args);
      this._patternVertexInfo.addQuadraticVertex(
        arguments[0],
        arguments[1],
        arguments[2],
        arguments[3]
      );
      return r;
    };
    p5.prototype.endContourPattern = function(...args) {
      return this.endContour(...args);
    };
    p5.prototype.endShapePattern = function(...args) {
      _disableColor(this);
      const r = this.endShape(...args);
      const area = this._patternVertexInfo.culclateArea();
      this._patternController.applyPattern(area.x, area.y, area.w, area.h, this);
      return r;
    };
  })();
  var PatternFunctions = class {
    constructor(density = 0.2, rt = window) {
      __publicField(this, "density");
      __publicField(this, "rt");
      this.density = density;
      this.rt = rt;
    }
    /**
     * Noise pattern
     * patternColors()[0]   base color
     * patternColors()[1]   dot color
     * @param {Number} _density  Density of dots. default = 0.2
     * Constrained between 0 and 1.
     */
    noise(_density) {
      const outerP5 = this.rt;
      const outerDensity = _density || this.density;
      const func = function(_w, _h, _rt) {
        const rt = _rt || outerP5;
        const density = rt.constrain(outerDensity, 0, 1);
        const c = rt.patternColors();
        const num = _w * _h * density;
        const ns = 0.01;
        rt.ellipseMode(rt.CENTER);
        rt.rectMode(rt.CORNER);
        rt.noStroke();
        rt.fill(c[0]);
        rt.rect(0, 0, _w, _h);
        rt.fill(c[1 % c.length]);
        for (let i = 0; i < num; i++) {
          const x = rt.random(_w);
          const y = rt.random(_h);
          const dia = rt.noise(x * ns, y * ns) * 0.5 + 1;
          rt.ellipse(x, y, dia, dia);
        }
      };
      return func;
    }
    /**
     * Noise gradient pattern
     * patternColors()[0]   base color
     * patternColors()[1]   dot color
     * @param {Number} _density  Density of dots. default = 0.2
     */
    noiseGrad(_density) {
      const outerP5 = this.rt;
      const outerDensity = _density || this.density;
      const func = function(_w, _h, _rt = window) {
        const rt = _rt || outerP5;
        const density = _rt.min(1, outerDensity);
        const c = _rt.patternColors();
        const num = _w * _h * density;
        const ns = 0.01;
        _rt.rectMode(_rt.CORNER);
        _rt.ellipseMode(_rt.CENTER);
        _rt.noStroke();
        _rt.fill(c[0]);
        _rt.rect(0, 0, _w, _h);
        _rt.fill(c[1 % c.length]);
        for (let i = 0; i < num; i++) {
          const x = _rt.abs(_rt.randomGaussian()) / 5 * _w;
          const y = _rt.random(_h);
          const dia = _rt.noise(x * ns, y * ns) * 0.5 + 1;
          _rt.ellipse(x, y, dia, dia);
        }
      };
      return func;
    }
    /**
     * Stripe pattern
     * Fill the colors of patternColors() in order.
     * @param {Number} _space   Stripe space. default = 10
     */
    stripe(_space = 10) {
      const func = function(_w, _h, _rt = window) {
        _space = Math.abs(_space);
        if (_space == 0) _space = 10;
        const c = _rt.patternColors();
        _rt.rectMode(_rt.CORNER);
        _rt.noStroke();
        let count = 0;
        for (let x = 0; x <= _w + _space; x += _space) {
          _rt.fill(c[count % c.length]);
          _rt.rect(x, 0, Math.ceil(_space), _h);
          count++;
        }
      };
      return func;
    }
    /**
     * Concentric circle stripe pattern.
     * Fill the colors of patternColors() in order.
     * @param {Number} _space      Stripe space. default = 10
     * @param {Number} _minRadius  Minimum radius. default = 0
     */
    stripeCircle(_space = 25, _minRadius = 0) {
      const func = function(_w, _h, _rt = window) {
        _space = _rt.abs(_space);
        if (_space == 0) _space = 25;
        const c = _rt.patternColors();
        const maxRadius = _rt.sqrt(_w * _w + _h * _h);
        const num = _rt.ceil((maxRadius - _minRadius) / _space);
        _rt.ellipseMode(_rt.CENTER);
        _rt.noStroke();
        for (let i = 0; i < num; i++) {
          _rt.fill(c[i % c.length]);
          const radius = _minRadius + (num - 1 - i) * _space;
          _rt.circle(_w / 2, _h / 2, radius * 2);
        }
      };
      return func;
    }
    /**
     * Concentric polygon stripe pattern.
     * @param {Number} _vertNum     Number of vertices in a polygon,
     *                              constrained between 3 and 20.    default = 3
     * @param {Number} _space       Stripe space. default = 10
     * @param {Number} _minRadius   Minimum radius. default = 0
     */
    stripePolygon(_vertNum = 3, _space = 25, _minRadius = 0) {
      const func = function(_w, _h, _rt = window) {
        _space = _rt.abs(_space);
        if (_space == 0) _space = 25;
        const vNum = _rt.int(_rt.constrain(_vertNum, 3, 30));
        const c = _rt.patternColors();
        const maxRadius = _rt.sqrt(_w * _w + _h * _h);
        const num = _rt.ceil((maxRadius - _minRadius) / _space);
        _rt.noStroke();
        for (let i = 0; i < num; i++) {
          _rt.fill(c[i % c.length]);
          const radius = _minRadius + (num - 1 - i) * _space;
          _rt.beginShape();
          for (let i2 = 0; i2 < vNum; i2++) {
            const rad = i2 * Math.PI * 2 / vNum;
            const x = _w / 2 + Math.cos(rad) * radius;
            const y = _h / 2 + Math.sin(rad) * radius;
            _rt.vertex(x, y);
          }
          _rt.endShape(_rt.CLOSE);
        }
      };
      return func;
    }
    /**
     * Radial stripe pattern.
     * @param {Number} _angleSpan   Stripe angle space. default = PI / 4,
     * specified in radians or degrees, depending on current angleMode
     */
    stripeRadial(_angleSpan = 1) {
      const func = function(_w, _h, _rt = window) {
        _angleSpan = _rt.abs(_angleSpan);
        if (_angleSpan == 0) _angleSpan = 1;
        const c = _rt.patternColors();
        const tau = _rt._angleMode == _rt.DEGREES ? 360 : _rt.TAU;
        _rt.ellipseMode(_rt.CENTER);
        _rt.noStroke();
        let count = 0;
        const dia = _rt.sqrt(_w * _w + _h * _h);
        for (let r = 0; r < tau; r += _angleSpan) {
          const endRad = r + _angleSpan > tau ? 1e-5 : r + _angleSpan;
          _rt.fill(c[count % c.length]);
          _rt.arc(_w / 2, _h / 2, dia, dia, r, endRad + 1e-4);
          count++;
        }
      };
      return func;
    }
    /**
     * Wave pattern
     * patternColors()[0]       base color
     * patternColors()[1]       wave color
     * @param {Number} _waveW   Wave width. default = 100
     * @param {Number} _waveH   Wave height. default = 20
     * @param {Number} _space   Line spacing. default = 20
     * @param {Number} _weight  Line weight. default = 5
     */
    wave(_waveW = 100, _waveH = 10, _space = 20, _weight = 5) {
      const func = function(_w, _h, _rt = window) {
        _space = _rt.abs(_space);
        if (_space == 0) _space = 20;
        _waveW = _rt.abs(_waveW);
        if (_waveW == 0) _waveW = 100;
        const c = _rt.patternColors();
        const vertSpan = 3;
        _rt.rectMode(_rt.CORNER);
        _rt.noStroke();
        _rt.fill(c[0]);
        _rt.rect(0, 0, _w, _h);
        _rt.fill(c[1]);
        for (let y = -_waveH; y <= _h + _waveH; y += _space) {
          _rt.beginShape();
          for (let x = 0; x < _w; x += vertSpan) {
            const rad = x / _waveW * _rt.TAU;
            _rt.vertex(x, y + Math.sin(rad) * _waveH);
          }
          _rt.vertex(_w, y + Math.sin(_w / _waveW * Math.PI * 2) * _waveH);
          for (let x = _w; x > 0; x -= vertSpan) {
            const rad = x / _waveW * Math.PI * 2;
            _rt.vertex(x, y + _weight + Math.sin(rad) * _waveH);
          }
          _rt.vertex(0, y + _weight + Math.sin(0) * _waveH);
          _rt.endShape(_rt.CLOSE);
        }
      };
      return func;
    }
    /*
      Private function.
      Generate tiling pattern functions.
      */
    _customTiling(_spaceX, _spaceY, _tileFunc, _useOffset = false) {
      const func = function(_w, _h, _rt) {
        _spaceX = _rt.abs(_spaceX);
        if (_spaceX == 0) _spaceX = 50;
        _spaceY = _rt.abs(_spaceY);
        if (_spaceY == 0) _spaceY = 50;
        const c = _rt.patternColors();
        _rt.rectMode(_rt.CORNER);
        _rt.noStroke();
        _rt.fill(c[0]);
        _rt.rect(0, 0, _w, _h);
        let yi = 0;
        _rt.fill(c[1]);
        for (let y = 0; y <= _h + _spaceY / 2; y += _spaceY) {
          let xi = 0;
          let offset = yi % 2 == 1 && _useOffset ? -_spaceX / 2 : 0;
          for (let x = offset; x <= _w + _spaceX / 2; x += _spaceX) {
            _rt.push();
            _rt.translate(x, y);
            _tileFunc(_rt, xi, yi);
            _rt.pop();
            xi++;
          }
          yi++;
        }
      };
      return func;
    }
    /**
     * Dot pattern
     * patternColors()[0]       base color
     * patternColors()[1]       Checked color
     * @param {Number} _space   Dot spacing. default = 15
     * @param {Number} _dia     Dot diameter. default = 15
     */
    dot(_space = 15, _dia = 7) {
      const func = this._customTiling(
        _space,
        _space,
        function(_rt) {
          _rt.noStroke();
          _rt.ellipseMode(_rt.CENTER);
          _rt.circle(0, 0, _dia);
        },
        false
      );
      return func;
    }
    /**
     * Checked pattern
     * patternColors()[0]       base color
     * patternColors()[1]       Checked color
     * @param {Number} _checkW    Width of checkered pattern. default = 10
     * @param {Number} _checkH    Height of checkered pattern (Optional)
     */
    checked(w = 10, h = 10) {
      if (w && !h) h = w;
      const func = this._customTiling(
        w * 2,
        h,
        function(_rt) {
          _rt.noStroke();
          _rt.rectMode(_rt.CORNER);
          _rt.rect(0, 0, w, h);
        },
        true
      );
      return func;
    }
    /**
     * Cross pattern
     * patternColors()[1]       base color
     * patternColors()[0]       line color
     * @param {Number} _space   Line spacing. default = 20
     * @param {Number} _weight  Line weight. default = 5
     */
    cross(_space = 20, _weight = 5) {
      const func = function(_w, _h, _rt = window) {
        const c = _rt.patternColors();
        _rt.rectMode(_rt.CORNER);
        _rt.fill(c[0]);
        _rt.rect(0, 0, _w, _h);
        _rt.fill(c[1 % c.length]);
        for (let y = 0; y < _h; y += _space) {
          _rt.rect(0, y + _space / 2 - _weight / 2, _w, _weight);
        }
        for (let x = 0; x < _w; x += _space) {
          _rt.rect(x + _space / 2 - _weight / 2, 0, _weight, _h);
        }
      };
      return func;
    }
    /**
     * Triangle pattern
     * patternColors()[0]       base color
     * patternColors()[1]       line color
     * @param {Number} _triW  Triangle width. default = 20
     * @param {Number} _triH  Triangle height. default = 20
     */
    triangle(_triW = 20, _triH = 20) {
      const func = this._customTiling(
        _triW,
        _triH,
        function(_rt) {
          _rt.noStroke();
          _rt.triangle(0, 0, _triW, 0, _triW / 2, _triH);
        },
        true
      );
      return func;
    }
  };

  // sketches/art/lib/site.ts
  function getSetupParams(sketchName) {
    const outerElement = document.getElementById(sketchName);
    let h = 800;
    let w = 800;
    if (outerElement) {
      h = outerElement.getAttribute("data-height") ? parseInt(outerElement.getAttribute("data-height"), 10) : 800;
      w = outerElement.getAttribute("data-width") ? parseInt(outerElement.getAttribute("data-width"), 10) : 800;
    } else {
      console.warn(`No element found with id ${sketchName}`);
    }
    const params = {
      height: h,
      width: w,
      smaller: Math.min(h, w)
    };
    console.table({
      name: "Sketch Params",
      ...params
    });
    return params;
  }
  function setupSketch(sketchName, p) {
    const params = getSetupParams(sketchName);
    p.createCanvas(params.width, params.height);
    window.p5Instance = p;
    return params;
  }

  // sketches/art/lines-with-patterns.ts
  var NAME = "lines-with-patterns";
  var sketch = (p) => {
    let colors = chromatomeColors();
    const lines = [];
    const linesNum = 60;
    const DIST = 10;
    let MAX;
    const GEN = 30;
    let stColor;
    let sketchParams;
    let running = true;
    p.setup = () => {
      sketchParams = setupSketch(NAME, p);
      MAX = sketchParams.smaller;
      p.angleMode(p.DEGREES);
      stColor = colors.next();
      for (let i = 0; i < linesNum; i++) {
        lines.push(new MyLine());
      }
      p.frameRate(30);
      console.log("setup complete");
    };
    p.keyPressed = (key) => {
      if (key.key === "r") {
        p.noLoop();
        console.log("redrawing");
        colors = chromatomeColors();
        p.background(colors.background());
        p.draw();
        if (running) {
          p.loop();
        }
      } else if (key.key === " ") {
        running = !running;
        if (running) {
          p.loop();
        } else {
          p.noLoop();
        }
      }
    };
    p.mousePressed = () => {
      const { height, width } = sketchParams;
      if (p.mouseX > 0 && p.mouseX < width && p.mouseY > 0 && p.mouseY < height) {
        const fs = p.fullscreen();
        p.fullscreen(!fs);
      }
    };
    p.draw = () => {
      const { width, height } = sketchParams;
      const bgColor = colors.background();
      p.background(bgColor);
      p.noStroke();
      for (let i = 0; i < lines.length; i++) {
        p.push();
        p.translate(width / 2, height / 2);
        p.rotate(360 * i / lines.length);
        lines[i].display();
        p.pop();
      }
      p.fill(bgColor);
      p.stroke(stColor);
      p.strokeWeight(10);
      p.circle(width / 2, height / 2, MAX * 0.2);
    };
    class MyLine {
      constructor() {
        __publicField(this, "objs");
        __publicField(this, "speed");
        __publicField(this, "h");
        this.objs = [];
        this.speed = p.random(3, 6);
        this.h = p.random(2, 10);
      }
      display() {
        if (p.random(100) < GEN) {
          if (this.objs.length == 0 || this.objs.length > 0 && this.objs[this.objs.length - 1].hasDistance()) {
            this.objs.push(new Obj(this.speed, this.h));
          }
        }
        for (let i = 0; i < this.objs.length; i++) {
          this.objs[i].move();
          this.objs[i].display();
        }
        if (this.objs.length > 0) {
          for (let j = this.objs.length - 1; j >= 0; j--) {
            if (this.objs[j].isFinished()) {
              this.objs.splice(j, 1);
            }
          }
        }
      }
    }
    class Obj {
      constructor(tmpSpeed, tmpH) {
        __publicField(this, "x");
        __publicField(this, "y");
        __publicField(this, "speed");
        __publicField(this, "w");
        __publicField(this, "h");
        __publicField(this, "c");
        __publicField(this, "pc");
        __publicField(this, "patternFuncs");
        this.x = 0;
        this.y = 0;
        this.speed = tmpSpeed;
        this.w = p.random(10, 100);
        this.h = tmpH;
        this.c = colors.next();
        this.pc = colors.next(3);
        this.patternFuncs = new PatternFunctions(0.2);
      }
      move() {
        this.x -= this.speed;
      }
      isFinished() {
        return this.x < -MAX * 0.6 - this.w;
      }
      hasDistance() {
        return this.x < -(this.w + DIST);
      }
      display() {
        p.fill(this.c);
        p.pattern(this.patternFuncs.stripe(20));
        p.patternColors(this.pc);
        p.rectPattern(this.x, this.y, this.w, this.h, this.h / 2);
      }
    }
  };
  var p5sketch = new p5(
    sketch,
    document.getElementById(NAME)
  );
})();
