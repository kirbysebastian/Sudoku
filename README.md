# Sudoku (Still ongoing...)
A Python language non-GUI Sudoku game.
This project will be based on Peter Norvig's approach of [Sudoku](https://norvig.com/sudoku.html)

## Rules
 - A grid of 9x9 square is initially filled with some digits represented from 1-9 and left with some blank spaces.
 - Puzzle is solved if the squares in each unit are filled with a permutation of digits 1-9 in which no digit can appear more than once in a 'UNIT'
 
 ## Notation and Prelimenary Notion
 - Grid is of 81 sqauares (9x9)
 - 1-9 as column label representation
 - A-I as row label representation
 - SQUARE -> a specific cell in a grid represented by a row and column coordinate ie. 'A3'
 - UNIT -> collection of 9 squares (row, column, and box)
 - PEERS -> a square that share a unit

![](https://raw.githubusercontent.com/kirbysebastian/Sudoku/master/img/unit_vs_peer.png)

 * Every square like 'C2', in the above image, have a total units of 3 and 20 peers.
 * Unit 1 -> A2, B2, C2, D2, E2, F2, G2, H2, I2 (column 2 along with C2)
 * Unit 2 -> C1, C2, C3, C4, C5, C6, C7, C8, C9 (row C along with C2)
* Unit 3 -> A1, A2, A3, B1, B2, B3, C1, C2, C3 (first box along with C2)
* Peers  -> A1, A2, A3, B1, B2, B3, C1, C3, C4, C5, C6, C7, C8, C9, D2, E2, F2, G2, H2, I2

## TODO LIST
- ~~Create a game loader to load an existing Sudoku game.~~
- System arg for loading existing puzzle
- Create a playable game
- Create tests for modules
- Integrate Travis-CI
- Create a Sudoku generator.
- Create a Sudoke solver. *dub* 
