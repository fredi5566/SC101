"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    length = width - 2*(GRAPH_MARGIN_SIZE)
    space = length / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * space

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,  CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)  # 上面那條
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)  # 下面那條

    # 畫 每一年的直線(x = x_coordinate)
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH,i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor = tkinter.NW, font ='time, 9')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)                    # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        name = lookup_names[i]                                        # Draw name_data by for loop(One loop one student)
        print(name)
        d = name_data[name]                                           # d is a value with dict type.
        color_num = i % len(COLORS)
        rank_lst = []                                                 # rank可能有問題

        print(d)
        for year in YEARS:                                            # 先把每個人rank的list整理好(ex: jennifer)
            if str(year) not in d:
                d[str(year)] = str(1000)                              # for each loop (這邊不用知道index!!)
                print(year)
            else:
                pass
            rank = d[str(year)]
            rank_lst.append(rank)
            # print('new:', rank_lst)

        # for key, value in sorted(d.items(),key=lambda s: s[0]):         # 改年份長度會有問題!!
        #     rank_lst.append(value)
        # print('rank_lst: ', rank_lst)

        for j in range(len(YEARS)-1):
            rank1 = int(rank_lst[j])
            rank2 = int(rank_lst[j+1])

            x1 = get_x_coordinate(CANVAS_WIDTH,j)
            x2 = get_x_coordinate(CANVAS_WIDTH,j+1)
            y1 = ((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)*rank1-CANVAS_HEIGHT+1001*GRAPH_MARGIN_SIZE)/999
            y2 = ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * rank2 - CANVAS_HEIGHT + 1001 * GRAPH_MARGIN_SIZE)/999
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_num])
            if rank1 == 1000:
                canvas.create_text(x1 + TEXT_DX, y1, text=[name, '*'], anchor=tkinter.SW, font='time, 8', fill=COLORS[color_num])
            else:
                canvas.create_text(x1+TEXT_DX,y1, text=[name,rank1], anchor=tkinter.SW, font='time, 8', fill=COLORS[color_num])

        last_x = get_x_coordinate(CANVAS_WIDTH, len(YEARS)-1)              # This is for last point
        last_rank = int(rank_lst[len(YEARS)-1])
        last_y = ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) * last_rank - CANVAS_HEIGHT + 1001 * GRAPH_MARGIN_SIZE)/999
        canvas.create_text(last_x + TEXT_DX, last_y, text=[name, last_rank], anchor=tkinter.SW, font='time, 8', fill=COLORS[color_num])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

    ##

