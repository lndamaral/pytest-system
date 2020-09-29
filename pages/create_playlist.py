class CreatePlaylist:

    PLAYLIST_NAME = {
        "title_re": "Name",
        "control_type": "Edit",
    }

    PLAYLIST_DESCRIPTION = {
        "title_re": "Description",
        "control_type": "Edit",
    }

    CREATE_BTN = {
        "title_re": "Create",
        "control_type": "Button",
    }

    def __init__(self, application):
        self.app = application

    def type_playlist_name(self, name):
        self.app.find_element(self.PLAYLIST_NAME).send_keys(name)

    def type_playlist_description(self, description):
        self.app.find_element(self.PLAYLIST_DESCRIPTION).send_keys(description)

    def click_create_btn(self):
        self.app.find_element(self.CREATE_BTN).click()
