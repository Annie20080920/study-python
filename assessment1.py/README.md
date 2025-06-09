# Hunt The Wumpus
## Table of Contents:
- Description of the game (introducing about the game)
- Instruction of the game (how to run the game)

### Description of the game:
This game is written in Python and is a text adventure game based on the Hunt The Wumpus game. In this game, the players select the direction related to the caves and get some items such as torch and vegemite to fight and survive.

**Cave:**
<br/>There are 5 different caves:
Cavern, Dungeon, Grotto, Burrow, and Hollow

Here is the map of the caves:
```
Dungeon <--> Grotto <--> Cavern
   │            │
Burrow  <-->  Hollow
```
**Character:**
<br/>There are 2 enemies and 2 friends:
<br/>Enemies: Harry(weakness: vegemite), Edric(weakness: ball)
<br/>Friends: Josephine, Alban

**Item:**
<br/>There are 4 items in each different caves: Torch, Vegemite, Bread, and Ball

**Mini Game:**
<br/>There is a mini game which is 'rock, scissors, paper'

### Instruction of the game:
Here is the rule and way to play the game.

1. Select the direction (one of two directions that provided).
2. If there isn't neither any character nor items to take, talk, or fight, then select it again. <br/>
If not, you have some options depends on the features:
- For Enemy - you can choose 'talk', and 'fight'.
- For Friend - you can choose 'talk', and 'pat' to get a pat from you friend.
- For Item - you can choose 'take' to put it into your bag.
3. If you choose 'fight' against enemy, you should have any item to fight. 
- If it is the one of the weakness of the enemy -> you would win the game.
- If not -> you would lose the game.
4. There is a option that doesn't matter to items or characters: `'play'`(you can choose this even at the start of the game)<br/> If you choose 'play', then you would do the mini game, 'rock, scissors, paper' with the enemy.
- If you win for the mini game -> you would win the whole game, so the game would be ended.
- If you lose for the mini game -> you can continue to play the game for survivng the adventure.
- If you draw with enemy -> you can choose to play it again or not. (if you choose to stop the mini game, the main game would be continued.)

**Therefore, there are two ways to win the game.**