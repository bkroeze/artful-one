import { setupSketch, SketchParams } from "./lib/site.ts";

const NAME = "neural-claude";
interface Point {
  position: p5.Vector;
  velocity: p5.Vector;
  activation: number;
}

interface Connection {
  p1: Point;
  p2: Point;
  strength: number;
}

export const sketch = (p: p5) => {
  const points: Point[] = [];
  let connections: Connection[] = [];
  const numPoints = 100;
  const connectionThreshold = 100;
  const fadeSpeed = 3;

  let sketchParams: SketchParams;

  p.setup = () => {
    sketchParams = setupSketch(NAME, p);
    const { width, height } = sketchParams;
    p.background(10);
    console.log("setup start");

    // Create initial points representing neural nodes
    for (let i = 0; i < numPoints; i++) {
      points.push({
        position: p.createVector(p.random(width), p.random(height)),
        velocity: p5.Vector.random2D().mult(0.5),
        activation: p.random(1),
      });
    }
    console.log("setup complete");
  };

  p.draw = () => {
    // Fade effect for trailing
    p.fill(10, fadeSpeed);
    p.noStroke();
    const { width, height } = sketchParams;
    p.rect(0, 0, width, height);

    // Update points
    points.forEach((point) => {
      // Update position with slight random movement
      point.position.add(point.velocity);
      point.velocity.rotate(p.random(-0.1, 0.1));

      // Bounce off edges
      if (point.position.x < 0 || point.position.x > width) {
        point.velocity.x *= -1;
      }
      if (point.position.y < 0 || point.position.y > height) {
        point.velocity.y *= -1;
      }

      // Randomly update activation
      point.activation += p.random(-0.05, 0.05);
      point.activation = p.constrain(point.activation, 0, 1);
    });

    // Draw connections
    connections = [];
    for (let i = 0; i < points.length; i++) {
      for (let j = i + 1; j < points.length; j++) {
        let d = p5.Vector.dist(points[i].position, points[j].position);
        if (d < connectionThreshold) {
          connections.push({
            p1: points[i],
            p2: points[j],
            strength: p.map(d, 0, connectionThreshold, 1, 0),
          });
        }
      }
    }

    // Draw connections first
    connections.forEach((conn) => {
      const alpha = conn.strength * 255 * conn.p1.activation *
        conn.p2.activation;
      p.stroke(100, 200, 255, alpha);
      p.strokeWeight(conn.strength * 2);
      p.line(
        conn.p1.position.x,
        conn.p1.position.y,
        conn.p2.position.x,
        conn.p2.position.y,
      );
    });

    // Draw points
    points.forEach((point) => {
      const size = p.map(point.activation, 0, 1, 2, 6);
      p.noStroke();
      p.fill(200, 255, 255, point.activation * 255);
      p.circle(point.position.x, point.position.y, size);
    });
  };
};

export const p5sketch = new p5(
  sketch,
  document.getElementById(NAME) as HTMLElement,
);
