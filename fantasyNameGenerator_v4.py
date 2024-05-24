import random

# First name components
female_starts = ['Sar', 'Ar', 'Mel', 'Al', 'Bel', 'Her', 'Hel', 'Aer', 'Sal', 'L', 'Qu', 'El', 'Mar', 'Jan', 'Elis', 'Em', 'Cat']
female_middles = ['ara', 'ora', 'ion', 'ili', 'an', 'ro', 'yn', 'ael', 'wen', 'yri', 'ery', 'dra', 'oga', 'ina', 'etta', 'ella']
female_ends = ['a', 'n', 'ra', 'la', 'is', 'ael', 'yn', 'ia', 'el']

male_starts = ['Fr', 'Th', 'Gr', 'Br', 'Leg', 'Gal', 'Sev', 'Nev', 'Ron', 'K', 'C', 'L', 'Qu', 'Wil', 'Jon', 'Chr', 'Rob', 'Dan']
male_middles = ['odo', 'ara', 'ora', 'ion', 'ili', 'an', 'ro', 'yn', 'ael', 'wen', 'yri', 'ery', 'dra', 'gon', 'do', 'oge']
male_ends = ['do', 'n', 'ron', 'las', 'um', 'on', 'gan', 'or', 'as', 'is', 'ael', 'an', 'inn', 'mond', 'dor']

neutral_starts = ['Sar', 'Ar', 'Mel', 'Al', 'Bel', 'Her', 'Hel', 'Aer', 'Sal', 'L', 'Qu', 'Fr', 'Th', 'Gr', 'Br', 'Leg', 'Gal', 'Sev', 'Nev', 'Ron', 'K', 'C', 'Wil', 'Jon', 'Chr', 'Rob', 'Dan']
neutral_middles = ['ara', 'ora', 'ion', 'ili', 'an', 'ro', 'yn', 'ael', 'wen', 'yri', 'ery', 'dra', 'oga', 'do', 'oge']
neutral_ends = ['a', 'n', 'ra', 'la', 'is', 'ael', 'yn', 'ia', 'el', 'do', 'ron', 'las', 'um', 'on', 'gan', 'or', 'as', 'is', 'an', 'inn', 'mond', 'dor']

# Surname components including new animal names
elements = ['Storm', 'Thorn', 'Silver', 'Bright', 'Shadow', 'Hall', 'Fell', 'Wind', 'Star', 'Light', 'Dark', 'Fire', 'Ice', 'Moon', 'Sun', 'Heart',
            'Raven', 'Wolf', 'Dragon', 'Iron', 'Gold', 'Mist', 'Cloud', 'Flame', 'Snow', 'River', 'Spear', 'Oak', 'Ash', 'Elm', 'Marble', 'Quartz', 'Amber', 'Emerald']
animals = ['Lion', 'Eagle', 'Falcon', 'Fox', 'Bear', 'Owl', 'Tiger', 'Serpent', 'Griffin', 'Phoenix', 'Dragon', 'Wolf', 'Elk', 'Stag', 'Horse']
professions = ['Butcher', 'Barker', 'Hunter', 'Smith', 'Wright', 'Tailor', 'Mason', 'Miner', 'Brewer', 'Fletcher', 'Scribe', 'Carpenter', 'Shepherd']
colors = ['Black', 'White', 'Red', 'Green', 'Blue', 'Gray', 'Silver', 'Golden', 'Copper', 'Bronze', 'Sapphire', 'Emerald', 'Scarlet', 'Ivory', 'Ebony']
modifiers = ['Wood', 'Ridge', 'Forge', 'Breaker', 'Bearer', 'Seeker', 'Ward', 'Blade', 'Song', 'Field', 'Stone', 'Cloak', 'Shield', 'Runner', 'Rider', 'Smith',
             'Mantle', 'Helm', 'Crest', 'Lock', 'Foot', 'Hand', 'Fist', 'Bend', 'Glow', 'March', 'Watch', 'Whisper', 'Spear', 'Bane', 'Vault', 'Guard', 'Wing']
suffixes = ['son', 'wyn', 'ovich', 'ski', 'stein', 'dottir', 'berg', 'ford', 'hall', 'wood', 'mark', 'shire', 'gate', 'brook', 'root', 'borne', 'ville', 'water',
            'thane', 'wynn', 'ley', 'mont', 'more', 'mere']

def make_name(gender):
    if gender == 'female':
        starts = female_starts + neutral_starts
        middles = female_middles + neutral_middles
        ends = female_ends + neutral_ends
    elif gender == 'male':
        starts = male_starts + neutral_starts
        middles = male_middles + neutral_middles
        ends = male_ends + neutral_ends

    parts = [random.choice(starts), random.choice(middles)]
    if random.random() > 0.8:
        parts.append(random.choice(ends))
    return ''.join(parts).capitalize()

def make_surname():
    base = random.choice(elements + professions + colors + animals)  # Including animals in the base selection
    modifier = random.choice(modifiers) if random.random() > 0.3 else ''
    suffix = random.choice(suffixes) if random.random() > 0.7 else ''

    components = [component for component in [modifier, base, suffix] if component]
    return ''.join(components).capitalize()

def run():
    while True:
        gender = input("Enter gender (male/female): ").strip().lower()
        if gender not in ['male', 'female']:
            print("Invalid gender. Please enter 'male' or 'female'.")
            continue
        first_name = make_name(gender)
        last_name = make_surname()
        print(f"{first_name} {last_name}\n")

if __name__ == "__main__":
    run()

