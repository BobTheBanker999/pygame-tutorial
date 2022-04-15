# Creating our game window

If we are going to make a video game, we will want to have some graphics so that the users can see the player moving around and the enemies moving and trying to kill the player. Now we need to make the window. Let's get started on the code!

## Code
First, we will need to import the pygame library. Go into your 'Untitled-1' Python file in VS code we created in chapter 00 and type:

```python
# Import needed modules
import pygame
import random # We will need this for later
from pygame.locals import *
```

Now we will need to create a couple of constant variables, `SCREEN_W` and `SCREEN_H`, to set the width and height for our window:

```python
# Create constants for screen width and height
SCREEN_W = 800
SCREEN_H = 600
```

Now we need to initialize pygame so that it is ready to be used in our game:

```python
# Initialize pygame
pygame.init()
```
Now we can set up a clock to manage frame rate:

```py
# Set up the clock
clock = pygame.time.Clock()
```

And now we can create the screen:

```python
# Create screen
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
```
You will probably want to have the window say something at the top other than 'pygame window.' Here is how to do that:

```python
# Set Screen title
pygame.display.set_caption("CAPTION HERE") # Put your caption here
```
If you ran the code now, you would not be able to actually close the window. Let's fix that:

```python
# Boolean to keep Main loop running
running = True

# Main loop
while running:

    # Scan all game events
    for event in pygame.event.get():

        # Quit if user closes the window or presses ESC.
        if event.type == QUIT:
            print("Why did you leave me, buddy? :(")
            pygame.quit()
        
```

I, for one, want my window to also close when the user presses `esc`. If you want something like that, type:

```python
	# Look for keypresses
        key = pygame.key.get_pressed()
        
        if key[K_ESCAPE]:
            print("Why did you leave me, buddy? :(")
            pygame.quit()
```

Now that we have a window, we can run the code!

## Running the code

Before we run the code, we must save our file. Press `Ctrl-S` on Windows or `Command-S` on MacOS to save the file. When prompted, save it to your desktop as `main.py`. Then, open the Terminal or Command Prompt again and type:

```bash
cd Desktop
python3 main.py
```
This should open up a plain, black window that is titled `CAPTION HERE`. Congrats! You now have a window where we can put the player in the next lesson! 

*You can find the code in 01-window/main.py*
