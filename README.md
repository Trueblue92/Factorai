# Factorai - A simple agent that tries to play facotry games autonomously.
<p> Inspiration for this project was Atari57. How is it possible for an AI to iteratively outperform itself and complete tasks in an enviornment that has such sparse rewards?</p>
<p> Tasks: 
    -1. Control the input an output of a window using python.
</p>


python monitorrun.py
python playback.py .\run1\inputs\keys.txt
python rewardextractor.py .\run1\capture\ .\run1\rewards\rewards.txt
python encodeActions.py .\run1\inputs\keys.txt
python decodeActions.py encodedActions.txt