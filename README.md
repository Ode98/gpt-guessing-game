# GPT-Powered Guessing Game

## Overview

This GPT-powered guessing game is an interactive Python application that uses OpenAI's language models to play a guessing game with the user. The game involves asking yes/no questions to narrow down what thing the user or AI is thinking of. It can be something specific like 'Godfather the movie' or something broad like 'war'. 

## Features

1. **Different Game Modes**: Choose between asking questions (g), answering questions (c), or making the AI play itself (a).
2. **Dynamic Difficulty**: The game generates objects or concepts with varying difficulty levels for the guessing game.
3. **Interactive Gameplay**: Engage in rounds of questioning to narrow down the possibilities and guess the correct answer.
4. **Flexible Questioning**: The game adapts to previous questions and answers to guide the questioning process effectively.

## Requirements

- Python 3.x
- OpenAI API key and organization ID

## Setup

1. **Install OpenAI Library**: Make sure to have the OpenAI library installed in your Python environment.
   ```bash
   pip install openai
   ```

2. **Configuration**: Update the script with your OpenAI organization ID and API key at the beginning of the code.

## Usage

1. **Start the Game**: Run the script in your Python environment.
   ```bash
   python guessing_game.py
   ```

2. **Choose Game Mode**: At the prompt, choose the game mode:
   - `c`: Answer questions.
   - `g`: Ask questions.
   - `a`: AI plays itself.

3. **Play the Game**:
   - In mode `c`, answer the AI's questions.
   - In mode `g`, ask questions to guess the AI's word.
   - In mode `a`, watch as the AI plays both roles.

4. **Continue or Quit**: Follow the on-screen prompts to continue or quit the game.

## Note

- The game relies on internet access to communicate with OpenAI's servers.
- Usage of the game will consume your OpenAI API quota.

## Contributing

Contributions, bug reports, and feature requests are welcome. Please adhere to the provided code standards and contribute via pull requests or issues on the repository.

## License

This project is open-source and available under MIT. Please review the license terms before modifying or distributing the software.

---

Enjoy playing the GPT-powered guessing game and explore the capabilities of AI in interactive entertainment! (this readme was definitely not generated with chatgpt...)
