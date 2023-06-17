#!/bin/bash

# Apply wallpaper using wal
wal -R &

# Start picom
picom --config ~/.config/picom/picom.conf &

# Start eww daemon
eww daemon &
