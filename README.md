# ProductivityCoach
Discord Bot made for HackDavis 2018.
Attempts to increase productivity and goal achievement via time management, particularly in managing gameplay time.
Coded in Python.

## Available commands (prefix : +)

### Study:
* [timer]: Starts the Pomodoro timer sequences beginning with a 25 minute session.

* [time_left]: Tells you the remaining time left for a session or break.

* [end]: Ends current session.

### GameTimer:
* [playtime]: Lets you know how long you've been playing. Only usable when bot is there to see a change in status (from not playing to playing). If not playing any games, will let you know for how long.

* [free]: Changes your 'status' to the bot to not send you game reminders. Use the command [busy] to set this again.

### Goals:
* [goal] [add/remove]: Adds or removes a goal from 'to-do list'. After adding a goal, prompts user for setting a deadline for the goal in MM-DD-YYYY format. Will send a reminder to the user on the deadline.

* [todo]: View the to-do list and deadlines.

## Work left:
* Detect when a user goes idle and automatically change the toggle in game_timer to 'free', and back to 'busy' when user goes out of idle while in-game.

* Prevent user from setting deadlines that are already past.

* Allow user to not set a deadline (defaults to just being on to-do list)

* Allow user to add more reminders before a deadline (alert x days before deadline.)

## Ideas:
* Points system: Keep track of a users' point gain using this bot, input into [userid]-points.csv to save data. Data format will be constant appends of date, points gained that day, total points so far. User's point gain totals _can not_ go past 0.

* Productivity timer: times study sessions with breaks, notifies you via messages (does not rely on your current status changes). Add command to stop productivity timer. For each study session completed, award 10 points. For each break, award 2 points.

* Gameplay timer: Reminds you when you are playing a game if gameplay time exceeds a certain time frame (customizable, default 2 hours? 1 hour?). If user stops playing a game <2 hours? 2.5 hours?, award 10 points with -5 points for every 10 minutes afterwards. Can go to negatives and will penalize the user's total point gain.  

* Motivational blurbs: Messages you with daily motivational quotes/pictures/etc.

* Goal reminders: Set multiple goals with deadlines (if no deadline, then bot will prompt for goal completion at weekly intervals). Bot will do several reminders at different intervals leading up to the deadline, and ask if user has completed the goal (or user can "command" the bot they completed a goal). For each goal completed, award user 10 points + 5 points per day done earlier. If goal is within _same day_, requires a time (in military) for deadline. If no deadline given, bot will assume deadline is at 23:59 of that day. No points are awarded for goals set with times <1 hour of current time.



#Repos used:
discord.py
