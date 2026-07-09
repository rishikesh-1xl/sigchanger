import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")


class Config:

    BASE_URL = config.get("common", "base_url")

    VIEWPORT_WIDTH = config.getint("common","viewport_width")

    VIEWPORT_HEIGHT = config.getint("common","viewport_height")

    TIMEOUT = config.getint("common","timeout")

    HEADLESS = config.getboolean("common","headless")

    