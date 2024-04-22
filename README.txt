Film Finder
___________
Purpose:
- Film Finder is a program that finds similar movies to the user's movie of choice.


Running the code:
- The program can be run in any IDE that uses Python. Make sure that all necessary packages (networkx and matplotlib) are installed.


Using Film Finder:
- Once the program is run, a screen will pop up asking for the user to input the title of a movie into a textbox. Make sure to hit ENTER after inputting the movie title so that the program knows which movie title the user wants to find similar movies to.  

- After, the user can rank attributes, such as genre and director, that will influence the output of what movies are most similar to the user's chosen movie. For example, if someone wants to find movies similar to "Inception" because they like the genre, they might rank genre "1" so that the program will weigh genre higher and take it more into consideration than other attributes when determining similar movies. As a note, "1" is the highest priority and "7" is the lowest.

- The user can then choose to how many similar movies they want shown under "Show results:"

- Assuming a movie title as been inputted and at least 1 priority has been chosen, the user can hit the submit button which will cause the program to output data from a map and a graph to visually show which movies are most similar to the user's movie choice. For the graph, smaller edge weights mean that the the movie is more similar than other movies.