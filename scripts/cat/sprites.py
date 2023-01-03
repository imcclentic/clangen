import pygame

from scripts.game_structure.game_essentials import *


class Sprites():

    def __init__(self, original_size, new_size=None):
        self.size = original_size  # size of a single sprite in a spritesheet
        self.new_size = self.size * 2 if new_size is None else new_size
        self.spritesheets = {}
        self.images = {}
        self.groups = {}
        self.sprites = {}

    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def find_sprite(self, group_name, x, y):
        """
        Find singular sprite from a group.

        Parameters:
        group_name -- Name of Pygame group to find sprite from.
        x -- X-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        y -- Y-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        """
        # pixels will be calculated automatically, so for x and y, just use 0, 1, 2, 3 etc.
        new_sprite = pygame.Surface((self.size, self.size),
                                    pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(self.groups[group_name], (0, 0),
                        (x * self.size, y * self.size, (x + 1) * self.size,
                         (y + 1) * self.size))
        return new_sprite

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=3):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        # making the group
        new_group = pygame.Surface(
            (self.size * sprites_x, self.size * sprites_y),
            pygame.HWSURFACE | pygame.SRCALPHA)
        new_group.blit(
            self.spritesheets[spritesheet], (0, 0),
            (pos[0] * sprites_x * self.size, pos[1] * sprites_y * self.size,
             (pos[0] + sprites_x) * self.size,
             (pos[1] + sprites_y) * self.size))

        self.groups[name] = new_group

        # splitting group into singular sprites and storing into self.sprites section
        x_spr = 0
        y_spr = 0
        for x in range(sprites_x * sprites_y):
            new_sprite = pygame.Surface((self.size, self.size),
                                        pygame.HWSURFACE | pygame.SRCALPHA)
            new_sprite.blit(new_group, (0, 0),
                            (x_spr * self.size, y_spr * self.size,
                             (x_spr + 1) * self.size, (y_spr + 1) * self.size))
            self.sprites[name + str(x)] = new_sprite
            x_spr += 1
            if x_spr == sprites_x:
                x_spr = 0
                y_spr += 1

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        scars = 'scars'

        for a, i in enumerate(
                ["ONE", "TWO", "THREE", "LEFTEAR", "RIGHTEAR", "NOTAIL"]):
            sprites.make_group('scars', (a, 0), f'scars{i}')
            sprites.make_group('scarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["MANLEG", "BRIGHTHEART", "MANTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]):
            sprites.make_group('scars', (a, 1), f'scars{i}')
            sprites.make_group('scarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL"]):
            sprites.make_group('scars', (a, 2), f'scars{i}')
            sprites.make_group('scarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE"]):
            sprites.make_group('scars', (a, 3), f'scars{i}')
            sprites.make_group('scarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE"]):
            sprites.make_group('Newscars', (a, 0), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["BELLY", "TOETRAP", "SNAKE"]):
            sprites.make_group('Newscars', (a, 1), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["LEGBITE", "NECKBITE", "FACE", "HALFTAIL", "NOPAW"]):
            sprites.make_group('Newscars', (a, 2), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]):
            sprites.make_group('Newscars', (a, 3), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

            # Accessories
        for a, i in enumerate([
            "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"]):
            sprites.make_group('medcatherbs', (a, 0), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 0), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"]):
            sprites.make_group('medcatherbs', (a, 1), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 1), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]):
            sprites.make_group('medcatherbs', (a, 3), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 3), f'acc_herbsextra{i}', sprites_y=2)
            sprites.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')
            sprites.make_group('medcatherbsextra', (5, 2), 'acc_herbsextraDRY HERBS', sprites_y=2)
        
        for a, i in enumerate([
            "POPPY FLOWER", "JUNIPER BERRIES", "DAISY FLOWER", "BORAGE FLOWER", "OAK LEAF", "BEECH LEAF"]):
            sprites.make_group('flowers', (a, 0), f'acc_herbs{i}')
            sprites.make_group('flowersextra', (a, 0), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "LAUREL LEAVES", "COLTSFOOT FLOWER", "BINDWEED VINE", "TORMENTIL FLOWER"]):
            sprites.make_group('flowers', (a, 1), f'acc_herbs{i}')
            sprites.make_group('flowersextra', (a, 1), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "BRIGHT-EYE FLOWER", "LAVENDER FLOWER", "YARROW CLUMP"]):
            sprites.make_group('flowers', (a, 2), f'acc_herbs{i}')
            sprites.make_group('flowersextra', (a, 2), f'acc_herbsextra{i}', sprites_y=2)

        for a, i in enumerate([
            "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]):
            sprites.make_group('medcatherbs', (a, 2), f'acc_wild{i}')
            sprites.make_group('medcatherbsextra', (a, 2), f'acc_wildextra{i}', sprites_y=2)
        for a, i in enumerate(["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"]):
            sprites.make_group('collars', (a, 0), f'collars{i}')
            sprites.make_group('collarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREEN", "RAINBOW", "BLACK", "SPIKES"]):
            sprites.make_group('collars', (a, 1), f'collars{i}')
            sprites.make_group('collarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINK", "PURPLE", "MULTI"]):
            sprites.make_group('collars', (a, 2), f'collars{i}')
            sprites.make_group('collarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL",
            "LIMEBELL"
        ]):
            sprites.make_group('bellcollars', (a, 0), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL"]):
            sprites.make_group('bellcollars', (a, 1), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBELL", "PURPLEBELL", "MULTIBELL"]):
            sprites.make_group('bellcollars', (a, 2), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
            "LIMEBOW"
        ]):
            sprites.make_group('bowcollars', (a, 0), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW"]):
            sprites.make_group('bowcollars', (a, 1), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBOW", "PURPLEBOW", "MULTIBOW"]):
            sprites.make_group('bowcollars', (a, 2), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)


sprites = Sprites(50)
tiles = Sprites(64)

for x in [
    'lineart', 'singlecolours', 'speckledcolours', 'tabbycolours',
    'whitepatches', 'eyes', 'singleextra', 'tabbyextra',
    'speckledextra', 'whiteextra', 'eyesextra', 'skin',
    'skinextra', 'scars', 'scarsextra', 'whitenewextra', 'whitepatchesnew',
    'scarsdark', 'scarsdarkextra', 'collars', 'collarsextra',
    'bellcollars', 'bellcollarsextra', 'bowcollars', 'bowcollarsextra',
    'speckledcolours2', 'speckledextra2', 'tabbycolours2', 'tabbyextra2',
    'rosettecolours', 'rosetteextra', 'smokecolours', 'smokeextra', 'tickedcolors', 'tickedextra',
    'whitepatches3', 'whitepatches3extra', 'whitepatches4', 'whitepatches4extra',
    'Newscars', 'Newscarsextra', 'shaders', 'lineartdead',
    'tortiecolourssolid', 'tortiecolourstabby', 'tortiecoloursbengal', 'tortiecoloursmarbled',
    'tortiecoloursticked', 'tortiecolourssmoke', 'tortiecoloursrosette', 'tortiecoloursspeckled',
    'tortiesextrasolid', 'tortiesextratabby', 'tortiesextrabengal', 'tortiesextramarbled', 'tortiesextraticked',
    'tortiesextrasmoke', 'tortiesextrarosette', 'tortiesextraspeckled',
    'medcatherbs', 'medcatherbsextra', 'lineartdf', 'eyes_df', 'eyesextra_df',
     'lineart', 'singlecolours', 'speckledcolours', 'tabbycolours',
    'whitepatches', 'eyes', 'singleextra', 'tabbyextra',
    'speckledextra', 'whiteextra', 'eyesextra', 'skin',
    'skinextra', 'scars', 'scarsextra', 'whitenewextra', 'whitepatchesnew',
    'scarsdark', 'scarsdarkextra', 'collars', 'collarsextra',
    'bellcollars', 'bellcollarsextra', 'bowcollars', 'bowcollarsextra',
    'speckledcolours2', 'speckledextra2', 'tabbycolours2', 'tabbyextra2',
    'rosettecolours', 'rosetteextra', 'smokecolours', 'smokeextra', 'tickedcolors', 'tickedextra',
    'Newscars', 'Newscarsextra', 'shaders', 'lineartdead',
    'tortiecolourssolid', 'tortiecolourstabby', 'tortiecoloursbengal', 'tortiecoloursmarbled',
    'tortiecoloursticked', 'tortiecolourssmoke', 'tortiecoloursrosette', 'tortiecoloursspeckled',
    'tortiesextrasolid', 'tortiesextratabby', 'tortiesextrabengal', 'tortiesextramarbled', 'tortiesextraticked',
    'tortiesextrasmoke', 'tortiesextrarosette', 'tortiesextraspeckled',
    'medcatherbs', 'medcatherbsextra', 'lineartdf', 'eyes_df', 'eyesextra_df',
    'snowflake','snowflakeextra', 'tortiesnowflake',
    'tortiesnowflakeextra', 'abyssinian', 'abyssinianextra', 'clouded', 'cloudedextra',
    'tortieclouded', 'tortiecloudedextra', 'merle', 'merleextra', 'tortiemerle',
    'tortiemerleextra', 'ghosttabby', 'ghosttabbyextra', 'pinstripetabby', 'pinstripetabbyextra',
    'tortieghostextra',
    'tortieghost', 'tortiepinstripeextra', 'tortiepinstripe', 'doberman', 'dobermanextra', 'oceloid', 'oceloidextra',
    'monarch', 'monarchextra', 'blackpatches', 'blackpatchesextra', 'newsingles', 'newtabby', 'newmarbled', 'newrosette',
    'newsmoke', 'newticked', 'newspeckled', 'newbengal', 'newsnowflake', 'newabyssinian', 'newclouded',
    'newmerle', 'newghosttabby',
    'newpinstripe', 'newdoberman', 'newoceloid', 'newmonarch', 'newsinglesextra', 'newtabbyextra',
    'newmarbledextra', 'newrosetteextra',
    'newsmokeextra', 'newtickedextra', 'newspeckledextra', 'newbengalextra', 'newsnowflakeextra',
    'newabyssinianextra', 'newcloudedextra',
    'newmerleextra', 'newghosttabbyextra','newpinstripeextra', 'newdobermanextra', 'newoceloidextra',
    'newmonarchextra', 'tortieabyssinian',
    'tortieabyssinianextra', 'sokoke', 'sokokeextra', 'tortiemonarch', 'tortiemonarchextra', 'tortiesokoke',
    'tortiesokokeextra', 'tortieoceloid',
    'tortieoceloidextra', 'newsokoke', 'newsokokeextra', 'classictabby', 'classictabbyextra',
    'classictabbynew', 'classictabbyextranew', 'lykoi', 'lykoiextra', 'lykoinew', 'lykoiextranew',
    'mackereltabby', 'mackereltabbyextra', 'mackereltabbynew', 'mackereltabbyextranew',
    'wavetabby', 'wavetabbyextra', 'wavetabbynew', 'wavetabbyextranew', 'eyes2', 'eyes2extra',
    'flowers', 'flowersextra', 'white2', 'white2extra', 'melalbino', 'melalbinoextra'

]:
    sprites.spritesheet(f"sprites/{x}.png", x)

for sprite in [
    'Paralyzed_lineart', 'singleparalyzed', 'speckledparalyzed',
    'tabbyparalyzed', 'whiteallparalyzed', 'eyesparalyzed',
    'tabbyparalyzed', 'tortiesparalyzed', 'scarsparalyzed', 'skinparalyzed',
    'medcatherbsparalyzed'

]:
    sprites.spritesheet(f"sprites/paralyzed/{sprite}.png", sprite)

for x in ['dithered']:
    tiles.spritesheet(f"sprites/{x}.png", x)

# Line art
sprites.make_group('lineart', (0, 0), 'lines', sprites_y=5)
sprites.make_group('Paralyzed_lineart', (0, 0),
                   'p_lines',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('shaders', (0, 0), 'shaders', sprites_y=5)
sprites.make_group('lineartdead', (0, 0), 'lineartdead', sprites_y=5)
sprites.make_group('lineartdf', (0, 0), 'lineartdf', sprites_y=5)

for a, i in enumerate(
        ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 0), f'eyesextra{i}', sprites_y=2)
# sprites.make_group('eyes', (0, 1), 'eyesDARKBLUE')
# sprites.make_group('eyes', (1, 1), 'eyesBLUEYELLOW')
# sprites.make_group('eyes', (2, 1), 'eyesBLUEGREEN')
# sprites.make_group('eyesextra', (0, 1), 'eyesextraDARKBLUE', sprites_y=2)
# sprites.make_group('eyesextra', (1, 1), 'eyesextraBLUEYELLOW', sprites_y=2)
# sprites.make_group('eyesextra', (2, 1), 'eyesextraBLUEGREEN', sprites_y=2)

for a, i in enumerate(
    ['DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN', 'PINK', 'SCARLET', 'VIOLET']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 1), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
    ['PALEYELLOW', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE']):
    sprites.make_group('eyes', (a, 2), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 2), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
    ['BROWN', 'SPRINGGREEN', 'GOLD', 'HONEY', 'COPPER', 'MAGENTA']):
    sprites.make_group('eyes2', (a, 0), f'eyes{i}')
    sprites.make_group('eyes2extra', (a, 0), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
    ['MINT', 'EMERALD', 'PUMPKIN', 'ROSEGOLD', 'GREENGOLD', 'PINKBLUE']):
    sprites.make_group('eyes2', (a, 1), f'eyes{i}')
    sprites.make_group('eyes2extra', (a, 1), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
    ['DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER']):
    sprites.make_group('eyes2', (a, 2), f'eyes{i}')
    sprites.make_group('eyes2extra', (a, 2), f'eyesextra{i}', sprites_y=2)

for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANY2']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
    sprites.make_group('whiteextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
    'LIGHTSONG', 'VITILIGO'
]):
    sprites.make_group('whitepatchesnew', (a, 0), f'white{i}')
    sprites.make_group('whitenewextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY', 'COLOURPOINTCREAMY',
    'VANCREAMY', 'ANY2CREAMY'
]):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
    sprites.make_group('whiteextra', (a, 1), f'whiteextra{i}', sprites_y=2)
# extra
sprites.make_group('whitepatches', (0, 2), 'whiteEXTRA')
sprites.make_group('whiteextra', (0, 2), 'whiteextraEXTRA', sprites_y=2)

# ryos white patches
for a, i in enumerate(
        ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'VITILIGO2']):
    sprites.make_group('whitepatches3', (a, 0), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'PAWS', 'MITAINE']):
    sprites.make_group('whitepatches3', (a, 1), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'SCOURGE']):
    sprites.make_group('whitepatches3', (a, 2), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 2), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'HONEY']):
    sprites.make_group('whitepatches3', (a, 3), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 3), f'whiteextra{i}', sprites_y=2)

# beejeans white patches
for a, i in enumerate(['PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED']):
    sprites.make_group('whitepatches4', (a, 0), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK']):
    sprites.make_group('whitepatches4', (a, 1), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 1), 'whiteextra' + i, sprites_y=2)
    
#black patches and chosen marks
for a, i in enumerate(['BCOLOURPOINT', 'BRAGDOLL', 'BPANTS', 'BREVERSEPANTS', 'BGLASS', 'BMISTER']):
    sprites.make_group('blackpatches', (a, 0), f'white{i}')
    sprites.make_group('blackpatchesextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['BFANCY', 'BFRECKLES', 'BRINGTAIL', 'BHALFFACE', 'BFAROFA', 'BDAMIEN']):
    sprites.make_group('blackpatches', (a, 1), f'white{i}')
    sprites.make_group('blackpatchesextra', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['CHOSENDF', 'CHOSENSC']):
    sprites.make_group('blackpatches', (a, 2), f'white{i}')
    sprites.make_group('blackpatchesextra', (a, 2), f'whiteextra{i}', sprites_y=2)
    
#more white marks
for a, i in enumerate(['MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT']):
    sprites.make_group('white2', (a, 0), f'white{i}')
    sprites.make_group('white2extra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['HUSKY', 'COW', 'MASK', 'SKUNK2', 'BROWNSPOTS', 'SWIFTPAW']):
    sprites.make_group('white2', (a, 1), f'white{i}')
    sprites.make_group('white2extra', (a, 1), f'whiteextra{i}', sprites_y=2)

#albino and melanistic
# for a, i in enumerate(['CHARCOAL', 'RUBY', 'BERRY', 'ROSE', 'TAN', 'SILVER']):
#     sprites.make_group('melalbino', (a, 0), f'white{i}')
#     sprites.make_group('melalbinoextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([None]):
    sprites.make_group('melalbino', (a, 0), f'white{i}')
    sprites.make_group('melalbinoextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['ALBINOPINK', 'ALBINOBLUE', 'ALBINORED', 'ALBINOVIOLET']):
    sprites.make_group('melalbino', (a, 1), f'white{i}')
    sprites.make_group('melalbinoextra', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['MELANISTICLIGHT', 'MELANISTICMEDIUM', 'MELANISTICDARK']):
    sprites.make_group('melalbino', (a, 2), f'white{i}')
    sprites.make_group('melalbinoextra', (a, 2), f'whiteextra{i}', sprites_y=2)

#single (solid)
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('singlecolours', (a, 0), f'single{i}')
    sprites.make_group('singleextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('singlecolours', (a, 1), f'single{i}')
    sprites.make_group('singleextra', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('singlecolours', (a, 2), f'single{i}')
    sprites.make_group('singleextra', (a, 2), f'singleextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newsingles', (a, 0), f'single{i}')
    sprites.make_group('newsinglesextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newsingles', (a, 1), f'single{i}')
    sprites.make_group('newsinglesextra', (a, 1), f'singleextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newsingles', (a, 2), f'single{i}')
#     sprites.make_group('newsinglesextra', (a, 2), f'singleextra{i}', sprites_y=2)
#tabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('tabbycolours', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('tabbycolours', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('tabbycolours', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 2), f'tabbyextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newtabby', (a, 0), f'tabby{i}')
    sprites.make_group('newtabbyextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newtabby', (a, 1), f'tabby{i}')
    sprites.make_group('newtabbyextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newtabby', (a, 2), f'tabby{i}')
#     sprites.make_group('newtabbyextra', (a, 2), f'tabbyextra{i}', sprites_y=2)
#marbled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('tabbycolours2', (a, 0), f'marbled{i}')
    sprites.make_group('tabbyextra2', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('tabbycolours2', (a, 1), f'marbled{i}')
    sprites.make_group('tabbyextra2', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('tabbycolours2', (a, 2), f'marbled{i}')
    sprites.make_group('tabbyextra2', (a, 2), f'marbledextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newmarbled', (a, 0), f'marbled{i}')
    sprites.make_group('newmarbledextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newmarbled', (a, 1), f'marbled{i}')
    sprites.make_group('newmarbledextra', (a, 1), f'marbledextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newmarbled', (a, 2), f'marbled{i}')
#     sprites.make_group('newmarbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
#rosette
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('rosettecolours', (a, 0), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('rosettecolours', (a, 1), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('rosettecolours', (a, 2), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 2), f'rosetteextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newrosette', (a, 0), f'rosette{i}')
    sprites.make_group('newrosetteextra', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newrosette', (a, 1), f'rosette{i}')
    sprites.make_group('newrosetteextra', (a, 1), f'rosetteextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newrosette', (a, 2), f'rosette{i}')
#     sprites.make_group('newrosetteextra', (a, 2), f'rosetteextra{i}', sprites_y=2)
#smoke
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('smokecolours', (a, 0), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('smokecolours', (a, 1), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('smokecolours', (a, 2), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 2), f'smokeextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newsmoke', (a, 0), f'smoke{i}')
    sprites.make_group('newsmokeextra', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newsmoke', (a, 1), f'smoke{i}')
    sprites.make_group('newsmokeextra', (a, 1), f'smokeextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newsmoke', (a, 2), f'smoke{i}')
#     sprites.make_group('newsmokeextra', (a, 2), f'smokeextra{i}', sprites_y=2)
#ticked
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('tickedcolors', (a, 0), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('tickedcolors', (a, 1), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('tickedcolors', (a, 2), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newticked', (a, 0), f'ticked{i}')
    sprites.make_group('newtickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newticked', (a, 1), f'ticked{i}')
    sprites.make_group('newtickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newticked', (a, 2), f'ticked{i}')
#     sprites.make_group('newtickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)

#speckled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('speckledcolours', (a, 0), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('speckledcolours', (a, 1), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('speckledcolours', (a, 2), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 2), f'speckledextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newspeckled', (a, 0), f'speckled{i}')
    sprites.make_group('newspeckledextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newspeckled', (a, 1), f'speckled{i}')
    sprites.make_group('newspeckledextra', (a, 1), f'speckledextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newspeckled', (a, 2), f'speckled{i}')
#     sprites.make_group('newspeckledextra', (a, 2), f'speckledextra{i}', sprites_y=2)

#bengal
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('speckledcolours2', (a, 0), f'bengal{i}')
    sprites.make_group('speckledextra2', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('speckledcolours2', (a, 1), f'bengal{i}')
    sprites.make_group('speckledextra2', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('speckledcolours2', (a, 2), f'bengal{i}')
    sprites.make_group('speckledextra2', (a, 2), f'bengalextra{i}', sprites_y=2)

for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newbengal', (a, 0), f'bengal{i}')
    sprites.make_group('newbengalextra', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newbengal', (a, 1), f'bengal{i}')
    sprites.make_group('newbengalextra', (a, 1), f'bengalextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newbengal', (a, 2), f'bengal{i}')
#     sprites.make_group('newbengalextra', (a, 2), f'bengalextra{i}', sprites_y=2)

#snowflake
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('snowflake', (a, 0), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 0), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('snowflake', (a, 1), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 1), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('snowflake', (a, 2), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 2), f'snowflakeextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newsnowflake', (a, 0), f'snowflake{i}')
    sprites.make_group('newsnowflakeextra', (a, 0), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newsnowflake', (a, 1), f'snowflake{i}')
    sprites.make_group('newsnowflakeextra', (a, 1), f'snowflakeextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newsnowflake', (a, 2), f'snowflake{i}')
#     sprites.make_group('newsnowflakeextra', (a, 2), f'snowflakeextra{i}', sprites_y=2)

#abyssinian
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('abyssinian', (a, 0), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 0), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('abyssinian', (a, 1), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 1), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('abyssinian', (a, 2), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 2), f'abyssinianextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newabyssinian', (a, 0), f'abyssinian{i}')
    sprites.make_group('newabyssinianextra', (a, 0), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newabyssinian', (a, 1), f'abyssinian{i}')
    sprites.make_group('newabyssinianextra', (a, 1), f'abyssinianextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newabyssinian', (a, 2), f'abyssinian{i}')
#     sprites.make_group('newabyssinianextra', (a, 2), f'abyssinianextra{i}', sprites_y=2)

#clouded
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('clouded', (a, 0), f'clouded{i}')
    sprites.make_group('cloudedextra', (a, 0), f'cloudedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('clouded', (a, 1), f'clouded{i}')
    sprites.make_group('cloudedextra', (a, 1), f'cloudedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('clouded', (a, 2), f'clouded{i}')
    sprites.make_group('cloudedextra', (a, 2), f'cloudedextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newclouded', (a, 0), f'clouded{i}')
    sprites.make_group('newcloudedextra', (a, 0), f'cloudedextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newclouded', (a, 1), f'clouded{i}')
    sprites.make_group('newcloudedextra', (a, 1), f'cloudedextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newclouded', (a, 2), f'clouded{i}')
#     sprites.make_group('newcloudedextra', (a, 2), f'cloudedextra{i}', sprites_y=2)

#merle
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('merle', (a, 0), f'merle{i}')
    sprites.make_group('merleextra', (a, 0), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('merle', (a, 1), f'merle{i}')
    sprites.make_group('merleextra', (a, 1), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('merle', (a, 2), f'merle{i}')
    sprites.make_group('merleextra', (a, 2), f'merleextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newmerle', (a, 0), f'merle{i}')
    sprites.make_group('newmerleextra', (a, 0), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newmerle', (a, 1), f'merle{i}')
    sprites.make_group('newmerleextra', (a, 1), f'merleextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newmerle', (a, 2), f'merle{i}')
#     sprites.make_group('newmerleextra', (a, 2), f'merleextra{i}', sprites_y=2)

#ghosttabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('ghosttabby', (a, 0), f'ghosttabby{i}')
    sprites.make_group('ghosttabbyextra', (a, 0), f'ghosttabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('ghosttabby', (a, 1), f'ghosttabby{i}')
    sprites.make_group('ghosttabbyextra', (a, 1), f'ghosttabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('ghosttabby', (a, 2), f'ghosttabby{i}')
    sprites.make_group('ghosttabbyextra', (a, 2), f'ghosttabbyextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newghosttabby', (a, 0), f'ghosttabby{i}')
    sprites.make_group('newghosttabbyextra', (a, 0), f'ghosttabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newghosttabby', (a, 1), f'ghosttabby{i}')
    sprites.make_group('newghosttabbyextra', (a, 1), f'ghosttabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newghosttabby', (a, 2), f'ghosttabby{i}')
#     sprites.make_group('newghosttabbyextra', (a, 2), f'ghosttabbyextra{i}', sprites_y=2)
# 
#pinstripetabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('pinstripetabby', (a, 0), f'pinstripetabby{i}')
    sprites.make_group('pinstripetabbyextra', (a, 0), f'pinstripetabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('pinstripetabby', (a, 1), f'pinstripetabby{i}')
    sprites.make_group('pinstripetabbyextra', (a, 1), f'pinstripetabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('pinstripetabby', (a, 2), f'pinstripetabby{i}')
    sprites.make_group('pinstripetabbyextra', (a, 2), f'pinstripetabbyextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newpinstripe', (a, 0), f'pinstripetabby{i}')
    sprites.make_group('newpinstripeextra', (a, 0), f'pinstripetabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newpinstripe', (a, 1), f'pinstripetabby{i}')
    sprites.make_group('newpinstripeextra', (a, 1), f'pinstripetabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newpinstripe', (a, 2), f'pinstripetabby{i}')
#     sprites.make_group('newpinstripeextra', (a, 2), f'pinstripetabbyextra{i}', sprites_y=2)

#doberman
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('doberman', (a, 0), f'doberman{i}')
    sprites.make_group('dobermanextra', (a, 0), f'dobermanextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('doberman', (a, 1), f'doberman{i}')
    sprites.make_group('dobermanextra', (a, 1), f'dobermanextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('doberman', (a, 2), f'doberman{i}')
    sprites.make_group('dobermanextra', (a, 2), f'dobermanextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newdoberman', (a, 0), f'doberman{i}')
    sprites.make_group('newdobermanextra', (a, 0), f'dobermanextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newdoberman', (a, 1), f'doberman{i}')
    sprites.make_group('newdobermanextra', (a, 1), f'dobermanextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newdoberman', (a, 2), f'doberman{i}')
#     sprites.make_group('newdobermanextra', (a, 2), f'dobermanextra{i}', sprites_y=2)

#oceloid
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('oceloid', (a, 0), f'oceloid{i}')
    sprites.make_group('oceloidextra', (a, 0), f'oceloidextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('oceloid', (a, 1), f'oceloid{i}')
    sprites.make_group('oceloidextra', (a, 1), f'oceloidextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('oceloid', (a, 2), f'oceloid{i}')
    sprites.make_group('oceloidextra', (a, 2), f'oceloidextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newoceloid', (a, 0), f'oceloid{i}')
    sprites.make_group('newoceloidextra', (a, 0), f'oceloidextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newoceloid', (a, 1), f'oceloid{i}')
    sprites.make_group('newoceloidextra', (a, 1), f'oceloidextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newoceloid', (a, 2), f'oceloid{i}')
#     sprites.make_group('newoceloidextra', (a, 2), f'oceloidextra{i}', sprites_y=2)

#monarch
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('monarch', (a, 0), f'monarch{i}')
    sprites.make_group('monarchextra', (a, 0), f'monarchextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('monarch', (a, 1), f'monarch{i}')
    sprites.make_group('monarchextra', (a, 1), f'monarchextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('monarch', (a, 2), f'monarch{i}')
    sprites.make_group('monarchextra', (a, 2), f'monarchextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newmonarch', (a, 0), f'monarch{i}')
    sprites.make_group('newmonarchextra', (a, 0), f'monarchextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newmonarch', (a, 1), f'monarch{i}')
    sprites.make_group('newmonarchextra', (a, 1), f'monarchextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newmonarch', (a, 2), f'monarch{i}')
#     sprites.make_group('newmonarchextra', (a, 2), f'monarchextra{i}', sprites_y=2)
    
#sokoke
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('sokoke', (a, 0), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('sokoke', (a, 1), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 1), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('sokoke', (a, 2), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 2), f'sokokeextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('newsokoke', (a, 0), f'sokoke{i}')
    sprites.make_group('newsokokeextra', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('newsokoke', (a, 1), f'sokoke{i}')
    sprites.make_group('newsokokeextra', (a, 1), f'sokokeextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('newsokoke', (a, 2), f'sokoke{i}')
#     sprites.make_group('newsokokeextra', (a, 2), f'sokokeextra{i}', sprites_y=2)
    
#classictabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('classictabby', (a, 0), f'classictabby{i}')
    sprites.make_group('classictabbyextra', (a, 0), f'classictabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('classictabby', (a, 1), f'classictabby{i}')
    sprites.make_group('classictabbyextra', (a, 1), f'classictabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('classictabby', (a, 2), f'classictabby{i}')
    sprites.make_group('classictabbyextra', (a, 2), f'classictabbyextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('classictabbynew', (a, 0), f'classictabby{i}')
    sprites.make_group('classictabbyextranew', (a, 0), f'classictabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('classictabbynew', (a, 1), f'classictabby{i}')
    sprites.make_group('classictabbyextranew', (a, 1), f'classictabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('classictabbynew', (a, 2), f'classictabby{i}')
#     sprites.make_group('classictabbyextranew', (a, 2), f'classictabbyextra{i}', sprites_y=2)

#lykoi
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('lykoi', (a, 0), f'lykoi{i}')
    sprites.make_group('lykoiextra', (a, 0), f'lykoiextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('lykoi', (a, 1), f'lykoi{i}')
    sprites.make_group('lykoiextra', (a, 1), f'lykoiextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('lykoi', (a, 2), f'lykoi{i}')
    sprites.make_group('lykoiextra', (a, 2), f'lykoiextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('lykoinew', (a, 0), f'lykoi{i}')
    sprites.make_group('lykoiextranew', (a, 0), f'lykoiextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('lykoinew', (a, 1), f'lykoi{i}')
    sprites.make_group('lykoiextranew', (a, 1), f'lykoiextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('lykoinew', (a, 2), f'lykoi{i}')
#     sprites.make_group('lykoiextranew', (a, 2), f'lykoiextra{i}', sprites_y=2)

#mackereltabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('mackereltabby', (a, 0), f'mackereltabby{i}')
    sprites.make_group('mackereltabbyextra', (a, 0), f'mackereltabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('mackereltabby', (a, 1), f'mackereltabby{i}')
    sprites.make_group('mackereltabbyextra', (a, 1), f'mackereltabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('mackereltabby', (a, 2), f'mackereltabby{i}')
    sprites.make_group('mackereltabbyextra', (a, 2), f'mackereltabbyextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('mackereltabbynew', (a, 0), f'mackereltabby{i}')
    sprites.make_group('mackereltabbyextranew', (a, 0), f'mackereltabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('mackereltabbynew', (a, 1), f'mackereltabby{i}')
    sprites.make_group('mackereltabbyextranew', (a, 1), f'mackereltabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('mackereltabbynew', (a, 2), f'mackereltabby{i}')
#     sprites.make_group('mackereltabbyextranew', (a, 2), f'mackereltabbyextra{i}', sprites_y=2)
    
#wavetabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('wavetabby', (a, 0), f'wavetabby{i}')
    sprites.make_group('wavetabbyextra', (a, 0), f'wavetabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('wavetabby', (a, 1), f'wavetabby{i}')
    sprites.make_group('wavetabbyextra', (a, 1), f'wavetabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('wavetabby', (a, 2), f'wavetabby{i}')
    sprites.make_group('wavetabbyextra', (a, 2), f'wavetabbyextra{i}', sprites_y=2)
    
for a, i in enumerate(['IVORY', 'PUMPKIN', 'APRICOT', 'COPPER', 'RUST', 'MIDNIGHT']):
    sprites.make_group('wavetabbynew', (a, 0), f'wavetabby{i}')
    sprites.make_group('wavetabbyextranew', (a, 0), f'wavetabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SAND', 'CARAMEL', 'TOFFEE', 'FAWN']):
    sprites.make_group('wavetabbynew', (a, 1), f'wavetabby{i}')
    sprites.make_group('wavetabbyextranew', (a, 1), f'wavetabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['LEUCISTIC', 'MELRED', 'MELBLUE']):
#     sprites.make_group('wavetabbynew', (a, 2), f'wavetabby{i}')
#     sprites.make_group('wavetabbyextranew', (a, 2), f'wavetabbyextra{i}', sprites_y=2)

# new torties
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 0), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 0), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 1), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 1), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 2), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 2), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 3), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 3), f'tortiesolidextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecolourssolid', (a, 4), f'tortiesolid{i}')
#     sprites.make_group('tortiesextrasolid', (a, 4), f'tortiesolidextra{i}', sprites_y=2)
#tabby
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 0), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 0), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 1), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 1), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 2), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 2), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 3), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 3), f'tortietabbyextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecolourstabby', (a, 4), f'tortietabby{i}')
#     sprites.make_group('tortiesextratabby', (a, 4), f'tortietabbyextra{i}', sprites_y=2)
#bengal
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 0), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 0), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 1), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 1), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 2), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 2), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 3), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 3), f'tortiebengalextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecoloursbengal', (a, 4), f'tortiebengal{i}')
#     sprites.make_group('tortiesextrabengal', (a, 4), f'tortiebengalextra{i}', sprites_y=2)
#marbled
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 0), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 0), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 1), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 1), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 2), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 2), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 3), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 3), f'tortiemarbledextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecoloursmarbled', (a, 4), f'tortiemarbled{i}')
#     sprites.make_group('tortiesextramarbled', (a, 4), f'tortiemarbledextra{i}', sprites_y=2)
#ticked
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 0), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 0), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 1), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 1), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 2), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 2), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 3), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 3), f'tortietickedextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecoloursticked', (a, 4), f'tortieticked{i}')
#     sprites.make_group('tortiesextraticked', (a, 4), f'tortietickedextra{i}', sprites_y=2)
#smoke
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 0), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 0), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 1), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 1), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 2), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 2), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 3), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 3), f'tortiesmokeextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecolourssmoke', (a, 4), f'tortiesmoke{i}')
#     sprites.make_group('tortiesextrasmoke', (a, 4), f'tortiesmokeextra{i}', sprites_y=2)
#rosette
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 0), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 0), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 1), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 1), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 2), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 2), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 3), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 3), f'tortierosetteextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#     sprites.make_group('tortiecoloursrosette', (a, 4), f'tortierosette{i}')
#     sprites.make_group('tortiesextrarosette', (a, 4), f'tortierosetteextra{i}', sprites_y=2)
#speckled
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 0), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 0), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 1), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 1), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 2), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 2), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 3), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 3), f'tortiespeckledextra{i}', sprites_y=2)
# for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
#    sprites.make_group('tortiecoloursspeckled', (a, 4), f'tortiespeckled{i}')
#    sprites.make_group('tortiesextraspeckled', (a, 4), f'tortiespeckledextra{i}', sprites_y=2)
#snowflake
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiesnowflake', (a, 0), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 0), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiesnowflake', (a, 1), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 1), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiesnowflake', (a, 2), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 2), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiesnowflake', (a, 3), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 3), f'tortiesnowflakeextra{i}', sprites_y=2)
#clouded
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieclouded', (a, 0), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 0), f'tortiecloudedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieclouded', (a, 1), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 1), f'tortiecloudedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieclouded', (a, 2), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 2), f'tortiecloudedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieclouded', (a, 3), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 3), f'tortiecloudedextra{i}', sprites_y=2)
#merle
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiemerle', (a, 0), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 0), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiemerle', (a, 1), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 1), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiemerle', (a, 2), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 2), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiemerle', (a, 3), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 3), f'tortiemerleextra{i}', sprites_y=2)
#ghosttabby
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieghost', (a, 0), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 0), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieghost', (a, 1), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 1), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieghost', (a, 2), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 2), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieghost', (a, 3), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 3), f'tortieghostextra{i}', sprites_y=2)
#pinstripetabby
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiepinstripe', (a, 0), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 0), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiepinstripe', (a, 1), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 1), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiepinstripe', (a, 2), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 2), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiepinstripe', (a, 3), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 3), f'tortiepinstripeextra{i}', sprites_y=2)
#abyssinian
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieabyssinian', (a, 0), f'tortieabyssinian{i}')
    sprites.make_group('tortieabyssinianextra', (a, 0), f'tortieabyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieabyssinian', (a, 1), f'tortieabyssinian{i}')
    sprites.make_group('tortieabyssinianextra', (a, 1), f'tortieabyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieabyssinian', (a, 2), f'tortieabyssinian{i}')
    sprites.make_group('tortieabyssinianextra', (a, 2), f'tortieabyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieabyssinian', (a, 3), f'tortieabyssinian{i}')
    sprites.make_group('tortieabyssinianextra', (a, 3), f'tortieabyssinianextra{i}', sprites_y=2)
#oceloid
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieoceloid', (a, 0), f'tortieoceloid{i}')
    sprites.make_group('tortieoceloidextra', (a, 0), f'tortieoceloidextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieoceloid', (a, 1), f'tortieoceloid{i}')
    sprites.make_group('tortieoceloidextra', (a, 1), f'tortieoceloidextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieoceloid', (a, 2), f'tortieoceloid{i}')
    sprites.make_group('tortieoceloidextra', (a, 2), f'tortieoceloidextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieoceloid', (a, 3), f'tortieoceloid{i}')
    sprites.make_group('tortieoceloidextra', (a, 3), f'tortieoceloidextra{i}', sprites_y=2)
#monarch
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiemonarch', (a, 0), f'tortiemonarch{i}')
    sprites.make_group('tortiemonarchextra', (a, 0), f'tortiemonarchextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiemonarch', (a, 1), f'tortiemonarch{i}')
    sprites.make_group('tortiemonarchextra', (a, 1), f'tortiemonarchextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiemonarch', (a, 2), f'tortiemonarch{i}')
    sprites.make_group('tortiemonarchextra', (a, 2), f'tortiemonarchextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiemonarch', (a, 3), f'tortiemonarch{i}')
    sprites.make_group('tortiemonarchextra', (a, 3), f'tortiemonarchextra{i}', sprites_y=2)
#sokoke
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiesokoke', (a, 0), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 0), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiesokoke', (a, 1), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 1), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiesokoke', (a, 2), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 2), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiesokoke', (a, 3), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 3), f'tortiesokokeextra{i}', sprites_y=2)

# SKINS
sprites.make_group('skin', (0, 0), 'skinBLACK')
sprites.make_group('skin', (1, 0), 'skinRED')
sprites.make_group('skin', (2, 0), 'skinPINK')
sprites.make_group('skin', (3, 0), 'skinDARKBROWN')
sprites.make_group('skin', (4, 0), 'skinBROWN')
sprites.make_group('skin', (5, 0), 'skinLIGHTBROWN')
sprites.make_group('skin', (0, 1), 'skinDARK')
sprites.make_group('skin', (1, 1), 'skinDARKGREY')
sprites.make_group('skin', (2, 1), 'skinGREY')
sprites.make_group('skin', (3, 1), 'skinDARKSALMON')
sprites.make_group('skin', (4, 1), 'skinSALMON')
sprites.make_group('skin', (5, 1), 'skinPEACH')
sprites.make_group('skin', (0, 2), 'skinDARKMARBLED')
sprites.make_group('skin', (1, 2), 'skinMARBLED')
sprites.make_group('skin', (2, 2), 'skinLIGHTMARBLED')
sprites.make_group('skin', (3, 2), 'skinDARKBLUE')
sprites.make_group('skin', (4, 2), 'skinBLUE')
sprites.make_group('skin', (5, 2), 'skinLIGHTBLUE')
sprites.make_group('skinparalyzed', (0, 0),
                   'skinparalyzedPINK',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (1, 0),
                   'skinparalyzedRED',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (2, 0),
                   'skinparalyzedBLACK',
                   sprites_x=1,
                   sprites_y=1)

sprites.make_group('skinextra', (0, 0), 'skinextraBLACK', sprites_y=2)
sprites.make_group('skinextra', (1, 0), 'skinextraRED', sprites_y=2)
sprites.make_group('skinextra', (2, 0), 'skinextraPINK', sprites_y=2)
sprites.make_group('skinextra', (3, 0), 'skinextraDARKBROWN', sprites_y=2)
sprites.make_group('skinextra', (4, 0), 'skinextraBROWN', sprites_y=2)
sprites.make_group('skinextra', (5, 0), 'skinextraLIGHTBROWN', sprites_y=2)
sprites.make_group('skinextra', (0, 1), 'skinextraDARK', sprites_y=2)
sprites.make_group('skinextra', (1, 1), 'skinextraDARKGREY', sprites_y=2)
sprites.make_group('skinextra', (2, 1), 'skinextraGREY', sprites_y=2)
sprites.make_group('skinextra', (3, 1), 'skinextraDARKSALMON', sprites_y=2)
sprites.make_group('skinextra', (4, 1), 'skinextraSALMON', sprites_y=2)
sprites.make_group('skinextra', (5, 1), 'skinextraPEACH', sprites_y=2)
sprites.make_group('skinextra', (0, 2), 'skinextraDARKMARBLED', sprites_y=2)
sprites.make_group('skinextra', (1, 2), 'skinextraMARBLED', sprites_y=2)
sprites.make_group('skinextra', (2, 2), 'skinextraLIGHTMARBLED', sprites_y=2)
sprites.make_group('skinextra', (3, 2), 'skinextraDARKBLUE', sprites_y=2)
sprites.make_group('skinextra', (4, 2), 'skinextraBLUE', sprites_y=2)
sprites.make_group('skinextra', (5, 2), 'skinextraLIGHTBLUE', sprites_y=2)

tiles.make_group('dithered', (0, 0), 'terrain')
tiles.make_group('dithered', (1, 0), 'terraintwo')

sprites.load_scars()
