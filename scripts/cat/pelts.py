from random import choice, randint


class SingleColour():
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class TwoColour():
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC'
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"

class Marbled():
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"

class Rosette():
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"

class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"

class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Speckled():
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"

class Bengal():
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'

    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"

class Snowflake(object):
    name = "Snowflake"
    sprites = {1: 'snowflake', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK',
        'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} snowflake{self.length}"
        else:
            return f"{self.colour} snowflake{self.length}"
        
class Abyssinian(object):
    name = "Abyssinian"
    sprites = {1: 'abyssinian', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK',
        'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} abyssinian{self.length}"
        else:
            return f"{self.colour} abyssinian{self.length}"
        
class Clouded(object):
    name = "Clouded"
    sprites = {1: 'clouded', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK',
        'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} clouded{self.length}"
        else:
            return f"{self.colour} clouded{self.length}"
        
class Merle(object):
    name = "Merle"
    sprites = {1: 'merle', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK',
        'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} merle{self.length}"
        else:
            return f"{self.colour} merle{self.length}"

class GhostTabby(object):
    name = "GhostTabby"
    sprites = {1: 'ghosttabby', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} ghosttabby{self.length}"
        else:
            return f"{self.colour} ghosttabby{self.length}"
        
class PinstripeTabby(object):
    name = "PinstripeTabby"
    sprites = {1: 'pinstripetabby', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pinstripetabby{self.length}"
        else:
            return f"{self.colour} pinstripetabby{self.length}"
class Doberman(object):
    name = "Doberman"
    sprites = {1: 'doberman', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} doberman{self.length}"
        else:
            return f"{self.colour} doberman{self.length}"
class Oceloid(object):
    name = "Oceloid"
    sprites = {1: 'oceloid', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} oceloid{self.length}"
        else:
            return f"{self.colour} oceloid{self.length}"
        
class Monarch(object):
    name = "Monarch"
    sprites = {1: 'monarch', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} monarch{self.length}"
        else:
            return f"{self.colour} monarch{self.length}"
        
class Sokoke(object):
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke{self.length}"
        else:
            return f"{self.colour} sokoke{self.length}"
        
class Sokoke(object):
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke{self.length}"
        else:
            return f"{self.colour} sokoke{self.length}"

class Classictabby(object):
    name = "Classictabby"
    sprites = {1: 'classictabby', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classictabby{self.length}"
        else:
            return f"{self.colour} classictabby{self.length}"

class Lykoi(object):
    name = "Lykoi"
    sprites = {1: 'lykoi', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} lykoi{self.length}"
        else:
            return f"{self.colour} lykoi{self.length}"

class Mackereltabby(object):
    name = "Mackereltabby"
    sprites = {1: 'mackereltabby', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mackereltabby{self.length}"
        else:
            return f"{self.colour} mackereltabby{self.length}"

class Waveltabby(object):
    name = "Waveltabby"
    sprites = {1: 'waveltabby', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK', 'VITILIGO',
        'VITILIGO2', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} waveltabby{self.length}"
        else:
            return f"{self.colour} waveltabby{self.length}"


class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',  'MITAINE', 'SQUEAKS', 'STAR',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO', 'VITILIGO2', 'BCOLOURPOINT',
        'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
        ]

    def __init__(self, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN"])
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}
    white_patches = [
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS',
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE', 'BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN', 'CHOSENDF', 'CHOSENSC',
        'MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT',
        'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW', 'ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET',
        'MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK'
    ]
    def __init__(self, length):
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN"])
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN','IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT', 'SAND', 'CARAMEL', 'TOFFEE', 'FAWN',
#     'LEUCISTIC', 'MELRED', 'MELBLUE'
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN','IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT', 'SAND', 'CARAMEL', 'TOFFEE', 'FAWN',
#     'LEUCISTIC', 'MELRED', 'MELBLUE'
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER','LIGHTBROWN', 'BROWN', 'DARKBROWN','IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT', 'SAND', 'CARAMEL', 'TOFFEE', 'FAWN',
#     'LEUCISTIC', 'MELRED', 'MELBLUE'
]
tortiepatterns = ['tortiesolid', 'tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked',
    'tortiesmoke', 'tortierosette', 'tortiespeckled', 'tortiesnowflake', 'tortieclouded',
                  'tortiemerle', 'tortieghost', 'tortiepinstripe', 'tortieabyssinian',
                  'tortieoceloid', 'tortiemonarch', 'tortiesokoke']
patch_colours = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'snowflake',
               'clouded', 'merle', 'ghost', 'pinstripe', 'abyssinian', 'oceloid', 'monarch', 'sokoke']
tortiecolours = ["SILVER", "GREY", "DARKGREY", "BLACK", "LIGHTBROWN", "BROWN", "DARKBROWN"]

pelt_length = ["short", "medium", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE',
               'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN', 'PINK', 'SCARLET', 'VIOLET',
               'PALEYELLOW', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE',
               'BROWN', 'SPRINGGREEN', 'GOLD', 'HONEY', 'COPPER', 'MAGENTA',
               'MINT', 'EMERALD', 'PUMPKIN', 'ROSEGOLD', 'GREENGOLD', 'PINKBLUE',
               'DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE"]
scars2 = ["LEFTEAR", "RIGHTEAR", "LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW"]
scars3 = ["SNAKE", "TOETRAP"]

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER",
                     "POPPY FLOWER", "JUNIPER BERRIES", "DAISY FLOWER", "BORAGE FLOWER", "OAK LEAF", "BEECH LEAF",
                     "LAUREL LEAVES", "COLTSFOOT FLOWER", "BINDWEED VINE", "TORMENTIL FLOWER",
                    "BRIGHT-EYE FLOWER", "LAVENDER FLOWER", "YARROW CLUMP"
]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "PINK", "PURPLE", "MULTI", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW"
]

pelt_names_F = ["SingleColour", "SingleColour", "TwoColour", "Tabby", "Tortie", "Calico",
    "Tabby", "TwoColour", "Speckled", "Marbled", "Bengal", "Rosette", "Smoke", "Ticked", "Snowflake", "Abyssinian",
                "Clouded", "Merle", "GhostTabby", "PinstripeTabby", "Doberman", "Oceloid", "Monarch", "Sokoke",
                 "Classictabby","Lykoi", "Mackereltabby", "Wavetabby"]
pelt_names_M = ["SingleColour", "SingleColour", "TwoColour", "Tabby", "Tabby", "Speckled",
    "TwoColour", "Marbled", "Bengal", "Rosette", "Smoke", "Ticked", "Snowflake", "Abyssinian",
                "Clouded", "Merle", "GhostTabby", "PinstripeTabby", "Doberman", "Oceloid", "Monarch", "Sokoke", "Classictabby",
                "Lykoi", "Mackereltabby", "Wavetabby"]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT', 'SAND', 'CARAMEL', 'TOFFEE', 'FAWN',
#     'LEUCISTIC', 'MELRED', 'MELBLUE'
]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE',
               'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN', 'PINK', 'SCARLET', 'VIOLET',
               'PALEYELLOW', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE',
               'BROWN', 'SPRINGGREEN', 'GOLD', 'HONEY', 'COPPER', 'MAGENTA',
               'MINT', 'EMERALD', 'PUMPKIN', 'ROSEGOLD', 'GREENGOLD', 'PINKBLUE',
               'DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER'
]
little_white = ['LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS', 
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'FRECKLES2']
mid_white = ['TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'HALFHEART',
             'WHITEEAR', 'HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS']
high_white = ['ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE', 'MOJO', 'STAINS1', 'STAINS2', 'CRESCENT', 'COW', 'SWIFTPAW']
mostly_white = ['VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE']
point_markings = ['COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL']
vit = ['VITILIGO', 'VITILIGO2']
black_patches = ['BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER',
        'BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN']
chosen = ['CHOSENDF', 'CHOSENSC']
albino = ['ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET']
melanistic = ['MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANSTICDARK']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, black_patches, chosen, albino, melanistic, 'FULLWHITE', 'EXTRA', 'POINTMARK'
]


skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']


# CHOOSING PELT
def choose_pelt(gender,colour=None,white=None,pelt=None,length=None,determined=False):
    if pelt is None:
        a = randint(0, 100)
        if a != 1:
            pelt = choice(pelt_names_F) if gender == "female" else choice(pelt_names_M)
        else:
            pelt = choice(pelt_names_F)
            if gender == 'male' and pelt in ['Tortie', 'Calico']:
                print("Male tortie/calico!")
    elif pelt in ['Tortie', 'Calico'] and gender == 'male' and not determined:
        a = randint(0, 200)
        if a != 1:
            pelt = choice(pelt_names_M)
    if length is None:
        length = choice(pelt_length)
    if pelt == "SingleColour":
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == "TwoColour":
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == "Tabby":
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == "Marbled":
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == "Rosette":
        if colour is None and white is None:
            return Rosette(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosette(choice(pelt_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == "Smoke":
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == "Ticked":
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == "Speckled":
        if colour is None and white is None:
            return Speckled(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Speckled(choice(pelt_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == "Bengal":
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == "Snowflake":
        if colour is None and white is None:
            return Snowflake(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Snowflake(choice(pelt_colours), white, length)
        else:
            return Snowflake(colour, white, length)
    elif pelt == "Abyssinian":
        if colour is None and white is None:
            return Abyssinian(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Abyssinian(choice(pelt_colours), white, length)
        else:
            return Abyssinian(colour, white, length)
    elif pelt == "Clouded":
        if colour is None and white is None:
            return Clouded(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Clouded(choice(pelt_colours), white, length)
        else:
            return Clouded(colour, white, length)
    elif pelt == "Merle":
        if colour is None and white is None:
            return Merle(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Merle(choice(pelt_colours), white, length)
        else:
            return Merle(colour, white, length)
    elif pelt == "GhostTabby":
        if colour is None and white is None:
            return GhostTabby(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return GhostTabby(choice(pelt_colours), white, length)
        else:
            return GhostTabby(colour, white, length)
    elif pelt == "PinstripeTabby":
        if colour is None and white is None:
            return PinstripeTabby(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return PinstripeTabby(choice(pelt_colours), white, length)
        else:
            return PinstripeTabby(colour, white, length)
    elif pelt == "Doberman":
        if colour is None and white is None:
            return Doberman(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Doberman(choice(pelt_colours), white, length)
        else:
            return Doberman(colour, white, length)
    elif pelt == "Oceloid":
        if colour is None and white is None:
            return Oceloid(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Oceloid(choice(pelt_colours), white, length)
        else:
            return Oceloid(colour, white, length)
    elif pelt == "Monarch":
        if colour is None and white is None:
            return Monarch(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Monarch(choice(pelt_colours), white, length)
        else:
            return Monarch(colour, white, length)
    elif pelt == "Sokoke":
        if colour is None and white is None:
            return Sokoke(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Sokoke(choice(pelt_colours), white, length)
        else:
            return Sokoke(colour, white, length)
    elif pelt == "Classictabby":
        if colour is None and white is None:
            return Classictabby(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Classictabby(choice(pelt_colours), white, length)
        else:
            return Classictabby(colour, white, length)
    elif pelt == "Lykoi":
        if colour is None and white is None:
            return Lykoi(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Lykoi(choice(pelt_colours), white, length)
        else:
            return Lykoi(colour, white, length)
    elif pelt == "Mackereltabby":
        if colour is None and white is None:
            return Mackereltabby(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Mackereltabby(choice(pelt_colours), white, length)
        else:
            return Mackereltabby(colour, white, length)
    elif pelt == "Waveltabby":
        if colour is None and white is None:
            return Waveltabby(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Waveltabby(choice(pelt_colours), white, length)
        else:
            return Waveltabby(colour, white, length)
    elif pelt == "Tortie":
        if white is None:
            return Tortie(choice([False, True]), length)
        else:
            return Tortie(white, length)
    else:
        return Calico(length)

def describe_color(pelt, tortiecolour, tortiepattern, white_patches):
        color_name = ''
        color_name = str(pelt.colour).lower()
        if tortiecolour is not None:
            color_name = str(tortiecolour).lower()
        if color_name == 'palegrey':
            color_name = 'pale grey'
        elif color_name == 'darkgrey':
            color_name = 'dark grey'
        elif color_name == 'paleginger':
            color_name = 'pale ginger'
        elif color_name == 'darkginger':
            color_name = 'dark ginger'
        elif color_name == 'lightbrown':
            color_name = 'light brown'
        elif color_name == 'darkbrown':
            color_name = 'dark brown'
        if pelt.name == "Tabby":
            color_name = color_name + ' tabby'
        elif pelt.name == "Speckled":
            color_name = color_name + ' speckled'
        elif pelt.name == "Bengal":
            color_name = color_name + ' bengal'
        elif pelt.name == "Marbled":
            color_name = color_name + ' marbled tabby'
        elif pelt.name == "Rosette":
            color_name = color_name + ' rosetted'
        elif pelt.name == "Ticked":
            color_name = color_name + ' ticked tabby'
        elif pelt.name == "Smoke":
            color_name = color_name + ' smoke'
        elif pelt.name == "Snowflake":
            color_name = color_name + ' snowflake'
        elif pelt.name == "Abyssinian":
            color_name = color_name + ' abyssinian'
        elif pelt.name == "Clouded":
            color_name = color_name + ' clouded'
        elif pelt.name == "Merle":
            color_name = color_name + ' merle'
        elif pelt.name == "GhostTabby":
            color_name = color_name + ' ghosttabby'
        elif pelt.name == "PinstripeTabby":
            color_name = color_name + ' pinstripe'
        elif pelt.name == "Doberman":
            color_name = color_name + ' doberman'
        elif pelt.name == "Oceloid":
            color_name = color_name + ' oceloid'
        elif pelt.name == "Monarch":
            color_name = color_name + ' monarch'
        elif pelt.name == "Sokoke":
            color_name = color_name + ' sokoke'
        elif pelt.name == "Classictabby":
            color_name = color_name + ' classictabby'
        elif pelt.name == "Lykoi":
            color_name = color_name + ' lykoi'
        elif pelt.name == "Mackereltabby":
            color_name = color_name + ' mackereltabby'
        elif pelt.name == "Wavetabby":
            color_name = color_name + ' wavetabby'

        elif pelt.name == "Tortie":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' torbie'
            else:
                color_name = color_name + ' tortie'
        elif pelt.name == "Calico":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' tabico'
            else:
                color_name = color_name + ' calico'
        # enough to comment but not make calico
        if white_patches is not None:
            if white_patches in little_white + mid_white:
                color_name = color_name + ' and white'
            # and white
            elif white_patches in high_white:
                if pelt.name != "Calico":
                    color_name = color_name + ' and white'
            # white and
            elif white_patches in mostly_white:
                color_name = 'white and ' + color_name
            # colorpoint
            elif white_patches in point_markings:
                color_name = color_name + ' point'
                if color_name == 'dark ginger point' or color_name == 'ginger point':
                    color_name = 'flame point'
            # vitiligo
            elif white_patches in vit:
                color_name = color_name + ' with vitiligo'
            # chosen
            elif white_patches in chosen:
                color_name = color_name + ' star marked'
            # black patches
            elif white_patches in black_patches:
                color_name = 'black and ' + color_name
            # melanistic
            elif white_patches in melanistic:
                color_name = 'melanistic ' + color_name
            # albino
            elif white_patches in albino:
                color_name = 'albino ' + color_name
        else:
            color_name = color_name

        if color_name == 'tortie':
            color_name = 'tortoiseshell'

        if white_patches == 'FULLWHITE':
            color_name = 'white'

        if color_name == 'white and white':
            color_name = 'white'

        return color_name

