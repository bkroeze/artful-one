const CANVAS = {
  width: 766,
  height: 1080,
};

const PARTS = [
  {
    name: 'tail',
    src: 'scorp_tail.png',
    className: 'tail',
    left: 320,
    top: 802,
    width: 268,
    height: 266,
    pivot: { x: 42, y: 7 },
    canvasPivot: { x: 364, y: 818 },
    duration: 2.6,
    delay: -0.4,
  },
  {
    name: 'leg 8',
    src: 'scorp_leg_8.png',
    className: 'leg left',
    left: 48,
    top: 360,
    width: 231,
    height: 98,
    pivot: { x: 230, y: 45 },
    canvasPivot: { x: 279, y: 407 },
    from: 6,
    to: -8,
    duration: 1.55,
    delay: -0.25,
  },
  {
    name: 'leg 7',
    src: 'scorp_leg_7.png',
    className: 'leg left',
    left: 22,
    top: 462,
    width: 259,
    height: 93,
    pivot: { x: 257, y: 12 },
    canvasPivot: { x: 281, y: 474 },
    from: -8,
    to: 7,
    duration: 1.7,
    delay: -0.95,
  },
  {
    name: 'leg 6',
    src: 'scorp_leg_6.png',
    className: 'leg left',
    left: 9,
    top: 527,
    width: 278,
    height: 176,
    pivot: { x: 277, y: 9 },
    canvasPivot: { x: 284, y: 539 },
    from: 7,
    to: -7,
    duration: 1.75,
    delay: -0.55,
  },
  {
    name: 'leg 5',
    src: 'scorp_leg_5.png',
    className: 'leg left',
    left: 105,
    top: 606,
    width: 186,
    height: 288,
    pivot: { x: 182, y: 6 },
    canvasPivot: { x: 289, y: 612 },
    from: -7,
    to: 6,
    duration: 1.9,
    delay: -1.25,
  },
  {
    name: 'leg 1',
    src: 'scorp_leg_1.png',
    className: 'leg right',
    left: 484,
    top: 360,
    width: 230,
    height: 98,
    pivot: { x: 0, y: 44 },
    canvasPivot: { x: 484, y: 407 },
    from: -6,
    to: 8,
    duration: 1.55,
    delay: -0.8,
  },
  {
    name: 'leg 2',
    src: 'scorp_leg_2.png',
    className: 'leg right',
    left: 481,
    top: 464,
    width: 269,
    height: 100,
    pivot: { x: 2, y: 8 },
    canvasPivot: { x: 483, y: 471 },
    from: 8,
    to: -7,
    duration: 1.7,
    delay: -0.15,
  },
  {
    name: 'leg 3',
    src: 'scorp_leg_3.png',
    className: 'leg right',
    left: 476,
    top: 527,
    width: 279,
    height: 185,
    pivot: { x: 2, y: 16 },
    canvasPivot: { x: 477, y: 537 },
    from: -7,
    to: 7,
    duration: 1.75,
    delay: -1.0,
  },
  {
    name: 'leg 4',
    src: 'scorp_leg_4.png',
    className: 'leg right',
    left: 467,
    top: 605,
    width: 187,
    height: 288,
    pivot: { x: 3, y: 7 },
    canvasPivot: { x: 472, y: 613 },
    from: 7,
    to: -6,
    duration: 1.9,
    delay: -0.45,
  },
  {
    name: 'claw 2',
    src: 'scorp_claw_2.png',
    className: 'claw left',
    left: 71,
    top: 11,
    width: 211,
    height: 364,
    pivot: { x: 208, y: 343 },
    canvasPivot: { x: 286, y: 353 },
    duration: 2.3,
    delay: -0.8,
  },
  {
    name: 'claw 1',
    src: 'scorp_claw_1.png',
    className: 'claw right',
    left: 473,
    top: 10,
    width: 220,
    height: 364,
    pivot: { x: 3, y: 344 },
    canvasPivot: { x: 477, y: 351 },
    duration: 2.3,
    delay: -1.6,
  },
  {
    name: 'body',
    src: 'scorp_body.png',
    className: 'body',
    left: 279,
    top: 216,
    width: 205,
    height: 603,
  },
];

const stage = document.getElementById('scorpionStage');
const viewport = document.querySelector('.scorpion-viewport');
const toggleMotion = document.getElementById('toggleMotion');
const speedRange = document.getElementById('speedRange');
const pivotToggle = document.getElementById('pivotToggle');
const assetBase = stage?.dataset.assetBase || '';

function createPart(part) {
  const img = document.createElement('img');
  img.className = `part ${part.className}`;
  img.src = new URL("scorpion/" + part.src, window.location.origin + assetBase).toString();
  console.log("img src: " + img);
  img.alt = '';
  img.draggable = false;
  img.style.left = `${part.left}px`;
  img.style.top = `${part.top}px`;
  img.style.width = `${part.width}px`;
  img.style.height = `${part.height}px`;

  if (part.pivot) {
    img.style.transformOrigin = `${part.pivot.x}px ${part.pivot.y}px`;
  }

  if (part.from !== undefined) {
    img.style.setProperty('--from', part.from);
    img.style.setProperty('--to', part.to);
  }

  if (part.duration) {
    img.style.setProperty('--duration', `${part.duration}s`);
  }

  if (part.delay) {
    img.style.setProperty('--delay', `${part.delay}s`);
  }

  stage.appendChild(img);

  if (part.canvasPivot) {
    const marker = document.createElement('span');
    marker.className = 'pivot-marker';
    marker.title = `${part.name} pivot`;
    marker.style.left = `${part.canvasPivot.x}px`;
    marker.style.top = `${part.canvasPivot.y}px`;
    stage.appendChild(marker);
  }
}

function resizeStage() {
  const { width } = viewport.getBoundingClientRect();
  const scale = width / CANVAS.width;
  stage.style.transform = `scale(${scale})`;
}

function setPaused(paused) {
  stage.classList.toggle('is-paused', paused);
  toggleMotion.setAttribute('aria-pressed', String(!paused));
  toggleMotion.title = paused ? 'Play animation' : 'Pause animation';
  toggleMotion.innerHTML = paused
    ? '<span class="play-icon" aria-hidden="true"></span><span class="sr-only">Play animation</span>'
    : '<span class="pause-icon" aria-hidden="true"></span><span class="sr-only">Pause animation</span>';
}

PARTS.forEach(createPart);
resizeStage();

toggleMotion.addEventListener('click', () => {
  setPaused(!stage.classList.contains('is-paused'));
});

speedRange.addEventListener('input', (event) => {
  stage.style.setProperty('--speed', event.target.value);
});

pivotToggle.addEventListener('change', (event) => {
  stage.classList.toggle('show-pivots', event.target.checked);
});

window.addEventListener('resize', resizeStage);
