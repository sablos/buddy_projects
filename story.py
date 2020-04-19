import textwrap

file = "story.txt"


class Scene:
    def __init__(self, name, description, options):
        self.name = name
        self.description = description
        self.options = options


def format_options(options):
    result = []
    opts = options.split("@")
    for opt in opts:
        opt_dict = {"prompt": opt.split(";")[0].strip(), "target": opt.split(";")[1].strip()}
        result.append(opt_dict)
    return result


def display_all_scenes(story):
    for scene in story:
        print("name =", scene.name)
        print("description")
        print(textwrap.fill(scene.description, 70))
        print("options")
        for i, option in enumerate(scene.options):
            print(f"{i + 1}. {option['prompt']} -> {option['target']}")


def get_scene(story, sc_name):
    for scene in story:
        if scene.name == sc_name:
            return scene
    # return next((scene for scene in story if scene.name == sc_name), None)


def display_scene(scene):
    print(textwrap.fill(scene.description, 70))
    for i, option in enumerate(scene.options):
        print(f"{i + 1}. {option['prompt']}")


def choose_option(scene):
    valid_choices = [str(x) for x in range(1, len(scene.options))]
    choice = ""
    while choice not in valid_choices:
        choice = input("Choose what to do: ")
    target = scene.options[int(choice) - 1]["target"]
    return target


def retrieve_scenes(file):
    scenes = []
    # read all the lines from the story into a list
    with open(file) as story:
        lines = [line for line in story]
    # break the list of lines into sets of 3, and create a scene object with the data from each set
    for i in range(len(lines) // 3):
        sc_name = lines[3 * i].rstrip("\n")
        sc_desc = lines[3 * i + 1].rstrip("\n")
        options = lines[3 * i + 2].rstrip("\n")
        # sc_opts = [opt.split(;) for opt in options]
        sc_opts = format_options(options)
        this_scene = Scene(sc_name, sc_desc, sc_opts)
        scenes.append(this_scene)
    return scenes


my_story = retrieve_scenes(file)

# display_all_scenes(my_story)

# play story
end = False
current_target = "scene1"

print("Welcome to the story\n")
while not end:
    current_scene = get_scene(my_story, current_target)
    if current_scene is None:
        end = True
    else:
        display_scene(current_scene)
        current_target = choose_option(current_scene)

print("Thank you for reading.")