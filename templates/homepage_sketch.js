const canvas = document.getElementById("dandelion");
const ctx = canvas.getContext("2d");

const W = canvas.width;
const H = canvas.height;

const BG = "#f1d39d";
const stemBase = { x: 118, y: 172 };
const stemTop  = { x: 142, y: 82 };
const groundY = 178;

// timing
const totalCycles = 5;
const bloomDuration = 2.7;
const preReleaseHold = 0.7;
const releaseStart = bloomDuration + preReleaseHold; // 3.4
const releaseDuration = 4.65; // 50% longer than 3.1
const postReleaseHold = 2.4;
const cycleDuration = releaseStart + releaseDuration + postReleaseHold; // 10.45
const finalHold = 2.0;
const masterDuration = totalCycles * cycleDuration + finalHold;

const startTime = performance.now();

function clamp01(v) {
  return Math.max(0, Math.min(1, v));
}

function lerp(a, b, t) {
  return a + (b - a) * t;
}

function easeOutCubic(t) {
  return 1 - Math.pow(1 - t, 3);
}

function easeOutQuad(t) {
  return 1 - (1 - t) * (1 - t);
}

function quadBezier(p0, p1, p2, t) {
  const mt = 1 - t;
  return mt * mt * p0 + 2 * mt * t * p1 + t * t * p2;
}

function seedProgress(release, seed) {
  return clamp01((release - seed.detachAt) / seed.duration);
}

// precompute the paper wash so it does not flicker frame-to-frame
const paperWashes = Array.from({ length: 16 }, () => ({
  x: Math.random() * W,
  y: Math.random() * H,
  rx: 80 + Math.random() * 140,
  ry: 12 + Math.random() * 20,
  rot: Math.random() * Math.PI
}));

function makeCycleSeeds(cycleIndex, seedCount = 48) {
  return Array.from({ length: seedCount }, (_, i) => {
    const a = (Math.PI * 2 * i / seedCount) - Math.PI * 0.12;
    const r = 20 + Math.random() * 10;
    const groundSeed = Math.random() < 0.28;

    // gradually spread the ground accumulation farther right over cycles
    const cycleSpread = cycleIndex * 22;

    return {
      a,
      r,
      size: 0.88 + Math.random() * 0.34,
      spin: -0.16 + Math.random() * 0.32,
      jitter: Math.random() * 10,

      detachAt: 0.02 + Math.random() * 0.56,
      duration: groundSeed
        ? 0.22 + Math.random() * 0.20
        : 0.50 + Math.random() * 0.38,

      groundSeed,

      // airborne seeds
      offX: 290 + Math.random() * 450,
      arcUp: 14 + Math.random() * 28,
      driftDown: 12 + Math.random() * 40,

      // landed seeds
      landX: stemTop.x + 70 + cycleSpread + Math.random() * (220 + cycleSpread * 0.6),
      landY: groundY - 0.5 + Math.random() * 2.0,
      controlLift: 16 + Math.random() * 22,
      settleAngle: -0.55 + Math.random() * 1.1
    };
  });
}

const cycleSeeds = Array.from({ length: totalCycles }, (_, i) => makeCycleSeeds(i));

const windLines = Array.from({ length: 9 }, (_, i) => ({
  y: 48 + i * 12 + Math.random() * 5,
  x: -160 - Math.random() * 140,
  len: 90 + Math.random() * 90,
  amp: 1.6 + Math.random() * 2.4,
  speed: 0.48 + Math.random() * 0.28,
  phase: Math.random() * 10
}));

function drawBackground() {
  ctx.fillStyle = BG;
  ctx.fillRect(0, 0, W, H);

  ctx.save();
  for (const wash of paperWashes) {
    ctx.fillStyle = "rgba(255,255,250,0.025)";
    ctx.beginPath();
    ctx.ellipse(wash.x, wash.y, wash.rx, wash.ry, wash.rot, 0, Math.PI * 2);
    ctx.fill();
  }

  const grad = ctx.createLinearGradient(0, 0, W, 0);
  grad.addColorStop(0, "rgba(80,50,20,0.04)");
  grad.addColorStop(0.5, "rgba(255,255,255,0)");
  grad.addColorStop(1, "rgba(80,50,20,0.04)");
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, W, H);
  ctx.restore();
}

function drawPlateDetails() {
  ctx.save();

  ctx.strokeStyle = "rgba(95,70,40,0.22)";
  ctx.lineWidth = 0.8;
  ctx.strokeRect(12, 12, W - 24, H - 24);

  ctx.fillStyle = "rgba(90,65,38,0.55)";
  ctx.font = "12px serif";
  ctx.fillText("Taraxacum officinale", 618, 178);
  ctx.fillText("Plate IV", 26, 178);

  ctx.restore();
}

function drawGroundShadow() {
  ctx.save();

  ctx.fillStyle = "rgba(80,58,30,0.08)";
  ctx.beginPath();
  ctx.ellipse(stemBase.x + 2, stemBase.y + 4, 46, 6, 0, 0, Math.PI * 2);
  ctx.fill();

  const g = ctx.createLinearGradient(60, groundY - 10, 520, groundY + 10);
  g.addColorStop(0, "rgba(95,70,40,0)");
  g.addColorStop(0.18, "rgba(95,70,40,0.03)");
  g.addColorStop(0.58, "rgba(95,70,40,0.07)");
  g.addColorStop(1, "rgba(95,70,40,0)");
  ctx.fillStyle = g;
  ctx.beginPath();
  ctx.ellipse(280, groundY + 1.5, 250, 9, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.restore();
}

function drawStem(grow, sway) {
  const gx = lerp(stemBase.x, stemTop.x, grow);
  const gy = lerp(stemBase.y, stemTop.y, grow);

  ctx.save();
  ctx.lineCap = "round";

  ctx.strokeStyle = "#5d7149";
  ctx.lineWidth = 2.0;
  ctx.beginPath();
  ctx.moveTo(stemBase.x, stemBase.y);
  ctx.bezierCurveTo(
    stemBase.x - 10,
    stemBase.y - 28 * grow,
    stemTop.x - 7 + sway * 3,
    stemBase.y - 56 * grow,
    gx + sway * 2,
    gy
  );
  ctx.stroke();

  ctx.strokeStyle = "rgba(250,246,232,0.22)";
  ctx.lineWidth = 0.65;
  ctx.beginPath();
  ctx.moveTo(stemBase.x - 0.4, stemBase.y);
  ctx.bezierCurveTo(
    stemBase.x - 9,
    stemBase.y - 28 * grow,
    stemTop.x - 8 + sway * 3,
    stemBase.y - 56 * grow,
    gx + sway * 2 - 0.7,
    gy
  );
  ctx.stroke();

  ctx.restore();
}

function drawLeaves(grow) {
  ctx.save();
  ctx.globalAlpha = grow;

  function leaf(x, y, flip, scale) {
    ctx.save();
    ctx.translate(x, y);
    ctx.scale(flip, 1);

    ctx.fillStyle = "rgba(104,123,76,0.85)";
    ctx.strokeStyle = "rgba(78,97,56,0.95)";
    ctx.lineWidth = 1.0;

    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.bezierCurveTo(14 * scale, -4 * scale, 36 * scale, -10 * scale, 49 * scale, -22 * scale);
    ctx.bezierCurveTo(42 * scale, -18 * scale, 33 * scale, -27 * scale, 37 * scale, -35 * scale);
    ctx.bezierCurveTo(29 * scale, -31 * scale, 20 * scale, -38 * scale, 23 * scale, -46 * scale);
    ctx.bezierCurveTo(16 * scale, -42 * scale, 9 * scale, -35 * scale, 10 * scale, -28 * scale);
    ctx.bezierCurveTo(5 * scale, -21 * scale, 3 * scale, -14 * scale, 0, 0);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    ctx.strokeStyle = "rgba(248,244,232,0.22)";
    ctx.lineWidth = 0.7;
    ctx.beginPath();
    ctx.moveTo(1, -1);
    ctx.bezierCurveTo(10 * scale, -9 * scale, 23 * scale, -20 * scale, 42 * scale, -29 * scale);
    ctx.stroke();

    ctx.strokeStyle = "rgba(70,85,50,0.18)";
    ctx.lineWidth = 0.45;
    for (let i = 0; i < 5; i++) {
      const sx = 12 * scale + i * 5 * scale;
      const sy = -9 * scale - i * 3.2 * scale;
      ctx.beginPath();
      ctx.moveTo(sx, sy);
      ctx.lineTo(sx + 8 * scale, sy - 4 * scale);
      ctx.stroke();
    }

    ctx.restore();
  }

  leaf(114, 156, -1, 0.88);
  leaf(122, 142,  1, 0.62);

  ctx.restore();
}

function drawBracts(cx, cy, scale, alpha = 1) {
  ctx.save();
  ctx.translate(cx, cy);
  ctx.globalAlpha = alpha;
  ctx.strokeStyle = "#6f8257";
  ctx.fillStyle = "#7d9562";
  ctx.lineWidth = 0.85;

  for (let i = -3; i <= 3; i++) {
    const ang = Math.PI / 2 + i * 0.18;
    ctx.save();
    ctx.rotate(ang);
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.bezierCurveTo(2 * scale, 4 * scale, 4 * scale, 9 * scale, 0, 14 * scale);
    ctx.bezierCurveTo(-4 * scale, 9 * scale, -2 * scale, 4 * scale, 0, 0);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }

  ctx.restore();
}

function drawSeed(cx, cy, angle, scale, alpha = 1) {
  ctx.save();
  ctx.translate(cx, cy);
  ctx.rotate(angle);
  ctx.globalAlpha = alpha;

  ctx.fillStyle = "rgba(104,77,47,0.85)";
  ctx.beginPath();
  ctx.ellipse(0, 1.6 * scale, 0.95 * scale, 2.2 * scale, 0, 0, Math.PI * 2);
  ctx.fill();

  ctx.strokeStyle = "rgba(230,226,214,0.8)";
  ctx.lineWidth = 0.55;
  ctx.beginPath();
  ctx.moveTo(0, 0.2 * scale);
  ctx.lineTo(0, -10 * scale);
  ctx.stroke();

  ctx.strokeStyle = "rgba(252,250,246,0.9)";
  ctx.lineWidth = 0.52;
  for (let i = -3; i <= 3; i++) {
    ctx.beginPath();
    ctx.moveTo(0, -10 * scale);
    ctx.lineTo(i * 2.5 * scale, (-16 - Math.abs(i) * 0.85) * scale);
    ctx.stroke();
  }

  ctx.restore();
}

function drawAttachedHead(grow, release, t, sway, seeds) {
  const headScale = easeOutCubic(grow);
  const cx = stemTop.x + sway * 2;
  const cy = stemTop.y;

  const headAlpha = headScale * (1 - release);

  ctx.save();
  ctx.globalAlpha = 0.95 * headAlpha;
  ctx.fillStyle = "#8b6a3e";
  ctx.beginPath();
  ctx.arc(cx, cy, 4.5 * headScale, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();

  drawBracts(cx, cy + 3.3 * headScale, headScale * 0.8, headAlpha);

  for (const s of seeds) {
    const detachProgress = clamp01((release - s.detachAt) / 0.15);
    const attachedAlpha = headAlpha * (1 - detachProgress);
    if (attachedAlpha <= 0.002) continue;

    const rr = s.r * headScale;
    const x = cx + Math.cos(s.a) * rr + Math.sin(t * 1.2 + s.jitter) * 0.45;
    const y = cy + Math.sin(s.a) * rr + Math.cos(t * 1.15 + s.jitter) * 0.35;

    drawSeed(
      x,
      y,
      s.a + Math.PI / 2 + s.spin * t * 0.25,
      0.94 * s.size * headScale,
      attachedAlpha
    );
  }
}

function drawSettledSeed(seed) {
  ctx.save();

  ctx.fillStyle = "rgba(75,55,28,0.12)";
  ctx.beginPath();
  ctx.ellipse(seed.landX + 1.5, seed.landY + 2.8, 5.5, 1.6, 0, 0, Math.PI * 2);
  ctx.fill();

  drawSeed(seed.landX, seed.landY, seed.settleAngle, 0.80 * seed.size, 0.9);

  ctx.restore();
}

function drawAccumulatedGroundSeeds(currentCycleIndex, currentRelease) {
  for (let cycleIndex = 0; cycleIndex < totalCycles; cycleIndex++) {
    const seeds = cycleSeeds[cycleIndex];

    for (const s of seeds) {
      if (!s.groundSeed) continue;

      let showSettled = false;

      if (cycleIndex < currentCycleIndex) {
        showSettled = true;
      } else if (cycleIndex === currentCycleIndex) {
        const local = seedProgress(currentRelease, s);
        if (local >= 1) showSettled = true;
      }

      if (showSettled) {
        drawSettledSeed(s);
      }
    }
  }
}

function drawReleasedSeeds(release, t, seeds) {
  if (release <= 0) return;

  const cx = stemTop.x;
  const cy = stemTop.y;

  for (const s of seeds) {
    if (release < s.detachAt) continue;

    const local = seedProgress(release, s);

    const startX = cx + Math.cos(s.a) * s.r;
    const startY = cy + Math.sin(s.a) * s.r;

    if (s.groundSeed) {
      if (local >= 1) continue;

      const controlX = lerp(startX, s.landX, 0.42);
      const controlY = Math.min(startY, s.landY) - s.controlLift;

      const x = quadBezier(startX, controlX, s.landX, local);
      const y = quadBezier(startY, controlY, s.landY, local);
      const angle = s.a + Math.PI / 2 + s.spin * t * 0.9;

      drawSeed(x, y, angle, 0.80 * s.size, 0.9);
    } else {
      const move = easeOutQuad(local);

      const x = startX + s.offX * move;
      const y = startY
        - Math.sin(move * Math.PI) * s.arcUp
        + s.driftDown * move
        + Math.sin(t * 1.2 + s.jitter) * 1.0;

      if (x > W + 30) continue;

      const angle = s.a + Math.PI / 2 + s.spin * t;
      const alpha = 0.88 * (1 - Math.max(0, local - 0.88) / 0.12);

      drawSeed(x, y, angle, 0.80 * s.size, alpha);
    }
  }
}

function drawWind(release, t) {
  if (release <= 0) return;

  ctx.save();
  ctx.strokeStyle = `rgba(255,252,245,${0.08 + release * 0.14})`;
  ctx.lineWidth = 0.9;
  ctx.lineCap = "round";

  for (const line of windLines) {
    const baseX = line.x + release * 620 + t * 12 * line.speed;

    ctx.beginPath();
    for (let i = 0; i <= line.len; i += 4) {
      const px = baseX + i;
      const py = line.y + Math.sin((i * 0.075) + t * 1.15 + line.phase) * line.amp;
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();
  }

  ctx.restore();
}

function drawBotanicalInsect(elapsed, grow, release) {
  const appear = clamp01((grow - 0.18) / 0.32);
  const retreat = easeOutQuad(release);
  const alpha = 0.88 * appear * (1 - release * 0.35);

  if (alpha <= 0.01) return;

  const hoverX = stemTop.x + 55 + Math.sin(elapsed * 1.1) * 8 + retreat * 90;
  const hoverY = stemTop.y - 26 + Math.cos(elapsed * 2.3) * 4 - retreat * 12;
  const wingFlutter = 1 + Math.sin(elapsed * 18) * 0.08;
  const bodyAngle = -0.18 + Math.sin(elapsed * 0.9) * 0.05 - release * 0.08;

  ctx.save();
  ctx.translate(hoverX, hoverY);
  ctx.rotate(bodyAngle);
  ctx.globalAlpha = alpha;

  // faint plate shadow
  ctx.fillStyle = "rgba(75,55,28,0.08)";
  ctx.beginPath();
  ctx.ellipse(1.5, 7, 9, 2.5, 0, 0, Math.PI * 2);
  ctx.fill();

  // wings
  ctx.save();
  ctx.scale(1, wingFlutter);
  ctx.fillStyle = "rgba(250,248,242,0.38)";
  ctx.strokeStyle = "rgba(120,96,66,0.35)";
  ctx.lineWidth = 0.45;

  ctx.beginPath();
  ctx.ellipse(-3.8, -2.6, 5.8, 3.0, -0.55, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();

  ctx.beginPath();
  ctx.ellipse(3.8, -2.6, 5.8, 3.0, 0.55, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();
  ctx.restore();

  // thorax
  ctx.fillStyle = "rgba(122,92,52,0.88)";
  ctx.strokeStyle = "rgba(78,55,30,0.7)";
  ctx.lineWidth = 0.6;
  ctx.beginPath();
  ctx.ellipse(0, 0.2, 3.0, 2.5, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();

  // abdomen
  ctx.fillStyle = "rgba(150,112,58,0.82)";
  ctx.beginPath();
  ctx.ellipse(0, 5.8, 2.8, 4.8, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();

  // stripes
  ctx.strokeStyle = "rgba(85,60,33,0.65)";
  ctx.lineWidth = 0.55;
  for (let y of [3.8, 5.8, 7.6]) {
    ctx.beginPath();
    ctx.moveTo(-2.1, y);
    ctx.lineTo(2.1, y);
    ctx.stroke();
  }

  // head
  ctx.fillStyle = "rgba(94,68,39,0.86)";
  ctx.beginPath();
  ctx.arc(0, -2.9, 1.7, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();

  // antennae
  ctx.strokeStyle = "rgba(82,58,33,0.6)";
  ctx.lineWidth = 0.5;
  ctx.beginPath();
  ctx.moveTo(-0.8, -4.0);
  ctx.quadraticCurveTo(-2.8, -6.5, -4.2, -7.2);
  ctx.moveTo(0.8, -4.0);
  ctx.quadraticCurveTo(2.8, -6.5, 4.2, -7.2);
  ctx.stroke();

  // legs
  ctx.beginPath();
  ctx.moveTo(-2.0, 1.5);
  ctx.lineTo(-4.6, 4.4);
  ctx.moveTo(2.0, 1.5);
  ctx.lineTo(4.6, 4.4);
  ctx.moveTo(-1.5, 2.8);
  ctx.lineTo(-4.0, 6.0);
  ctx.moveTo(1.5, 2.8);
  ctx.lineTo(4.0, 6.0);
  ctx.stroke();

  ctx.restore();
}

function getMasterState(elapsedSeconds) {
  const masterTime = elapsedSeconds % masterDuration;
  const activeTime = totalCycles * cycleDuration;

  if (masterTime >= activeTime) {
    return {
      currentCycleIndex: totalCycles - 1,
      localTime: cycleDuration,
      inFinalHold: true
    };
  }
  // Firefox can occasionally land right on the boundary,
  // producing index 5 for a 5-cycle animation.
  const rawCycleIndex = Math.floor(masterTime / cycleDuration);
  const currentCycleIndex = Math.min(totalCycles - 1, rawCycleIndex);
  const localTime = masterTime - currentCycleIndex * cycleDuration;

  return {
    currentCycleIndex,
    localTime,
    inFinalHold: false
  };
}

function animate(now) {
  const elapsed = (now - startTime) / 1000;
  const { currentCycleIndex, localTime } = getMasterState(elapsed);
  const seeds = cycleSeeds[currentCycleIndex] || cycleSeeds[totalCycles - 1]

  const grow = clamp01(localTime / bloomDuration);
  const hold = clamp01((localTime - bloomDuration) / preReleaseHold);
  const release = clamp01((localTime - releaseStart) / releaseDuration);

  const sway = Math.sin(elapsed * 1.0) * 0.75 * (0.25 + hold * 0.75);

  drawBackground();
  drawPlateDetails();
  drawGroundShadow();

  drawAccumulatedGroundSeeds(currentCycleIndex, release);

  drawWind(release, elapsed);
  drawLeaves(easeOutCubic(grow));
  drawStem(easeOutCubic(grow), sway);
  drawAttachedHead(grow, release, elapsed, sway, seeds);
  drawBotanicalInsect(elapsed, grow, release);
  drawReleasedSeeds(release, elapsed, seeds);

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
