############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    # def __repr__(self):

    #     return f'{self.name}'

    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


# functions outside of class MelonType
def make_melon_types():
    """Returns a list of current melon types."""

    melon_types = []

    def add_to_list(*melon):

        melon_types.extend(melon)

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries', 'mint')
    
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')

    watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    watermelon.add_pairing('ice cream')

    add_to_list(musk, casaba, crenshaw, watermelon)

    return melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        if len(melon.pairings) > 1:
            print(f'\n{melon.name} pairs with')
            for i in range(len(melon.pairings)):
                print(f'- {melon.pairings[i]}')
        else:
            print(f"\n{melon.name} pairs with\n- {melon.pairings[0]}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melontype_code = {}

    for melon in melon_types:
        melontype_code[melon.code] = melon

    return melontype_code

# melon_types = make_melon_types()
# melontype_code_dict = make_melon_type_lookup(melon_types)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, type_code, shape, color, field, harvester):
        """Initialize a melon""" 

        self.type_code = type_code
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """ sellable if shape and color rating > 5 and not from field 3. """

        if self.shape > 5 and self.color > 5 and self.field != 3:
            return True
        else:
            return False

# melon_types = make_melon_types()
# make_melons(melon_types)

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvested_melons = []
    
    melon_dict = make_melon_type_lookup(melon_types)
    # store dictionary of melon types with code as key in variable melon_by_id
    
    def add_to_list(*melon):

        harvested_melons.extend(melon)

    melon1 = Melon(melon_dict['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melon_dict['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melon_dict['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melon_dict['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melon_dict['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melon_dict['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melon_dict['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melon_dict['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melon_dict['yw'], 7, 10, 3, 'Sheila')

    add_to_list(melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9)

    return harvested_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



