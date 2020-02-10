### EMOTIV-INSIGHT-EEG-CURSOR-CONTROL ###
Author: Siwen Wang <siwenw2@illinois.edu>

### Explanation of application
The python script maps trained brain activity to cursor movement on screen. Current command includes move left and stay in place. More command such as move up and down, double click etc. can also be added.

### Explanation of Repository
Contains all relavent files besides cortex credential

### File Structure:

* **cortex.py** contains a set of pre-defined functions provided by cortex developer guide
* **cursor_control.py** contains the executable program
* **How_it_work.png** contains a graphical explanation of how the program works
* **pyautogui_test.py** is a testing script for author to understand how to use pyautogui library
* **sample_code.png** contains screen shot of the program and cortex training profile
* **Demo.mp4** is a demonstration of the program running in real time: Action push corresponds to move left; Action Neutral corresponds to stay in place.

### Solution of some of the potential errors may occur:
1. Error: Modulenotfounderror: "No module named websockets" 
   Solution: Install the websockets package in python. Google it if not familar with python install package process.
2. Error: Invalid Profile Name
   Solution: This is due to that I changed the predefined function "load_profile" in cortex.py. To fix the error, open cortex.py and find where the function is declared, change '1stTry' in params to your own profile name. Your profile name can be found in the EmotivBCI app.
3. More to be updated
	
### Note from Author
This project idea is inspired by the work from https://github.com/kevinjycui/EEG-Cursor-Control
I got lots of help by looking at Kevin's code and implementation, and this helped me come up with my own style later on.
This is my first project using Brain Computer Interface to accomplish a very simple yet meaningful task, and I'm greatly inspired by the possibility of this technology.
Cheers,
Siwen


