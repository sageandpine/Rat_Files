""" ToDo:
        1. Get individual Rooms to Launch
        2. Get Player Class Working
        3. Incorporate Game Engine
        4. Link Classes Together Properly
        5. Start linking Rooms by Decisions/Actions
        6. Re-introduce more full bodied text formatted correctly
        7. Save state to make saving and returning to your game possible
        8. Clean up code
        """
        
import levels as lvl

class GameEngine:
    """Launch game and end game"""
    
    def __init__(self):
        P1 = Player()
        self.game_end = exit(0)

    def launch(self):
        pass
        # P1.Rooms.start_room()

    def end(self):
        print("Game Over!")
        return self.game_end

class Rooms():
    """Load scenes for players to interact with."""
    
    def __init__(self):
        self.lvl = lvl

    def statue_room(self):
        return self.lvl.rat_file_levels["Statue_Room"]

    def sci_lab(self):
        return self.lvl.rat_file_levels["Sci_Lab"]

    def long_hall(self):
        return self.lvl.rat_file_levels["Long_Hall"]

    def north_rope_room(self):
        return self.lvl.rat_file_levels["N_Rope_Room"]

    def rope_room(self):
        return self.lvl.rat_file_levels["Rope_Room"]

    def south_basement(self):
        return self.lvl.rat_file_levels["S_Basement"]

    def basement_2(self):
        return self.lvl.rat_file_levels["Return_To_Basement"]

    def basement(self):
        return self.lvl.rat_file_levels["Basement"]

    def tv_room(self):
        return self.lvl.rat_file_levels["Tv_Room"]

    def start_room_2(self):
        return self.lvl.rat_file_levels["Return_To_Start"]

    def start_room(self):
        return self.lvl.rat_file_levels["Start_Room"]

class Player(GameEngine):
    """A class containing all the attributes and actions each player has access to"""
   
    def __init__(self, name='', is_alive=True, inventory=["knife"]):
        self.inventory = inventory
        self.name = name
        self.is_alive = is_alive
        #self.game_end = GameEngine.game_end
        
    def move(self):
        """Moves Player in a specific direction."""
        print(f"{self.name} moved!")
    
    def action(self):
        """Defines the actions a player can make."""
        print(f"{self.name} Threw a thing!")

    def check_inventory(self):
        """Check items in inventory"""
        print(f"You have the following items --> {self.inventory}")

    def remove_from_inv(self):
        """Remove item from inventory"""
        print("item removed")
    
    def add_item_to_inv(self):
        """Adds item to inventory"""
        print("item added")
    
    def use_item_from_inv(self):
        """Uses specific item in inventory"""
        print("item used")
        
    def dead(self):
        pass
        #print(why, "No book deal....you dead.")
        #return game_end

R = Rooms()

print(R.statue_room())
print(R.start_room())
print(R.tv_room())
print(R.start_room_2())
print(R.long_hall())
print(R.north_rope_room())
print(R.rope_room())
print(R.basement())
print(R.basement_2())
print(R.south_basement())
print(R.sci_lab())

P = Player()
P.check_inventory()
P.move()
P.action()
P.remove_from_inv()
P.add_item_to_inv()
P.use_item_from_inv()
P.dead()

Game = GameEngine
Game.end


