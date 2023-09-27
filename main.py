from enum import Enum, auto
import time


"""
I want to easily add new categories without having to hard code them. I want to be efficient with space and time. Space and time are not that important to make it work. Maybe later.
I may need to make all categories into bool attributes of the class activity but that would mean I would have to hard code it.
"""

class category(Enum):
    RESTAURANT = auto()
    FOOD = auto()
    CREATIVE = auto()
    COOKING = auto()
    LAZY = auto()
    LOTS_OF_MOVEMENT = auto()

# MAYBE USE STRINGS AS VALUES FOR CATEGORIES
# categories = [
#     "restaurant",
#     "food",
#     "creative",
#     "cooking/baking",
#     "lazy",
#     "lots of movement",
#     "chill",
# ]

class temp(Enum):
    WINTER = "winter"
    SUMMER = "summer"
    FALL = "fall"
    SPRING = "spring"

class activity:
    """Class that describes an activity"""

    def __str__(self) -> str:
        return self.name

    def __init__(self, name, indoor, home, time_cost_max, time_cost_min, money_cost, categories, temp) -> None:
        self.name = name
        self.indoor = indoor
        self.home = home
        self.time_cost_max = time_cost_max
        self.time_cost_min = time_cost_min
        self.money_cost = money_cost
        self.categories = categories
        self.temp = temp
        # self.opening_hours = opening_hours
    name = ""
    indoor = False
    home = False
    time_cost_max = 0.0
    time_cost_min = 0.0
    money_cost = 0.0
    categories = []
    temp = []
    # num_people = 0
    # opening_hours = None


# ACTIVITIES

"""Creating the activities with their attributes and adding them to a list of all activities"""

all_activities = []

t = time.process_time()

Kino = activity(name="kino", indoor=False, home=False, time_cost_max=4, time_cost_min=3, money_cost=20.0, categories=[category.LAZY], temp=[temp.FALL, temp.SPRING, temp.SUMMER, temp.WINTER])
all_activities.append(Kino)

Lasertag = activity(name="lasertag", indoor=True, home=False, time_cost_max=24.0, time_cost_min=1.0, money_cost=0.0, categories=[category.LOTS_OF_MOVEMENT], temp=[temp.FALL, temp.SPRING, temp.SUMMER, temp.WINTER])
all_activities.append(Lasertag)

Tretboot = activity(name="tretboot", indoor=False, home=False, time_cost_max=4.0, time_cost_min=1.0, money_cost=12.0, categories=[category.LOTS_OF_MOVEMENT], temp=[temp.SPRING, temp.SUMMER])
all_activities.append(Tretboot)

elapsed_time = time.process_time() - t


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

# def filter_by_indoor(activities) -> []:
#     filtered_activities = []
#     for activity in all_activities:
#         if(activity.indoor == True):
#             filtered_activities.append(activity)
#     return filtered_activities

def filter1(activities, attribute_name) -> []:
    filtered_activities = []

    if activities==None:
        return []

    type_of_attribute = type(getattr(activities[0], attribute_name))

    if type_of_attribute is bool:
        user_input = bool(input("Do you want the attribute to be [1]True or [0]False?\n"))
        for activity in activities:
            if(getattr(activity, attribute_name) ==  user_input):
                filtered_activities.append(activity)
    
    elif type_of_attribute is float:
        pass

    elif type_of_attribute is category:
        pass

    elif type_of_attribute is temp:
        pass


    

    return filtered_activities

print_activities(filter1(all_activities, "indoor"))

