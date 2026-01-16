export type SketchParams = {
  height: number;
  width: number;
  smaller: number;
};

export function getSetupParams(sketchName: string): SketchParams {
  const outerElement = document.getElementById(sketchName);
  let h = 800;
  let w = 800;
  if (outerElement) {
    h = outerElement.getAttribute("data-height")
      ? parseInt(outerElement.getAttribute("data-height")!, 10)
      : 800;
    w = outerElement.getAttribute("data-width")
      ? parseInt(outerElement.getAttribute("data-width")!, 10)
      : 800;
  } else {
    console.warn(`No element found with id ${sketchName}`);
  }
  const params: SketchParams = {
    height: h,
    width: w,
    smaller: Math.min(h, w),
  };

  console.table({
    name: "Sketch Params",
    ...params,
  });
  return params;
}

export function setupSketch(
  sketchName: string,
  p: p5,
): SketchParams {
  const params = getSetupParams(sketchName);
  p.createCanvas(params.width, params.height);
  // ensure it receives key events
  (window as any).p5Instance = p;
  return params;
}
