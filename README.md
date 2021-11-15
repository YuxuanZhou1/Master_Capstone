# Master_Capstone League of Legend match result analysis


## Introduction
League of Legends, commonly referred to as League, is a 2009 multiplayer online battle arena video game developed and published by Riot Games. Inspired by Defense of the Ancients, a custom map for Warcraft III, Riot's founders sought to develop a stand-alone game in the same genre.

![alt text](https://cdn1.dotesports.com/wp-content/uploads/2019/09/12195522/league-of-legends.jpg)

In this project, we wonder how to predict the result of a single match, what makes the team win. How to help those people who don't understand this game can understand the game by data analysis. And throughout current data, we can get the win rate. 

## Decision tree
A decision tree is a decision support tool that uses a tree-like model of decisions and their possible consequences, including chance event outcomes, resource costs, and utility. It is one way to display an algorithm that only contains conditional control statements. https://en.wikipedia.org/wiki/Decision_tree

## Processes
- 0_information
  This folder contains four regions usernames; those data are collect from opgg (https://na.op.gg/). Then I use stratified sampling to sampling username by rank information,
player's rank distribution usually like this:  

  -Iron – 7.1% of players
  -Bronze – 22% of players
  -Silver – 35% of players
  -Gold – 23% of players
  -Platinum – 7.9% of players
  -Diamond – 2.5% of players
  -Master – 0.032% of players
  -Grandmaster – 0.040% of players
  -Challenger – 0.017% of players 

people will get servel different files with userID, username, and their rank. After we get different rank of people, we can go to next step. 
  
- 1_processing
- 2_analysing
- 3_classifier
