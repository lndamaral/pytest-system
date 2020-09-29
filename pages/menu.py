class Menu:

    NEW_PLAYLIST_BTN = {
        "title_re": "Create New Playlist",
        "control_type": "Button",
    }

    def __init__(self, application):
        self.app = application

    def click_new_playlist(self):
        self.app.find_element(self.NEW_PLAYLIST_BTN).click()
