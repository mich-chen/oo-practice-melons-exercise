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

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries', 'mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cred', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    watermelon.add_pairing('ice cream')
    all_melon_types.append(watermelon)


    return all_melon_types

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

    reporting_codes = ('musk', 'cas', 'cren', 'yw')

    melontype_code = {}

    for melon in melon_types:
        melontype_code[melon.code] = melon

    return melontype_code

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




def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



