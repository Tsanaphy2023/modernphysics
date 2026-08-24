import React, { useState, useEffect, useRef } from 'react'
import { motion } from 'framer-motion'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Slider } from '@/components/ui/slider.jsx'
import { Play, Pause, RotateCcw, Settings, Zap, Activity } from 'lucide-react'

const InteractiveSimulation = ({ 
  title = "Physics Simulation",
  description = "การจำลองปรากฏการณ์ทางฟิสิกส์แบบโต้ตอบ",
  type = "wave", // wave, particle, neural_network, quantum
  parameters = {}
}) => {
  const [isPlaying, setIsPlaying] = useState(false)
  const [currentTime, setCurrentTime] = useState(0)
  const [params, setParams] = useState({
    amplitude: 1,
    frequency: 1,
    speed: 1,
    particles: 50,
    ...parameters
  })
  const canvasRef = useRef(null)
  const animationRef = useRef(null)

  // Animation loop
  useEffect(() => {
    if (isPlaying) {
      const animate = () => {
        setCurrentTime(prev => prev + 0.016 * params.speed) // 60fps
        animationRef.current = requestAnimationFrame(animate)
      }
      animationRef.current = requestAnimationFrame(animate)
    } else {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current)
      }
    }

    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current)
      }
    }
  }, [isPlaying, params.speed])

  // Canvas drawing
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d')
    const width = canvas.width
    const height = canvas.height

    // Clear canvas
    ctx.clearRect(0, 0, width, height)
    ctx.fillStyle = '#1e293b'
    ctx.fillRect(0, 0, width, height)

    // Draw based on simulation type
    switch (type) {
      case 'wave':
        drawWaveSimulation(ctx, width, height)
        break
      case 'particle':
        drawParticleSimulation(ctx, width, height)
        break
      case 'neural_network':
        drawNeuralNetworkSimulation(ctx, width, height)
        break
      case 'quantum':
        drawQuantumSimulation(ctx, width, height)
        break
      default:
        drawWaveSimulation(ctx, width, height)
    }
  }, [currentTime, params, type])

  const drawWaveSimulation = (ctx, width, height) => {
    const centerY = height / 2
    const wavelength = width / (params.frequency * 2)
    
    ctx.strokeStyle = '#3b82f6'
    ctx.lineWidth = 3
    ctx.beginPath()
    
    for (let x = 0; x < width; x++) {
      const y = centerY + params.amplitude * 50 * Math.sin((x / wavelength) * 2 * Math.PI - currentTime * 2)
      if (x === 0) {
        ctx.moveTo(x, y)
      } else {
        ctx.lineTo(x, y)
      }
    }
    ctx.stroke()

    // Add wave equation
    ctx.fillStyle = '#ffffff'
    ctx.font = '16px monospace'
    ctx.fillText(`y = A sin(kx - ωt)`, 20, 30)
    ctx.fillText(`A = ${params.amplitude.toFixed(1)}`, 20, 50)
    ctx.fillText(`ω = ${params.frequency.toFixed(1)}`, 20, 70)
    ctx.fillText(`t = ${currentTime.toFixed(1)}s`, 20, 90)
  }

  const drawParticleSimulation = (ctx, width, height) => {
    const particleCount = params.particles
    
    for (let i = 0; i < particleCount; i++) {
      const angle = (i / particleCount) * 2 * Math.PI + currentTime
      const radius = 100 + 50 * Math.sin(currentTime + i)
      const x = width / 2 + radius * Math.cos(angle)
      const y = height / 2 + radius * Math.sin(angle)
      
      const hue = (i / particleCount) * 360
      ctx.fillStyle = `hsl(${hue}, 70%, 60%)`
      ctx.beginPath()
      ctx.arc(x, y, 3, 0, 2 * Math.PI)
      ctx.fill()
      
      // Add trails
      ctx.strokeStyle = `hsla(${hue}, 70%, 60%, 0.3)`
      ctx.lineWidth = 1
      ctx.beginPath()
      const prevX = width / 2 + (radius - 10) * Math.cos(angle - 0.1)
      const prevY = height / 2 + (radius - 10) * Math.sin(angle - 0.1)
      ctx.moveTo(prevX, prevY)
      ctx.lineTo(x, y)
      ctx.stroke()
    }

    // Add physics info
    ctx.fillStyle = '#ffffff'
    ctx.font = '14px monospace'
    ctx.fillText(`Particles: ${particleCount}`, 20, 30)
    ctx.fillText(`Angular velocity: ${params.speed.toFixed(1)} rad/s`, 20, 50)
  }

  const drawNeuralNetworkSimulation = (ctx, width, height) => {
    const layers = [4, 6, 4, 2]
    const layerSpacing = width / (layers.length + 1)
    const nodeRadius = 15
    
    // Draw connections
    ctx.strokeStyle = '#4ade80'
    ctx.lineWidth = 1
    
    for (let l = 0; l < layers.length - 1; l++) {
      const currentLayerSize = layers[l]
      const nextLayerSize = layers[l + 1]
      
      for (let i = 0; i < currentLayerSize; i++) {
        for (let j = 0; j < nextLayerSize; j++) {
          const x1 = layerSpacing * (l + 1)
          const y1 = (height / (currentLayerSize + 1)) * (i + 1)
          const x2 = layerSpacing * (l + 2)
          const y2 = (height / (nextLayerSize + 1)) * (j + 1)
          
          const activation = Math.sin(currentTime + i + j) * 0.5 + 0.5
          ctx.globalAlpha = activation
          ctx.beginPath()
          ctx.moveTo(x1, y1)
          ctx.lineTo(x2, y2)
          ctx.stroke()
        }
      }
    }
    
    ctx.globalAlpha = 1
    
    // Draw nodes
    layers.forEach((layerSize, layerIndex) => {
      for (let i = 0; i < layerSize; i++) {
        const x = layerSpacing * (layerIndex + 1)
        const y = (height / (layerSize + 1)) * (i + 1)
        
        const activation = Math.sin(currentTime + layerIndex + i) * 0.5 + 0.5
        const intensity = Math.floor(activation * 255)
        
        ctx.fillStyle = `rgb(${intensity}, ${intensity}, 255)`
        ctx.beginPath()
        ctx.arc(x, y, nodeRadius, 0, 2 * Math.PI)
        ctx.fill()
        
        ctx.strokeStyle = '#ffffff'
        ctx.lineWidth = 2
        ctx.stroke()
      }
    })

    // Add neural network info
    ctx.fillStyle = '#ffffff'
    ctx.font = '14px monospace'
    ctx.fillText('Neural Network Activation', 20, 30)
    ctx.fillText(`Layers: ${layers.join('-')}`, 20, 50)
  }

  const drawQuantumSimulation = (ctx, width, height) => {
    const centerX = width / 2
    const centerY = height / 2
    const maxRadius = Math.min(width, height) / 3
    
    // Draw probability wave function
    for (let r = 0; r < maxRadius; r += 2) {
      const probability = Math.exp(-r / 50) * (Math.sin(r / 10 + currentTime * 3) ** 2)
      const alpha = probability
      
      ctx.strokeStyle = `rgba(255, 100, 255, ${alpha})`
      ctx.lineWidth = 2
      ctx.beginPath()
      ctx.arc(centerX, centerY, r, 0, 2 * Math.PI)
      ctx.stroke()
    }
    
    // Draw quantum states
    for (let i = 0; i < 8; i++) {
      const angle = (i / 8) * 2 * Math.PI + currentTime
      const r = maxRadius * 0.7
      const x = centerX + r * Math.cos(angle)
      const y = centerY + r * Math.sin(angle)
      
      const phase = Math.sin(currentTime * 2 + i) * 0.5 + 0.5
      ctx.fillStyle = `hsla(${i * 45}, 80%, 60%, ${phase})`
      ctx.beginPath()
      ctx.arc(x, y, 8, 0, 2 * Math.PI)
      ctx.fill()
    }

    // Add quantum info
    ctx.fillStyle = '#ffffff'
    ctx.font = '14px monospace'
    ctx.fillText('Quantum Wave Function |ψ⟩', 20, 30)
    ctx.fillText(`|ψ|² = probability density`, 20, 50)
    ctx.fillText(`ℏω = ${(currentTime * 0.5).toFixed(2)} eV`, 20, 70)
  }

  const togglePlayPause = () => {
    setIsPlaying(!isPlaying)
  }

  const reset = () => {
    setIsPlaying(false)
    setCurrentTime(0)
  }

  const updateParameter = (key, value) => {
    setParams(prev => ({ ...prev, [key]: value[0] }))
  }

  const getSimulationIcon = () => {
    switch (type) {
      case 'wave': return <Activity className="h-5 w-5" />
      case 'particle': return <Zap className="h-5 w-5" />
      case 'neural_network': return <Settings className="h-5 w-5" />
      case 'quantum': return <Activity className="h-5 w-5" />
      default: return <Activity className="h-5 w-5" />
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="w-full max-w-4xl mx-auto"
    >
      <Card className="border-2 border-purple-200 dark:border-purple-800">
        <CardHeader className="bg-gradient-to-r from-purple-50 to-pink-50 dark:from-purple-900/20 dark:to-pink-900/20">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="p-2 bg-purple-600 rounded-lg text-white">
                {getSimulationIcon()}
              </div>
              <div>
                <CardTitle className="text-xl font-bold text-purple-900 dark:text-purple-100">
                  {title}
                </CardTitle>
                <p className="text-sm text-purple-700 dark:text-purple-300 mt-1">
                  {description}
                </p>
              </div>
            </div>
            <Badge className="bg-purple-600 text-white">
              Simulation
            </Badge>
          </div>
        </CardHeader>
        
        <CardContent className="p-6">
          {/* Simulation Canvas */}
          <div className="mb-6">
            <canvas
              ref={canvasRef}
              width={800}
              height={400}
              className="w-full border border-gray-300 dark:border-gray-700 rounded-lg bg-slate-800"
            />
          </div>

          {/* Controls */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Playback Controls */}
            <div className="space-y-4">
              <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200">
                การควบคุม
              </h3>
              
              <div className="flex space-x-3">
                <Button
                  onClick={togglePlayPause}
                  className={`${isPlaying ? 'bg-red-600 hover:bg-red-700' : 'bg-green-600 hover:bg-green-700'} text-white`}
                >
                  {isPlaying ? (
                    <>
                      <Pause className="h-4 w-4 mr-2" />
                      หยุด
                    </>
                  ) : (
                    <>
                      <Play className="h-4 w-4 mr-2" />
                      เริ่ม
                    </>
                  )}
                </Button>
                
                <Button
                  onClick={reset}
                  variant="outline"
                >
                  <RotateCcw className="h-4 w-4 mr-2" />
                  รีเซ็ต
                </Button>
              </div>

              <div className="text-sm text-gray-600 dark:text-gray-400">
                เวลา: {currentTime.toFixed(2)} วินาที
              </div>
            </div>

            {/* Parameter Controls */}
            <div className="space-y-4">
              <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-200">
                พารามิเตอร์
              </h3>
              
              {type === 'wave' && (
                <>
                  <div>
                    <label className="text-sm font-medium text-gray-700 dark:text-gray-300">
                      แอมพลิจูด: {params.amplitude.toFixed(1)}
                    </label>
                    <Slider
                      value={[params.amplitude]}
                      onValueChange={(value) => updateParameter('amplitude', value)}
                      max={3}
                      min={0.1}
                      step={0.1}
                      className="mt-2"
                    />
                  </div>
                  
                  <div>
                    <label className="text-sm font-medium text-gray-700 dark:text-gray-300">
                      ความถี่: {params.frequency.toFixed(1)}
                    </label>
                    <Slider
                      value={[params.frequency]}
                      onValueChange={(value) => updateParameter('frequency', value)}
                      max={5}
                      min={0.1}
                      step={0.1}
                      className="mt-2"
                    />
                  </div>
                </>
              )}

              {type === 'particle' && (
                <div>
                  <label className="text-sm font-medium text-gray-700 dark:text-gray-300">
                    จำนวนอนุภาค: {params.particles}
                  </label>
                  <Slider
                    value={[params.particles]}
                    onValueChange={(value) => updateParameter('particles', value)}
                    max={100}
                    min={10}
                    step={5}
                    className="mt-2"
                  />
                </div>
              )}

              <div>
                <label className="text-sm font-medium text-gray-700 dark:text-gray-300">
                  ความเร็ว: {params.speed.toFixed(1)}x
                </label>
                <Slider
                  value={[params.speed]}
                  onValueChange={(value) => updateParameter('speed', value)}
                  max={3}
                  min={0.1}
                  step={0.1}
                  className="mt-2"
                />
              </div>
            </div>
          </div>

          {/* Information */}
          <div className="mt-6 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
            <h4 className="font-semibold text-purple-900 dark:text-purple-100 mb-2">
              🔬 เกี่ยวกับการจำลองนี้:
            </h4>
            <p className="text-sm text-purple-800 dark:text-purple-200">
              {type === 'wave' && "การจำลองคลื่นแสดงให้เห็นการเคลื่อนที่ของคลื่นไซน์ตามสมการ y = A sin(kx - ωt)"}
              {type === 'particle' && "การจำลองอนุภาคแสดงการเคลื่อนที่แบบวงกลมของอนุภาคหลายตัวพร้อมเส้นทางการเคลื่อนที่"}
              {type === 'neural_network' && "การจำลองโครงข่ายประสาทเทียมแสดงการส่งผ่านสัญญาณระหว่างโหนดในแต่ละชั้น"}
              {type === 'quantum' && "การจำลองควอนตัมแสดงฟังก์ชันคลื่นความน่าจะเป็นและสถานะควอนตัม"}
            </p>
          </div>
        </CardContent>
      </Card>
    </motion.div>
  )
}

export default InteractiveSimulation
