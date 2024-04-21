from movie import *
from tkinter import *
from weighted_graph import *


# checks if the movie title inputted by the user is in the list of movies in "movies.txt"
def validate_movie(user_input):
    file = open('movies.txt', 'r', errors='ignore')

    while True:
        movie_info = file.readline()

        if not movie_info:
            break
        else:
            movie_info = movie_info.split('\t')
            movie_title = movie_info[0]

            if movie_title == user_input:
                return True

    file.close()
    return False


# Main function
def main():
    # creates window
    window = Tk()
    # resizes window
    window.geometry('1200x675')
    # changes background color of window
    window.configure(bg='#f5f7c1')
    # makes it so window cannot be resized
    window.resizable(False, False)

    # creates "Film Finder" text
    title = Label(window, text='Film Finder', font=('Algerian', 40), bg='#f5f7c1', fg='#cc3f14')
    # puts "Film Finder" on screen
    title.pack(pady=15)

    # creates dropdown area
    rectangle = Canvas(window, width=550, height=550, bg='#40a6c2')
    # puts dropdown area on screen
    rectangle.place(x=600, y=85)

    # creates prompt1 text
    prompt1 = Label(window, text='Please enter title of movie:', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    prompt1.place(x=765, y=95)

    # creates textbox for prompt1
    textbox = Entry(window, width=40, font=('Times New Roman', 12))
    textbox.place(x=715, y=130)

    # placeholder
    outcome = Label(window, text='', font=('Times New Roman', 10), bg='#40a6c2')
    outcome.place(x=713, y=155)

    # creates movie object
    movie = Movie()

    # gets input from textbox and validates it
    def check_input(event=None):
        user_input = textbox.get()
        textbox.delete(0, 'end')

        movie_found = validate_movie(user_input)

        if movie_found:
            successful_text = 'You entered \"' + user_input + '\"'
            outcome.config(text=successful_text, fg='black')
            movie.set_title(user_input)

            file = open('movies.txt', 'r', errors='ignore')

            while True:
                movie_info = file.readline()

                if not movie_info:
                    break
                else:
                    movie_info = movie_info.split('\t')
                    movie_title = movie_info[0]

                    if movie_title == user_input:
                        movie.set_year(movie_info[1])
                        movie.set_rating(movie_info[2])
                        movie.set_runtime(movie_info[3])
                        movie.set_genre(movie_info[4])
                        movie.set_rating(movie_info[5])
                        movie.set_director(movie_info[6])
                        movie.set_main_stars(movie_info[7])

            file.close()
        else:
            unsuccessful_text = 'Movie title not found. Please enter another movie title.'
            outcome.config(text=unsuccessful_text, fg='#cc3f14')

    textbox.bind('<Return>', check_input)

    # creates prompt2 text
    prompt2 = Label(window, text='Select similarity priorities:', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    prompt2.place(x=760, y=220)

    # creates dropdown menus
    priorities1 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option1 = StringVar()
    clicked_option1.set(priorities1[0])
    text1 = Label(window, text='Genre   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text1.place(x=800, y=270)
    dropdown1 = OptionMenu(window, clicked_option1, *priorities1)
    dropdown1.place(x=890, y=270)

    priorities2 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option2 = StringVar()
    clicked_option2.set(priorities2[0])
    text2 = Label(window, text='Year   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text2.place(x=810, y=310)
    dropdown2 = OptionMenu(window, clicked_option2, *priorities2)
    dropdown2.place(x=890, y=310)

    priorities3 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option3 = StringVar()
    clicked_option3.set(priorities3[0])
    text3 = Label(window, text='Runtime   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text3.place(x=778, y=350)
    dropdown3 = OptionMenu(window, clicked_option3, *priorities3)
    dropdown3.place(x=890, y=350)

    priorities4 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option4 = StringVar()
    clicked_option4.set(priorities4[0])
    text4 = Label(window, text='Main Stars   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text4.place(x=761, y=390)
    dropdown4 = OptionMenu(window, clicked_option4, *priorities4)
    dropdown4.place(x=890, y=390)

    priorities5 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option5 = StringVar()
    clicked_option5.set(priorities5[0])
    text5 = Label(window, text='Director   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text5.place(x=780, y=430)
    dropdown5 = OptionMenu(window, clicked_option5, *priorities5)
    dropdown5.place(x=890, y=430)

    priorities6 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option6 = StringVar()
    clicked_option6.set(priorities6[0])
    text6 = Label(window, text='Reviews (IMDb)   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text6.place(x=711, y=470)
    dropdown6 = OptionMenu(window, clicked_option6, *priorities6)
    dropdown6.place(x=890, y=470)

    priorities7 = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option7 = StringVar()
    clicked_option7.set(priorities7[0])
    text7 = Label(window, text='Rating   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text7.place(x=796, y=510)
    dropdown7 = OptionMenu(window, clicked_option7, *priorities7)
    dropdown7.place(x=890, y=510)

    top_results = ['Top 5', 'Top 10', 'Top 25']
    clicked_option8 = StringVar()
    clicked_option8.set(top_results[0])
    text8 = Label(window, text='Show results: ', font=('Times New Roman', 12), bg='#40a6c2', fg='black')
    text8.place(x=620, y=560)
    dropdown8 = OptionMenu(window, clicked_option8, *top_results)
    dropdown8.place(x=625, y=590)

    def find_similar_movies():
        # finds the rank of all movies based on priorities to determine which is most similar to inputted movie
        similar_movies = movie.find_similar_movies(clicked_option1.get(), clicked_option2.get(), clicked_option3.get(), clicked_option4.get(), clicked_option5.get(), clicked_option6.get(), clicked_option7.get())
        movie.set_similar_movies(similar_movies)

        # TODO:: maps output

        # weighted graph output showing similar movies to inputted movie
        weighted_graph = WeightedGraph()
        weighted_graph.create_graph(movie, similar_movies)
        weighted_graph.output_graph(clicked_option8)

    submit_button = Button(window, text='Submit', font=('Times New Roman', 12), command=find_similar_movies)
    submit_button.place(x=1075, y=590)

    window.mainloop()


if __name__ == '__main__':
    main()
