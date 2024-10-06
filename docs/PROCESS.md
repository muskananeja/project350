
# Looking Back: A Project Process Journal




## Authors

Team Look Back
- [@adityaswamii](https://github.com/adityaswamii)
- [@muskananeja](https://github.com/muskananeja)
- [@wahiqq](https://github.com/wahiqq)
- [@window763](https://github.com/window763)



Behold, the process journal of Look Back; a humble group with a simple goal: to have fun with the Software Design Group Project. This document chronicles the trials and tribulations our group has gone through to ultimately get us to where we are right now. From moments of arguing over mechanics to points where we all stared at a computer screen with awe at the newest implementation, Look Back has gone through a lot to construct our final project: A game designed to dissociate the player from the character they’re playing as. Here is our journey to get there:


## 1st meeting (deciding our name):

The aim of this meeting was twofold:
1) Pick a name for the group
2) Discuss ideas we had for what we could do for the final project

This led us to two approaches to trying to identify a good team name:
- Off the cuff ideas
- Trying to find a name based on a project we all thought was interesting
The off-the-cuff ideas approach was jovial in nature. We suggested names based on things that were in our line of sight or stuff that sounded neat. This approach didn’t seem to be leading to any consensus.

![kalai_naturals](https://github.com/muskananeja/project350/blob/3699a07888238acd17eb84528cdb52c938ede924/docs/Kalai_naturals.jpg "Fig.1 - Image of Kalai Naturals taken from where we were sitting, a name that was suggested for our group")

The second approach gave us a bit more direction because by focusing on the project ideas we had, we also inevitably started discussing our hopes and expectations for what we wanted from the Software Design Project. 

At some point, the idea of making a video game was pitched, and that seemed to generate excitement from all of us. The video game idea made us realize:
- We wanted to work on something primarily creative
- We didn’t want to make a product that had to justify its existence or utility
- A video game seemed like something fun to work on
Using that project idea as a starting point, we started thinking about group names that matched our hopes and dreams for the project. 

At last, we settled on our final name: Look Back

The name was suggested based on the following features:
- It’s the name of a oneshot manga about two artists and the power of stories
- Encapsulated the idea of storytelling and doing something creative
- Was akin to the process of working things out, ie. looking back and seeing where else we could go
- It also sounded pretty cool
While we still weren’t 100% committed to making a video game, we left our first meeting having successfully named ourselves. It was a great start to our project.


## 2nd meeting (brainstorming ideas):

2nd meeting (brainstorming ideas):
The aim of this meeting was to discuss interesting video games we were aware of as well as ideas we had for the game we wanted to make.

Ideas that were pitched:

- 2D side-scroller
- Multiple levels
- Multiple characters
- Pixel-based
- Bird’s eye view of the world (akin to [GTA 2](https://www.rockstargames.com/games/gta2#:~:text=the%20Rockstar%20Newswire-,Screens,-Specifications))
- Possibility of using tools like Unreal Engine
- Doing frontend and backend in javascript
- Making a game based around Krea (eg. a game where Noor chases the player, a game where the player survives a cyclone on campus, etc.)

Games that were discussed:

- Grand Theft Auto 2
    - Was discussed as an example of a game that uses a [top-down view](https://www.rockstargames.com/games/gta2#:~:text=the%20Rockstar%20Newswire-,Screens,-Specifications)
- [Super Mario](https://supermarioplay.com/)
    - Was used as an example of side-scroller elements that could inspire us
- [Fear and Hunger](https://store.steampowered.com/app/1002300/Fear__Hunger/)
    - A dungeon crawler that’s known for being notoriously difficult.
    - Was brought up as an example of a possible aesthetic design
- [Greener Grass Awaits](https://yatoimtop.itch.io/greener-grass-awaits)
    - A game about playing golf while monsters pursue you
    - Game mechanics are intentionally tedious, in order to complement its horror nature by forcing the player to go through the entire process of hitting the ball while a monster is actively pursuing them
    - Was brought up as an example of a game whose mechanics complement the experience that the developer wanted to create
- [Before Your Eyes](https://store.steampowered.com/app/1082430/Before_Your_Eyes/)
    - A game where time passes by every time the player blinks
    - Was brought up as an example of a game with a really interesting mechanic
    - Also used as an example of a game whose mechanic feeds into the narrative of the game


## 3rd meeting (writing our project abstract):

The aim of this meeting was to further refine our project idea in order to fit it within a 5 sentence abstract outline given by Professor Srikumar.

This meeting came after the 5 sentence abstract was introduced in class and we had to provide a preliminary outline within the span of around 5 minutes. Based on the interactions that were had during that class, certain doubts were raised:

1) Would we be able to finish making a video game in the span of two months?
2) Could the video game idea even be fit into the 5 sentence abstract framework?

The doubts raised by this exercise were a bit concerning. In particular, some of us felt like the 5 sentence abstract required us to justify our project despite the fact that in our first meeting, we decided that we didn’t want to work on a project whose existence we felt we needed to justify.

We were largely stumped by the idea of having to identify a problem statement/gap in order to make an argument as to why this particular game should exist, and as such, led some of to question whether making a video game was really something that was expected by the course, or whether it was a valid project at all.

Based on the issues raised, we decided to brainstorm possible back-up projects while for the time being, sticking to the video game idea.

Trying to identify a gap in the related work:
- We discussed ideas for mechanics that we thought seemed cool and didn’t exist in any games we were aware of
- We discussed games that had cool/interesting mechanics that played into the story of the game. (ie. Greener Grass Awaits, Before Your Eyes, etc.)
- We discussed things we wanted to do/explore with games

Eventually, an idea was brought up of a game that punishes the player for messing with it. It was conceptualized as a game where a player is given an opportunity to change base properties of the game through some sort of command line interface, but every time the player does this, the game breaks in a way that makes it harder for the player to play the game. From this root idea, we discussed the idea of not the game punishing the player, but rather the player character itself. The idea was broken down as follows:

- Typically, when a person plays a game, they sort of see themselves as synonymous with the player character
- That isn’t really true though. In a meta-contextual sense, the player isn’t the character, but rather, an entity that manipulates the choices of the character (a game that explores this idea is [Who’s Lila](https://store.steampowered.com/app/1697700/Whos_Lila/))
- What would it be like to make a game that doesn’t just address this disconnect between the player and the character, but tries to dissociate the player from the character? What would it be like to make a game that makes the player realize they aren’t the character they’re playing as?

This question felt like a satisfactory gap to explore, and as such, we found a path forward with our 5 sentence abstract.

Our discussion also led us to talk about possible game loops that we could implement that would allow us to explore this idea of dissociation. We wanted something that could be simple enough for a player to complete by themselves, but with enough iterations, make the player want to mess around and see what else was possible. We discussed the idea of making a platformer or a maze-solving game, and ended up informally settling on the maze-solving game for the simple reason that it would be easy to procedurally generate mazes, allowing for pretty much endless possible levels. With enough time and incentive, the player would hopefully start messing with the game and through that, we could implement mechanics that separate the player from the character.


## 4th meeting (going over gameplay ideas):

This was a series of impromptu meetings where we briefly discussed gameplay ideas using a particular game as inspiration and showed each other code that we were testing out.

The game that was discussed by Muskan was [This is the Only Level](https://thisistheonlylevel.github.io/), a game where the level layout remains the same throughout, but every time the player completes a level, the controls change in the next iteration. This was brought up as a possible idea to disorient the player or as a penalty for certain player actions, but there was also a question as to how it would add to specifically making the player feel distinct from the character. 

In the next impromptu meeting we had, Muskan presented her maze generating program that used a DFS search algorithm to generate the maze. 

Initial implementations:

The maze generating program was written in Javascript using a tutorial by Conner Bailey on YouTube

Resources:
[Tutorial](https://youtu.be/nHjqkLV_Tp0?si=vMLV_VadwQ3Cwj9D)



## 5th meeting (full-game pitches):

The aim of this meeting was for each of us to make a pitch for the game. This pitch included a breakdown of the mechanics, story and gameplay loop.

Wahiq’s pitch:

![wahiq_maze_outline](https://github.com/muskananeja/project350/blob/05ed231db422b2b7dcca054a0b0ba17e518f66d4/docs/Maze_wireframe.jpg "Fig.2.1 - Possible maze framework/wireframe (made using Figma)")

1) The maze will have a starting point and an exit point
2) The blue color character is you. the green one is good and the red one is bad
3) Interaction with the green one will trigger some easy sort of task/game and if the user wins, they will be rewarded with the commands
4) Interaction with the red one will trigger a harder task/minigame and it can be either super hard or super easy.  
5) Player can wish to remove/add a wall based on the scenario. player can also wish to directly pass the wall
6) Player can also remove the beast and also pass them
7) Commands are limited. The user might exhaust them in the first level itself and then in order to achieve more they have to interact with the green creatures.
8) Player can switch to the red or green character and they can control them, but they can only do it for a limited number of times (99 in the screenshot is inaccurate)
9) In total there will be multiple mazes for the player to complete

Shiv’s pitch:

1) Game Title: Turn Back
2) Game starts with the player character outside an entrance. They’re met by an NPC asking them not to go through the entrance. Before the player continues their journey, the NPC gives them a sack of food, a torch and a computer
3) As the player enters, they are asked whether or not they want to turn back. This happens multiple times during the game
4) Basic premise: The character is being manipulated by the player to go into hell (essentially, the player is condemning the character to hell). Because the character doesn’t belong in hell, it has constructed its shape as a series of mazes to make it more difficult for the character to go further in.
5) The penalties that the player faces depends on how many times they use the Command Line Interface tool (which they access using the computer in their inventory). With each use, the character continuously stops responding to player input, eventually starting to sabotage the player by throwing away their food, blowing out their torch, etc. 
6) There are multiple points where the player interacts with NPCs and are asked identity affirming questions. There is already an identity for the player hard-coded into the game. Depending on how congruent the player choices are to the identity pre-defined for the character, different outcomes occur.
7) Eventually ends after 9 CLI uses, the character completely dissociates from player input, gives a monologue about being their own being, and then walks out of hell

![Shiv_pitch_concept](https://github.com/muskananeja/project350/blob/2f0da5864b6763ff43e67d1cf6b1d04f7173004f/docs/Shiv_pitch_concept.jpg "Fig 2.2 - Breakdown of Shiv's game pitch")

Aditya’s pitch:

1) Game surrounds a spirit trapped in hell trying to escape
2) Spirit has the ability to control NPCs
3) The game is split into 9 levels (akin to the nine circles of hell in Dante’s Inferno)
4) Every level has a different biome (eg. Ice level, fire level, etc.)
5) As the player spends time controlling each NPCs, they gradually lose their grasp and the character begins to dissociate from the player in attempts to regain their independence. 
6) To get to the end, the player has to keep switching between NPCs to maintain control.
7) There are multiple different types of NPCs that we can choose to “possess,” each with different types of powers they grant the player access to.
8) Some levels will need the player to be controlling a specific type of character to get through.
9) As the spirit gets closer to escaping hell, its power to control other creatures gets weaker, making the gameplay more challenging. This might show in ways of increasing the cooldown between switching NPCs, losing control to dissociation more rapidly or simply not being able to control some stronger NPCs.

Muskan's pitch

1) The game will have four mini-levels, each connected by mazes:

    - Level 1: A 2D platformer inspired by Mario, where the player navigates through a side-scrolling environment. (Inspired by [Minecraft 2D Beta)](https://www.khanacademy.org/computer-programming/minecraft-2d-beta/1450378472).
    - Level 2: A Flappy Bird-style game where the player must fly through obstacles. (Inspired by [Flappy Bird Noob Version](https://khanacademy.org/computer-programming/flappy-bird-noob-version/4826118257377280)).
    - Level 3: A choice-based Yes/No story game where the player faces moral decisions.
    - Level 4: A final maze to complete the game.

2) The journey begins with a 2D platformer inspired by Mario, where players control a blue character through a side-scrolling environment, followed by a Flappy Bird-style game that tests their skills in flying through obstacles. 
3) After these challenges, players will face a choice-based Yes/No story game, culminating in a final maze that wraps up their adventure. 
4) Throughout the game, players will encounter a green character, representing positive interactions, which triggers easier tasks or mini-games; success in these tasks rewards them with additional commands. 
5) The gameplay loop involves navigating through mazes, completing tasks, and managing limited resources while facing escalating challenges through strategic character interactions and task completion.

![Muskan_pitch_concept](https://github.com/muskananeja/project350/blob/6d6e10e0ad6dc5780e2e668a621c637151b5a18d/docs/Muskan_pitch_concept.jpg "Fig 2.3 - Breakdown of Muskan's game pitch")

While there were a lot of similarities between our pitches, this meeting highlighted that we also had very different goals with the implementation of the game. Some of us were more interested in the narrative and story aspect of the game, and some of us were more interested in implementing a wide array of mechanics that would allow us to learn more skills and become more proficient programmers. Some of us were simply just interested in making sure our game would be fun to play. This led to another point of contention, leading us to once again question our justification for making this game, whether it aligned with the goals of what the Software Design Practical course was meant to teach students, and what we were trying to gain from the course as well.

At this point, because of the uncertainty surrounding these aspects of the project, we were considering falling back on the back-up plans we were considering. Wahiq suggested we make a general purpose application akin to skyscanner, where if a user is looking for a particular item, the application will collate all the possible online services that can be used to purchase the item so that the user can look for a competitive price. We briefly discussed the possibility of switching to this idea, before agreeing that at this point in time, we’d gone too far to turn back. At this point, we all needed to get onto the same page.

We discussed our plan moving forward and decided to limit the scope of our project to just one level. One single maze that will have all the functionalities we want to showcase. 


## 6th meeting (mechanics pitches):

The aim of this meeting was to pitch specific mechanics we wanted to implement for the one level maze we’d be showcasing for the final presentation. Based on what we’d agreed on, the maze design would be as follows:

- A procedurally generated maze with a centroid area, and two sections separated by a gate
- An exit area
- Possibly one NPC
- At least one enemy
- Possibility for minigame interactions between the character and the NPCs in order to get the key for the gate

This seemed like a good idea, though a potential concern was whether we could guarantee that the centroid area and gate would be reachable from the start of the maze. A proposed solution to the gate concern was to have the whole maze be a combination of two separately generated mazes, with the starting cell of the second maze being set adjacent to the to the ending cell of the first maze.

Using this as a basis, we pitched mechanics that we thought would be implementable and could add to the idea of dissociation. The way it was broken down was into two categories: power-ups and penalties. Here were the following proposals:

- Power-up: Teleport
    - Penalty: Screen goes dark
- Power-up: Freeze enemies
    - Penalty: Extra enemy spawns
- Power-up: Show the solution to the maze
    - Penalty: Player loses control for a bit

Some other proposed penalties included:
- Spikes/hazards spawning randomly
- Player gets randomly teleported
- Enemies move faster

There was also a proposed idea to have pads randomly placed around a maze that’s split into multiple sections that the player could use to teleport between different maze areas. A question that still permeated our mind was how to dissociate the player from the character. 

We continued to discuss the idea of implementing a mechanic that allowed the player to take control of different characters within the maze. Something that seemed interesting was to see how a mechanic like that could be utilized along with the Command Line power-ups. For example, if a player is currently controlling a character of the enemy class, and then uses the freeze enemy power-up, they would also freeze due to them currently being in control of an enemy. 

From this discussion, we made a semi-final decision on what kind of mechanics we were going to implement, and following this, our goal was to find resources/methods that could help us implement these mechanics for our game.



## 7th meeting (progress update):

7th meeting (progress update):
The aim of this meeting was to get an update on methods to implement the discussed mechanics. 
At this point, it was decided that we switch from js for our front and backend, instead using python and the pygame library. 

During this meeting it was also suggested we alter the maze generation algorithm. A reason we couldn’t continue with the previous implementation was because:
1) We couldn’t figure out a way to generate that central area that would house the CLI
2) We couldn’t guarantee that every maze generated would have a path to all the areas we wanted the player to be able to reach

As such, it was proposed that instead of running a DFS as a method to generate the maze, if we considered the maze to be a series of edges and vertices that make up a graph, how the vertices got connected together would generate a maze. Because of this, any maze cell, which at max can be bounded by four edges, could always be represented by one of 16 values depending on which edges of the cell were ‘active’, ie. which sides of the cell had walls. Using this idea to set-up the bones of the maze, we could use a recursive backtracking algorithm to generate the maze in such a way that there is always a solution. 

By thinking of the maze as something made up of discrete cells, we could also make it so things we wanted to add like the CLI or a reward or enemy could randomly spawn in any cell within the maze. 

All of this seemed quite promising, but a problem that was raised in class was one of redundancy. With our proposed framework, if two cells were together that had a wall between them, such a configuration would be possible if both cells had that adjoining wall as an ‘active’ edge, or simply if one cell did. As such, there would be a possibility of generating the exact same maze despite the cells constituting that maze being represented by different values. As such, it was recommended we think of the cells as the vertices and the edges from each vertex as the possible paths that can be taken from a given cell.



## Implementation meetings:

This log accounts for a series of meetings that we had as a group to go over implementing mechanics.

Command Line Interface:

- Rationale:
    - The CLI mechanic harkens back to some of the earliest mechanics ideas we had for the game, but also acts as a neat way to sort of incorporate a narrative reason for having the character dissociate from player input.

    - The idea of the Command Line was to sort of give the player a way to ‘mess’ with the game and as such, cause issues to arise. While that initial idea sort of drifted away, now the role that the Command Line takes up is one that exposes the character to the inner workings of the game every time the player uses a command. It works sort of like a moment where the character is able to see the code of the Matrix. This gives them enough incentive/ability to not only break away from the player control, but also try to sabotage the player.

- Implementation:

    - The basic implementation of the CLI mode is handled through the enter_cli_mode function. When activated, this function pauses the main game loop and starts a continuous input loop, allowing the player to type commands.

    - Initially, we wanted the Command Line to be accessed entirely through the game through something like a pop-up menu or additional window, but after implementing it through such that the player inputs commands in the actual terminal, we realized we enjoyed the disconnect that the player has to make in order to input a command in the terminal.

Enemy 1 and Enemy 2:

- Rationale:

    - The rationale for the enemy mechanics were to provide the player more incentives to either finish the game, or in the instance that they’re not able to make it to the end, use the CLI. 

- Implementation:

    - The Enemy1 class is implemented using the Enemy class, which initializes its position, size, and movement attributes. The enemy checks its position relative to the player using the check_player method, which determines if it has reached the player based on their grid positions.

    - The Enemy2 class is built similarly to Enemy1, but with a few key differences in behavior. It has its own check_player method that checks if it is within a specified margin of the player, allowing it to react differently compared to Enemy1.

    - The enemy moves towards the player in the update method, but it also includes logic to prevent it from moving through walls. The check_move method verifies the enemy's current position in the grid and adjusts its movement if it detects walls nearby, using the redirect_movement method to select a new random direction if movement in the intended direction is blocked.

The Commands:

- Rationale:

    - The idea of the commands was to give the player a power-up that they could use to their own volition, but more importantly, incentivise usage of the Command Line feature. The power-ups themselves didn’t need to be anything specific, so we just focused on trying to add things that we felt were possible to implement given the amount of time we had.
    
1) Teleport:

- Implementation:

    - The teleport command requires the player to provide an x and y coordinate to enter in order to teleport to a particular cell. Their inputs are scaled by a factor of 30 to fit the specifications of the maze’s grid space and then the player’s position is updated to match the player’s input.

2) Answer:

- Implementation:

    - The answer command utilizes the solve_maze function in the maze file, which implements a DFS to search through the grid cells in order to find a valid solution to the maze, which then gets highlighted to the player.

3) Freeze:

- Implementation:

    - The freeze command simply sets the enemy speeds to 0.

The Penalties: 

1) Lose Visibility:

- Rationale:

    - The rationale for this penalty would be that the character in taking control for a moment, purposely blows out their torch as an attempt to sabotage the player

- Implementation:

    - Initial idea was to only limit the scope of what the player would be able to see. This would mean that there would be an area encompassing the player that would still be visible but the rest of the maze wouldn’t.
    - Ultimately though, we realized it was simpler to just make the maze background entirely black rather than implementing a reduced visibility parameter, as all we needed to do for that was add a flag for when the maze background was black, and a function to change the maze background to black whenever the teleport command was used.

2) Random Movement:

- Rationale:

    - The purpose of this penalty was to make it seem like the character was taking control of their own movement for a brief period of time, not allowing the player to control them.

- Implementation:

    - The basic implementation of this mechanic simply used a function that would generate random movements for the character when called. This was ultimately the implementation we’ve stuck with, but the final outcome could certainly be improved. A lot of us thought that with this implementation, the character moved too erratically and as such, their movement didn’t seem very deliberate. A proposed solution was to augment the maze solving function to use the character’s current position as the starting point, and the start of the maze as the ending point, in order to find a path from the current player position to the beginning of the maze, and have the character follow that path. Ultimately, this didn’t seem too fruitful a path and was ultimately scrapped.

3) Slow Player Speed/Increase Enemy Speed:

- Rationale:

    - The rationale for this penalty was twofold:
        - Actually make the game much harder
        - Add to the dissociation aspect

    - For these reasons, we chose to not just have the character move slower as a means of sabotaging the player, but also have the enemies get much faster to make it harder for the player. In terms of how it’s currently been implemented, it feels like unless the player can reach the ending within the freeze-enemy cooldown or at least a few seconds after it, they’re very likely to get caught by enemy1. 

- Implementation:

    - Implementation for this mechanic was fairly straightforward with the freeze_penalty function. When this function gets called, the enemy frozen flags get set to False and the enemy and player speeds get updated to match the goals of the penalty.