from jproperties import Properties


class PropertyReader:
    @staticmethod
    def read_property(file, property_to_search):
        config = Properties()
        with open(f'./{file}', 'rb') as config_file:
            config.load(config_file)
            return config.get(property_to_search).data
