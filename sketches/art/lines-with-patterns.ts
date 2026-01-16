import { h } from "https://esm.sh/v128/preact@10.22.0/src/index.js";

import { chromatomeColors, ColorStack } from "./lib/colors.js";
import { PatternFunctions } from "./lib/patterns.ts";
import { setupSketch, SketchParams } from "./lib/site.ts";

const NAME = "lines-with-patterns";

export const sketch = (p: p5) => {
  let colors: ColorStack = chromatomeColors();
  const lines: MyLine[] = [];
  const linesNum: number = 60;

  const DIST: number = 10;
  let MAX: number;
  const GEN: number = 30;

  let stColor: string;

  let sketchParams: SketchParams;
  let running: boolean = true;

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
    objs: Obj[];
    speed: number;
    h: number;

    constructor() {
      this.objs = [];
      this.speed = p.random(3, 6);
      this.h = p.random(2, 10);
    }

    display(): void {
      if (p.random(100) < GEN) {
        if (
          (this.objs.length == 0) ||
          (this.objs.length > 0 &&
            this.objs[this.objs.length - 1].hasDistance())
        ) {
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
    x: number;
    y: number;
    speed: number;
    w: number;
    h: number;
    c: p5.Color;
    pc: string[];
    patternFuncs: any;

    constructor(tmpSpeed: number, tmpH: number) {
      this.x = 0;
      this.y = 0;
      this.speed = tmpSpeed;
      this.w = p.random(10, 100);
      this.h = tmpH;
      this.c = colors.next();
      this.pc = colors.next(3);
      this.patternFuncs = new PatternFunctions(0.2);
    }

    move(): void {
      this.x -= this.speed;
    }

    isFinished(): boolean {
      return this.x < -MAX * 0.6 - this.w;
    }

    hasDistance(): boolean {
      return this.x < -(this.w + DIST);
    }

    display(): void {
      p.fill(this.c);
      p.pattern(this.patternFuncs.stripe(20));
      p.patternColors(this.pc);
      p.rectPattern(this.x, this.y, this.w, this.h, this.h / 2);
    }
  }
};

export const p5sketch = new p5(
  sketch,
  document.getElementById(NAME) as HTMLElement,
);
