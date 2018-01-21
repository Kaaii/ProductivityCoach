# ProductivityCoach
Discord Bot made for HackDavis 2018.
Attempts to increase productivity and goal achievement via time management, particularly in managing gameplay time.

##Available commands (prefix : +)
* [timer]: Starts the Pomodoro timer sequences beginning with a 25 minute session.

* [time_left]: Tells you the remaining time left for a session or break.

* [rest], [cont]: Use when prompted to continue to start the break timer or continue to the next session.

* [end]: Ends current session. 

## Goals:
* Point tracking: Keep track of a users' point gain using this bot, input into [userid]-points.csv to save data. Data format will be constant appends of date, points gained that day, total points so far. User's point gain totals _can not_ go past 0.

* Productivity timer: times study sessions with breaks, notifies you via messages (does not rely on your current status changes). Add command to stop productivity timer. For each study session completed, award 10 points. For each break, award 2 points.

* Gameplay timer: Reminds you when you are playing a game if gameplay time exceeds a certain time frame (customizable, default 2 hours? 1 hour?). If user stops playing a game <2 hours? 2.5 hours?, award 10 points with -5 points for every 10 minutes afterwards. Can go to negatives and will penalize the user's total point gain.  

* Motivational blurbs: Messages you with daily motivational quotes/pictures/etc.

* Goal reminders: Set multiple goals with deadlines (if no deadline, then bot will prompt for goal completion at weekly intervals). Bot will do several reminders at different intervals leading up to the deadline, and ask if user has completed the goal (or user can "command" the bot they completed a goal). For each goal completed, award user 10 points + 5 points per day done earlier. If goal is within _same day_, requires a time (in military) for deadline. If no deadline given, bot will assume deadline is at 23:59 of that day. No points are awarded for goals set with times <1 hour of current time.

* Fitness coaching: Starts and manages a simple fitness plan. (If time allows, add data tracking by inputting date, fitness data into a .csv file for analysis or graphical display).

* Gaming wellness: If session time is over a certain length of time, prompts user to do certain stretches/light exercise

* Diet input: When command is initiated, waits for user input of a list of caloric intake. Possibly combinable with fitness coaching data. Only to be implemented if time allows.
