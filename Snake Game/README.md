**🐍 Snake Game**

  An enhanced version of the classic Snake Game using Python and Tkinter, originally based on BroCode’s YouTube tutorial. Now upgraded with more gameplay features and polish.

**✨ Features**

  • 3-lives system – lose life on hitting wall, obstacle, or yourself  
  • Random obstacle generation with collision  
  • Score, High Score, and Time Survived tracking  
  • Save and Load previous game session (auto-loads on start)  
  • Sound effects for eating and game over (toggle sound)  
  • Themes: Dark, Light, Neon  
  • Difficulty levels: Easy, Medium, Hard  
  • Pause (`P`) and Restart (`R`) support  
  • Clean UI with status bar (score/time/lives)

**⚙️ How to Run**

  • Make sure Python 3 is installed  
  • Install pygame: `pip install pygame`  
  • Place sound files (`eat.wav`, `gameover.wav`) inside an `assets` folder  
  • Run the script: `python snake_game.py`  

**📁 Files Used**

  • snake_game.py – main game file  
  • assets/eat.wav – eating sound  
  • assets/gameover.wav – game over sound  
  • highscore.txt – stores highest score  
  • savegame.json – auto-saves game data (score/lives/time)

**🔗 Credits**

  Based on a tutorial by BroCode on YouTube.  
  Added improvements: multiple lives, obstacles, saving/loading system, difficulty selector, sound toggle, and bug fixes.

**💡 Improvements Done**

  • Fixed lives going into negative values  
  • Lives now reset to 3 on every new game  
  • Prevented collisions from freezing the snake on death  
  • Added obstacle collision detection  
  • Auto-loaded saved game data on start  
  • Improved layout, status bar, and UI responsiveness  
  • Cleaned up redundant code for better readability
