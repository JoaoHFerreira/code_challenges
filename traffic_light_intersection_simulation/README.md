**Traffic Light Intersection Simulation**

---

### **Objective:**

Simulate a real-world traffic intersection where traffic lights manage vehicle flow in multiple directions. The simulation should **update in real-time**, showing changes in light states (e.g., red to green), and manage timing and logic to avoid collisions.

---

### **Core Requirements:**

1. **Intersection Design:**

   * Simulate at least **two intersecting roads** (e.g., a classic four-way crossroad).
   * Each road should support **two directions**: one for each way (north-south, east-west).

2. **Traffic Light States:**

   * Lights must transition between:

     * **Red** – stop
     * **Green** – go
     * **Yellow/Amber** – prepare to stop
   * Timing for each light cycle must follow a set duration (e.g., Green: 10 sec, Yellow: 3 sec, Red: rest of the cycle).

3. **Real-Time Updates:**

   * The simulation should visually (or textually) reflect the current state of each light.
   * Transitions should be automated without manual input once started.

4. **Coordination Logic:**

   * **Prevent conflicting green lights** (e.g., both north-south and east-west can’t be green at the same time).
   * Include a **safe delay** between light changes if necessary (e.g., all red for 1 sec before switching).

5. **Optional Add-Ons (for more challenge):**

   * Add **pedestrian signals** with "Walk"/"Don't Walk" signs.
   * Include **vehicles** approaching the intersection and responding to light changes.
   * Log or display how many cars pass during each green phase.
   * Add **emergency override** logic for emergency vehicles.

---

### **Learning Focus:**

* **Timers / Delays**: Managing time-based events
* **State Machines**: Keeping track of and transitioning between light states
* **Concurrency (Optional)**: Managing simultaneous actions (e.g., cars on different roads)
* **Real-Time UI or Console Output**: Presenting live updates clearly
* **Code Organization**: Keeping logic modular and maintainable

