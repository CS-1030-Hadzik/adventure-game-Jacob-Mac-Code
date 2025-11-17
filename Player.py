class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False






# TODO: (Optional Stretch) Add a check before certain choices
#       - Example: If player.has_lantern is False, prevent entering a cave
#       - Print a message like “It’s too dark to continue without a lantern.”

# TODO: Update all print statements that used player_name to use player.name

# TODO: Commit and push your code with a message like:
#       REF player class added and game state flags implemented