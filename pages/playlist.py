class Playlist:
    def __init__(self, application):
        self.app = application
        self.parent = {
            "title_re": "Playlist",
            "control_type": "Document",
        }

    def click_more_btn(self):
        self.app.find_element(
            parent=self.parent,
            selectors={
                "title_re": "More",
                "control_type": "Button",
            },
        ).click()

    def click_delete_playlist(self):
        self.app.find_element(
            selectors={
                "title_re": "Delete",
                "control_type": "Text",
            }
        ).click()

        self.app.find_element(
            selectors={
                "title_re": "DELETE",
                "control_type": "Button",
            },
        ).click()
