# Smart Vacuum Cleaner Simulation

A university project for an Introduction to Artificial Intelligence course, 
simulating a simple reflex agent that cleans two rooms based on their 
dirty/clean state.

## How it works
- The agent perceives the state of **Room A** and **Room B** (dirty or clean), 
  simulated randomly each cycle
- Based on this perception, it decides an action: clean the dirty room(s), 
  or do nothing if already clean
- The agent has a battery that drains by 25% each cleaning cycle
- When battery drops below 25%, the agent stops and recharges to full 
  before continuing
- The simulation runs in a loop, printing each step with a typewriter-style 
  animation for readability

## AI Concept
This is a simple example of a **simple reflex agent**: an agent that maps 
its current percept (room states) directly to an action, without keeping 
memory of past states or planning ahead.

## Tech
- Python (standard library only: `random`, `time`)

## How to run
```bash
python jaroobarqi.py
```
