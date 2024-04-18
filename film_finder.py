from matplotlib.pyplot import *
from networkx import *
from tkinter import *
from algorithms import *
from data_structures import *
matplotlib.use('TkAgg')


# checks if the movie title inputted by the user is in the list of movies in "movies.txt"
def check_movie(user_input):
    file = open('movies.txt', 'r', errors='ignore')

    while True:
        movie_info = file.readline()

        if not movie_info:
            break
        else:
            movie_info = movie_info.split('\t')
            movie = movie_info[0]

            if movie == user_input:
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

    # gets input from textbox
    def check_input(event=None):
        user_input = textbox.get()
        textbox.delete(0, 'end')

        movie_found = check_movie(user_input)

        if movie_found:
            text = 'You entered \"' + user_input + '\"'
            outcome.config(text=text, fg='black')
        else:
            text = 'Movie title not found. Please enter another movie title.'
            outcome.config(text=text, fg='#cc3f14')

    textbox.bind('<Return>', check_input)

    # creates prompt2 text
    prompt2 = Label(window, text='Select similarity priorities:', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    prompt2.place(x=760, y=220)

    # creates dropdown menus
    priorities = ['None', '1', '2', '3', '4', '5', '6', '7']
    clicked_option = StringVar()
    clicked_option.set(priorities[0])

    text1 = Label(window, text='Genre   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text1.place(x=800, y=270)
    dropdown1 = OptionMenu(window, clicked_option, *priorities)
    dropdown1.place(x=890, y=270)

    text2 = Label(window, text='Year   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text2.place(x=810, y=310)
    dropdown2 = OptionMenu(window, clicked_option, *priorities)
    dropdown2.place(x=890, y=310)

    text3 = Label(window, text='Runtime   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text3.place(x=778, y=350)
    dropdown3 = OptionMenu(window, clicked_option, *priorities)
    dropdown3.place(x=890, y=350)

    text4 = Label(window, text='Main Stars   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text4.place(x=761, y=390)
    dropdown4 = OptionMenu(window, clicked_option, *priorities)
    dropdown4.place(x=890, y=390)

    text5 = Label(window, text='Director   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text5.place(x=780, y=430)
    dropdown5 = OptionMenu(window, clicked_option, *priorities)
    dropdown5.place(x=890, y=430)

    text6 = Label(window, text='Reviews (IMDb)   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text6.place(x=711, y=470)
    dropdown6 = OptionMenu(window, clicked_option, *priorities)
    dropdown6.place(x=890, y=470)

    text7 = Label(window, text='Rating   -', font=('Times New Roman', 16), bg='#40a6c2', fg='black')
    text7.place(x=796, y=510)
    dropdown7 = OptionMenu(window, clicked_option, *priorities)
    dropdown7.place(x=890, y=510)

    submit_button = Button(window, text='Submit', font=('Times New Roman', 12))
    submit_button.place(x=847, y=580)

    """graph = Graph()
    graph.add_edge("a", "b", weight=0.6)
    graph.add_edge("a", "c", weight=0.2)
    graph.add_edge("c", "d", weight=0.1)
    graph.add_edge("c", "e", weight=0.7)
    graph.add_edge("c", "f", weight=0.9)
    graph.add_edge("a", "d", weight=0.3)
    pos = spring_layout(graph)
    draw(graph, pos, node_color='red', node_size=600)
    edge_labels = get_edge_attributes(graph, 'weight')
    draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels, label_pos=0.5)
    axis('off')
    show()"""

    window.mainloop()


if __name__ == '__main__':
    main()
