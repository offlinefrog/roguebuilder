from dataclasses import dataclass, field, fields
import json
import re

from registry import (Artifacts, Specializations, Companions, Scrolls,
                      Weapons, Helmets, Chestplates, Leggings, Boots, Pets, Foods)

@dataclass
class Build:
    name: str = ""

    artifact: str = field(default=None, metadata={'lookup': 'Artifacts'})
    specialization: str = field(default=None, metadata={'lookup': 'Specializations'})
    companion: str = field(default=None, metadata={'lookup': 'Companions'})

    first_scroll: str = field(default=None, metadata={'lookup': 'Scrolls'})
    second_scroll: str = field(default=None, metadata={'lookup': 'Scrolls'})
    third_scroll: str = field(default=None, metadata={'lookup': 'Scrolls'})
    fourth_scroll: str = field(default=None, metadata={'lookup': 'Scrolls'})
    fifth_scroll: str = field(default=None, metadata={'lookup': 'Scrolls'})

    weapon: str = field(default=None, metadata={'lookup': 'Weapons'})
    helmet: str = field(default=None, metadata={'lookup': 'Helmets'})
    chestplate: str = field(default=None, metadata={'lookup': 'Chestplates'})
    leggings: str = field(default=None, metadata={'lookup': 'Leggings'})
    boots: str = field(default=None, metadata={'lookup': 'Boots'})

    food: str = field(default=None, metadata={'lookup': 'Foods'})

    @classmethod
    def manual(cls):
        kwargs = {}
        while True:
            try:
                userinput = input("Enter Build name to save Build (press 'Enter' to leave unsaved: ")
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

        print('Enter Build details')
        for f in fields(cls)[1:]:
            while True:
                try:
                    userinput = input(f'{f.name.replace('_', ' ').title()}: ')
                    if not userinput:
                        break

                    attr = userinput.upper().replace(' ', '_')
                    cls_name = f.metadata["lookup"]
                    _cls = globals().get(cls_name)

                    if _cls is None or not hasattr(_cls, attr):
                        raise ValueError

                    kwargs[f.name] = attr
                    break
                except ValueError:
                    print(f"Invalid value: '{userinput}'")

        if 'name' in kwargs:
            with open('data/builds.json', 'a') as f:
                f.write('\n')
                json.dump(kwargs, f)

        return cls(**kwargs)

    def __iter__(self):
        for f in fields(self)[1:]:
            value = getattr(self, f.name)
            if value is None:
                yield None
            else:
                lookup_cls = globals()[f.metadata['lookup']]
                yield getattr(lookup_cls, value)

    def __repr__(self):
        return self.name