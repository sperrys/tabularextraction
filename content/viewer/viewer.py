#
#   viewer.py
#

import pandas as pd
import time
import os


DATA_PATH = 'data/'
INPUT_PDF = 114
END_PAGE = 10


class Viewer(object):

    def __init__(self):

        self.dfs = {}
        self.views = {}
        self.current_page = 0

        # (row, col)
        self.current_index = (0, 0)

    #
    #   return current_index
    #

    def get_current_index(self):
        return self.current_index

    #
    #   set current_index
    #

    def set_current_index(self, r, c):

        try:
            p = self.get_current_page()
            cur_view = self.views[p]

            count_row, count_col = pd.DataFrame(cur_view).shape

            if (r < 0 or r > count_row - 1) or (c < 0 or c > count_col - 1):
                print("Set Bad Index for page: {}: vals tried: ({}, {})".format(p, r, c))
                time.sleep(3)
                return False

            else:
                self.current_index = (r, c)
                return True
        except Exception as e:
            print(e)
            print("Set Bad Index for page: {}: vals tried: ({}, {})".format(p, r, c))
            return False


    def row_col(self, page):

        cur_view = self.views[page]
        count_row, count_col = pd.DataFrame(cur_view).shape

        return count_row, count_col

    #
    #   return current_page
    #

    def get_current_page(self):
        return self.current_page


    #
    #   set the current_page
    #

    def set_current_page(self, num):

        try:
            if num > len(self.dfs.items()) or num < 1:
                print("Page Not Valid!: {}".format(num))
                return False
            else:
                self.current_page = num
                return self.get_current_page()
        except Exception as e:
            print("Page Not Valid!!")
            return False

    #
    #   store a df associated with the index
    #

    def add_view(self, index, df):

        count_row, count_col = df.shape
        grid = [[df.iloc[r, c] for c in range(count_col)] for r in range(count_row)]

        self.views[index] = grid
        self.current_page = index

    #
    #
    #

    def print_grid(self, index):

        os.system('clear')

        try:
            view = self.views[index]
            print(pd.DataFrame(view))

            r, c = self.get_current_index()
            cell = self.get_cell(index, r, c)

            print("\nCurrent Page: {}".format(index))
            print(("Current Index: ({}, {}): [\"{}\"]\n".format(r, c, cell)))
        except Exception as e:
            print(e)
            return None

    #
    #
    #

    def change_cell(self, index, r, c, val):

        try:
            view = self.views[index]
            cell = pd.DataFrame(view).iloc[r, c]
            self.views[index][r, c] = val

            return cell
        except Exception as e:
            print(e)
            return False


    #
    #  grab any addded ndividual cell
    #

    def get_cell(self, index, r, c):

        try:
            view = self.views[index]
            cell = pd.DataFrame(view).iloc[r, c]
            return cell

        except Exception as e:
            print(e)
            return None


    #
    #   load a csv from file to the viewer
    #

    def load(self, file, index):

        try:
            frame = pd.read_csv(file, header=None)
            self.dfs[index] = frame
            self.add_view(index, frame)

        except Exception as e:
            print("Error Loading: {}".format(index))
            print(e)
            return None

    #
    # function for handling the scroll mode of the view
    #

    def handle_scroll(self):

        # TODO make this less ugly

        try:
            d = input("Scroll:\nValid Options: (<, >, q):\n")
            if d == "<":
                new_page = self.get_current_page() - 1
                if self.set_current_page(new_page):
                    self.print_grid(self.get_current_page())
                    return self.handle_scroll()
                return False

            elif d == ">":
                new_page = self.get_current_page() + 1
                if self.set_current_page(new_page):
                    self.print_grid(self.get_current_page())
                    return self.handle_scroll()
                return False

            elif d == "q":
                return True
            else:
                print("Invalid Input!")
                self.handle_scroll()
        except Exception as e:
            print(e)
            print("Invalid Input!")
            self.handle_scroll()


    #
    # function for handling the select mode of the viewer

    def handle_select(self):

        d = input("Select:\nValid Options: (<, >, ^, v, q):\n")

        r, c = self.get_current_index()
        p = self.get_current_page()

        # Direction Movement of Selection
        if d == "<":
            self.set_current_index(r, c - 1,)
        elif d == ">":
            self.set_current_index(r, c + 1)
        elif d == "^":
            self.set_current_index(r - 1, c)
        elif d == "v":
            self.set_current_index(r + 1, c)

        # Return the Value of the Current Cell Selected
        elif d == "s":
            cell = self.get_cell(p, r, c)
            return True, (r, c), cell
        elif d == "q":
            return False, None, None
        else:
            print("Invalid Input!")
            self.handle_select()
            time.sleep(3)

        self.print_grid(p)
        return self.handle_select()


    #
    #  generic input handler associated with the viewer
    #

    def input(self):

        print("Current Page: {}".format(self.get_current_page()))
        self.print_grid(self.get_current_page())

        d = input("Choose a Viewer Method:\nValid Options: 'scroll', 'select':\n")
        if d == "scroll":
            if not self.handle_scroll():
                self.input()
        elif d == "select":
            if not self.handle_select():
                self.input()
        elif d == "q":
            return False
        else:
            print("Invalid Input!")
            time.sleep(3)
            self.input()


