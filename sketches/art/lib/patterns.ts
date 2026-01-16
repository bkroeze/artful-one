// p5.Pattern
// MIT License
// Copyright (c) 2021 Taichi Sayama
// A pattern drawing library for p5.js.

export class PatternController {
  x: number;
  y: number;
  w: number;
  h: number;
  colors: string[];
  angle: number;
  patternFunction: ((w: number, h: number, rt: p5) => void) | null;
  renderTarget: p5 | null;

  constructor() {
    this.x = 0;
    this.y = 0;
    this.w = 0;
    this.h = 0;
    this.colors = ["#FFFFFF", "#000000"];
    this.angle = 0;
    this.patternFunction = null;
    this.renderTarget = null;
  }

  patternAngle(_angle: number): number {
    if (typeof _angle === "number") this.angle = _angle;
    return this.angle;
  }

  setPatternFunction(
    _func: (w: number, h: number, rt: p5) => void,
  ): boolean | ((w: number, h: number, rt: p5) => void) {
    if (typeof _func !== "function") return false;
    this.patternFunction = _func;
    return this.patternFunction;
  }

  applyPattern(
    _x: number,
    _y: number,
    _w: number,
    _h: number,
    _renderTarget: p5,
  ): void {
    this._setPatternArea(_x, _y, _w, _h);
    this._setRenderTarget(_renderTarget);
    this.renderTarget = _renderTarget;
    this._drawPattern();
  }

  patternColors(_colsArr: string[]): string[] {
    if (Array.isArray(_colsArr)) this.colors = _colsArr;
    return this.colors.slice(0, this.colors.length);
  }

  private _setPatternArea(
    _x: number,
    _y: number,
    _w: number,
    _h: number,
  ): void {
    this.x = _x;
    this.y = _y;
    this.w = _w;
    this.h = _h;
  }

  private _setRenderTarget(_renderTarget: p5): void {
    this.renderTarget = _renderTarget;
  }

  private _drawPattern(): void {
    const rt = this.renderTarget!;
    const func = typeof this.patternFunction === "function"
      ? this.patternFunction
      : this._flatFill();
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

  private _rotatedFuncGen(
    _ptnFunc: (w: number, h: number, rt: p5) => void,
    _angle: number,
  ): (w: number, h: number, rt: p5) => void {
    const func = function (_w: number, _h: number, _rt: p5) {
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

  private _flatFill(): (w: number, h: number, rt: p5) => void {
    const c = this.patternColors(this.colors);

    return function (_w: number, _h: number, _rt: p5) {
      _rt.rectMode(_rt.CORNER);
      _rt.fill(c[0]);
      _rt.noStroke();
      _rt.rect(0, 0, _w, _h);
    };
  }
}

export class PatternVertexInfo {
  verticies: [number, number][];
  isCurve: boolean;
  curveAreaMult: number;

  constructor() {
    this.verticies = [];
    this.isCurve = false;
    this.curveAreaMult = 1.25;
  }

  reset(): void {
    this.verticies = [];
    this.isCurve = false;
  }

  addVertex(x: number, y: number): void {
    this.verticies.push([x, y]);
  }

  addCurveVertex(x: number, y: number): void {
    this.addVertex(x, y);
    this.isCurve = true;
  }

  addBezierVertex(
    x2: number,
    y2: number,
    x3: number,
    y3: number,
    x4: number,
    y4: number,
  ): void {
    this.addVertex(x2, y2);
    this.addVertex(x3, y3);
    this.addVertex(x4, y4);
  }

  addQuadraticVertex(cx: number, cy: number, x3: number, y3: number): void {
    this.addVertex(cx, cy);
    this.addVertex(x3, y3);
  }

  culclateArea(): { x: number; y: number; w: number; h: number } {
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

    const area = { x: x, y: y, w: w, h: h };

    return area;
  }
}

// ---------------------------------------------------------------------------
// p5 extentions
// ---------------------------------------------------------------------------

p5.prototype._patternController = new PatternController();
p5.Graphics.prototype._patternController = new PatternController();

p5.prototype._patternVertexInfo = new PatternVertexInfo();
p5.Graphics.prototype._patternVertexInfo = new PatternVertexInfo();

/**
 * Function to change the amount of pattern rotation.
 * Use patternAngle() to check current angle.
 * @param {Number} _angle  the angle of rotation,
 * specified in radians or degrees, depending on current angleMode
 */
p5.prototype.patternAngle = function (_angle: number): number {
  return this._patternController.patternAngle(_angle);
};

/**
 * Function to set the color palette of the pattern.
 * Use patternColors() to check current palette.
 * @param {Array} _colsArr
 */
p5.prototype.patternColors = function (_colsArr: string[]): string[] {
  return this._patternController.patternColors(_colsArr);
};

/**
 * Function to set the pattern
 * @param  {function} _func     Pattern drawing function.
 */
p5.prototype.pattern = function (
  _func: (w: number, h: number, rt: p5) => void,
): boolean | ((w: number, h: number, rt: p5) => void) {
  return this._patternController.setPatternFunction(_func);
};

// ---------------------------------------------------------------------------
//Shape functions

(function () {
  /*
	Functions to adjust coordinate data
	*/
  const _modeAdjust = function (
    a: number,
    b: number,
    c: number,
    d: number,
    mode: number,
  ) {
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

  /*
	Function to disable drawing of fills and stroke.
	*/
  const _disableColor = function (_renderTarget: p5) {
    _renderTarget.noStroke();
    _renderTarget.fill(255, 0);
  };

  // ---------------------------------------------------------------------------

  //rect
  p5.prototype.rectPattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.rect(...args);

    const val = _modeAdjust(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[3],
      this._renderer._rectMode,
    );

    this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);

    return r;
  };

  //square
  p5.prototype.squarePattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.square(...args);

    const val = _modeAdjust(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[2],
      this._renderer._rectMode,
    );

    this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
    return r;
  };

  //ellipse
  p5.prototype.ellipsePattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.ellipse(...args);

    const val = _modeAdjust(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[3],
      this._renderer._ellipseMode,
    );

    this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
    return r;
  };

  //arc
  p5.prototype.arcPattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.arc(...args);

    const val = _modeAdjust(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[3],
      this._renderer._ellipseMode,
    );

    this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
    return r;
  };

  //circle
  p5.prototype.circlePattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.circle(...args);

    const val = _modeAdjust(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[2],
      this._renderer._ellipseMode,
    );
    this._patternController.applyPattern(val.x, val.y, val.w, val.h, this);
    return r;
  };

  //triangle
  p5.prototype.trianglePattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.triangle(...args);

    //Calculates the drawing area of the pattern with the center of gravity.
    const cx = (arguments[0] + arguments[2] + arguments[4]) / 3;
    const cy = (arguments[1] + arguments[3] + arguments[5]) / 3;
    const w =
      this.max([
        Math.abs(cx - arguments[0]),
        Math.abs(cx - arguments[2]),
        Math.abs(cx - arguments[4]),
      ]) * 2;
    const h =
      this.max([
        Math.abs(cy - arguments[1]),
        Math.abs(cy - arguments[3]),
        Math.abs(cy - arguments[5]),
      ]) * 2;
    this._patternController.applyPattern(cx - w / 2, cy - h / 2, w, h, this);

    //Calculates center position.(Not used)
    /*
		const minX = min(min(arguments[0], arguments[2]), arguments[4]);
		const maxX = max(max(arguments[0], arguments[2]), arguments[4]);
		const minY = min(min(arguments[1], arguments[3]), arguments[5]);
		const maxY = max(max(arguments[1], arguments[3]), arguments[5]);
		*/
    return r;
  };

  //quad
  p5.prototype.quadPattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.quad(...args);

    const minX = this.min([
      arguments[0],
      arguments[2],
      arguments[4],
      arguments[6],
    ]);
    const maxX = this.max([
      arguments[0],
      arguments[2],
      arguments[4],
      arguments[6],
    ]);
    const minY = this.min([
      arguments[1],
      arguments[3],
      arguments[5],
      arguments[7],
    ]);
    const maxY = this.max([
      arguments[1],
      arguments[3],
      arguments[5],
      arguments[7],
    ]);

    this._patternController.applyPattern(
      minX,
      minY,
      maxX - minX,
      maxY - minY,
      this,
    );
    return r;
  };

  //vertex
  p5.prototype.beginShapePattern = function (...args: any[]) {
    const r = this.beginShape(...args);
    this._patternVertexInfo.reset();
    return r;
  };

  p5.prototype.beginContourPattern = function (...args: any[]) {
    return this.beginContour(...args);
  };

  p5.prototype.vertexPattern = function (...args: any[]) {
    const r = this.vertex(...args);
    this._patternVertexInfo.addVertex(arguments[0], arguments[1]);
    return r;
  };

  p5.prototype.curveVertexPattern = function (...args: any[]) {
    const r = this.curveVertex(...args);
    this._patternVertexInfo.addCurveVertex(arguments[0], arguments[1]);
    return r;
  };

  p5.prototype.bezierVertexPattern = function (...args: any[]) {
    const r = this.bezierVertex(...args);
    this._patternVertexInfo.addBezierVertex(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[3],
      arguments[4],
      arguments[5],
    );
    return r;
  };

  p5.prototype.quadraticVertexPattern = function (...args: any[]) {
    const r = this.quadraticVertex(...args);
    this._patternVertexInfo.addQuadraticVertex(
      arguments[0],
      arguments[1],
      arguments[2],
      arguments[3],
    );
    return r;
  };

  p5.prototype.endContourPattern = function (...args: any[]) {
    return this.endContour(...args);
  };

  p5.prototype.endShapePattern = function (...args: any[]) {
    _disableColor(this);
    const r = this.endShape(...args);
    const area = this._patternVertexInfo.culclateArea();
    this._patternController.applyPattern(area.x, area.y, area.w, area.h, this);
    return r;
  };
})();

// ---------------------------------------------------------------------------
// Pattern functions.
// ---------------------------------------------------------------------------

type TileFunction = (rt: p5, xi: number, yi: number) => void;

export class PatternFunctions {
  density: number;
  rt: any;

  constructor(density: number = 0.2, rt: p5 = window) {
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
  noise(_density?: number) {
    const outerP5 = this.rt;
    const outerDensity = _density || this.density;
    const func = function (_w: number, _h: number, _rt: p5) {
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
  noiseGrad(_density?: number) {
    const outerP5 = this.rt;
    const outerDensity = _density || this.density;
    const func = function (_w: number, _h: number, _rt: p5 = window) {
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
  stripe(_space: number = 10) {
    const func = function (_w: number, _h: number, _rt: p5 = window) {
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
  stripeCircle(_space: number = 25, _minRadius: number = 0) {
    const func = function (_w: number, _h: number, _rt: p5 = window) {
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
  stripePolygon(
    _vertNum: number = 3,
    _space: number = 25,
    _minRadius: number = 0,
  ) {
    const func = function (_w: number, _h: number, _rt: p5 = window) {
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
        for (let i = 0; i < vNum; i++) {
          const rad = i * Math.PI * 2 / vNum;
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
  stripeRadial(_angleSpan: number = 1) {
    const func = function (_w: number, _h: number, _rt: p5 = window) {
      _angleSpan = _rt.abs(_angleSpan);
      if (_angleSpan == 0) _angleSpan = 1;

      const c = _rt.patternColors();
      const tau = _rt._angleMode == _rt.DEGREES ? 360 : _rt.TAU;

      _rt.ellipseMode(_rt.CENTER);
      _rt.noStroke();

      let count = 0;
      const dia = _rt.sqrt(_w * _w + _h * _h);
      for (let r = 0; r < tau; r += _angleSpan) {
        const endRad = r + _angleSpan > tau ? 0.00001 : r + _angleSpan;
        _rt.fill(c[count % c.length]);
        _rt.arc(_w / 2, _h / 2, dia, dia, r, endRad + 0.0001);
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
  wave(
    _waveW: number = 100,
    _waveH: number = 10,
    _space: number = 20,
    _weight: number = 5,
  ) {
    const func = function (_w: number, _h: number, _rt: p5 = window) {
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
  _customTiling(
    _spaceX: number,
    _spaceY: number,
    _tileFunc: TileFunction,
    _useOffset: boolean = false,
  ) {
    const func = function (_w: number, _h: number, _rt: p5) {
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
      function (_rt) {
        _rt.noStroke();
        _rt.ellipseMode(_rt.CENTER);
        _rt.circle(0, 0, _dia);
      },
      false,
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
  checked(w?: number = 10, h?: number = 10) {
    if (w && !h) h = w;

    const func = this._customTiling(
      w * 2,
      h,
      function (_rt) {
        _rt.noStroke();
        _rt.rectMode(_rt.CORNER);
        _rt.rect(0, 0, w, h);
      },
      true,
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
    const func = function (_w: number, _h: number, _rt = window) {
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
      function (_rt) {
        _rt.noStroke();
        _rt.triangle(0, 0, _triW, 0, _triW / 2, _triH);
      },
      true,
    );
    return func;
  }
}
