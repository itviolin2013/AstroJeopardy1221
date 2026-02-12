Project 14: Astronomy Jeopardy Game Generator
Build a fully functional Jeopardy-style astronomy game that generates questions from real astronomy facts and manages gameplay. 
The challenge is parsing factual content to create clever reverse-questions, implementing game logic with proper scoring, and 
maintaining the distinctive Jeopardy style while ensuring educational value.

Students collect astronomy facts from various sources (textbooks, NASA fact sheets, Wikipedia) and organize them into text files 
by category. The system uses string manipulation to transform facts into Jeopardy-style answers, stores questions in nested 
dictionaries organized by category and dollar value, implements game state tracking with NumPy arrays (scores, question availability, 
Daily Doubles), and creates Matplotlib visualizations for score displays and game boards. The LLM API generates creative clues that 
hint at the answer without being too obvious, creates host commentary and fun facts, and evaluates whether player responses are 
acceptable variations of the correct question. Build Question and GameBoard classes to manage game state, implement file I/O to 
save/load game sets, use try/except for handling invalid player inputs, and apply control flow for game rules.

The minimal version creates one game board (6 categories, 5 questions each), uses dictionaries to track which questions have been 
asked, implements basic scoring with NumPy, generates clues via LLM for each fact, and creates a simple text-based interface. 
Advanced versions might implement wagering for Daily Doubles and Final Jeopardy, use string similarity to accept approximate 
answers, build multiple difficulty levels by analyzing fact complexity, create themed weeks, generate contestant backstories 
and banter, implement timer functionality, visualize score progression throughout the game, or build a tournament mode tracking 
statistics across multiple games.
