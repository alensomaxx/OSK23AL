# Efficient Garbage Collection in OS (Mark & Sweep Visual Simulator)
OS K23AL GARBAGE COLLECTOR PROJECT
## 📌 Project Title
**Efficient Garbage Collection in OS**

---

## 🧠 Introduction
This project simulates an optimized Garbage Collection (GC) mechanism using the **Mark and Sweep** algorithm, designed for educational and visualization purposes. It demonstrates how memory management works in user-space and provides real-time graphical feedback for allocation, collection, and fragmentation handling.

Built with Python, this simulator is modular, lightweight, and a powerful tool for learning about how GC systems work at a conceptual level.

---

## 🎯 Objectives
- Implement a simulated GC system using **Mark and Sweep**.
- Visualize memory allocation, deallocation, and compaction in real-time.
- Minimize fragmentation through memory compaction techniques.
- Benchmark and analyze memory usage across GC cycles.

---

## 🧩 Modules
### 1. Core GC Logic
- Memory block allocation and deallocation
- Mark phase (simulates reachability)
- Sweep phase (collects unmarked memory)
- Compaction for fragmentation reduction

### 2. Monitoring & Analysis
- Real-time memory usage graph
- Fragmentation heatmap view
- GC status updates per cycle

### 3. Simulation Environment
- Interactive GUI using **Tkinter** + **Matplotlib**
- Adjustable GC cycle timing
- Status feedback for each simulation cycle

---

## 💻 Technologies Used
- Python 3
- Tkinter (GUI)
- Matplotlib (Visualization)
- NumPy

---

## 📊 Features
- Live memory allocation and GC cycle
- Real-time visualization of memory fragmentation
- GC stats after each cycle (used memory, reclaimed memory)
- GUI with a "Start Simulation" button

---

## ❓ Real-time vs Real Memory Usage

> ### ⚙️ **Current GC Simulator: What’s It Doing?**
> 
> ✅ It is running in **real-time**, meaning:
> - It **allocates**, **marks**, **sweeps**, and **compacts** memory block-by-block **live per cycle**.
> - It **visualizes each step instantly** with updated graphs and memory layout.
> 
> ❌ But it is **not using your actual system’s memory** or OS processes.
> - It’s using **`random` numbers** to simulate memory allocation sizes, object life cycles, and reachability (i.e., whether an object should be collected).
> - This is done to mimic how a GC works **conceptually**, not to monitor your local PC’s RAM.
> 
> ### 🔬 Why This Is Done:
> - Accessing actual system memory (heap, stack, etc.) is **dangerous**, OS-restricted, and **not portable** across platforms.
> - The project goal is about **designing an efficient GC system**, not monitoring real RAM usage (which would be more like building a system profiler).
> 
> ### ✅ Pros of This Approach:
> - **Safe & Cross-platform**
> - **Easy to visualize and benchmark**
> - **Fully custom logic for GC simulation**
> - Ideal for projects, reports, viva, and extending into ML/optimization later

> ### 💡 Bonus Idea:
> If you *do* want to monitor real memory stats (like how much RAM your Python program is using), we can integrate something like:
>
> ```python
> import psutil
>
> memory_info = psutil.virtual_memory()
> print(f"Available RAM: {memory_info.available}")
> ```
> 
> That gives real data, but it won't be used inside GC simulation logic — more like a system stat overlay.

---

## 🚀 How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/OSK23AL
cd OSK23AL
```

2. Run the simulation:
```bash
python gc_gui.py
```

> **Make sure** you have Python 3 and the required libraries:
```bash
pip install matplotlib numpy
```

---

## 📸 Screenshots
*Add screenshots of GUI window, memory usage graph, fragmentation layout here*

---

## 📈 Future Scope
- Add support for **Reference Counting**, **Generational GC**
- Integrate **real RAM usage stats** using `psutil`
- Add export feature for logs and benchmarking results
- Deploy as a standalone cross-platform desktop app

---

## 🧑‍💻 Author
**ALENSO**  
GitHub: [@alensomaxx](https://github.com/alensomaxx)

---

## 📄 License
This project is licensed under the MIT License.