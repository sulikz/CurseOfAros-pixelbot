# CurseOfAros-pixelbot

UPDATE: Not finished and outdated, but you can look it up for reference


This is an image recognition bot for Curse of Aros mobile game. It is intended to use with Bluestacks emulator.
I have never finished this project, to run it you would need to update Coordinates to your resolution, or even better rewrite it to set it dynamically based on BlueStacks window. Currently it's hardcoded for my screen.

Implemented features:

- farm specific mobs by searching a box around player for a color specific to this monster
- auto heal
- auto loot

I also created what I would call an 'intelligent macro':
- chop trees/mine ores
- smelt ores
- forge bars

For example, chopping/mining would run character from the bank to the tree/ore spot, and then randomly move between the trees/ores to get it until full inventory, at which it would suicide, go to bank, leave items and then go back to the same spot. Smelting/forging was similar process to this
