import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Enable interactive mode
plt.ion()

# Constants
MEMORY_SIZE = 1000
OBJECT_RANGE = (5, 50)
ALLOCATION_CYCLES = 30
DELAY = 0.5  # seconds between frames for visualization

# Memory block representation
class MemoryBlock:
    def __init__(self, size, id):
        self.size = size
        self.id = id
        self.marked = False

# Memory Manager
class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = []
        self.allocated_memory = []
        self.memory_usage = []

    def allocate(self):
        size = random.randint(*OBJECT_RANGE)
        if self.get_used_memory() + size <= self.total_memory:
            obj = MemoryBlock(size, len(self.allocated_memory))
            self.memory.append(obj)
            self.allocated_memory.append(obj)
            return obj
        return None

    def get_used_memory(self):
        return sum(obj.size for obj in self.memory)

    def mark(self):
        for obj in self.memory:
            obj.marked = random.choice([True, False])

    def sweep(self):
        before_sweep = len(self.memory)
        self.memory = [obj for obj in self.memory if obj.marked]
        after_sweep = len(self.memory)
        return before_sweep - after_sweep

    def compact(self):
        self.memory.sort(key=lambda x: x.marked, reverse=True)

    def simulate_cycle(self):
        self.allocate()
        self.mark()
        collected = self.sweep()
        self.compact()
        used_memory = self.get_used_memory()
        self.memory_usage.append(used_memory)
        return collected, used_memory

# Initialize manager
manager = MemoryManager(MEMORY_SIZE)

# Set up the real-time plot
plt.figure(figsize=(10, 5))
line, = plt.plot([], [], marker='o', label='Used Memory')
plt.title('Real-Time Memory Usage (Mark & Sweep)')
plt.xlabel('Cycle')
plt.ylabel('Used Memory')
plt.ylim(0, MEMORY_SIZE)
plt.grid(True)
plt.legend()

# Run GC cycles with real-time updates
for cycle in range(ALLOCATION_CYCLES):
    collected, used = manager.simulate_cycle()

    # Update plot data
    line.set_xdata(range(len(manager.memory_usage)))
    line.set_ydata(manager.memory_usage)
    plt.xlim(0, ALLOCATION_CYCLES)
    plt.draw()
    plt.pause(DELAY)  # Pause to simulate real-time
    print(f"Cycle {cycle+1}: Used Memory = {used}, Collected = {collected}")

plt.ioff()  # Turn off interactive mode
plt.show()  # Show final graph
