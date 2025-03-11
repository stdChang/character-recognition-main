"use client";
"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var react_1 = require("react");
var canvas_1 = require("./components/canvas");
var material_1 = require("@mui/material/");
var page_module_css_1 = require("./page.module.css");
var theme_1 = require("./components/theme");
var about_1 = require("./components/about");
function Home() {
    var isMobile = (0, material_1.useMediaQuery)(theme_1.theme.breakpoints.down("sm"));
    var primary_color = theme_1.theme.palette.primary;
    // setState for responsive frontend to any backend calls
    var _a = (0, react_1.useState)(""), tempMsg = _a[0], settempMsg = _a[1];
    var updateTempMsg = function (newMsg) {
        settempMsg(newMsg);
    };
    return (<material_1.ThemeProvider theme={theme_1.theme}>
      <material_1.Container>
        <material_1.Stack spacing={2} sx={{ height: "95%" }} padding={1} justifyContent="center">
          <material_1.Paper sx={{ backgroundColor: primary_color.light }}>
            <material_1.Typography variant="h3" margin={3} sx={{ textAlign: "center", fontFamily: "__Merienda_9ceaa0", fontWeight: "medium" }} className={page_module_css_1.default.heading}>
              ECS 170 Optical Character Recognition Demo
            </material_1.Typography>
          </material_1.Paper>
          <material_1.Stack direction={{ xs: "column", sm: "row" }} spacing={2} sx={{ height: "100%" }}>
            <canvas_1.default tempMsg={tempMsg} updateTempMsg={updateTempMsg}/>
            <material_1.Paper sx={{
            backgroundColor: primary_color.light,
            height: "400",
            padding: { xs: 0, sm: 2 },
            width: { xs: "100%", sm: "35%" }
        }}>
              <div style={isMobile
            ? {
                display: "flex",
                height: "100%",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center"
            }
            : { height: "100%" }}>
                <material_1.Typography variant="h4" sx={{
            textAlign: "center",
            height: "max-content",
            lineHeight: 2.75,
            fontFamily: "Inter",
            fontWeight: "regular"
        }}>
                  Predicted Word
                </material_1.Typography>
                <material_1.Box sx={{
            display: "flex",
            height: "80%",
            justifyContent: "center",
            alignItems: "center"
        }}>
                  <material_1.Typography variant="h4" sx={{ margin: "8px", fontFamily: "Inter", fontWeight: "regular" }}>
                    {tempMsg}
                  </material_1.Typography>
                </material_1.Box>
              </div>
            </material_1.Paper>
          </material_1.Stack>
          <about_1.default />
        </material_1.Stack>
      </material_1.Container>
    </material_1.ThemeProvider>);
}
exports.default = Home;
