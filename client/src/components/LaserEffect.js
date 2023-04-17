import React, { useRef, useEffect } from 'react';

const LaserEffect = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const canvasWidth = canvas.width;
    const canvasHeight = canvas.height;

    const laserColor = 'rgba(0, 255, 0, 0.8)';

    const drawLaser = () => {
      ctx.clearRect(0, 0, canvasWidth, canvasHeight);

      ctx.beginPath();
      ctx.strokeStyle = laserColor;
      ctx.lineWidth = 2;
      ctx.moveTo(Math.random() * canvasWidth, 0);
      ctx.lineTo(Math.random() * canvasWidth, canvasHeight);
      ctx.stroke();

      requestAnimationFrame(drawLaser);
    };

    drawLaser();
  }, []);

  return (
    <canvas
      ref={canvasRef}
      width={window.innerWidth}
      height={window.innerHeight}
      style={{ background: 'black', display: 'block' }}
    />
  );
};

export default LaserEffect;