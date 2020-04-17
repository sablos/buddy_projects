
class Scene:
    def __init__(self, name, description, options):
        self.scene_name = name
        self.description = description
        self.options = self.format_options(options)

    def format_options(self, options):
        result = []
        opts = split(options, "@")
        for opt in opts:
            opt_dict = {}
            opt_dict["prompt"], opt_dict["target"] = split(opt, ";")
            result.append(opt_dict)