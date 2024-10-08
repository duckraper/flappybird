import configparser as cp


class SettingsManagerMixin:
    def exists_config(self) -> bool:
        try:
            with open('data/config.ini', 'r'):
                return True
        except FileNotFoundError:
            return False

    def import_config(self):
        config = cp.ConfigParser()
        config.read('data/config.ini')

        self.difficulty = config.get('Game', 'difficulty')

    def export_config(self):
        config = cp.ConfigParser()
        config['Game'] = {
            'difficulty': self.difficulty
        }

        config['Display'] = {
            'resolution': f'{self.width}x{self.height}'
        }

        with open('data/config.ini', 'w') as configfile:
            config.write(configfile)
