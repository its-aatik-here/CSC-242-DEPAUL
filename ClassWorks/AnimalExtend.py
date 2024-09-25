class Animal(object):
    'a class that abstracts an animal'


    #Class invariants
    #1. the species is a non empty string
    #2 The language is a string that may be empty

    def __init__(self, spec = 'chicken', lang = 'bawk'):
        'the constructor'
        assert type(spec) == str and  len(spec) > 0, 'species must be a non empty string'

        self.species = spec
        self.language = lang
        
    def setSpecies(self, name):
        'sets the species of the animal'
        self.species = name
        
    def setLanguage(self, lang):
        'sets the language of the animal'
        self.language = lang
        
    def speak(self):
        'make the animal speak by returning a string'
        return f"I am a {self.species} and I {self.language}"

    def __repr__(self):
        'the representation of an animal'
        return f"Animal({self.species}, {self.language})"

    def __str__(self):
        'the string representation of an animal'
        return Animal.speak(self)

    def __eq__(self, other):
        'return True if self and other have the same species and language'
        return self.species.lower() == other.species.lower() and self.language == other.language

    def __add__(self, other):
        'returns a new hybrid Animal by combining self and other'
        spec = self.species + "/" + other.species
        lang = self.language + "/" + other.language
        return Animal(spec, lang)
