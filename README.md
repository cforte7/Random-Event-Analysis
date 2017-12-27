# Analysis of Random Event Generation in Computer Gaming 


## Introduction

  In modern computing, the generation of events with specific probabilities has been considered a necessary tool for applications ranging from executing computer simulation models, to running gambling machines. Another field where this is prevelant is in E-Sports. With viewership [quickly growing and experts ancitipating it to become a billion dollar industry](http://www.businessinsider.com/esports-popularity-revenue-forecast-chart-2017-3), understanding the mechanism by which these games function can have major impacts. 
  
  In this paper I will explore the usage of random event generation in the computer game Dota 2 and compare the stated probabilities and expected results to collected gameplay data.
  
  [General information about Dota 2 can be found here.](https://en.wikipedia.org/wiki/Dota_2)
  
  First we will walk through the application of a Monte Carlo experiment in order to generate data within the game, followed by the processing of this data. After, we will discuss the methods of the statistical tests utilized and end with our finalized results and conclusions.    

## Data Collection
  The first step of this experiment is to collect a large number of trials of one type of event in Dota 2, constituting a form of [Monte Carlo experiment](https://en.wikipedia.org/wiki/Monte_Carlo_method). Without diving too far into the details of the game, in our experiment we are observing the repeated attack by one player who has a stated 15% chance to deal extra damage in order to compare the frequency of the attack bonus triggering (event sucess) 
  
  The results of this controlled in-game environment is exported as a log file, which can be found [here](test.txt).
