import React, { useState, useEffect, useRef } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Slider } from './ui/slider';
import { Badge } from './ui/badge';
import { Play, Pause, RotateCcw, Download, Settings, Maximize2 } from 'lucide-react';

const EnhancedSimulation = ({ 
  title, 
  type, 
  description,
  parameters = {},
  onParameterChange,
  className = ""
}) => {
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [time, setTime] = useState(0);
  const [speed, setSpeed] = useState(1);
  const [showSettings, setShowSettings] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  // Default parameters for different simulation types
  const defaultParams = {
    wave: {
      amplitude: 1.0,
      frequency: 1.0,
      wavelength: 2.0,
      phase: 0.0
    },
    pendulum: {
      length: 1.0,
      mass: 1.0,
      gravity: 9.81,
      damping: 0.01,
      initialAngle: Math.PI / 4
    },
    spring: {
      mass: 1.0,
      springConstant: 10.0,
      damping: 0.1,
      initialPosition: 1.0
    },
    particle: {
      mass: 1.0,
      charge: 1.0,
      electricField: 1.0,
      magneticField: 0.5
    },
    quantum: {
      potential: 1.0,
      energy: 0.5,
      mass: 1.0,
      hbar: 1.0
    }
  };

  const [params, setParams] = useState({
    ...defaultParams[type] || {},
    ...parameters
  });

  useEffect(() => {
    if (isPlaying) {
      const animate = () => {
        setTime(prevTime => prevTime + 0.016 * speed); // 60 FPS
        animationRef.current = requestAnimationFrame(animate);
      };
      animationRef.current = requestAnimationFrame(animate);
    } else {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    }

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [isPlaying, speed]);

  useEffect(() => {
    drawSimulation();
  }, [time, params, type]);

  const drawSimulation = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear canvas
    ctx.fillStyle = '#1a1a2e';
    ctx.fillRect(0, 0, width, height);

    // Draw grid
    drawGrid(ctx, width, height);

    // Draw simulation based on type
    switch (type) {
      case 'wave':
        drawWaveSimulation(ctx, width, height);
        break;
      case 'pendulum':
        drawPendulumSimulation(ctx, width, height);
        break;
      case 'spring':
        drawSpringSimulation(ctx, width, height);
        break;
      case 'particle':
        drawParticleSimulation(ctx, width, height);
        break;
      case 'quantum':
        drawQuantumSimulation(ctx, width, height);
        break;
      case 'neural_network':
        drawNeuralNetworkSimulation(ctx, width, height);
        break;
      case 'fourier':
        drawFourierSimulation(ctx, width, height);
        break;
      default:
        drawDefaultSimulation(ctx, width, height);
    }

    // Draw info overlay
    drawInfoOverlay(ctx, width, height);
  };

  const drawGrid = (ctx, width, height) => {
    ctx.strokeStyle = '#333366';
    ctx.lineWidth = 0.5;
    
    const gridSize = 20;
    for (let x = 0; x <= width; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }
    
    for (let y = 0; y <= height; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Draw axes
    ctx.strokeStyle = '#666699';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(width / 2, 0);
    ctx.lineTo(width / 2, height);
    ctx.moveTo(0, height / 2);
    ctx.lineTo(width, height / 2);
    ctx.stroke();
  };

  const drawWaveSimulation = (ctx, width, height) => {
    const { amplitude, frequency, wavelength, phase } = params;
    
    ctx.strokeStyle = '#00ffff';
    ctx.lineWidth = 3;
    ctx.beginPath();

    const centerY = height / 2;
    const scale = 100;

    for (let x = 0; x < width; x++) {
      const normalizedX = (x - width / 2) / scale;
      const y = amplitude * Math.sin(2 * Math.PI * frequency * time + 
                                   2 * Math.PI * normalizedX / wavelength + phase);
      const canvasY = centerY - y * scale;

      if (x === 0) {
        ctx.moveTo(x, canvasY);
      } else {
        ctx.lineTo(x, canvasY);
      }
    }
    ctx.stroke();

    // Draw wave equation
    ctx.fillStyle = '#ffffff';
    ctx.font = '16px monospace';
    ctx.fillText(`y = ${amplitude.toFixed(1)} sin(2π × ${frequency.toFixed(1)} × t + 2π × x / ${wavelength.toFixed(1)} + ${phase.toFixed(1)})`, 10, 30);
  };

  const drawPendulumSimulation = (ctx, width, height) => {
    const { length, mass, gravity, damping, initialAngle } = params;
    
    const centerX = width / 2;
    const centerY = 50;
    const scale = 200;
    
    // Calculate pendulum position with damping
    const dampedAmplitude = initialAngle * Math.exp(-damping * time);
    const omega = Math.sqrt(gravity / length);
    const angle = dampedAmplitude * Math.cos(omega * time);
    
    const bobX = centerX + scale * length * Math.sin(angle);
    const bobY = centerY + scale * length * Math.cos(angle);
    
    // Draw string
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(bobX, bobY);
    ctx.stroke();
    
    // Draw pivot
    ctx.fillStyle = '#ffff00';
    ctx.beginPath();
    ctx.arc(centerX, centerY, 5, 0, 2 * Math.PI);
    ctx.fill();
    
    // Draw bob
    ctx.fillStyle = '#ff6600';
    ctx.beginPath();
    ctx.arc(bobX, bobY, mass * 10, 0, 2 * Math.PI);
    ctx.fill();
    
    // Draw trajectory
    ctx.strokeStyle = '#ff660033';
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let t = 0; t <= time; t += 0.1) {
      const pastDampedAmplitude = initialAngle * Math.exp(-damping * t);
      const pastAngle = pastDampedAmplitude * Math.cos(omega * t);
      const pastX = centerX + scale * length * Math.sin(pastAngle);
      const pastY = centerY + scale * length * Math.cos(pastAngle);
      
      if (t === 0) {
        ctx.moveTo(pastX, pastY);
      } else {
        ctx.lineTo(pastX, pastY);
      }
    }
    ctx.stroke();
  };

  const drawSpringSimulation = (ctx, width, height) => {
    const { mass, springConstant, damping, initialPosition } = params;
    
    const centerX = width / 2;
    const centerY = height / 2;
    const scale = 100;
    
    // Calculate spring motion
    const omega = Math.sqrt(springConstant / mass);
    const dampedOmega = omega * Math.sqrt(1 - (damping / (2 * mass))**2);
    const dampingFactor = Math.exp(-damping * time / (2 * mass));
    const position = initialPosition * dampingFactor * Math.cos(dampedOmega * time);
    
    const massX = centerX + position * scale;
    
    // Draw spring
    ctx.strokeStyle = '#00ff00';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    const springCoils = 10;
    const springWidth = 20;
    const springLength = Math.abs(massX - centerX);
    
    for (let i = 0; i <= springCoils; i++) {
      const x = centerX + (i / springCoils) * (massX - centerX);
      const y = centerY + (i % 2 === 0 ? 0 : springWidth) * Math.sin(i * Math.PI);
      
      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    }
    ctx.stroke();
    
    // Draw mass
    ctx.fillStyle = '#ff0000';
    ctx.fillRect(massX - 15, centerY - 15, 30, 30);
    
    // Draw equilibrium position
    ctx.strokeStyle = '#ffffff44';
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(centerX, 0);
    ctx.lineTo(centerX, height);
    ctx.stroke();
    ctx.setLineDash([]);
  };

  const drawParticleSimulation = (ctx, width, height) => {
    const { mass, charge, electricField, magneticField } = params;
    
    const centerX = width / 2;
    const centerY = height / 2;
    const scale = 50;
    
    // Calculate particle motion in electromagnetic field
    const cyclotronFreq = charge * magneticField / mass;
    const driftVelocity = electricField / magneticField;
    
    const x = driftVelocity * time + (1 / cyclotronFreq) * Math.sin(cyclotronFreq * time);
    const y = (1 / cyclotronFreq) * (1 - Math.cos(cyclotronFreq * time));
    
    const particleX = centerX + x * scale;
    const particleY = centerY + y * scale;
    
    // Draw electric field lines
    ctx.strokeStyle = '#ffff0044';
    ctx.lineWidth = 1;
    for (let i = 0; i < 10; i++) {
      const fieldY = (i / 9) * height;
      ctx.beginPath();
      ctx.moveTo(0, fieldY);
      ctx.lineTo(width, fieldY);
      ctx.stroke();
      
      // Draw arrows
      ctx.beginPath();
      ctx.moveTo(width - 10, fieldY - 5);
      ctx.lineTo(width, fieldY);
      ctx.lineTo(width - 10, fieldY + 5);
      ctx.stroke();
    }
    
    // Draw magnetic field (into page)
    ctx.fillStyle = '#0000ff44';
    for (let x = 50; x < width; x += 50) {
      for (let y = 50; y < height; y += 50) {
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, 2 * Math.PI);
        ctx.fill();
        
        ctx.strokeStyle = '#0000ff44';
        ctx.beginPath();
        ctx.moveTo(x - 5, y - 5);
        ctx.lineTo(x + 5, y + 5);
        ctx.moveTo(x + 5, y - 5);
        ctx.lineTo(x - 5, y + 5);
        ctx.stroke();
      }
    }
    
    // Draw particle trajectory
    ctx.strokeStyle = '#ff00ff88';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let t = 0; t <= time; t += 0.05) {
      const pastX = driftVelocity * t + (1 / cyclotronFreq) * Math.sin(cyclotronFreq * t);
      const pastY = (1 / cyclotronFreq) * (1 - Math.cos(cyclotronFreq * t));
      const pastParticleX = centerX + pastX * scale;
      const pastParticleY = centerY + pastY * scale;
      
      if (t === 0) {
        ctx.moveTo(pastParticleX, pastParticleY);
      } else {
        ctx.lineTo(pastParticleX, pastParticleY);
      }
    }
    ctx.stroke();
    
    // Draw particle
    ctx.fillStyle = charge > 0 ? '#ff0000' : '#0000ff';
    ctx.beginPath();
    ctx.arc(particleX, particleY, 8, 0, 2 * Math.PI);
    ctx.fill();
  };

  const drawQuantumSimulation = (ctx, width, height) => {
    const { potential, energy, mass, hbar } = params;
    
    const centerY = height / 2;
    const scale = 100;
    
    // Draw potential well
    ctx.strokeStyle = '#ffff00';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    for (let x = 0; x < width; x++) {
      const normalizedX = (x - width / 2) / scale;
      const V = potential * normalizedX * normalizedX; // Harmonic oscillator
      const y = centerY - V * scale / 10;
      
      if (x === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    }
    ctx.stroke();
    
    // Draw energy level
    ctx.strokeStyle = '#00ff00';
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    const energyY = centerY - energy * scale / 10;
    ctx.moveTo(0, energyY);
    ctx.lineTo(width, energyY);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Draw wavefunction
    ctx.strokeStyle = '#00ffff';
    ctx.lineWidth = 3;
    ctx.beginPath();
    
    const omega = Math.sqrt(potential / mass);
    const alpha = Math.sqrt(mass * omega / hbar);
    
    for (let x = 0; x < width; x++) {
      const normalizedX = (x - width / 2) / scale;
      const psi = Math.exp(-alpha * normalizedX * normalizedX / 2) * 
                  Math.cos(Math.sqrt(2 * mass * energy / hbar) * normalizedX + time);
      const y = centerY - psi * scale;
      
      if (x === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    }
    ctx.stroke();
    
    // Draw probability density
    ctx.fillStyle = '#ff00ff44';
    ctx.beginPath();
    ctx.moveTo(0, centerY);
    
    for (let x = 0; x < width; x++) {
      const normalizedX = (x - width / 2) / scale;
      const psi = Math.exp(-alpha * normalizedX * normalizedX / 2) * 
                  Math.cos(Math.sqrt(2 * mass * energy / hbar) * normalizedX + time);
      const probability = psi * psi;
      const y = centerY - probability * scale;
      ctx.lineTo(x, y);
    }
    
    ctx.lineTo(width, centerY);
    ctx.closePath();
    ctx.fill();
  };

  const drawNeuralNetworkSimulation = (ctx, width, height) => {
    const layers = [3, 4, 4, 2];
    const layerSpacing = width / (layers.length + 1);
    const nodeRadius = 15;
    
    // Draw connections
    ctx.strokeStyle = '#666699';
    ctx.lineWidth = 1;
    
    for (let l = 0; l < layers.length - 1; l++) {
      const currentLayerX = (l + 1) * layerSpacing;
      const nextLayerX = (l + 2) * layerSpacing;
      
      for (let i = 0; i < layers[l]; i++) {
        const currentY = height / 2 + (i - (layers[l] - 1) / 2) * 60;
        
        for (let j = 0; j < layers[l + 1]; j++) {
          const nextY = height / 2 + (j - (layers[l + 1] - 1) / 2) * 60;
          
          // Animate connection strength
          const weight = Math.sin(time + i + j) * 0.5 + 0.5;
          ctx.globalAlpha = weight;
          
          ctx.beginPath();
          ctx.moveTo(currentLayerX + nodeRadius, currentY);
          ctx.lineTo(nextLayerX - nodeRadius, nextY);
          ctx.stroke();
        }
      }
    }
    
    ctx.globalAlpha = 1;
    
    // Draw nodes
    for (let l = 0; l < layers.length; l++) {
      const layerX = (l + 1) * layerSpacing;
      
      for (let i = 0; i < layers[l]; i++) {
        const nodeY = height / 2 + (i - (layers[l] - 1) / 2) * 60;
        
        // Animate node activation
        const activation = Math.sin(time * 2 + l + i) * 0.5 + 0.5;
        const intensity = Math.floor(activation * 255);
        
        ctx.fillStyle = `rgb(${intensity}, ${intensity}, 255)`;
        ctx.beginPath();
        ctx.arc(layerX, nodeY, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Draw activation value
        ctx.fillStyle = '#000000';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(activation.toFixed(2), layerX, nodeY + 3);
      }
    }
  };

  const drawFourierSimulation = (ctx, width, height) => {
    const centerY = height / 2;
    const scale = 100;
    
    // Draw original signal (sum of harmonics)
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.beginPath();
    
    for (let x = 0; x < width; x++) {
      const t = (x / width) * 4 * Math.PI;
      let signal = 0;
      
      // Add harmonics
      for (let n = 1; n <= 5; n++) {
        const amplitude = 1 / n;
        const frequency = n;
        signal += amplitude * Math.sin(frequency * t + time);
      }
      
      const y = centerY - signal * scale / 5;
      
      if (x === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    }
    ctx.stroke();
    
    // Draw individual harmonics
    const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff'];
    
    for (let n = 1; n <= 5; n++) {
      ctx.strokeStyle = colors[n - 1] + '88';
      ctx.lineWidth = 1;
      ctx.beginPath();
      
      for (let x = 0; x < width; x++) {
        const t = (x / width) * 4 * Math.PI;
        const amplitude = 1 / n;
        const frequency = n;
        const harmonic = amplitude * Math.sin(frequency * t + time);
        const y = centerY - harmonic * scale;
        
        if (x === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      ctx.stroke();
    }
    
    // Draw frequency spectrum
    const spectrumX = width - 150;
    const spectrumY = 50;
    const spectrumWidth = 100;
    const spectrumHeight = 100;
    
    ctx.fillStyle = '#ffffff22';
    ctx.fillRect(spectrumX, spectrumY, spectrumWidth, spectrumHeight);
    
    ctx.fillStyle = '#ffffff';
    ctx.font = '12px Arial';
    ctx.fillText('Frequency Spectrum', spectrumX, spectrumY - 10);
    
    for (let n = 1; n <= 5; n++) {
      const amplitude = 1 / n;
      const barHeight = amplitude * spectrumHeight;
      const barWidth = spectrumWidth / 6;
      const barX = spectrumX + n * barWidth;
      const barY = spectrumY + spectrumHeight - barHeight;
      
      ctx.fillStyle = colors[n - 1];
      ctx.fillRect(barX, barY, barWidth - 2, barHeight);
      
      ctx.fillStyle = '#ffffff';
      ctx.font = '10px Arial';
      ctx.textAlign = 'center';
      ctx.fillText(n.toString(), barX + barWidth / 2, spectrumY + spectrumHeight + 15);
    }
  };

  const drawDefaultSimulation = (ctx, width, height) => {
    // Default wave simulation
    drawWaveSimulation(ctx, width, height);
  };

  const drawInfoOverlay = (ctx, width, height) => {
    // Draw time and speed info
    ctx.fillStyle = '#ffffff';
    ctx.font = '14px monospace';
    ctx.textAlign = 'left';
    ctx.fillText(`Time: ${time.toFixed(2)}s`, 10, height - 40);
    ctx.fillText(`Speed: ${speed.toFixed(1)}x`, 10, height - 20);
    
    // Draw parameter values
    let yOffset = 50;
    Object.entries(params).forEach(([key, value]) => {
      ctx.fillText(`${key}: ${value.toFixed(2)}`, width - 150, yOffset);
      yOffset += 20;
    });
  };

  const handleParameterChange = (paramName, value) => {
    const newParams = { ...params, [paramName]: value[0] };
    setParams(newParams);
    if (onParameterChange) {
      onParameterChange(newParams);
    }
  };

  const togglePlayPause = () => {
    setIsPlaying(!isPlaying);
  };

  const resetSimulation = () => {
    setTime(0);
    setIsPlaying(false);
  };

  const downloadFrame = () => {
    const canvas = canvasRef.current;
    if (canvas) {
      const link = document.createElement('a');
      link.download = `${type}_simulation_${Date.now()}.png`;
      link.href = canvas.toDataURL();
      link.click();
    }
  };

  const toggleFullscreen = () => {
    setIsFullscreen(!isFullscreen);
  };

  return (
    <Card className={`${className} ${isFullscreen ? 'fixed inset-4 z-50' : ''}`}>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Badge variant="secondary" className="bg-purple-100 text-purple-700">
              การจำลอง
            </Badge>
            <CardTitle>{title}</CardTitle>
          </div>
          <div className="flex items-center gap-2">
            <Button variant="outline" size="sm" onClick={() => setShowSettings(!showSettings)}>
              <Settings className="w-4 h-4" />
            </Button>
            <Button variant="outline" size="sm" onClick={downloadFrame}>
              <Download className="w-4 h-4" />
            </Button>
            <Button variant="outline" size="sm" onClick={toggleFullscreen}>
              <Maximize2 className="w-4 h-4" />
            </Button>
          </div>
        </div>
        {description && (
          <p className="text-gray-600">{description}</p>
        )}
      </CardHeader>
      
      <CardContent>
        <div className="space-y-4">
          {/* Canvas */}
          <div className="relative">
            <canvas
              ref={canvasRef}
              width={isFullscreen ? 800 : 600}
              height={isFullscreen ? 500 : 300}
              className="border rounded-lg bg-gray-900 w-full"
              style={{ maxWidth: '100%', height: 'auto' }}
            />
          </div>

          {/* Controls */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <Button onClick={togglePlayPause} variant="outline">
                {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                {isPlaying ? 'หยุด' : 'เริ่ม'}
              </Button>
              <Button onClick={resetSimulation} variant="outline">
                <RotateCcw className="w-4 h-4" />
                รีเซ็ต
              </Button>
            </div>

            <div className="flex items-center gap-4">
              <div className="flex items-center gap-2">
                <span className="text-sm">ความเร็ว:</span>
                <Slider
                  value={[speed]}
                  onValueChange={(value) => setSpeed(value[0])}
                  min={0.1}
                  max={3}
                  step={0.1}
                  className="w-20"
                />
                <span className="text-sm font-mono">{speed.toFixed(1)}x</span>
              </div>
            </div>
          </div>

          {/* Parameter Controls */}
          {showSettings && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4 bg-gray-50 rounded-lg">
              {Object.entries(params).map(([paramName, value]) => (
                <div key={paramName} className="space-y-2">
                  <div className="flex justify-between">
                    <label className="text-sm font-medium capitalize">
                      {paramName.replace(/([A-Z])/g, ' $1').toLowerCase()}
                    </label>
                    <span className="text-sm font-mono">{value.toFixed(2)}</span>
                  </div>
                  <Slider
                    value={[value]}
                    onValueChange={(newValue) => handleParameterChange(paramName, newValue)}
                    min={0.1}
                    max={paramName === 'phase' ? 2 * Math.PI : 5}
                    step={0.1}
                    className="w-full"
                  />
                </div>
              ))}
            </div>
          )}

          {/* Info Display */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div className="p-2 bg-blue-50 rounded">
              <div className="text-lg font-bold text-blue-600">{time.toFixed(2)}s</div>
              <div className="text-xs text-gray-600">เวลา</div>
            </div>
            <div className="p-2 bg-green-50 rounded">
              <div className="text-lg font-bold text-green-600">{speed.toFixed(1)}x</div>
              <div className="text-xs text-gray-600">ความเร็ว</div>
            </div>
            <div className="p-2 bg-orange-50 rounded">
              <div className="text-lg font-bold text-orange-600">{isPlaying ? 'กำลังทำงาน' : 'หยุด'}</div>
              <div className="text-xs text-gray-600">สถานะ</div>
            </div>
            <div className="p-2 bg-purple-50 rounded">
              <div className="text-lg font-bold text-purple-600">{type}</div>
              <div className="text-xs text-gray-600">ประเภท</div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default EnhancedSimulation;
