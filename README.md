## What I Wanted To Get From Scraping 

 

For this assignment, I wanted to scrape the rosters of all the official University of Florida’s sports teams __(17 in total)__. From the rosters, I wanted to get the name of every athlete, as well as their hometown and high school.  

 

I wanted to get this because it offers insight into what states and schools are getting scouted the most for UF.

 

## The Steps I Took 

 

For this page, I utilized **four main functions.**  

The first step I had to do was figure out which pages were formatted differently. Then, I made three different functions that take the URLs and scrape them for the sport on the page, the players’ names, the players’ hometowns, and the players' high schools. These three functions are __get_baseball_football()__, __get_other_sports()__ and __get_running()__. These three functions take the partial URLs from their specific list, scrape the information, put the information into individual lists for each player, and then put those individual lists into one overarching list. 

After getting all these functions to output the information properly, I created the __write_csv()__ function. This function takes three arguments and calls the three functions to pass those arguments __(the three lists)__ to the functions. It also opens a CSV file and writes the information coming from those three functions into the file. 

 

## Unexpected Problems 

 

There were a few unexpected problems I ran into.  

1. The first problem was figuring out how to properly get the information into the CSV file. While the scraping functions worked, I originally was trying to put all the information into one list, instead of one list for each player into a list containing all the lists. This was an easy fix once I realized my mistake, as I just needed to create another list and append the information lists to that one. 

2. The second problem I ran into was with the for loop in the get_baseball_football_rows function. For the other functions, I was able to find a relatively easy overarching HTML element that contained the other elements I needed. This way I could find all the information I needed in one for loop, which was necessary for getting all the information into individual lists. Yet, for the baseball and football roster pages, I could not find one overarching element that worked well. This took me the longest to figure out, as I had to go back and look at how I could format for loops differently __(in range vs. in a specific list)__ to make the loop run to produce all the lists I needed. I was able to implement that loop into my code and the function ran successfully. 

3. The third big problem I came across was with my functions. I originally only had two functions, one for baseball and football and one for all the other sports. Yet, I realized when the function ran for the co-ed sports __(track and cross county)__, it was only picking up the women's rosters, not the men’s rosters. The hardest part of this was figuring out why it was only giving me the women’s names, which I figured out was because I was only finding the first table on the page. This worked for all the other rosters because there was only one table, but for this one, the men’s and women’s rosters were separated into two tables. After I figured it out, I just created another function __(get_running())__ and added a part to the for loop that looped through the tables on the page to get the information. This solved the problem. 

 

 

 

 