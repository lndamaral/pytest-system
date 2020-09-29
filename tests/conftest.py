import pytest

"""Import all fixtures exposed by test framework."""
from fixtures.conftest import *  # noqa: F403, F401
from pages.menu import Menu
from pages.create_playlist import CreatePlaylist
from pages.playlist import Playlist


@pytest.fixture(scope="function")
def menu(app_instance):
    return Menu(app_instance)


@pytest.fixture(scope="function")
def create_playlist(app_instance):
    return CreatePlaylist(app_instance)


@pytest.fixture(scope="function")
def playlist(app_instance):
    return Playlist(app_instance)
