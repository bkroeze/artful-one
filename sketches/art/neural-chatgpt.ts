import { setupSketch, SketchParams } from "./lib/site.ts";

const NAME = "neural-chatgpt";

export const sketch = (p: p5) => {
  const nodes: Node[] = []; // Array to store nodes
  const connections: Connection[] = []; // Array to store connections
  let waveOffset = 0; // Wave animation offset
  let sketchParams: SketchParams;

  p.setup = () => {
    sketchParams = setupSketch(NAME, p);
    p.noStroke(); // No default stroke lines
    initializeNodes(12); // Initialize 12 nodes
    initializeConnections();
  };

  p.draw = () => {
    p.background(20, 24, 40); // Dark background for contrast
    waveOffset += 0.03; // Animate the wave

    // Animate nodes by moving them slightly
    nodes.forEach((n) => n.animate());

    // Draw connections and waves
    connections.forEach((c) => c.display());

    // Draw nodes
    nodes.forEach((n) => n.display());
  };

  // Initialize nodes at random positions
  function initializeNodes(count: number) {
    const { height, width } = sketchParams;
    for (let i = 0; i < count; i++) {
      const x = p.random(width * 0.2, width * 0.8);
      const y = p.random(height * 0.2, height * 0.8);
      const size = p.random(15, 30);
      nodes.push(new Node(x, y, size));
    }
  }

  // Initialize connections between random pairs of nodes
  function initializeConnections() {
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        if (p.random(1) > 0.5) { // Randomly decide whether to connect nodes
          connections.push(new Connection(nodes[i], nodes[j]));
        }
      }
    }
  }

  // Node class to represent individual points
  class Node {
    x: number;
    y: number;
    xSpeed: number;
    ySpeed: number;
    size: number;
    color: p5.Color;

    constructor(x, y, size) {
      this.x = x;
      this.y = y;
      this.size = size;
      this.color = p.color(p.random(150, 255), p.random(100, 200), 255, 200);
      this.xSpeed = p.random(-0.5, 0.5); // Horizontal movement speed
      this.ySpeed = p.random(-0.5, 0.5); // Vertical movement speed
    }

    display() {
      p.fill(this.color);
      p.noStroke();
      p.ellipse(this.x, this.y, this.size, this.size); // Draw a circle for the node
    }

    animate() {
      const { height, width } = sketchParams;
      // Move node slightly
      this.x += this.xSpeed;
      this.y += this.ySpeed;

      // Keep nodes within canvas boundaries
      if (this.x < 0 || this.x > width) this.xSpeed *= -1;
      if (this.y < 0 || this.y > height) this.ySpeed *= -1;
    }
  }

  // Connection class to represent links between nodes
  class Connection {
    nodeA: Node;
    nodeB: Node;
    waveSpeed: number;
    waveLength: number;
    color: p5.Color;

    constructor(nodeA: Node, nodeB: Node) {
      this.nodeA = nodeA;
      this.nodeB = nodeB;
      this.waveSpeed = p.random(0.02, 0.05); // Speed of the wave animation
      this.waveLength = p.random(20, 60); // Length of the wave
      this.color = p.color(255, p.random(150, 200), p.random(150, 200), 180);
    }

    display() {
      p.stroke(this.color);
      p.strokeWeight(2);

      // Draw the main connection line
      p.line(this.nodeA.x, this.nodeA.y, this.nodeB.x, this.nodeB.y);

      // Draw the wave animation on the connection
      const waveAmplitude = 8; // Wave height
      const segments = 50; // Number of points to draw the wave

      p.noFill();
      p.beginShape();
      for (let i = 0; i <= segments; i++) {
        let t = i / segments; // Normalize t between 0 and 1
        let x = p.lerp(this.nodeA.x, this.nodeB.x, t);
        let y = p.lerp(this.nodeA.y, this.nodeB.y, t);
        y +=
          p.sin(p.TWO_PI * t * this.waveLength + waveOffset * this.waveSpeed) *
          waveAmplitude;
        p.vertex(x, y);
      }
      p.endShape();
    }
  }
};

export const p5sketch = new p5(
  sketch,
  document.getElementById(NAME) as HTMLElement,
);
