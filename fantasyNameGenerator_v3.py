import random

# First name components
starts = ['Fr', 'Th', 'Gr', 'Br', 'Sar', 'Ar', 'Leg', 'Gal', 'Mel', 'Al', 'Sev', 'Bel', 'Nev', 'Ron', 'Her']
middles = ['odo', 'ara', 'ora', 'ion', 'ili', 'an', 'ro', 'yn', 'ael', 'wen', 'yri', 'ery', 'dra', 'gon', 'do']
ends = ['do', 'n', 'ron', 'las', 'um', 'on', 'gan', 'or', 'as', 'is', 'ael', 'an', 'inn', 'mond', 'dor']

# Surname components
elements = ['Storm', 'Thorn', 'Silver', 'Bright', 'Shadow', 'Hall', 'Fell', 'Wind', 'Star', 'Light', 'Dark', 'Fire', 'Ice', 'Moon', 'Sun', 'Heart',
            'Raven', 'Wolf', 'Dragon', 'Iron', 'Gold', 'Mist', 'Cloud', 'Flame', 'Snow', 'River', 'Spear', 'Oak', 'Ash', 'Elm', 'Marble', 'Quartz', 'Amber', 'Emerald']
professions = ['Butcher', 'Barker', 'Hunter', 'Smith', 'Wright', 'Tailor', 'Mason', 'Miner', 'Brewer', 'Fletcher', 'Scribe', 'Carpenter', 'Shepherd']
colors = ['Black', 'White', 'Red', 'Green', 'Blue', 'Gray', 'Silver', 'Golden', 'Copper', 'Bronze', 'Sapphire', 'Emerald', 'Scarlet', 'Ivory', 'Ebony']
modifiers = ['Wood', 'Ridge', 'Forge', 'Breaker', 'Bearer', 'Seeker', 'Ward', 'Blade', 'Song', 'Field', 'Stone', 'Cloak', 'Shield', 'Runner', 'Rider', 'Smith',
             'Mantle', 'Helm', 'Crest', 'Lock', 'Foot', 'Hand', 'Fist', 'Bend', 'Glow', 'March', 'Watch', 'Whisper', 'Spear', 'Bane', 'Vault', 'Guard', 'Wing']
suffixes = ['son', 'wyn', 'ovich', 'ski', 'stein', 'dottir', 'berg', 'ford', 'hall', 'wood', 'mark', 'shire', 'gate', 'brook', 'root', 'borne', 'ville', 'water',
            'thane', 'wynn', 'ley', 'mont', 'more']

def make_name():
    part1 = random.choice(starts)
    part2 = random.choice(middles)
    part3 = random.choice(ends) if random.random() > 0.5 else ''
    return part1 + part2 + part3

def make_surname():
    base = random.choice(elements + professions + colors)
    modifier = random.choice(modifiers) if random.random() > 0.3 else ''
    suffix = random.choice(suffixes) if random.random() > 0.7 else ''
    
    components = [component for component in [modifier, base, suffix] if component]
    return ''.join(components)

def run():
    while True:
        input("Hit enter to generate a full name...")
        first_name = make_name().capitalize()
        last_name = make_surname().capitalize()
        print(f"{first_name} {last_name}\n")

if __name__ == "__main__":
    run()

