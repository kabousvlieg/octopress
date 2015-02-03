---
layout: post
title: "When is a team agile?"
date: 2015-01-29 13:30:37 +0200
comments: true
categories: 
---


<h2>Background</h2>
This post serves as part of study on the effectiveness of the DO-178B certification in achieving correctness of implementation and safety guarantees in the presence of incomplete requirements, feature creep and complex technology stacks, also known as your typical software project.

If you are currently; or in the past have worked on DO-178 projects, it would be appreciated if you would be so kind as to [take part in a survey](https://www.surveymonkey.com/s/SV9KX7M) about the state of DO-178 development.

One of the challenges in defining a more agile DO-178 process, is proving that the process is actually agile. Proving it conforms to DO-178 is easy, there is an entire specification written for that, but agile...hmmm.  

<h2>So what is agile?</h2>
What a question...the software development world is a buzz with agile this and agile that, but ask any practitioner of agile software development this question, and you'll invariably get a different answer from [each](http://www.cio.com/article/2385322/agile-development/why-agile-isn-t-working--bringing-common-sense-to-agile-principles.html) and [every](http://www.allaboutagile.com/category/10-key-principles-of-agile/) one of [them.](http://pragdave.me/blog/2014/03/04/time-to-kill-agile/)

So to ask the question, lets first frame what I mean with agile. In my mind, agile can be seen to exist on three tiers, let's call it the agile pyramid if you will. 

{% img center /images/agile_pyramid.png 600 %}

<h4>Tier 1- Philosophy</h4>
First tier is the [agile manifesto](http://www.agilemanifesto.org/), where it all began off course. The manifesto states:

- _Individuals and interactions over processes and tools_
- _Working software over comprehensive documentation_
- _Customer collaboration over contract negotiation_
- _Responding to change over following a plan_ 

The agile manifesto also talks about twelve principles of agile, but I think the above four statements captures the intention well enough.

Now the manifesto sounds great and all, but it doesn't give you much of an example to work with on how to run an agile project. Fortunately shortly after the manifesto Kent Beck lead a [software project](http://en.wikipedia.org/wiki/Chrysler_Comprehensive_Compensation_System) that has been studied quite a bit, and gave rise to [Extreme Programming (XP)](http://en.wikipedia.org/wiki/Extreme_programming). But extreme programming was a little bit too extreme for some, and besides, project managers still didn't have much of a clue about how this agile thing works exactly anyway, which leads us to our next tier in the pyramid.

<h4>Tier 2- Project management</h4>

In order to formalize what agile software development is exactly, legions of consultants sprang up to [teach these projects managers and their programmers](http://www.thoughtworks.com/talks/the-death-of-agile). What came forth was the leading agile development methodology, Scrum, but also Kanban. 

{% img center /images/scrum.png 600 %}

Ok so scrum is a daily ritual of scrum masters, stand up meetings, user stories, time limits and velocity tracking. Oh and Kanban boards.

{% img center /images/kanban.png 600 %}  

So what is the difference between Scrum and Kanban? Well, not much, except Scrum could be described as the anal retentive cousin of Kanban. For where scrum has roles, time limits, velocity tracking, daily meetings, scrum masters etc, Kanban has none, just a board and a team.  (Ok I might just have started a religious war, don't take this stuff too seriously).

<h4>Tier 3- Best practices</h4>  

So Scrum and Kanban relies on certain agile best practices to really succeed, and if you really get down to it, this can become a very long list. I've listed the most important ones for my purposes (agile DO-178), but there are many more:

- [Continuous integration](http://en.wikipedia.org/wiki/Continuous_integration)
- [Continuous deployment](http://en.wikipedia.org/wiki/Continuous_delivery)
- [Pair programming](http://en.wikipedia.org/wiki/Pair_programming)
- Regular code refactoring
- [Velocity tracking](http://en.wikipedia.org/wiki/Velocity_%28software_development%29)
- [Feature driven development](http://en.wikipedia.org/wiki/Feature-driven_development)
- [Test driven development](http://en.wikipedia.org/wiki/Test-driven_development)
- [Behaviour driven development](http://en.wikipedia.org/wiki/Behavior-driven_development)

Ok so back to my initial question, at what point can it be said a team is agile? Is it only necessary that the spirit of agile is followed (agile manifesto), or only when the entire pyramid is in effect?

Please join the discussion at [HN]() and [reddit](). Comments are very welcome.