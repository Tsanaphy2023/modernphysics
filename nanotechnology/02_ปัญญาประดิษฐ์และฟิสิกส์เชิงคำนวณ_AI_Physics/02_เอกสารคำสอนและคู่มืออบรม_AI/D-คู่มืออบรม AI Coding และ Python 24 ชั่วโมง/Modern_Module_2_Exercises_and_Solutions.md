## Module 2: Data Structures & Object-Oriented Programming for Modern AI - Exercises

These exercises are designed to test your understanding of modern Python data structures and Object-Oriented Programming (OOP) concepts, with a focus on their application in AI and machine learning contexts.

---

### Exercise 1: Model Configuration with `dataclasses`

**Objective:** Use `dataclasses` to define a configuration object for an AI model, ensuring type safety and immutability.

**Problem:** You are developing a neural network and need a structured way to store its hyperparameters (learning rate, number of epochs, batch size, and optimizer type). Create a `dataclass` named `ModelConfig` that includes these parameters. Ensure that once a `ModelConfig` object is created, its values cannot be changed (i.e., it should be immutable).

**Requirements:**
1.  Define a `dataclass` named `ModelConfig`.
2.  Include the following fields with appropriate type hints:
    *   `learning_rate`: `float`
    *   `epochs`: `int`
    *   `batch_size`: `int`
    *   `optimizer_type`: `str`
3.  Make the `ModelConfig` immutable.
4.  Create an instance of `ModelConfig` with sample values (e.g., `lr=0.001`, `epochs=10`, `batch_size=32`, `optimizer=\'Adam\'`).
5.  Attempt to change one of its attributes to verify immutability (this should raise an error).

---

### Exercise 2: Base Model Class with Inheritance

**Objective:** Implement a base class for AI models and demonstrate inheritance by creating specialized model classes.

**Problem:** You want to create a flexible framework for different types of AI models (e.g., `Classifier`, `Regressor`). Design a `BaseModel` class that provides a common interface for `train` and `predict` methods. Then, create `ImageClassifier` and `TextRegressor` classes that inherit from `BaseModel` and implement these methods specifically for their tasks.

**Requirements:**
1.  Define a `BaseModel` class with `train(self, data, labels)` and `predict(self, data)` methods. These methods should raise a `NotImplementedError` if not overridden by subclasses.
2.  Create an `ImageClassifier` class that inherits from `BaseModel`.
    *   Override `train` to print "Training Image Classifier..."
    *   Override `predict` to print "Predicting image class..."
3.  Create a `TextRegressor` class that inherits from `BaseModel`.
    *   Override `train` to print "Training Text Regressor..."
    *   Override `predict` to print "Predicting text value..."
4.  Instantiate both `ImageClassifier` and `TextRegressor` and call their `train` and `predict` methods.

---

### Exercise 3: Hyperparameter Validation with `@property`

**Objective:** Use `@property` and setters to encapsulate and validate hyperparameters within an AI model class.

**Problem:** You are building a custom `NeuralNetwork` class. The learning rate (`lr`) for this network must always be between 0.0001 and 0.1 (exclusive). Implement a property for `learning_rate` that enforces this validation rule.

**Requirements:**
1.  Define a `NeuralNetwork` class.
2.  Implement a private attribute `_learning_rate`.
3.  Create a `@property` getter for `learning_rate` that returns `_learning_rate`.
4.  Create a `@learning_rate.setter` that:
    *   Checks if the `value` is within the valid range (0.0001 < `value` < 0.1).
    *   If valid, sets `_learning_rate` to `value`.
    *   If invalid, prints an error message and keeps the `_learning_rate` unchanged.
5.  Test the property by:
    *   Creating an instance of `NeuralNetwork`.
    *   Setting a valid learning rate.
    *   Attempting to set an invalid learning rate (e.g., 0.00005 or 0.5).

---

### Exercise 4: Performance Timing with Decorators

**Objective:** Create a decorator to measure the execution time of AI-related functions.

**Problem:** You often need to measure how long certain parts of your AI pipeline take to run (e.g., data loading, model inference). Write a decorator named `time_execution` that prints the execution time of any function it decorates.

**Requirements:**
1.  Define a decorator `time_execution`.
2.  The decorator should wrap the decorated function and print its execution time in seconds.
3.  Apply this decorator to two sample functions:
    *   `load_large_dataset()`: Simulate loading a large dataset (e.g., `time.sleep(2)`).
    *   `run_inference()`: Simulate running a model inference (e.g., `time.sleep(0.5)`).
4.  Call both decorated functions to observe the timing output.

---

### Exercise 5: Custom Context Manager for GPU Memory

**Objective:** Implement a custom context manager to simulate managing GPU memory allocation and deallocation.

**Problem:** In deep learning, managing GPU memory is crucial. You want to ensure that GPU memory is "allocated" before a task and "deallocated" afterward, even if errors occur. Create a custom context manager named `gpu_memory_manager` that simulates this behavior.

**Requirements:**
1.  Define a class `GPUMemoryManager` that implements the context manager protocol (`__enter__` and `__exit__` methods).
2.  In `__enter__`:
    *   Print "GPU Memory Allocated."
    *   Return `self`.
3.  In `__exit__`:
    *   Print "GPU Memory Deallocated."
    *   Handle potential exceptions: if an exception occurred within the `with` block, print "An error occurred during GPU task." and return `False` to propagate the exception.
4.  Test the context manager with:
    *   A successful block (e.g., print "Running AI task...").
    *   A block that raises an exception (e.g., `raise ValueError("GPU out of memory!")`).


## Module 2: Data Structures & Object-Oriented Programming for Modern AI - Solutions

---

### Exercise 1: Model Configuration with `dataclasses`

```python
from dataclasses import dataclass, frozen

@frozen
@dataclass
class ModelConfig:
    learning_rate: float
    epochs: int
    batch_size: int
    optimizer_type: str

# 4. Create an instance of ModelConfig
config = ModelConfig(learning_rate=0.001, epochs=10, batch_size=32, optimizer_type=\'Adam\')
print(f"Initial Config: {config}")

# 5. Attempt to change one of its attributes to verify immutability
try:
    config.learning_rate = 0.002
except Exception as e:
    print(f"\nAttempting to change learning_rate resulted in an error (as expected): {e}")

# Verify that the original value remains unchanged
print(f"Config after attempted change: {config}")
```

**Explanation:**
By decorating `ModelConfig` with `@frozen` (from `dataclasses`), we make all instances of this dataclass immutable. Any attempt to assign a new value to an attribute after initialization will raise a `FrozenInstanceError`, ensuring that our model\'s configuration remains consistent throughout its lifecycle.

---

### Exercise 2: Base Model Class with Inheritance

```python
class BaseModel:
    def train(self, data, labels):
        raise NotImplementedError("Subclasses must implement the \'train\' method")

    def predict(self, data):
        raise NotImplementedError("Subclasses must implement the \'predict\' method")

class ImageClassifier(BaseModel):
    def train(self, data, labels):
        print(f"Training Image Classifier with {len(data)} samples...")
        # Simulate image classification training logic

    def predict(self, data):
        print(f"Predicting image class for {len(data)} samples...")
        # Simulate image classification prediction logic
        return ["cat", "dog"] * (len(data) // 2) # Example output

class TextRegressor(BaseModel):
    def train(self, data, labels):
        print(f"Training Text Regressor with {len(data)} text entries...")
        # Simulate text regression training logic

    def predict(self, data):
        print(f"Predicting text value for {len(data)} text entries...")
        # Simulate text regression prediction logic
        return [0.5, 0.8] * (len(data) // 2) # Example output

# Instantiate and test
image_model = ImageClassifier()
text_model = TextRegressor()

print("\n--- Image Classifier ---")
image_model.train(data=[1,2,3,4], labels=[0,1,0,1])
predictions = image_model.predict(data=[5,6,7,8])
print(f"Image predictions: {predictions}")

print("\n--- Text Regressor ---")
text_model.train(data=["text1", "text2", "text3", "text4"], labels=[0.1,0.2,0.3,0.4])
predictions = text_model.predict(data=["text5", "text6", "text7", "text8"])
print(f"Text predictions: {predictions}")
```

**Explanation:**
`BaseModel` defines a contract for all AI models, ensuring they have `train` and `predict` methods. `ImageClassifier` and `TextRegressor` inherit this contract and provide their specific implementations. This demonstrates polymorphism, where different model types can be treated uniformly through the `BaseModel` interface.

---

### Exercise 3: Hyperparameter Validation with `@property`

```python
class NeuralNetwork:
    def __init__(self, initial_lr: float = 0.005):
        self._learning_rate = 0.0  # Initialize to a dummy value
        self.learning_rate = initial_lr # Use setter for initial validation

    @property
    def learning_rate(self) -> float:
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value: float):
        if 0.0001 < value < 0.1:
            self._learning_rate = value
            print(f"Learning rate set to: {self._learning_rate}")
        else:
            print(f"Error: Invalid learning rate {value}. Must be between 0.0001 and 0.1 (exclusive). Current LR: {self._learning_rate}")

# Test the property
print("\n--- Neural Network LR Validation ---")
network = NeuralNetwork()
print(f"Initial LR: {network.learning_rate}")

# Set a valid learning rate
network.learning_rate = 0.05
print(f"Current LR: {network.learning_rate}")

# Attempt to set an invalid learning rate (too low)
network.learning_rate = 0.00005
print(f"Current LR: {network.learning_rate}")

# Attempt to set an invalid learning rate (too high)
network.learning_rate = 0.5
print(f"Current LR: {network.learning_rate}")

# Set another valid learning rate
network.learning_rate = 0.002
print(f"Current LR: {network.learning_rate}")
```

**Explanation:**
The `@property` decorator allows us to define getter and setter methods for an attribute, making it behave like a direct attribute access while providing control over how the attribute is accessed and modified. The setter method here enforces the validation rule for the learning rate, preventing invalid values from being assigned and ensuring data integrity.

---

### Exercise 4: Performance Timing with Decorators

```python
import time
import functools

def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Function \'{func.__name__}\' executed in {run_time:.4f} seconds")
        return result
    return wrapper

@time_execution
def load_large_dataset():
    print("Loading large dataset...")
    time.sleep(2)  # Simulate a time-consuming operation
    print("Dataset loaded.")
    return {"data": [i for i in range(100000)]}

@time_execution
def run_inference(model_input):
    print(f"Running inference on {len(model_input)} items...")
    time.sleep(0.5)  # Simulate model inference time
    print("Inference complete.")
    return "Prediction Result"

# Call the decorated functions
print("\n--- Performance Timing ---")
dataset = load_large_dataset()
prediction = run_inference(dataset["data"])
print(f"Received prediction: {prediction}")
```

**Explanation:**
The `time_execution` decorator takes a function as input, defines a `wrapper` function that measures the execution time of the original function, and then returns the `wrapper`. The `@functools.wraps(func)` decorator is used to preserve the original function\'s metadata (like `__name__` and `__doc__`). When `load_large_dataset` and `run_inference` are called, the `time_execution` decorator automatically measures and prints their execution times, which is very useful for profiling AI pipelines.

---

### Exercise 5: Custom Context Manager for GPU Memory

```python
class GPUMemoryManager:
    def __init__(self, device_id: int = 0):
        self.device_id = device_id
        print(f"Initializing GPU Memory Manager for device {self.device_id}")

    def __enter__(self):
        print(f"\nGPU Memory Allocated for device {self.device_id}.")
        # Simulate actual GPU memory allocation here
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"GPU Memory Deallocated for device {self.device_id}.")
        # Simulate actual GPU memory deallocation here
        if exc_type:
            print(f"An error occurred during GPU task: {exc_val}")
            # Return False to propagate the exception, True to suppress it
            return False 
        return True

# Test the context manager with a successful block
print("\n--- Successful GPU Task ---")
with GPUMemoryManager(device_id=0) as gpu:
    print("Running AI task on GPU...")
    # Simulate some GPU-intensive computation
    result = "Task Completed"
    print(f"Task result: {result}")

# Test the context manager with a block that raises an exception
print("\n--- GPU Task with Error ---")
try:
    with GPUMemoryManager(device_id=1) as gpu:
        print("Running AI task on GPU (expecting error)...")
        # Simulate an error condition
        raise ValueError("GPU out of memory!")
except ValueError as e:
    print(f"Caught expected exception outside context manager: {e}")
```

**Explanation:**
The `GPUMemoryManager` class implements the context manager protocol using `__enter__` and `__exit__` methods. The `__enter__` method is called when the `with` statement is entered, simulating memory allocation. The `__exit__` method is called when the `with` block is exited (either normally or due to an exception), simulating memory deallocation. This ensures that resources are properly managed and cleaned up, even if errors occur during the execution of the task within the `with` block. If `__exit__` returns `False`, the exception is re-raised after cleanup; if it returns `True`, the exception is suppressed.
