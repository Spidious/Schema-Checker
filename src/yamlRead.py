import yaml

class yamlReader():
    def __init__(self, file: str):
        self.data = {}

        # Open and read yaml file
        with open(file) as fp:
            try:
                self.data = yaml.safe_load(fp)
            except yaml.YAMLError as e:
                print(e)
