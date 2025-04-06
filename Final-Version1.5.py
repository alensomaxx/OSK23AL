import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import random
import time
import csv

# Constants
MEMORY_SIZE = 1000
OBJECT_RANGE = (20, 100)
ALLOCATION_CYCLES = 20
DELAY = 500  # milliseconds

class MemoryBlock:
    def __init__(self, size, id):
        self.size = size
        self.id = id
        self.marked = False
        self.start_index = None

class RefCountedObject:
    def __init__(self, size, id):
        self.size = size
        self.id = id
        self.ref_count = random.randint(0, 2)
        self.start_index = None

class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory = []
        self.allocated_memory = []
        self.memory_usage = []
        self.memory_layout = [-1] * self.total_memory
        self.benchmark_times = []

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
        start_time = time.time()
        self.allocate()
        self.mark()
        collected = self.sweep()
        self.compact()
        used = self.get_used_memory()
        self.memory_usage.append(used)
        end_time = time.time()
        self.benchmark_times.append(end_time - start_time)
        return collected, used, self.memory_layout.copy()

class GCManagerWithReferenceCounting(MemoryManager):
    def allocate(self):
        size = random.randint(*OBJECT_RANGE)
        start = self.find_space(size)
        if start is not None:
            obj = RefCountedObject(size, len(self.allocated_memory))
            obj.start_index = start
            self.memory.append(obj)
            self.allocated_memory.append(obj)
            for i in range(start, start + size):
                self.memory_layout[i] = obj.id
            return obj
        return None

    def simulate_cycle(self):
        start_time = time.time()
        self.allocate()
        collected = self.collect_garbage()
        self.compact()
        used = self.get_used_memory()
        self.memory_usage.append(used)
        end_time = time.time()
        self.benchmark_times.append(end_time - start_time)
        return collected, used, self.memory_layout.copy()

    def collect_garbage(self):
        before = len(self.memory)
        new_memory = []
        self.memory_layout = [-1] * self.total_memory
        for obj in self.memory:
            if obj.ref_count > 0:
                new_memory.append(obj)
        self.memory = new_memory
        for obj in self.memory:
            start = self.find_space(obj.size)
            if start is not None:
                obj.start_index = start
                for i in range(start, start + obj.size):
                    self.memory_layout[i] = obj.id
        return before - len(self.memory)

class GCVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Efficient Garbage Collector Simulator")
        self.geometry("1000x800")
        self.cycle = 0
        self.manager = None
        self.selected_algo = tk.StringVar(value="Mark and Sweep")
        self.start_time = None
        self.setup_ui()
        self.after_id = None

    def setup_ui(self):
        control_frame = ttk.Frame(self)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="GC Algorithm:").grid(row=0, column=0, padx=5)
        algo_dropdown = ttk.Combobox(control_frame, textvariable=self.selected_algo, values=["Mark and Sweep", "Reference Counting"], state="readonly")
        algo_dropdown.grid(row=0, column=1, padx=5)

        self.start_button = ttk.Button(control_frame, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=0, column=2, padx=10)

        self.export_button = ttk.Button(control_frame, text="Export Logs to CSV", command=self.export_logs)
        self.export_button.grid(row=0, column=3, padx=10)

        self.status_label = ttk.Label(control_frame, text="Status: Ready")
        self.status_label.grid(row=1, column=0, columnspan=4, pady=5)

        self.benchmark_label = ttk.Label(control_frame, text="Benchmark: -")
        self.benchmark_label.grid(row=2, column=0, columnspan=4)

        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(10, 6))
        self.fig.tight_layout(pad=3.0)

        self.line, = self.ax1.plot([], [], marker='o', label='Used Memory')
        self.ax1.set_title('Memory Usage Over Time')
        self.ax1.set_xlabel('Cycle')
        self.ax1.set_ylabel('Used Memory')
        self.ax1.set_ylim(0, MEMORY_SIZE)
        self.ax1.legend()
        self.ax1.grid(True)

        self.fragment_display = self.ax2.imshow(np.zeros((1, MEMORY_SIZE)), aspect='auto', cmap='tab20', interpolation='nearest', vmin=-1, vmax=20)
        self.ax2.set_title('Memory Fragmentation')
        self.ax2.set_yticks([])

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

    def start_simulation(self):
        self.cycle = 0
        algo = self.selected_algo.get()
        if algo == "Reference Counting":
            self.manager = GCManagerWithReferenceCounting(MEMORY_SIZE)
        else:
            self.manager = MemoryManager(MEMORY_SIZE)

        self.start_time = time.time()
        self.run_cycle()

    def run_cycle(self):
        if self.cycle < ALLOCATION_CYCLES:
            collected, used, layout = self.manager.simulate_cycle()
            self.line.set_xdata(range(len(self.manager.memory_usage)))
            self.line.set_ydata(self.manager.memory_usage)
            self.ax1.set_xlim(0, ALLOCATION_CYCLES)

            visual_array = np.array(layout).reshape((1, -1))
            self.fragment_display.set_data(visual_array)

            avg_time = np.mean(self.manager.benchmark_times)
            self.status_label.config(text=f"Cycle {self.cycle+1}: Used={used}, Collected={collected}")
            self.benchmark_label.config(text=f"Avg GC Time: {avg_time:.4f} sec")

            self.canvas.draw()
            self.cycle += 1
            self.after_id = self.after(DELAY, self.run_cycle)
        else:
            total_time = time.time() - self.start_time
            self.status_label.config(text="Simulation Completed")
            self.benchmark_label.config(text=f"Total Time: {total_time:.2f} sec | Avg GC Time: {np.mean(self.manager.benchmark_times):.4f} sec")

    def export_logs(self):
        if not self.manager or not self.manager.memory_usage:
            self.status_label.config(text="No data to export yet!")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Cycle", "Used Memory", "GC Time (sec)"])
            for i, (mem, t) in enumerate(zip(self.manager.memory_usage, self.manager.benchmark_times), start=1):
                writer.writerow([i, mem, round(t, 6)])

        self.status_label.config(text=f"Logs exported to: {file_path}")

# Run the final GUI
if __name__ == "__main__":
    app = GCVisualizer()
    app.mainloop()