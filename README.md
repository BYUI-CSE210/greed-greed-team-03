# Greed
 Greed is played according to the following rules.

    -Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
    -The player (#) can move left or right along the bottom of the screen.
    -If the player touches a gem they earn a point.
    -If the player touches a rock they lose a point.
    -Gems and rocks are removed when the player touches them.
    -The game continues until the player closes the window.

## Getting Started
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 rfk 

You can run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
greed-team-03   (project root folder)
+-- greed              (source code for game)
  +-- game              (specific classes)
    +--actor.py
    +--cast.py
    +--gems.py
    +--rocks.py
    +--director.py
    +--keyboard_service.py
    +--video_service.py
    +--color.py
    +--interval.py
    +--point.py
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* Nayara Mateus Nobre (nayara.mnobre@gmail.com)
* Olamilekan Ajibola (aji22001@byui.edu)
* Hannah Mosier(hannah89mosier@byui.edu)
* Paul  Agyare(agy21003@byui.edu)
