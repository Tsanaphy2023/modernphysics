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
4.  Create an instance of `ModelConfig` with sample values (e.g., `lr=0.001`, `epochs=10`, `batch_size=32`, `optimizer='Adam'`).
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

