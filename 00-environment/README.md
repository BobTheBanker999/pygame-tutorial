# Environment

In this lesson, we will be setting up the environment for programming our game.  We will install the [Python](https://python.org/) programming language, Pygame and Microsoft's Visual Studio Code an IDE (**I**ntergrated **D**evelopment **E**nvironment) to write the code in.

## Steps

1. [Install Python](https://python.org/download) and follow any installation instructions.

2. Install Pygame (the Python game engine we will be using to create our game).

On a Mac:

Open the Spotlight Search, type 'terminal' and press enter and then type the following line of code at the `$` prompt:
```bash
$ python3 -m pip install -U pygame --user
```
Then to test if it works:
```bash
$ python3 -m pygame.examples.aliens
```

On Windows:

Click the little Windows window at the bottom of the screen and then search up 'command prompt' and press enter. At the `>` prompt, type:
```powershell
> py -m pip install -U pygame --user
> #This may not work; if it does not try the above instructions for Macs
```
Then to test if it works:
```powershell
> py -m pygame.examples.aliens
```

3. Go to [Visual Studio Code Download](https://code.visualstudio.com/download), or as I will be calling it in this tutorial, VS Code, and download the file for your operating system. Your browser should open the .app or .exe file and press `Ctrl-N` on Windows or `Command-N` on a Mac to open up a new, blank text file. Go down to the bar at the bottom where it says 'Plain Text'.  Click on it and type 'python' into the bar that comes up. Press enter and we are ready to start coding!
