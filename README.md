# Sovereign Galaxy Simulation

A minimalist N-Body gravity simulation built with Python. This project simulates the gravitational interaction of stars in a 2D space, demonstrating the balance between initial velocity and gravitational collapse.

### The Vision
This project was built to explore a "sovereign nonchalant" approach to programming—focusing on the core laws of physics and watching a self-contained universe unfold from simple rules.

![Uploading e42086ab-a720-4c60-8378-755bfbf08ac3.jpg…]()


### Features
* Newtonian Physics: Uses the standard gravitational force equation with a "softening factor" to prevent numerical explosions.
* Euler Integration: Updates velocity and position based on discrete time steps (DT).
* Cinematic Rendering: Dark-mode visualization using Matplotlib for a "space wallpaper" aesthetic.

### How to Run
1. Clone the repo (or just download the main.py).
2. Install dependencies by running: pip install -r requirements.txt
3. Run the simulation by running: python main.py

### Technical Notes
* Complexity: Currently O(N^2) due to nested loops.
* Integration: First-order Euler method.
* Stability: Uses a softening factor of 0.1 to handle close-range stellar encounters without infinite acceleration.

---

### Learning Log: February 2026
* The "Jump" (DT): Learned that DT is the "frame rate" of the math. A smaller DT means more accuracy, while a larger DT can lead to "Numerical Explosions" where stars teleport to infinity.
* Integration: Implemented the transition from Acceleration -> Velocity -> Position using the Euler method.
* Vectorization vs. Loops: Recognized the O(N^2) bottleneck. While nested loops are easier to read, they struggle with high star counts (N > 500) because they don't utilize the CPU's matrix processing power.
