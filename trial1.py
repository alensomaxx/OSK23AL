import matplotlib.pyplot as plt
import numpy as np
import random
import time
#with Internal Instructions
# Constants
MEMORY_SIZE = 1000  # Total memory blocks available
OBJECT_RANGE = (5, 50)  # Size range of each object
ALLOCATION_CYCLES = 30  # Number of allocation/deallocation cycles

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
        # Simulate marking reachable objects (randomly for demo)
        for obj in self.memory:
            obj.marked = random.choice([True, False])

    def sweep(self):
        before_sweep = len(self.memory)
        self.memory = [obj for obj in self.memory if obj.marked]
        after_sweep = len(self.memory)
        return before_sweep - after_sweep

    def compact(self):
        # Simulate memory compaction by reordering objects
        self.memory.sort(key=lambda x: x.marked, reverse=True)

    def simulate_cycle(self):
        self.allocate()
        self.mark()
        collected = self.sweep()
        self.compact()
        used_memory = self.get_used_memory()
        self.memory_usage.append(used_memory)
        return collected, used_memory

# Initialize Memory Manager
manager = MemoryManager(MEMORY_SIZE)

# Run allocation cycles
collected_history = []
for _ in range(ALLOCATION_CYCLES):
    collected, used = manager.simulate_cycle()
    collected_history.append(collected)

# Plot memory usage
plt.figure(figsize=(10, 5))
plt.plot(manager.memory_usage, marker='o', label='Used Memory')
plt.title('Memory Usage Over Time (Mark & Sweep)')
plt.xlabel('Cycle')
plt.ylabel('Used Memory')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
