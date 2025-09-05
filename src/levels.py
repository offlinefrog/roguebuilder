from dataclasses import dataclass, fields
import json
import re

@dataclass
class Levels:
    name: str = ''

    WARRIOR: int = 0
    ATHLETE: int = 0
    COLLECTOR: int = 0
    FARMER: int = 0
    TRAINER: int = 0
    WITCH: int = 0
    PURIST: int = 0

    LADYBUG: int = 0
    OCELOT: int = 0
    ANT: int = 0
    SILVERFISH: int = 0
    BEE: int = 0
    MONKEY: int = 0
    PARROT: int = 0
    CHICKEN: int = 0
    SHEEP: int = 0
    CRAB: int = 0
    FROG: int = 0
    SNAIL: int = 0
    BAT: int = 0
    GOLDEN_MONKEY: int = 0
    POLAR_BEAR: int = 0

    @classmethod
    def manual(cls):
        kwargs = {}
        while True:
            try:
                userinput = input("Enter Player name to save Player (press 'Enter' to leave unsaved): ")
                if not userinput:
                    break
                if not re.match(r'^\w+$', userinput):
                    raise ValueError
                if userinput.lower() == 'src':
                    raise ValueError
                kwargs['name'] = userinput
                break
            except ValueError:
                print(f"Invalid name: '{userinput}'")

        print('Enter Specialization and Companion levels')
        for field in fields(cls)[1:]:
            while True:
                try:
                    userinput = input(f'{field.name.replace('_', ' ').title()}: ')
                    kwargs[field.name] = int(userinput)
                    break
                except ValueError:
                    print(f"Invalid value: '{userinput}'")

        if 'name' in kwargs:
            with open('data/levels.json', 'a') as f:
                f.write('\n')
                json.dump(kwargs, f)

        return cls(**kwargs)

    def specializations(self):
        specializations = {'WARRIOR', 'ATHLETE', 'COLLECTOR', 'FARMER', 'TRAINER', 'WITCH', 'PURIST'}
        return {
            name: getattr(self, name) for name in specializations
        }

    def companions(self):
        companions = {'LADYBUG', 'OCELOT', 'ANT', 'SILVERFISH', 'BEE', 'MONKEY', 'PARROT', 'CHICKEN',
                      'SHEEP', 'CRAB', 'FROG', 'SNAIL', 'BAT', 'GOLDEN_MONKEY', 'POLAR_BEAR'}
        return {
            name: getattr(self, name) for name in companions
        }

    def __repr__(self):
        return self.name