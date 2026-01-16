(() => {
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

  // sketches/art/neural-claude.ts
  var NAME = "neural-claude";
  var sketch = (p) => {
    const points = [];
    let connections = [];
    const numPoints = 100;
    const connectionThreshold = 100;
    const fadeSpeed = 3;
    let sketchParams;
    p.setup = () => {
      sketchParams = setupSketch(NAME, p);
      const { width, height } = sketchParams;
      p.background(10);
      console.log("setup start");
      for (let i = 0; i < numPoints; i++) {
        points.push({
          position: p.createVector(p.random(width), p.random(height)),
          velocity: p5.Vector.random2D().mult(0.5),
          activation: p.random(1)
        });
      }
      console.log("setup complete");
    };
    p.draw = () => {
      p.fill(10, fadeSpeed);
      p.noStroke();
      const { width, height } = sketchParams;
      p.rect(0, 0, width, height);
      points.forEach((point) => {
        point.position.add(point.velocity);
        point.velocity.rotate(p.random(-0.1, 0.1));
        if (point.position.x < 0 || point.position.x > width) {
          point.velocity.x *= -1;
        }
        if (point.position.y < 0 || point.position.y > height) {
          point.velocity.y *= -1;
        }
        point.activation += p.random(-0.05, 0.05);
        point.activation = p.constrain(point.activation, 0, 1);
      });
      connections = [];
      for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
          let d = p5.Vector.dist(points[i].position, points[j].position);
          if (d < connectionThreshold) {
            connections.push({
              p1: points[i],
              p2: points[j],
              strength: p.map(d, 0, connectionThreshold, 1, 0)
            });
          }
        }
      }
      connections.forEach((conn) => {
        const alpha = conn.strength * 255 * conn.p1.activation * conn.p2.activation;
        p.stroke(100, 200, 255, alpha);
        p.strokeWeight(conn.strength * 2);
        p.line(
          conn.p1.position.x,
          conn.p1.position.y,
          conn.p2.position.x,
          conn.p2.position.y
        );
      });
      points.forEach((point) => {
        const size = p.map(point.activation, 0, 1, 2, 6);
        p.noStroke();
        p.fill(200, 255, 255, point.activation * 255);
        p.circle(point.position.x, point.position.y, size);
      });
    };
  };
  var p5sketch = new p5(
    sketch,
    document.getElementById(NAME)
  );
})();
