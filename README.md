# 👾 Crossfire

**A classic alien-shooter arcade game, built entirely with Python's Turtle module.**

Crossfire is a Space-Invaders-style shooting game where you pilot a ship along the bottom of the screen, dodging enemy fire and blasting through five rows of advancing aliens before they reach you — or your lives run out.

---

## 🎮 Gameplay

- Move your ship left and right to dodge incoming alien missiles
- Fire your own missile straight up to take out aliens
- Aliens march side to side as a formation, shifting downward whenever they hit the screen edge
- Survive as long as possible — you start with **3 lives**, and losing all of them ends the game
- Clear all 50 aliens to **win**
- A starfield background and a flashing "hit" effect on your ship add some arcade polish

---

## 🛠️ Tech Stack

- **Python 3**
- **`turtle`** — rendering, movement, and keyboard input
- **`random`** — star placement and alien missile firing logic
- **`time`** — game loop timing

No external dependencies — everything used is part of Python's standard library.

---

## 📁 Project Structure

```
crossfire/
├── code.py          # Full game logic
└── README.md
```

---

## ⌨️ Controls

| Key           | Action           |
|----------------|------------------|
| `→` Right Arrow | Move ship right  |
| `←` Left Arrow  | Move ship left   |
| `Space`         | Fire missile     |

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (Turtle is included in the standard library, so no extra installs are needed)

### Running the Game

```
git clone https://github.com/rhitamcoder/crossfire.git
```
```
cd crossfire
```
```
python code.py
```

A game window will open — use the arrow keys to move and spacebar to fire. Close the window at any time to end the game.

---

## 🧠 How It Works

- **Alien formation:** 5 rows × 10 columns of aliens are generated at the start, each stored in a list for collision checking and formation movement
- **Collision detection:** Uses simple distance-based checks (comparing x/y coordinates within a threshold) to detect missile-alien and missile-ship hits — no physics engine, just Turtle coordinates
- **Score & lives tracking:** Displayed via dedicated Turtle text objects, updated and re-rendered on every hit
- **Game loop:** A `while True` loop paced with `time.sleep()` and `screen.update()` drives all movement, firing, and collision logic each frame

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
