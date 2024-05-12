# PlayerAgent repo

## This repo is for an AI Player ageent for Warhammer 40k. It is open for addtional developers, testers and strageists

## Justification:

# New and casual players:
1. New users are hesistant to ask others to play, out of fear of being rejected. 
2. Scheduling can fail
3. No one is available at the time, or waiting for someone to show
4. Players may be brand new, and require large amounts of patience

# Experienced players (future development with AI)
1. An anytime, anywhere training option
2. Novel playstyles by AI triggering learning new strategies for Player
3. Integrate with TTS, or if can't, a standalone simulator

# To complete the basic program, the project will be initially contrained by:

1. Only Core rules 
2. 200pt army size, no CP, no Battleshock, no markers
3. One predefined board and terrain
4. User imports roster, program generates enemy roster
5. Used as a companion for IRL play
6. User controls their battle steps, and enters the results
7. Program controls its battle steps
8. User decides who wins and stops battle

# Things to find out:
1. Can this code be integrated into TTS to simulate the 2nd player?
2. What langauge is best?
3. Is this best to start with a phone app (Android)?


# Directory structure

pyproject.toml
\src
    \agent
	  ....source code
\tests
	  ....pytests
	  

# Pytest command
python -m pytest -vv


