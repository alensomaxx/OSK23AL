# 🧠 Efficient Garbage Collection in OS  
**(Mark & Sweep + Reference Counting Visual Simulator)**  
**OSK23AL Garbage Collector Project**

---

## 📌 Project Title  
**Efficient Garbage Collection in Operating Systems**

---

## 🧠 Introduction  
This project simulates optimized Garbage Collection (GC) mechanisms using two classic algorithms: **Mark and Sweep** and **Reference Counting**.

It provides real-time graphical feedback for memory allocation, collection, and fragmentation, and is built to help you understand how memory management works in modern OS environments at a conceptual level.  

Developed with Python, this tool uses a lightweight GUI to visualize GC operations and performance metrics cycle-by-cycle.

---

## 🎯 Objectives  
- Implement simulated GC algorithms: **Mark and Sweep** + **Reference Counting**  
- Visualize allocation, deallocation, sweeping, and compaction in real-time  
- Measure GC performance with live **benchmarking**  
- Enable data **export** for reporting and analysis

---

## 🧩 Modules

### 1. Core GC Logic  
- Allocate/deallocate memory blocks dynamically  
- GC Algorithms:  
  - **Mark and Sweep** (mark reachables, sweep unreachables)  
  - **Reference Counting** (collect when reference count = 0)  
- Compaction to reduce fragmentation

### 2. Monitoring & Analysis  
- Real-time memory usage chart  
- Fragmentation heatmap  
- Benchmark: average & per-cycle GC time  
- Cycle-by-cycle status updates

### 3. Simulation & Test Environment  
- Built with **Tkinter + Matplotlib**  
- Adjustable GC speed  
- Run up to 20 GC cycles in real-time  
- Log memory usage + GC time per cycle

---

## 💻 Tech Stack  
- Python 3  
- Tkinter – GUI  
- Matplotlib – Visualization  
- NumPy – Simulation arrays  
- CSV – Log export  
- Time – Benchmarking

---

## 📊 Core Features

### 🧠 Algorithms
- ✅ **Mark and Sweep GC**
- ✅ **Reference Counting GC**
- 🧩 Switch algorithms via dropdown in GUI

### 🎯 Real-Time Visualization
- 📈 Live memory usage line graph
- 📊 Fragmentation layout heatmap
- 🔁 Simulated allocation, GC, compaction per cycle

### ⏱ Benchmarking & Logs
- GC time per cycle and average time across session  
- Final summary upon completion  
- ✅ Export logs as `.csv`

### 🖥️ GUI Interface
- "Start Simulation" button  
- GC algorithm dropdown  
- Benchmark + status labels  
- Data export button

---

## ❓ Real-Time vs System RAM  

> This simulator runs in **real-time**, but:  
> ❌ It does **not use your PC’s actual RAM**  
> ✅ All workloads are randomly generated to simulate memory behavior  
> ✅ Each object has randomly assigned size and reachability (or ref count)  

### Why simulate?
- Safe, cross-platform  
- No OS-level access needed  
- Educational and customizable

> *Bonus idea:* Use `psutil` to monitor real RAM (optional):
```python
import psutil
print(psutil.virtual_memory().available)
```

---

## 🚀 How to Run
```bash
git clone https://github.com/yourusername/OSK23AL
cd OSK23AL
pip install matplotlib numpy
python gc_gui.py
```

---

## 📤 Export Format
On clicking **Export Logs to CSV**, you’ll get:
```csv
Cycle, Used Memory, GC Time (sec)
1, 145, 0.00234
2, 198, 0.00321
...
```

---

## 📸 Screenshots
*Add these for GitHub previews:*  
- GUI window with dropdown + buttons  
- Memory usage graph  
- Fragmentation layout  
- Exported CSV preview

---

## 📈 Future Scope
- Add support for **Generational GC** and **Hybrid GC**
- Real system memory overlays via `psutil`
- Export logs + visuals to **PDF reports**
- Create a web version using **Streamlit** or **Flask**

---

## 📁 Project Structure

```bash
📦 OSK23AL
├── Versions/                  # Archived versions and dev iterations
├── Final-Version1.5.py   # Final Python script with all features
├── OS Report K23AL 15 16 17.pdf  # Full documentation/report
├── README.md                 # Project overview and usage guide
├── /exports                  # Logs exported as CSV
└── requirements.txt          # Python dependencies
```

---

## 🧑‍💻 Author
**ALENSO**  
GitHub: [@alensomaxx](https://github.com/alensomaxx)

---

## 📄 License  
This project is licensed under the **MIT License**
