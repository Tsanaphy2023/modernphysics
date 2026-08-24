// Performance optimization utilities

// Debounce function for search and input optimization
export const debounce = (func, wait) => {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Throttle function for scroll and resize events
export const throttle = (func, limit) => {
  let inThrottle
  return function() {
    const args = arguments
    const context = this
    if (!inThrottle) {
      func.apply(context, args)
      inThrottle = true
      setTimeout(() => inThrottle = false, limit)
    }
  }
}

// Intersection Observer for lazy loading
export const createIntersectionObserver = (callback, options = {}) => {
  const defaultOptions = {
    root: null,
    rootMargin: '50px',
    threshold: 0.1
  }
  
  return new IntersectionObserver(callback, { ...defaultOptions, ...options })
}

// Local storage with error handling
export const safeLocalStorage = {
  getItem: (key, defaultValue = null) => {
    try {
      const item = localStorage.getItem(key)
      return item ? JSON.parse(item) : defaultValue
    } catch (error) {
      console.warn(`Error reading from localStorage for key "${key}":`, error)
      return defaultValue
    }
  },
  
  setItem: (key, value) => {
    try {
      localStorage.setItem(key, JSON.stringify(value))
      return true
    } catch (error) {
      console.warn(`Error writing to localStorage for key "${key}":`, error)
      return false
    }
  },
  
  removeItem: (key) => {
    try {
      localStorage.removeItem(key)
      return true
    } catch (error) {
      console.warn(`Error removing from localStorage for key "${key}":`, error)
      return false
    }
  }
}

// Memory usage monitoring (for development)
export const logMemoryUsage = () => {
  if (performance.memory) {
    console.log('Memory Usage:', {
      used: Math.round(performance.memory.usedJSHeapSize / 1048576) + ' MB',
      total: Math.round(performance.memory.totalJSHeapSize / 1048576) + ' MB',
      limit: Math.round(performance.memory.jsHeapSizeLimit / 1048576) + ' MB'
    })
  }
}

// Performance timing utilities
export const measurePerformance = (name, fn) => {
  const start = performance.now()
  const result = fn()
  const end = performance.now()
  console.log(`${name} took ${end - start} milliseconds`)
  return result
}

// Image optimization utilities
export const preloadImage = (src) => {
  return new Promise((resolve, reject) => {
    const img = new Image()
    img.onload = () => resolve(img)
    img.onerror = reject
    img.src = src
  })
}

export const preloadImages = async (srcArray) => {
  try {
    const promises = srcArray.map(preloadImage)
    return await Promise.all(promises)
  } catch (error) {
    console.warn('Error preloading images:', error)
    return []
  }
}

// Bundle size optimization - dynamic imports
export const loadComponent = async (componentPath) => {
  try {
    const module = await import(componentPath)
    return module.default || module
  } catch (error) {
    console.error(`Error loading component from ${componentPath}:`, error)
    throw error
  }
}

// Virtual scrolling helper for large lists
export const calculateVisibleItems = (containerHeight, itemHeight, scrollTop, totalItems, buffer = 5) => {
  const startIndex = Math.max(0, Math.floor(scrollTop / itemHeight) - buffer)
  const endIndex = Math.min(
    totalItems - 1,
    Math.ceil((scrollTop + containerHeight) / itemHeight) + buffer
  )
  
  return {
    startIndex,
    endIndex,
    visibleItems: endIndex - startIndex + 1
  }
}

// Animation frame utilities
export const requestIdleCallback = (callback, options = {}) => {
  if (window.requestIdleCallback) {
    return window.requestIdleCallback(callback, options)
  } else {
    // Fallback for browsers that don't support requestIdleCallback
    return setTimeout(() => {
      const start = Date.now()
      callback({
        didTimeout: false,
        timeRemaining() {
          return Math.max(0, 50 - (Date.now() - start))
        }
      })
    }, 1)
  }
}

// Code splitting utilities
export const loadChunkWithRetry = async (importFn, retries = 3) => {
  for (let i = 0; i < retries; i++) {
    try {
      return await importFn()
    } catch (error) {
      if (i === retries - 1) throw error
      // Wait before retrying
      await new Promise(resolve => setTimeout(resolve, 1000 * (i + 1)))
    }
  }
}

// Service Worker utilities
export const registerServiceWorker = async () => {
  if ('serviceWorker' in navigator) {
    try {
      const registration = await navigator.serviceWorker.register('/sw.js')
      console.log('Service Worker registered successfully:', registration)
      return registration
    } catch (error) {
      console.error('Service Worker registration failed:', error)
      return null
    }
  }
  return null
}

// Cache management
export const cacheManager = {
  set: (key, data, ttl = 3600000) => { // Default TTL: 1 hour
    const item = {
      data,
      timestamp: Date.now(),
      ttl
    }
    safeLocalStorage.setItem(`cache_${key}`, item)
  },
  
  get: (key) => {
    const item = safeLocalStorage.getItem(`cache_${key}`)
    if (!item) return null
    
    const now = Date.now()
    if (now - item.timestamp > item.ttl) {
      safeLocalStorage.removeItem(`cache_${key}`)
      return null
    }
    
    return item.data
  },
  
  clear: () => {
    const keys = Object.keys(localStorage).filter(key => key.startsWith('cache_'))
    keys.forEach(key => localStorage.removeItem(key))
  }
}
