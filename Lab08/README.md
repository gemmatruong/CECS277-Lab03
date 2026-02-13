# 🏁 Rad Racer (Python Console Game) — Lab 08

A Python **console-based racing game** where you choose a vehicle (Car, Motorcycle, or Truck) and **race against AI opponents** down a 100-tile track. Manage speed, avoid obstacles, and use each vehicle’s special ability strategically to finish first.

---

## 🎮 Gameplay Overview

- Pick one of three vehicles:
  - **Lightning Car (Speed 7)** — *Nitro Boost* (1.5× speed)
  - **Swift Bike (Speed 8)** — *Wheelie* (2× speed, risk of wiping out)
  - **Behemoth Truck (Speed 6)** — *Ram* (2× speed and can smash obstacles)
- The track contains **random obstacles (`O`)** in each lane.
- Your vehicle is marked as **`P`** on the track.
- Each turn, choose an action:
  1. **Fast**
  2. **Slow**
  3. **Special Move**
- AI opponents choose actions automatically.
- Winners are displayed in **1st / 2nd / 3rd** place order.

---

## 🧠 Core Concepts Demonstrated

- Object-Oriented Programming (OOP)
  - Inheritance and polymorphism via `Vehicle`, `Car`, `Motorcycle`, `Truck`
- Modular design across multiple files
- Turn-based game loop logic
- Randomized obstacle placement and AI decisions
- Console rendering of a multi-lane race track

---

## 📁 Project Structure

> Your exact filenames may vary slightly—this reflects the imports used in the main program.

