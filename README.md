
# Dueling Pianos Game
Dueling Pianos is a prototype game inspired by Guitar Hero but designed for MIDI pianos. It allows pianists to play real songs and simulate dueling piano battles. This README provides an overview of the codebase and instructions for setting up and running the game.

##  Table of Contents
Features
Requirements
Installation
Usage
Contributing
License
Features
MIDI input handling for real-time piano playing.
Game interface with falling notes displayed on a track.
Timing mechanism to match the tempo of the song.
Multiplayer mode for dueling piano battles.
Support for different keyboard sizes and song variations.
Error handling and exception management.
Requirements
Python 3.9 or above
Libraries: pygame, mido, python-rtmidi, websockets
Installation
Clone the repository:

git clone https://github.com/Toyolo/dueling-pianos.git
Navigate to the project directory:

cd dueling-pianos
Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # For Unix/Linux
venv\Scripts\activate  # For Windows
Install the required libraries:

pip install -r requirements.txt
Usage
Connect your MIDI piano device to your computer.

Run the game:
python main.py
Use the MIDI piano to play the falling notes and match the tempo of the song.

Enjoy the dueling piano battles or single-player mode.

Contributing:
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

### License
MIT License

Feel free to customize and expand this README file based on your specific requirements and the details of your project.