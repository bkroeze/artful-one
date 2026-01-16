import { chromatomeColors, ColorStack } from "./lib/colors.js";
import { setupSketch, SketchParams } from "./lib/site.ts";

const NAME = "sawtooth";

export const sketch = (p: p5) => {
  let colors: ColorStack;
  let bg: string;
  let fg: string;
  let fg2: string;

  let sketchParams: SketchParams;

  p.setup = () => {
    sketchParams = setupSketch(NAME, p);
    colors = chromatomeColors();
    p.background(colors.background());
    console.log("setup complete");
  };

  p.keyPressed = (key: KeyboardEvent) => {
    if (key.key === "r") {
      console.log("redrawing");
      colors = chromatomeColors();
      p.background(colors.background());
      p.draw();
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
    p.noLoop();
    p.blendMode(p.BLEND);
    const span = Math.floor(sketchParams.height / 6);
    bg = colors.background();
    fg = colors.next();
    fg2 = colors.next();
    for (let y = 0; y < sketchParams.height / span + 1; y++) {
      for (let x = 0; x < sketchParams.width / span + 1; x++) {
        SawToothWithDoubleCircle(x * span, y * span, span, 30, bg, fg, 4);
        SawToothWithInnerCircle(
          x * span + span / 2,
          y * span + span / 2,
          span / 3,
          8,
          bg,
          fg,
          fg2,
          8,
        );
      }
    }
  };

  function SawToothWithDoubleCircle(
    x: number,
    y: number,
    span: number,
    teeth: number,
    bg: string,
    fg: string,
    triangleWidth: number = 4,
  ): void {
    p.push();
    p.translate(x, y);
    SawTooth(0, 0, span, teeth, bg, fg, triangleWidth);
    p.noFill();
    p.stroke(bg);
    p.strokeWeight(span / 18);
    p.circle(0, 0, span * 0.7);
    p.noStroke();
    p.fill(bg);
    p.circle(0, 0, span * 0.55);
    p.pop();
  }

  function SawToothWithInnerCircle(
    x: number,
    y: number,
    span: number,
    teeth: number,
    bg: string,
    fg: string,
    fg2: string,
    triangleWidth: number = 8,
  ): void {
    p.push();
    p.translate(x, y);
    SawTooth(0, 0, span, teeth, bg, fg2, triangleWidth);
    p.noStroke();
    p.fill(bg);
    p.circle(0, 0, span * 0.25);
    p.pop();
  }

  function SawTooth(
    x: number,
    y: number,
    span: number,
    teeth: number,
    bg: string,
    fg: string,
    triangleWidth: number,
  ): void {
    const increment = 2 * Math.PI / teeth;
    p.noStroke();
    p.fill(fg);
    for (let i = 0; i < teeth; i++) {
      i > 0 && p.rotate(increment);
      p.triangle(
        0,
        -span / triangleWidth,
        0,
        span / triangleWidth,
        span / 2,
        0,
      );
    }
  }
};

export const p5sketch = new p5(
  sketch,
  document.getElementById(NAME) as HTMLElement,
);
