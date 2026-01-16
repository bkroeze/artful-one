(() => {
  var __defProp = Object.defineProperty;
  var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
  var __publicField = (obj, key, value) => __defNormalProp(obj, typeof key !== "symbol" ? key + "" : key, value);

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

  // sketches/art/neural-chatgpt.ts
  var NAME = "neural-chatgpt";
  var sketch = (p) => {
    const nodes = [];
    const connections = [];
    let waveOffset = 0;
    let sketchParams;
    p.setup = () => {
      sketchParams = setupSketch(NAME, p);
      p.noStroke();
      initializeNodes(12);
      initializeConnections();
    };
    p.draw = () => {
      p.background(20, 24, 40);
      waveOffset += 0.03;
      nodes.forEach((n) => n.animate());
      connections.forEach((c) => c.display());
      nodes.forEach((n) => n.display());
    };
    function initializeNodes(count) {
      const { height, width } = sketchParams;
      for (let i = 0; i < count; i++) {
        const x = p.random(width * 0.2, width * 0.8);
        const y = p.random(height * 0.2, height * 0.8);
        const size = p.random(15, 30);
        nodes.push(new Node(x, y, size));
      }
    }
    function initializeConnections() {
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          if (p.random(1) > 0.5) {
            connections.push(new Connection(nodes[i], nodes[j]));
          }
        }
      }
    }
    class Node {
      constructor(x, y, size) {
        __publicField(this, "x");
        __publicField(this, "y");
        __publicField(this, "xSpeed");
        __publicField(this, "ySpeed");
        __publicField(this, "size");
        __publicField(this, "color");
        this.x = x;
        this.y = y;
        this.size = size;
        this.color = p.color(p.random(150, 255), p.random(100, 200), 255, 200);
        this.xSpeed = p.random(-0.5, 0.5);
        this.ySpeed = p.random(-0.5, 0.5);
      }
      display() {
        p.fill(this.color);
        p.noStroke();
        p.ellipse(this.x, this.y, this.size, this.size);
      }
      animate() {
        const { height, width } = sketchParams;
        this.x += this.xSpeed;
        this.y += this.ySpeed;
        if (this.x < 0 || this.x > width) this.xSpeed *= -1;
        if (this.y < 0 || this.y > height) this.ySpeed *= -1;
      }
    }
    class Connection {
      constructor(nodeA, nodeB) {
        __publicField(this, "nodeA");
        __publicField(this, "nodeB");
        __publicField(this, "waveSpeed");
        __publicField(this, "waveLength");
        __publicField(this, "color");
        this.nodeA = nodeA;
        this.nodeB = nodeB;
        this.waveSpeed = p.random(0.02, 0.05);
        this.waveLength = p.random(20, 60);
        this.color = p.color(255, p.random(150, 200), p.random(150, 200), 180);
      }
      display() {
        p.stroke(this.color);
        p.strokeWeight(2);
        p.line(this.nodeA.x, this.nodeA.y, this.nodeB.x, this.nodeB.y);
        const waveAmplitude = 8;
        const segments = 50;
        p.noFill();
        p.beginShape();
        for (let i = 0; i <= segments; i++) {
          let t = i / segments;
          let x = p.lerp(this.nodeA.x, this.nodeB.x, t);
          let y = p.lerp(this.nodeA.y, this.nodeB.y, t);
          y += p.sin(p.TWO_PI * t * this.waveLength + waveOffset * this.waveSpeed) * waveAmplitude;
          p.vertex(x, y);
        }
        p.endShape();
      }
    }
  };
  var p5sketch = new p5(
    sketch,
    document.getElementById(NAME)
  );
})();
