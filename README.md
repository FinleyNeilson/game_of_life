Game of Life Simulator
Overview

This project is a simulation of Conway's Game of Life implemented using Pygame. The Game of Life is a zero-player game where its progression is determined by its initial state. This project allows users to interact with the simulation by toggling cell states and controlling the simulation with keyboard and mouse events.
Features

    Interactive Grid: Users can click on cells to toggle their states between alive and dead.
    Real-Time Simulation: Press the spacebar to start or pause the simulation.
    Dynamic Rendering: Cells are drawn in real-time, reflecting their current state.
    Efficient Performance: Optimized rendering and simulation for smooth gameplay.

Getting Started
Downloading the Executable

    Download the Executable: Obtain the pre-built executable from the releases page (or another distribution method).

    Run the Executable:
        Windows: Double-click the game_of_life.exe file.
        macOS/Linux: Open a terminal, navigate to the directory containing the executable, and run:

        bash

        ./game_of_life

Controls

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
    Uses Pygame library for rendering and event handling.
