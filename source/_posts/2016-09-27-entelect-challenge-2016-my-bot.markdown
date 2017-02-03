---
layout: post
title: "Entelect Challenge 2016"
date: 2016-09-27 21:34:35 +0200
comments: true
categories: AI, South Africa
---

This year I participated in the [Entelect AI challenge](todo link), a yearly South African programming competition that has been running for five years now where programmers can match their skills in writing an autonomous agent competing in a classic computer game. This year was bomberman, but previous years competitions were based on tron light cycles, tanks, space invaders etc.

My bot unfortunately did not reach the final, but I am nevertheless not too disappointed in my bots performance, and in this post I will give a quick run down on the approach I took with developing my entry.

<h2>The game</h2>

The full list of rules can be found [here](todo link), but what follows is a short description:
The game is turn based and loosely based on bomberman, where between two to four contestants control an avatar. {% img center /images/avatars.png %}

Each avatar can navigate a 21x21 map containing destructible {% img center /images/wall.png %}
and indestructible walls {% img center /images/iwall.png %}
by moving up, down, left and right. Each avatar can also plant a bomb {% img center /images/bomb.png %}
, thereby either attempting to blow up his opponent, or a destructible wall possibly uncovering a powerup (granting the avatar more bombs or longer fuses on his  bombs). {% img center /images/powerups.png %}
An avatar can also choose to detonate his bomb with the shortest fuse.

The complete map might look something like this: {% img center /images/Sample_map.png 600 %}

Points are scored for blowing your opponent up, blowing up destructible walls and exploring the map.

The competition also had a GUI component, and the images you see here is from the winner of the GUI competition (Ruan Moolman) and reproduced with his kind permission. 


<h2>My approach</h2>

<h4>Markov decision process</h4>
For a great introduction to Markov decision processes (MDP), you are free to have a look at [Introduction to Artificial Intelligence](https://www.udacity.com/course/intro-to-artificial-intelligence--cs271) presented by Peter Norvig and Sebastian Thrun. 

MDP's as a concept is quite simple. You assign a desireable objective, like say a powerup a value. Then each square next to this powerup gets a value equal to the value you assigned to the powerup minus a penalty value. Two squares away from the powerup gets assigned a value minus two times the penalty and so forth.

{% img center /images/mdp_concept.png %}

You have to run the algorithm a couple of times over your map until the values settle, because with multiple powerups you want to give each square it's highest possible value (i.e. the value it derives from the closest powerup to it). Then not only powerups can have assigned values, but any other objective (like destructible walls) as well, and you can assign the objectives different weights based on their perceived importance (and given I have done very little rigorous analysis about what weight each objective should have or what the penalty should be, the final weighting was admit-ably a bit of a thumb suck.   

What you end up with is a map that looks as follows (based on the game map above):

{% img center /images/mdp_map.png %} 

This is basically a map with hills and valleys, with the hills being desirable locations, and the valleys less desirable. All that is left for the AI to do is then move in the direction of the steepest ascend to reach the closest most desirable location. This is great as a relatively simple and robust mechanism to decide what my bot's next action should be. As a side bonus, it is independent of my bot's location, so it could also be used to guess what my opponents next move might be as well...

<h4>Decision tree overlay</h4>
On top of the Markov decision tree, I implemented a basic [expert system](https://en.wikipedia.org/wiki/Expert_system) (if this then do that). I had basically only 5 general rules:

	Should we blow a bomb

	Can we steal a wall

	Can we blow up an enemy player

	Should we plant a bomb
 
	Dont walk into explosions


The problem with this kind of ruleset, is it becomes very complex very quickly, and cannot accommodate all the edge cases you might face. A rule that works in one situation might be less than ideal in another. For instance, to determine if my bot should plant a bomb, I first only checked if the square is in range of a destructible wall. But what if one square on you can blow two (or more) wall simultaneously, or if there is a power up, should the bot pick up the power up first, or if there is another player close by, and on and on. Hence the success of neural nets for these kinds of problems. Because having a human write a ruleset for something like this is a never ending job. Nevertheless my basic rule set had to suffice for the competition.   

<h4>Multiround look ahead</h4>
Lastly my bot could predict up to nine rounds forward from the current game state. The competition rules stated that each bot had up to two seconds each round to determine its next move. Remember a bot had the choice to either move up, down, left, right, do nothing, plant or blow a bomb, thus seven actions; and there were up to four bots in each game; and bombs had a maximum timer of 9 rounds. Thus if you wanted to brute force your solution by working out the best possible move out of all the possible moves (min maxing), you had to compute (7 x 4e9) = 2e37 positions every two seconds. Now modern computers are fast, but not that fast. 

Modern computer clockcycles are about 1 Ghz, and lets say you have an octacore processor, and you are uber programmer (so you can compute a position every clock cycle and can code perfect multithreaded code with no overhead), that still only gives you about 2e31 clock cycles every two seconds to work with.

So clearly brute forcing every possible game state wasn't going to cut it. So I had to reduce the search space, by not computing the impossible moves (bots can't walk through walls), and only guessing my opponent bots most probable move, and only calculating three possible moves for my own bot, and then deciding which of those three was my best next move.
 
That cuts the worst case problem space to about 6e9 = 2e23 game states I had to calculate. Not quite doable for the worst case, but for most cases I could reduce the search space by not calculating future states where I had already died. From the 51 test cases I wrote for my bot, most ran under 200 ms, some to 700ms and one or two over two seconds, where I had code detecting it took to long and just went with the best result I had at that stage.        

<h2>Results</h2>

Like I said, I didn't get very far in the competion. (Be sure to view these videos using the desktop client, the mobile client is disabled for some reason)
My bot competed in four rounds, top two goes through. Rounds 1 and 2 it dit quite well:

[Round 1](https://youtu.be/9TiEMZNVI24?t=2h21m38s)

[Round 2](https://youtu.be/9TiEMZNVI24?t=2h41m38s)

Rounds 3 and 4 did not go so well, though as a consolation my bot was leading in points just before the end.

[Round 3](https://youtu.be/9TiEMZNVI24?t=3h31m50s)

[Round 4](https://youtu.be/9TiEMZNVI24?t=3h50m07s)

<h2>Limitations of my approach</h2>

 - Writing rule sets like I have done is error prone and cannot catch all edge cases even in a relatively simple game environment such as this one.
 - Even though brute forcing every game state is not possible, my approach of aggressively cutting the solution space does come with its own set of problems. You want to be able to look 9 moves ahead in order not to get trapped in a corridor by your own bomb. But you also want to calculate each possible move your opponent might make not to be caught by surprise. Thus a better approach would have been more brute force calculation for one or two rounds ahead, and then minimal calculation for longer horizon predictions. (If that makes sense)
 - Calculating the best possible move (brute force min maxing) seems to still be a better solution than using Markov decision process to calculate a bots next move. MDP's is simple and provides a general good solution, but in a competitive space it does not necessarily provide the best move which is what you want to win. 


<h2>Lessons learned in general</h2>

 - Use unit tests to test your game logic. Not fine grained unit testing, basic functional testing, it will speed up your ability to test multiple strategies for your bot knowing the basic soundness of your solution is still intact.
 - In addition to writing the bot, I had to write a game viewer, unit tests, get the game harnass working, update periodically to the latest game engine, test multiple strategies, fix bugs, play test (a lot). The point being that it will take more time than you think to provide a competitive solution.
 - Compete against other competitors as early as you can before the actual competition, even if your bot is not quite ready yet. The lessons you will learn are invaluable and the earlier you can learn them the better.  
 - Do not rest on your laurels, if your bot performs well early before the competition, keep working.
 - Plan to have your bot done a week before the competition closes. There are always issues uploading your bot at the very end, and you make mistakes if you still try to implement major functionality right before the end.

<h2>Why not a neural network</h2>

Neural networks, especially deep neural nets are actually a very good solution for a competition such as this one. Unfortunately in 2016, by the time I learned of [OpenAI](https://openai.com/blog/), [Tensorflow](https://www.tensorflow.org/) and the [Sedel Go competition](https://www.wired.com/2016/03/googles-ai-wins-fifth-final-game-go-genius-lee-sedol/), I was already quite a far with my bot not wanting to trash it all and start again.

I think if I have time to enter such a competition again, I would like to see if I can train a neural net and see how competitive it could be. It is without a doubt nearly all entries of these competitions is already mostly deep neural nets, with the only reason this competition didn't have much neural net entries (to my knowledge) yet is because South Africa is a small market with a fairly small developer community lacking the necessary skill set / experience (please correct me if I am wrong).      

Code is available on [Github](https://github.com/kabousvlieg/2016-Bomberman)
