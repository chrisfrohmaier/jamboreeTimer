# jamboreeTimer
Code for the countdown timer used in the Soton Astro Jamboree

You can create a fresh environment if you wish, probably a good idea to, but there are only a couple of dependencies. Then install the required packages as follows
```
python -m pip install -r requirements.txt
```

## Run code

First you need to place all the auido files you want to play in a single directory. The code will randomly select a file from this directory and play it when the timer reaches 0 or the "Random" button is clicked.

We then launch the code and point it to the audio file directory as follows:

```
python jamboreeTimer.py -p /path/to/audio/files
```