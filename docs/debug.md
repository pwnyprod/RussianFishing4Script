# Debugging for Development new stuff (in work)

### Find Pixel Position on Window for Visual Check

This script helps you find the pixel position on a window for visual checks. It uses the `pyautogui` and `pygetwindow` libraries to get the coordinates of a specified window and display the mouse position relative to that window.

#### Steps:
1. Import the necessary libraries: `pyautogui` and `pygetwindow`.
2. Get the `x` and `y` coordinates of the top-left corner of the window titled 'Russian Fishing 4'.
3. Use `pyautogui` to display the mouse position relative to the window's coordinates.

#### Example:
```python
import pyautogui as pag
import pygetwindow

# Get the top-left corner coordinates of the window
x = pygetwindow.getWindowsWithTitle('Russian Fishing 4')[0].left
y = pygetwindow.getWindowsWithTitle('Russian Fishing 4')[0].top

# Display the mouse position relative to the window
pag.displayMousePosition(x, y)
```