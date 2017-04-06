#!/bin/bash

# snapshot running processes when cpu usage is high
echo $(top -bn2 -d0.5 | grep Cpu | sed 1d | \
           grep "Cpu(s)" | \
           sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | \
           awk '{print 100 - $1}')
#top -bn1
