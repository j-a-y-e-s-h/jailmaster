from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller


from .add_prison_cell.gui import AddPrisonCell
from .view_prison_cell.main import ViewPrisonCell
from .update_prison_cell.main import UpdatePrisonCell

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def prison_cell():
    PrisonCell()


class PrisonCell(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # self.selected_pid = None
        # self.prison_cell_data = db_controller.get_prison_cell()
        self.selected_pca_id = None
        self.prison_cell_data = db_controller.get_prison_cell()


        self.configure(bg="#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            "add": AddPrisonCell(self),
            "view": ViewPrisonCell(self),
            "edit": UpdatePrisonCell(self),
        }

        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1013.0, height=506.0)

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1013.0, height=506.0)
