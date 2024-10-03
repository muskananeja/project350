
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

While there were a lot of similarities between our pitches, this meeting highlighted that we also had very different goals with the implementation of the game. Some of us were more interested in the narrative and story aspect of the game, and some of us were more interested in implementing a wide array of mechanics that would allow us to learn more skills and become more proficient programmers. Some of us were simply just interested in making sure our game would be fun to play. This led to another point of contention, leading us to once again question our justification for making this game, whether it aligned with the goals of what the Software Design Practical course was meant to teach students, and what we were trying to gain from the course as well.

At this point, because of the uncertainty surrounding these aspects of the project, we were considering falling back on the back-up plans we were considering. Wahiq suggested we make a general purpose application akin to skyscanner, where if a user is looking for a particular item, the application will collate all the possible online services that can be used to purchase the item so that the user can look for a competitive price. We briefly discussed the possibility of switching to this idea, before agreeing that at this point in time, we’d gone too far to turn back. At this point, we all needed to get onto the same page.

We discussed our plan moving forward and decided to limit the scope of our project to just one level. One single maze that will have all the functionalities we want to showcase. 
