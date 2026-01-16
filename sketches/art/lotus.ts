import { chromatomeColors, ColorStack } from "./lib/colors.js";
import { getSetupParams, SketchParams } from "./lib/site.ts";

const NAME = "lotus";

// --- main
export const sketch = (p: p5) => {
  let sketchParams: SketchParams;
  let colors: ColorStack;
  let span: number;

  p.setup = () => {
    sketchParams = getSetupParams(NAME);
    const { width, height } = sketchParams;
    p.createCanvas(width, height);
    colors = chromatomeColors();
    p.background(colors.background());
    const smaller: number = Math.min(height, width);
    span = smaller / 4.25;
    const frameSpeed: number = Math.floor(Math.random() * 10) + 7;
    p.frameRate(frameSpeed);
  };

  let running: boolean = true;

  p.keyPressed = (code: number) => {
    console.log("code", code);
    if (!running) {
      running = true;
      p.loop();
    } else {
      running = false;
      p.noLoop();
    }
  };

  p.draw = () => {
    p.clear();
    colors.reset();
    const { height, width } = sketchParams;
    p.translate(width / 2, height / 2);
    drawAll(span, p.frameCount % (40 * Math.PI));
  };

  p.keyPressed = (key: KeyboardEvent) => {
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

  function SawTooth(
    span: number,
    teeth: number,
    fg: string,
    triangleWidth: number,
  ): void {
    const increment = (2 * Math.PI) / teeth;
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

  function Lotus(
    x: number,
    y: number,
    span: number,
    petals: number,
    petalColor: string,
    innerColor: string,
    dotColor: string,
  ): void {
    p.push();
    p.translate(x, y);
    SawTooth(span, petals, petalColor, 2);
    const seg = Math.PI / petals;
    for (let i = 0; i < petals * 2; i++) {
      p.rotate(seg);
      p.fill(innerColor);
      p.circle(span / 4, 0, span / 12);
      p.triangle(span / 6, span / 16, span / 6, -span / 16, span / 3, 0);
      p.fill(dotColor);
      p.circle(span / 5, 0, span / 32);
    }
    p.noFill();
    p.strokeWeight(span / 48);
    p.stroke(petalColor);

    p.circle(0, 0, span / 3.1);
    p.pop();
  }

  function drawAll(span: number, r: number): void {
    let s1 = colors.next();
    let fg1 = colors.next();
    let fg2 = colors.next();
    //drawingContext.shadowBlur = 20;
    //drawingContext.shadowColor = colors.nextWithOpacity(0.8);
    Lotus(0, 0, span * 1.5, 6, s1, fg1, fg2);
    p.rotate(-r);
    s1 = colors.next();
    fg1 = colors.next();
    fg2 = colors.next();
    const s1b = colors.next();
    const fg1b = colors.next();
    const fg2b = colors.next();

    const seg = Math.PI / 6;
    for (let i = 0; i < 12; i++) {
      (i > 0) && p.rotate(seg);
      if (i % 2 === 0) {
        Lotus(span * 2, 0, span * 0.66, 8, s1b, fg1b, fg2b);
        p.stroke(s1);
        p.strokeWeight(span / 32);
        p.line(span * 0.8, 0, span * 1.6, 0);
        p.noStroke();
      } else {
        Lotus(span * 1.5, 0, span, 8, s1, fg1, fg2);
      }
    }
  }
};

export const p5sketch = new p5(
  sketch,
  document.getElementById(NAME) as HTMLElement,
);
