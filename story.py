def format_options(options):
    result = []
    opts = split(options, "@")
    for opt in opts:
        opt_dict = {}
        opt_dict["prompt"], opt_dict["target"] = opt.split(";")
        result.append(opt_dict)

    return result


class Scene:
    def __init__(self, name, description, options):
        self.scene_name = name
        self.description = description
        self.options = format_options(options)

