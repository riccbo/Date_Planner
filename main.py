from enum import Enum, auto
import time, json


"""
I want to easily add new categories without having to hard code them. I want to be efficient with space and time. Space and time are not that important to make it work. Maybe later.
I may need to make all categories into bool attributes of the class activity but that would mean I would have to hard code it.
Turn all categories to enums but the ones that are not booleans. For example cost should be a seperate attribute.
"""
# CLASSES
class category(Enum):
    RESTAURANT = auto()
    FOOD = auto()
    CREATIVE = auto()
    COOKING = auto()
    LAZY = auto()
    LOTS_OF_MOVEMENT = auto()
    WINTER = auto()
    SUMMER = auto()
    FALL = auto()
    SPRING = auto()
    INDOOR = auto()
    OUTDOOR = auto()
    HOME = auto()


class activity:
    """Class that describes an activity"""

    def __str__(self) -> str:
        return self.name

    def __init__(self, name, time_cost, money_cost, categories) -> None:
        self.name = name
        self.time_cost = time_cost
        self.money_cost = money_cost
        self.categories = categories

    name = ""

    time_cost = [0.0, 0.0]
    money_cost = 0.0
    # num_people = 0
    # opening_hours = None

    categories = []

# FUNCTIONS

def get_data():
    with open('Date_Planner\data.json', 'r') as file:
        json_data = json.load(file)

    data_as_dict = []

    for json_string in json_data:
        dict = json.loads(json_string)
        data_as_dict.append(dict)

    for item in data_as_dict:
        # for loop for categories
        activity = activity(name=item["name"], time_cost=item["time_cost"], money_cost=item["money_cost"], categories=item["categories"])
        all_activities.append(activity)
    print("Data retrieved!")

def save_data():
    json_strings = []

    for activity in all_activities:
        json_string = json.dumps(activity.__dict__)
        print(json_string)
        json_strings.append(json_string)

    with open("Date_Planner\data.json", "w") as file:
        json.dump(json_strings, file, indent=4)
    print("Successfully saved data!")


# ACTIVITIES

"""Creating the activities with their attributes and adding them to a list of all activities"""

all_activities = [] #h global list of all activities

# Get all the activities from JSON file



# Kino = activity(name="kino", time_cost=4, money_cost=0.0, categories=[])
# all_activities.append(Kino)

# Lasertag = activity(name="lasertag", time_cost=24.0, money_cost=0.0, categories=[category.LOTS_OF_MOVEMENT])
# all_activities.append(Lasertag)

# Tretboot = activity(name="tretboot", time_cost=4.0, money_cost=12.0, categories=[category.LOTS_OF_MOVEMENT])
# all_activities.append(Tretboot)


# print out a list of all activities
def print_activities(activities):
    for activity in activities:
        print(activity)


# FILTERS

"""
Maybe make a dummy activity that all activities of the list will be compared to.
Maybe just write a filter for every attribute, but this is horrible.
Make a filter function for every type of attribute
"""

def filter1(activities, categories) -> []:
    filtered_categories = []
    for activity in activities:
        has_all_categories = True
        for category in categories:
            if(category not in activity.categories):
                has_all_categories = False
        if has_all_categories:
            filtered_categories.append(activity)
    return filtered_categories


# TODO maybe create a function that lets you create a new activity. All of this means that the activities have to be saved as a JSON


# save all activities to json


