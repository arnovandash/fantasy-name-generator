import random

syllables_start = ('Bl', 'Br', 'Cl', 'Cr', 'Dr', 'Tr', 'Fr', 'Fl', 'Gr', 'Gl', 'Pr', 'Pl', 'Sc', 'St', 'Sp', 'Sk', 'Sl', 'Kr', 'Kl')
syllables_end = ('nd', 'ng', 'nt', 'nk', 'mp', 'rd', 'ld', 'lp', 'rk', 'lt', 'lf', 'pt', 'ct', 'ck', 'rt')
#vowels = ('a', 'e', 'i', 'o', 'u', 'ai', 'au', 'oi', 'ou', 'ei', 'eu', 'ia', 'io', 'iu', 'ie', 'oa', 'oe', 'ua', 'ue', 'ui', 'uo', 'iy', 'ey', 'ay', 'ee', 'oo', 'aa', 'ae', 'ea', 'ie')
vowels = ('a', 'e', 'i', 'o', 'u')

def make_syllable():
    part1 = random.choice(syllables_start) if random.random() > 0.4 else ''
    part2 = random.choice(vowels)
    part3 = random.choice(syllables_end) if random.random() > 0.4 else ''
    syllable = part1 + part2 + part3
    if len(syllable) < 2:
        return make_syllable()  # Ensure each syllable is robust
    return syllable

def name_gen(min_syllables, max_syllables):
    if min_syllables > max_syllables:
        min_syllables, max_syllables = max_syllables, min_syllables  # Swap if out of order
    num_syllables = random.randint(min_syllables, max_syllables)
    name = ''.join(make_syllable() for _ in range(num_syllables))
    if len(name) < 3:
        return name_gen(min_syllables, max_syllables)  # Regenerate if too short
    return name.capitalize()

def run():
    while True:
        input("Hit enter to generate a name...")
        first = name_gen(1, random.randint(1, 2))
        last = name_gen(random.randint(1, 2), random.randint(2, 3))
        print(f"{first} {last}\n")

if __name__ == "__main__":
    run()

