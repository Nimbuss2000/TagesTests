from json import load
from configs.config import tests_data


class TestData:
    def __init__(self):
        with open(tests_data, 'r', encoding='utf-8') as f:
            self.data = load(f)

    def get_sections(self, section):
        return {param: self.data[section][param] for param in self.data[section]}
