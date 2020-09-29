"""First test."""
from time import sleep


def test_delete_playlist(app, menu, create_playlist, playlist):
    sleep(5)

    # Parameters
    __playlist_name = app.utils.random_string()
    __playlist_description = app.utils.random_string(80)

    # Click on create new playlist button
    menu.click_new_playlist()

    # Create playlist
    create_playlist.type_playlist_name(__playlist_name)
    create_playlist.type_playlist_description(__playlist_description)
    create_playlist.click_create_btn()

    # Delete playlist
    playlist.click_more_btn()
    playlist.click_delete_playlist()
