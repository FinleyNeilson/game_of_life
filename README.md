Game of Life Simulator
Overview

This project is a simulation of Conway's Game of Life implemented using Pygame. The Game of Life is a cellular automaton devised by mathematician John Conway. It is a zero-player game, meaning that its progression is determined by its initial state, requiring no further input from humans.

The project allows users to interact with the simulation by toggling cell states and controlling the simulation with keyboard and mouse events. It features real-time rendering of the cellular grid and efficient performance handling.
Features

    Interactive Grid: Users can click on cells to toggle their states between alive and dead.
    Real-Time Simulation: Press the spacebar to start and pause the simulation.
    Dynamic Rendering: Cells are drawn in real-time, reflecting their current state.
    Efficient Performance: Optimized rendering and simulation to ensure smooth gameplay.

Getting Started
Prerequisites

    Python 3.x
    Pygame library

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/game-of-life-simulator.git

Navigate to the project directory:

bash

cd game-of-life-simulator

Install the required dependencies:

bash

    pip install pygame

Usage

    Run the application:

    bash

    python game_of_life.py

    Control the simulation:
        Left Click: Toggle the state of a cell (alive/dead).
        Spacebar: Start or pause the simulation.
        Close Window: Exit the application.

Code Overview

    Cell Class: Manages the state, color, and rendering of individual cells.
    Utility Functions:
        pos_to_cell(pos): Converts screen position to the corresponding cell in the grid.
        alive_neighbours(cell_instance): Counts the number of alive neighbors for a given cell.
        apply_rules(cell_instance): Applies Conway's rules to determine the next state of a cell.
    Main Loop: Handles user input, updates the simulation, and renders the grid.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    Inspired by John Conway's Game of Life.
    Uses Pygame library for rendering and event handlin
