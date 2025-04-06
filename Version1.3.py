import matplotlib.pyplot as plt
import numpy as np
import random
import time

plt.ion()

# Constants
MEMORY_SIZE = 1000
OBJECT_RANGE = (20, 100)
ALLOCATION_CYCLES = 20
DELAY = 0.8  # seconds

class MemoryBlock:
    def __init__(self, size, id):
        self.size = size
        self.id = id
        self.marked = False
        self.start_index = None

class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = []
        self.allocated_memory = []
        self.memory_usage = []
        self.memory_layout = [-1] * self.total_memory  # -1 = free

    def allocate(self):
        size = random.randint(*OBJECT_RANGE)
        start = self.find_space(size)
        if start is not None:
            obj = MemoryBlock(size, len(self.allocated_memory))
            obj.start_index = start
            self.memory.append(obj)
            self.allocated_memory.append(obj)
            for i in range(start, start + size):
                self.memory_layout[i] = obj.id
            return obj
        return None

    def find_space(self, size):
        count = 0
        start = 0
        for i in range(self.total_memory):
            if self.memory_layout[i] == -1:
                if count == 0:
                    start = i
                count += 1
                if count == size:
                    return start
            else:
                count = 0
        return None

    def get_used_memory(self):
        return sum(obj.size for obj in self.memory)

    def mark(self):
        for obj in self.memory:
            obj.marked = random.choice([True, False])

    def sweep(self):
        before = len(self.memory)
        new_memory = []
        self.memory_layout = [-1] * self.total_memory
        for obj in self.memory:
            if obj.marked:
                new_memory.append(obj)
        self.memory = new_memory
        for obj in self.memory:
            start = self.find_space(obj.size)
            if start is not None:
                obj.start_index = start
                for i in range(start, start + obj.size):
                    self.memory_layout[i] = obj.id
        return before - len(self.memory)

    def compact(self):
        self.memory.sort(key=lambda x: x.id)
        self.memory_layout = [-1] * self.total_memory
        current = 0
        for obj in self.memory:
            obj.start_index = current
            for i in range(current, current + obj.size):
                self.memory_layout[i] = obj.id
            current += obj.size

    def simulate_cycle(self):
        self.allocate()
        self.mark()
        collected = self.sweep()
        self.compact()
        used = self.get_used_memory()
        self.memory_usage.append(used)
        return collected, used, self.memory_layout.copy()

# Init
manager = MemoryManager(MEMORY_SIZE)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Memory Usage Plot
line, = ax1.plot([], [], marker='o', label='Used Memory')
ax1.set_title('Real-Time Memory Usage (Mark & Sweep)')
ax1.set_xlabel('Cycle')
ax1.set_ylabel('Used Memory')
ax1.set_ylim(0, MEMORY_SIZE)
ax1.grid(True)
ax1.legend()

# Fragmentation Plot
fragment_display = ax2.imshow(np.zeros((1, MEMORY_SIZE)), aspect='auto', cmap='tab20', interpolation='nearest', vmin=-1, vmax=20)
ax2.set_title('Memory Fragmentation View')
ax2.set_yticks([])

# Real-time loop
for cycle in range(ALLOCATION_CYCLES):
    collected, used, layout = manager.simulate_cycle()

    # Update memory usage graph
    line.set_xdata(range(len(manager.memory_usage)))
    line.set_ydata(manager.memory_usage)
    ax1.set_xlim(0, ALLOCATION_CYCLES)

    # Convert layout to 2D NumPy array and plot
    visual_array = np.array(layout).reshape((1, -1))
    fragment_display.set_data(visual_array)

    plt.draw()
    plt.pause(DELAY)
    print(f"Cycle {cycle+1}: Used = {used}, Collected = {collected}")

plt.ioff()
plt.show()
