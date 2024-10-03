
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