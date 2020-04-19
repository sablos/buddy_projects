import textwrap

file = "story.txt"
title = "The Iron Sandwich"


class Scene:
    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options


def format_options(options):
    """Converts the options line from the file into a list of dictionaries"""
    result = []
    opts = options.split("@")
    for opt in opts:
        opt_dict = {"prompt": opt.split(";")[0].strip(), "target": opt.split(";")[1].strip()}
        result.append(opt_dict)
    return result


def clr_screen():
    """Clears the screen by inserting a number of linefeeds"""
    print(50 * "\n")

def display_all_scenes(story):
    """Prints a list of all scenes, descriptions and options"""
    for scene in story:
        print("name =", scene.name)
        print("description")
        print(textwrap.fill(scene.description, 70))
        print("options")
        for i, option in enumerate(scene.options):
            print(f"{i + 1}. {option['prompt']} -> {option['target']}")


def get_scene(story, sc_name):
    """Returns the scene from the story based on the scene name provided"""
    for scene in story:
        if scene.name == sc_name:
            return scene
    # return next((scene for scene in story if scene.name == sc_name), None)


def display_scene(scene):
    """Displays the description and options of the chosen scene"""
    print(textwrap.fill(scene.description, 70))
    print("\n")
    for i, option in enumerate(scene.options):
        print(f"{i + 1}. {option['prompt']}")


def choose_option(scene):
    """Allows the user to choose one of the options, and returns the scene name"""
    valid_choices = [str(x) for x in range(1, len(scene.options) + 1)]
    choice = ""
    while choice not in valid_choices:
        choice = input("Choose what to do: ")
    target = scene.options[int(choice) - 1]["target"]
    return target


def retrieve_scenes(file):
    """Retrieves the story from the text file and returns it as a list of scenes"""
    scenes = []
    # read all the lines from the story into a list
    with open(file) as story:
        lines = [line for line in story]
    # break the list of lines into sets of 3, and create a scene object with the data from each set
    for i in range(len(lines) // 3):
        sc_name = lines[3 * i].rstrip("\n")
        sc_desc = lines[3 * i + 1].rstrip("\n")
        options = lines[3 * i + 2].rstrip("\n")
        sc_opts = format_options(options)
        this_scene = Scene(sc_name, sc_desc, sc_opts)
        scenes.append(this_scene)
    return scenes


my_story = retrieve_scenes(file)

# display_all_scenes(my_story)

# play story
end = False
current_target = "scene1"

print(f"* * *    {title}   * * * \n\n")
input("Press enter to begin...")
while not end:
    current_scene = get_scene(my_story, current_target)
    if current_scene is None:
        end = True
    else:
        clr_screen()
        display_scene(current_scene)
        current_target = choose_option(current_scene)

print("Thank you for reading.")