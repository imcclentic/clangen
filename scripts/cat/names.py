import random
import os


class Name():
    special_suffixes = {
        "kitten": "kit",
        "apprentice": "paw",
        "medicine cat apprentice": "paw",
        "leader": "star"
    }
    normal_suffixes = [  # common suffixes
        "fur", "fur", "fur", "fur", #"fur", "fur", "fur", "fur", "fur", "fur", 'fur', 'fur', 'fur',
        'pelt', "pelt", "pelt", "pelt", #"pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "tail", "tail", "tail",# "tail", "tail", "tail", "tail", "tail",
        "claw", "claw", "claw", #"claw", "claw", "claw", "claw",
        "foot","foot", #"foot","foot", "foot",
        "whisker", "whisker", "whisker", #"whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", #"heart", "heart", "heart", "heart", "heart", 'heart',

        # regular suffixes
        "acorn", "ash", "aster", "back", "beam", "bee", "belly", "berry", "bite", "bird", "blaze", "blink",
        "blossom", "bloom", "blotch", "bounce", "branch", "breeze", "briar", "bright", "brook", "burr", "bush",
        "call", "cloud", "clover", "coral", "creek", "cry", "dapple", "daisy", "dawn", "drift", "drop",
        "dusk", "dust", "ear", "ears", "eye", "eyes", "face", "fall", "fang", "feather", "fern", "fin", "fire",
        "fish", "flame", "flight", "flood", "flower", "frost", "gaze", "goose", "gorse", "grass", "hail", "hare", 
        "hawk", "haze", "heather", "holly", "hollow", "ivy", "jaw", "jay", "jump",
        "lake", "larch", "leaf", "leap", "leg", "light", "lilac", "lily", "lotus", "mask", "mist", "moth",
        "moon", "mouse", "needle", "nettle", "night", "noise", "nose", "nut", "pad", "path", "patch",
        "petal", "pond", "pool", "poppy", "pounce", "puddle", "rapid", "rose", "rump", "run", "runner",
        "scar", "seed", "shade", "shadow", "shell", "shine", "sight", "skip", "sky", "slip", "snow", "song", 
        "spark", "speck", "speckle", "spirit", "splash", "spot", "spots", "spring", "stalk", "stem", "step",
        "stone", "storm", "streak", "stream", "strike", "stripe", "sun", "swipe", "swoop",
        "tail", "tree", "throat", "tuft", "watcher", "water", "whisper", "willow", "wind", "wing", "wish",
        
        #New - Test
        'acorn', 'adder', 'alder', 'almond',
        'amber', 'apple', 'apricot',
        'ash','aspen', 'aster','badger', 'bark',
        'bat', 'beam',
        'bear', 'beaver', 'bee', 'berry', 'birch',
        'bird', 'bite', 'blaze', 'blight',
        'blink', 'bliss', 'bloom', 'blossom', 'blotch',
        'boulder', 'bounce', 'bracken', 'bramble',
        'branch', 'brave', 'breeze', 'breeze', 'briar', 'bright', 'brindle',
        'bristle', 'broken', 'brook', 'bubble', 'buck',
        'burn','burr', 'bush',
        'cheetah', 'cherry',
        'cinder', 'cinnamon',
        'cloud', 'clover', 'coast', 'cobra',
        'condor', 'conifer','cotton', 'cougar',
        'coyote','crane', 'creek',
        'crouch', 'crow',
        'cypress', 'dahlia', 'daisy', 'damp', 'dapple',
        'dark', 'dawn', 'day', 'deer', 'dew', 'doe', 'dog',
        'dove', 'drake', 'drift', 'drizzle',
        'duck','dusk', 'dust', 'eagle', 'echo',
        'elk', 'elm', 'ember',
        'falcon','fallow', 'fawn', 'feather',
        'fern', 'ferret', 'fierce', 'fin', 'finch', 'fir',
        'flame', 'flash', 'fleck', 'fleet',
        'flight', 'flint', 'flood', 'flower',
        'forest', 'fox', 'freckle', 'flare'
        'freeze', 'fringe', 'frog', 'frond', 'frost',
        'gem',  'gleam', 'glow',
        'grass', 'gust',
        'hail', 'hare', 'harvest', 'hawk', 'haze',
        'heather','hedge', 'heron',
        'hill', 'hoarse', 'hollow', 'holly', 'hoot','hope', 'hornet',
        'hound', 'ice', 'iris', 'ivy', 'jasper', 'jay', 'jet',
        'juniper', 'lake', 'larch', 'lark',
        'laurel', 'lavender', 'leaf', 'leap', 'leopard', 'light',
        'lightning', 'lilac', 'lily', 'little', 'lizard', 'locust',
        'log', 'lost', 'lotus', 'lynx',
        'mantis', 'maple','marsh', 'marten', 'meadow',
        'midge','mink', 'minnow', 'mint', 'mist',
        'moon', 'moor',
        'moss','moth',
        'mouse','nectar',
        'needle', 'nettle','night', 'oak',
        'otter', 'owl', 'panther',
        'patch', 'peak', 'pear',
        'pebble', 'pepper', 'perch', 'petal',
        'pond', 'pool', 'poppy', 'posy',
        'puddle', 'python', 'quail',
        'quill', 'rabbit', 'raccoon','rain',
        'rattle', 'raven', 'reed', 'ridge', 'rift',
        'ripple', 'river','robin', 'rock', 'rook', 'root', 'rose',
        'rosy', 'rowan', 'rubble', 'running', 'rush', 'rust', 'rye',
        'sage', 'scar', 'scorch', 'sea','seed', 'shade',
        'shard', 'shell', 'shimmer','shrew', 'shy', 'silk',
        'skip', 'sky', 'slate', 'sleek', 'sleet', 'slight',
        'slope', 'smoke', 'snake',
        'song', 'soot', 'sorrel', 'spark', 'sparrow',
        'speckle', 'spider', 'spike', 'spire', 'splash', 'spot', 'spring',
        'spruce', 'squirrel', 'stag', 'starling', 'steam', 'stoat', 'stone',
        'storm', 'stream', 'strike', 'stump',
        'swan','swift','talon', 'thistle', 'thorn',
        'thrift', 'tiger', 'timber',
        'tuft', 'tulip', 'turtle', 'twig', 'vine', 'violet', 'vixen',
        'vole', 'warm', 'wasp', 'weasel', 'web','wheat', 'whirl',
        'whisker', 'wild', 'willow', 'wind', 'wisteria', 'wolf', 'wood', 'widow',
        'wren', 'yarrow', 'yew'

    ]

    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Tabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Marbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Speckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Bengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'Tortie': ['dapple', 'speckle', 'spot', 'dapple'],
        'Rosette': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch'],
        'Smoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'Ticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Snowflake': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow'],
        'Abyssinian': ['fade', 'dusk', 'dawn', 'smoke'],
        'Clouded': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'cloud'],
        'Merle': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'GhostTabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fade'],
        'PinstripeTabby': ['breeze', 'ripple', 'river', 'brook', 'creek', 'slash', 'streak', 'stream', 'stripe',
                  'wind'],
        'Doberman': ['hound', 'cry', 'vixen'],
        'Oceloid': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'Monarch': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'cloud'],
        'Sokoke': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'cloud'],
        'Classictabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Lykoi': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Mackereltabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Wavetabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortietabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiebengal': ['dapple', 'speckle', 'spots', 'speck', 'fern', 'freckle'],
        'tortiemarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortieticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'tortiesmoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'tortierosette': ['dapple', 'speckle', 'spots', 'dapple', 'fern', 'freckle'],
        'tortiespeckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortiesnowflake': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'splash'],
        'tortieclouded': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'splash'],
        'tortiemerle': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortieghost': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'splash', 'ash', 'fleck'],
        'tortiepinstripe': ['dapple', 'patch', 'mask', 'fire', 'flare', 'flame', 'shade', 'shadow', 'spark', 'splash',
                        'spot', 'spots', 'streak', 'sun', 'wisp', 'breeze', 'ripple', 'river', 'brook', 'creek',
                        'slash', 'streak', 'stream', 'stripe',
                        'wind'],
        'tortiebyssinian': ['fade', 'dusk', 'dawn', 'smoke'],
        'tortieoceloid': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'tortiemonarch': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'cloud'],
        'tortiesokoke': ['spots', 'pelt', 'speckle', 'freckle', 'dapple', 'snow', 'cloud']

    }

    normal_prefixes = [
        'Acacia', 'Acorn', 'Adder', 'Alder', 'Almond',
        'Amber', 'Ant', 'Antler', 'Apple', 'Apricot', 'Arc', 'Arch', 'Arctic',
        'Ash', 'Ashen', 'Aspen', 'Aster', 'Aster', 'Autumn', 'Badger', 'Bark',
        'Barley', 'Barley', 'Basil', 'Bat', 'Bay', 'Bayou', 'Beam',
        'Bear', 'Beaver', 'Bee', 'Beetle', 'Berry', 'Birch',
        'Bird', 'Bite', 'Bitter', 'Blaze', 'Bleak', 'Blight',
        'Blink', 'Bliss', 'Bloom', 'Blossom', 'Blotch', 'Bluff', 'Bog',
        'Boulder', 'Bounce', 'Bracken', 'Bramble',
        'Branch', 'Brave', 'Breeze', 'Breeze', 'Briar', 'Bright', 'Brindle',
        'Bristle', 'Broken', 'Brook', 'Brush', 'Bubble', 'Buck',
        'Bumble', 'Burn', 'Burnt', 'Burr', 'Bush', 'Buzzard',
        'Carp', 'Cedar', 'Cedar', 'Cheetah', 'Cherry',
        'Chestnut', 'Chive', 'Cicada', 'Cinder', 'Cinnamon', 'Claw', 'Clay',
        'Cliff', 'Cloud', 'Clover', 'Coast', 'Cobra', 'Cold',
        'Condor', 'Conifer', 'Copper', 'Cotton', 'Cougar',
        'Coyote', 'Crag', 'Crane', 'Creek', 'Crested',
        'Cricket', 'Crooked', 'Crouch', 'Crow', 'Curl',
        'Curly', 'Cypress', 'Dahlia', 'Daisy', 'Damp', 'Dapple', 'Dappled',
        'Dark', 'Dawn', 'Day', 'Dead', 'Deer', 'Dew', 'Doe', 'Dog',
        'Dove', 'Downy', 'Drake', 'Drift', 'Drizzle', 'Drought', 'Dry',
        'Duck', 'Dull', 'Dune', 'Dusk', 'Dust', 'Eagle', 'Echo', 'Eel',
        'Elk', 'Elm', 'Ember','Faded', 'Faded', 'Fading',
        'Falcon', 'Fallen', 'Fallow', 'Fawn', 'Feather',
        'Fern', 'Ferret', 'Fidget', 'Fierce', 'Fin', 'Finch', 'Fir',
        'Flail', 'Flame', 'Flash', 'Fleck', 'Fleet', 'Flicker',
        'Flight', 'Flint', 'Flip', 'Flood', 'Flood', 'Flower', 'Flower',
        'Flurry', 'Flutter', 'Fly', 'Foam', 'Forest', 'Fox', 'Freckle',
        'Freeze', 'Fringe', 'Frog', 'Frond', 'Frost', 'Frozen',
        'Fuzzy', 'Gander', 'Gannet', 'Gem', 'Giant','Gleam', 'Glow',
        'Goose', 'Gorge', 'Gorse', 'Grass', 'Gravel', 'Grouse', 'Gull', 'Gust',
        'Hail', 'Half', 'Hare', 'Harvest', 'Hatch', 'Hawk', 'Hay', 'Haze',
        'Heather', 'Heavy', 'Hedge', 'Heron', 'Hickory',
        'Hill', 'Hoarse', 'Hollow', 'Holly', 'Hoot', 'Hop', 'Hope', 'Hornet',
        'Hound', 'Ice', 'Icy', 'Iris', 'Ivy', 'Jagged', 'Jasper', 'Jay', 'Jet',
        'Jump', 'Juniper', 'Kestrel', 'Lake', 'Larch', 'Lark',
        'Laurel', 'Lavender', 'Leaf', 'Leap', 'Leopard', 'Light',
        'Lightning', 'Lilac', 'Lily', 'Little', 'Lizard', 'Locust',
        'Log', 'Long', 'Lost', 'Lotus', 'Loud', 'Low', 'Lynx',
        'Mallow', 'Mantis', 'Maple', 'Marigold', 'Marsh', 'Marten', 'Meadow',
        'Mellow', 'Merry', 'Midge', 'Milk', 'Mink', 'Minnow', 'Mint', 'Mist',
        'Mistle', 'Misty', 'Mole', 'Moon', 'Moor',
        'Morning', 'Moss', 'Mossy', 'Moth',
        'Mouse','Mumble', 'Murk', 'Nacre', 'Narrow', 'Nectar',
        'Needle', 'Nettle', 'Newt', 'Night', 'Nut', 'Oak', 'Oat', 'Odd', 'One',
        'Orange', 'Otter', 'Owl', 'Pale', 'Panther',
        'Parsley', 'Partridge', 'Patch', 'Peak', 'Pear',
        'Pebble', 'Pepper', 'Perch', 'Petal', 'Pheasant', 'Pigeon', 'Pike',
        'Pine', 'Piper', 'Plover', 'Pod', 'Pond', 'Pool', 'Poppy', 'Posy',
        'Pounce', 'Prance', 'Prickle', 'Prim', 'Puddle', 'Python', 'Quail',
        'Quick', 'Quiet', 'Quill', 'Rabbit', 'Raccoon', 'Ragged', 'Rain',
        'Rat', 'Rattle', 'Raven', 'Reed', 'Ridge', 'Rift',
        'Ripple', 'River', 'Roach', 'Robin', 'Rock', 'Rook', 'Root', 'Rose',
        'Rosy', 'Rot', 'Rowan', 'Rubble', 'Running', 'Rush', 'Rust', 'Rye',
        'Sage', 'Sandy', 'Scar', 'Scorch', 'Sea','Seed', 'Shade',
        'Shard', 'Sharp', 'Shell', 'Shimmer', 'Short', 'Shrew', 'Shy', 'Silk',
        'Silt', 'Skip', 'Sky', 'Slate', 'Sleek', 'Sleet', 'Slight',
        'Slope', 'Small', 'Smoke', 'Smoky', 'Snail', 'Snake', 'Snap', 'Sneeze',
        'Snip', 'Soft', 'Song', 'Soot', 'Sorrel', 'Spark', 'Sparrow',
        'Speckle', 'Spider', 'Spike', 'Spire', 'Splash', 'Spotted', 'Spring',
        'Spruce', 'Squirrel', 'Stag', 'Starling', 'Steam', 'Stoat', 'Stone',
        'Stork', 'Storm', 'Stream', 'Strike', 'Stump', 'Swallow',
        'Swan', 'Sweet', 'Swift', 'Tall', 'Talon', 'Thistle', 'Thorn',
        'Thrift', 'Thyme', 'Tiger', 'Timber', 'Torn',
        'Tuft', 'Tulip', 'Tumble', 'Turtle', 'Twig', 'Vine', 'Violet', 'Vixen',
        'Vole', 'Warm', 'Wasp', 'Weasel', 'Web', 'Wet', 'Wheat', 'Whirl',
        'Whisker', 'Wild', 'Willow', 'Wind', 'Wisteria', 'Wolf', 'Wood', 'Widow',
        'Wren', 'Yarrow', 'Yew'
    ]

    colour_prefixes = {
        'WHITE': [
            'Alabaster', 'Avalanche', 'Blizzard', 'Bone', 'Cherry', 'Cloud', 'Cobweb', 'Cotton',
            'Crane', 'Down', 'Fade', 'Faded', 'Flash', 'Flurry', 'Frigid', 'Frost', 'Frozen',
            'Glacier',
            'Gleam', 'Gull', 'Hail', 'Hemlock', 'Heron', 'Ice', 'Icicle', 'Ivory', 'Lamb', 'Light',
            'Lightning', 'Milk', 'Mushroom', 'Oleander', 'Pale', 'Seafoam', 'Sheep',
            'Shimmer',
            'Shine', 'Shrike', 'Silk', 'Snow', 'Snowdrop', 'Swan', 'Tundra', 'White',
            'Zephyr'
        ],
        'PALEGREY': [
            'Ash', 'Ashen', 'Blizzard', 'Bluebell', 'Blueberry', 'Blue', 'Boulder', 'Cinder',
                     'Cloud', 'Cobweb', 'Creek', 'Damp', 'Dew', 'Dove', 'Down', 'Drizzle', 'Fade',
                     'Faded', 'Fjord', 'Flood', 'Fog', 'Frigid', 'Frost', 'Frozen', 'Gale',
                     'Geyser', 'Glacier', 'Gravel', 'Grey', 'Hail', 'Haze', 'Hurricane', 'Lagoon',
                     'Minnow',
                     'Mist', 'Misty', 'Mistral', 'Moon', 'Pale', 'Pebble', 'Pigeon', 'Puddle', 'Rain',
                     'Ripple',
                     'River', 'Rock', 'Shallow', 'Shimmer', 'Shine', 'Shrike', 'Silver', 'Sky', 'Sleet',
                     'Smoke', 'Stone', 'Tempest', 'Tornado', 'Zephyr'
        ],
        'SILVER': [
            'Ash', 'Ashen', 'Azure', 'Bay', 'Blizzard', 'Bluebell', 'Blueberry', 'Blue',
            'Boulder', 'Brook', 'Cascade', 'Cloud', 'Creek', 'Cyclone', 'Current',
            'Dew', 'Dove', 'Down', 'Drizzle', 'Estuary', 'Fade', 'Faded', 'Fjord',
            'Flood', 'Fog', 'Frigid', 'Frost', 'Frozen', 'Gale', 'Geyser', 'Glacier', 'Grey', 'Hail',
            'Haze', 'Hurricane', 'Jay', 'Lagoon', 'Lake', 'Mist', 'Misty', 'Mistral', 'Moon', 'Ocean',
            'Pond', 'Pool', 'Puddle', 'Rain', 'Ripple', 'River', 'Rock', 'Sea', 'Seafoam', 'Shallow',
            'Shimmer', 'Shine', 'Shore', 'Shrike', 'Silver', 'Sky', 'Sleet', 'Splash', 'Stream', 'Tempest',
            'Tide', 'Torrent', 'Water', 'Ash', 'Ashen', 'Bay', 'Blizzard', 'Bluebell',
            'Blue', 'Brook', 'Bubble','Cascade',
            'Cloud', 'Creek', 'Current', 'Cyclone', 'Delta', 'Dew', 'Echo',
            'Drizzle', 'Fjord', 'Flood', 'Flurry', 'Frigid', 'Frost',
            'Frozen', 'Gale', 'Gleam', 'Glacier', 'Grey', 'Gust', 'Hail', 'Ice', 'Icicle',
            'Hurricane', 'Jay', 'Lake', 'Lagoon', 'Light', 'Minnow', 'Ocean', 'Pale',
             'Pebble', 'Pigeon', 'Puddle', 'Pond', 'Pool', 'Rain', 'River', 'Ripple', 'Sea',
             'Seafoam', 'Shrike', 'Sleet', 'Silver', 'Sky', 'Snowdrop', 'Splash', 'Stream',
             'Tempest', 'Tide', 'Torrent', 'Tornado', 'Tuna', 'Water', 'Web',
             'Wet', 'Wave', 'Zephyr'
        ],
        'GREY': [
            'Ash', 'Ashen', 'Boulder', 'Cinder', 'Damp', 'Dove', 'Drizzle', 'Flint',
                 'Flood', 'Fog', 'Frigid', 'Gale', 'Granite', 'Gravel', 'Grey', 'Haze', 'Hurricane', 'Minnow',
                 'Mist', 'Misty', 'Mistral', 'Moon', 'Mouse', 'Pebble', 'Pigeon', 'Puddle', 'Raccoon', 'Rain',
                 'River', 'Rock', 'Shale', 'Shrike', 'Sky', 'Slate', 'Sleet', 'Smoke', 'Stone', 'Tempest',
                 'Torrent', 'Tornado', 'Wolf'
        ],
        'DARKGREY': [
            'Ash', 'Ashen', 'Basalt', 'Boulder', 'Cave', 'Cavern', 'Cinder', 'Damp', 'Dark',
            'Evening', 'Flint', 'Granite', 'Gravel', 'Grey', 'Murk', 'Pebble',
            'Raccoon',
            'Rat', 'Rock', 'Rubble', 'Shade', 'Shadow', 'Shale', 'Slate', 'Smoke', 'Smoulder',
            'Soot',
            'Stone', 'Storm', 'Torrent', 'Tornado', 'Twilight', 'Wolf'
        ],
        'BLACK': [
              'Basalt', 'Bat', 'Bear', 'Black', 'Blackberry', 'Cave', 'Cavern', 'Charcoal', 'Coal',
            'Crow', 'Dark', 'Dusk', 'Ebony', 'Eclipse', 'Evening',
            'Jackdaw', 'Magpie', 'Midnight', 'Night', 'Rat', 'Raven', 'Rook',
            'Sable',
            'Scorch', 'Shade', 'Shadow', 'Singe', 'Smoulder', 'Soot', 'Spider', 'Storm',
            'Twilight',
            'Umbra'
        ],
        'PALEGINGER': [
             'Barley', 'Beach', 'Bee', 'Buttercup', 'Cream', 'Daffodil', 'Daisy', 'Dandelion',
            'Dawn', 'Day', 'Desert', 'Dune', 'Flash', 'Flicker', 'Ginger', 'Gold', 'Hay',
            'Honey', 'Light', 'Lightning', 'Lion', 'Maize', 'Marigold', 'Morning', 'Oasis', 'Oat'
            'Orange', 'Pale', 'Peach',
            'Sand', 'Sandy', 'Sun', 'Tawny', 'Wheat', 'Yellow'
        ],
        'GOLDEN': [
            'Amber', 'Barley', 'Bee', 'Bumble', 'Buttercup', 'Canary', 'Cheetah', 'Daffodil',
            'Daisy', 'Dandelion,' 'Dawn', 'Day', 'Desert', 'Dune', 'Fire', 'Firefly',
            'Flame', 'Flare', 'Flash', 'Flicker', 'Ginger', 'Gold', 'Golden', 'Goldenrod', 'Hay',
            'Honey', 'Hornet', 'Leopard', 'Lion', 'Maize', 'Marigold', 'Morning', 'Oat', 'Saffron',
            'Sand', 'Sandy', 'Sun', 'Tawny', 'Thunder', 'Wasp', 'Wheat', 'Yellow'
        ],
        'GINGER': [
            'Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
            'Dawn', 'Day', 'Ember', 'Fire', 'Firefly', 'Flame', 'Flare', 'Flash', 'Flicker',
            'Fox', 'Ginger', 'Inferno', 'Maple', 'Marigold', 'Morning', 'Orange', 'Poppy', 'Saffron',
            'Scorch', 'Singe', 'Smoulder', 'Spark', 'Sun', 'Tangerine', 'Tawny', 'Tiger', 'Vixen'
        ],
        'DARKGINGER': [
            'Amaranth', 'Amber', 'Apple', 'Auburn', 'Blaze', 'Bronze', 'Burn', 'Cardinal',
            'Cherry', 'Chestnut', 'Cinnabar', 'Cinnamon', 'Clay', 'Copper', 'Coral',
            'Cranberry',
            'Crimson', 'Ember', 'Fire', 'Firefly', 'Flame', 'Flare', 'Flash', 'Flicker', 'Fox'
            'Ginger', 'Inferno', 'Jasper',
            'Mahogany', 'Maple', 'Morning', 'Orange', 'Plum',
            'Poinsettia', 'Poppy', 'Raspberry', 'Red', 'Rose', 'Rowan', 'Ruddy', 'Russet',
            'Saffron',
            'Scarlet', 'Scorch', 'Sierra', 'Singe', 'Smoulder', 'Spark', 'Strawberry',
            'Tiger',
            'Vixen'
        ],
        'LIGHTBROWN': [
            'Acorn', 'Beaver', 'Brown', 'Caribou', 'Chickadee', 'Chipmunk',
            'Cinnamon', 'Clay', 'Cougar', 'Coyote', 'Deer', 'Dirt', 'Doe', 'Dun', 'Dust',
            'Earth', 'Elk', 'Fallow', 'Gopher', 'Groundhog', 'Hare', 'Hazel', 'Heather',
            'Hedgehog', 'Moth', 'Mouse', 'Mushroom', 'Nut', 'Pale', 'Pika', 'Rabbit', 'Sepia',
            'Shrew', 'Silt', 'Snail', 'Sparrow', 'Stag', 'Timber'
        ],
        'BROWN': [
            'Acorn', 'Bear', 'Beaver', 'Bronze', 'Brown', 'Chestnut', 'Chipmunk', 'Cinnamon',
            'Clay', 'Cougar', 'Coyote', 'Deer', 'Doe', 'Dun', 'Earth', 'Elk', 'Groundhog',
            'Hare', 'Hawk', 'Log', 'Mink', 'Moose', 'Moth', 'Mouse', 'Mud', 'Mushroom',
            'Nut',
            'Nutmeg', 'Oak', 'Otter', 'Owl', 'Porcupine', 'Rabbit', 'Sepia', 'Shrew', 'Sierra',
            'Silt',
            'Snail', 'Sparrow', 'Splinter', 'Stag', 'Stoat', 'Sycamore', 'Timber',
            'Weasel'
        ],
        'DARKBROWN':
        ['Acorn', 'Bat', 'Bear', 'Beaver', 'Bison', 'Bog', 'Bronze', 'Brown',
             'Burrow', 'Chestnut', 'Clay', 'Dark', 'Doe', 'Dun', 'Dusk', 
             'Hickory', 'Log', 'Mahogany', 'Moose',
             'Mushroom',
             'Muskrat', 'Nightingale', 'Nut', 'Nutmeg', 'Oak', 'Otter', 'Owl', 'Porcupine',
             'Rat',
             'Sable', 'Sepia', 'Silt', 'Splinter', 'Swamp', 'Sycamore', 'Timber', 'Toad',
             'Truffle',
             'Umber', 'Walnut', 'Warren', 'Wolverine'
         ],
#          'LEUCISM': [
#             'Alabaster', 'Avalanche', 'Blizzard', 'Bone', 'Cherry', 'Cloud', 'Cobweb', 'Cotton',
#             'Crane', 'Down', 'Fade', 'Faded', 'Flash', 'Flurry', 'Frigid', 'Frost', 'Frozen',
#             'Glacier',
#             'Gleam', 'Gull', 'Hail', 'Hemlock', 'Heron', 'Ice', 'Icicle', 'Ivory', 'Lamb', 'Light',
#             'Lightning', 'Milk', 'Mushroom', 'Oleander', 'Pale', 'Seafoam', 'Sheep',
#             'Shimmer',
#             'Shine', 'Shrike', 'Silk', 'Snow', 'Snowdrop', 'Swan', 'Tundra', 'White',
#             'Zephyr'
#         ],
        'IVORY': [
            'Ash', 'Ashen', 'Blizzard', 'Bluebell', 'Blueberry', 'Blue', 'Boulder', 'Cinder',
                     'Cloud', 'Cobweb', 'Creek', 'Damp', 'Dew', 'Dove', 'Down', 'Drizzle', 'Fade',
                     'Faded', 'Fjord', 'Flood', 'Fog', 'Frigid', 'Frost', 'Frozen', 'Gale',
                     'Geyser', 'Glacier', 'Gravel', 'Grey', 'Hail', 'Haze', 'Hurricane', 'Lagoon',
                     'Minnow',
                     'Mist', 'Misty', 'Mistral', 'Moon', 'Pale', 'Pebble', 'Pigeon', 'Puddle', 'Rain',
                     'Ripple',
                     'River', 'Rock', 'Shallow', 'Shimmer', 'Shine', 'Shrike', 'Silver', 'Sky', 'Sleet',
                     'Smoke', 'Stone', 'Tempest', 'Tornado', 'Zephyr'
        ],
#         'MELRED': [
#               'Basalt', 'Bat', 'Bear', 'Black', 'Blackberry', 'Cave', 'Cavern', 'Charcoal', 'Coal',
#             'Crow', 'Dark', 'Dusk', 'Ebony', 'Eclipse', 'Evening',
#             'Jackdaw', 'Magpie', 'Midnight', 'Night', 'Rat', 'Raven', 'Rook',
#             'Sable',
#             'Scorch', 'Shade', 'Shadow', 'Singe', 'Smoulder', 'Soot', 'Spider', 'Storm',
#             'Twilight',
#             'Umbra'
#         ],
#          'MELBLUE': [
#               'Basalt', 'Bat', 'Bear', 'Black', 'Blackberry', 'Cave', 'Cavern', 'Charcoal', 'Coal',
#             'Crow', 'Dark', 'Dusk', 'Ebony', 'Eclipse', 'Evening',
#             'Jackdaw', 'Magpie', 'Midnight', 'Night', 'Rat', 'Raven', 'Rook',
#             'Sable',
#             'Scorch', 'Shade', 'Shadow', 'Singe', 'Smoulder', 'Soot', 'Spider', 'Storm',
#             'Twilight',
#             'Umbra'
#         ],
        'PUMPKIN': [
             'Barley', 'Beach', 'Bee', 'Buttercup', 'Cream', 'Daffodil', 'Daisy', 'Dandelion',
            'Dawn', 'Day', 'Desert', 'Dune', 'Flash', 'Flicker', 'Ginger', 'Gold', 'Hay',
            'Honey', 'Light', 'Lightning', 'Lion', 'Maize', 'Marigold', 'Morning', 'Oasis', 'Oat'
            'Orange', 'Pale', 'Peach', 'Pumpkin'
            'Sand', 'Sandy', 'Sun', 'Tawny', 'Wheat'
        ],
        'APRICOT': [
            'Amber', 'Barley', 'Bee', 'Bumble', 'Buttercup', 'Canary', 'Cheetah', 'Daffodil',
            'Daisy', 'Dandelion,' 'Dawn', 'Day', 'Desert', 'Dune', 'Fire', 'Firefly',
            'Flame', 'Flare', 'Flash', 'Flicker', 'Ginger', 'Gold', 'Golden', 'Goldenrod', 'Hay',
            'Honey', 'Hornet', 'Leopard', 'Lion', 'Maize', 'Marigold', 'Morning', 'Oat', 'Saffron',
            'Sand', 'Sandy', 'Sun', 'Tawny', 'Thunder', 'Wasp', 'Wheat', 'Yellow'
        ],
        'COPPER': [
            'Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
            'Dawn', 'Day', 'Ember', 'Fire', 'Firefly', 'Flame', 'Flare', 'Flash', 'Flicker',
            'Fox', 'Ginger', 'Inferno', 'Maple', 'Marigold', 'Morning', 'Orange', 'Poppy', 'Saffron',
            'Scorch', 'Singe', 'Smoulder', 'Spark', 'Sun', 'Tangerine', 'Tawny', 'Tiger', 'Vixen'
        ],
        'RUST': [
            'Amaranth', 'Amber', 'Apple', 'Auburn', 'Blaze', 'Bronze', 'Burn', 'Cardinal',
            'Cherry', 'Chestnut', 'Cinnabar', 'Cinnamon', 'Clay', 'Copper', 'Coral',
            'Cranberry',
            'Crimson', 'Ember', 'Fire', 'Firefly', 'Flame', 'Flare', 'Flash', 'Flicker', 'Fox'
            'Ginger', 'Inferno', 'Jasper',
            'Mahogany', 'Maple', 'Morning', 'Orange', 'Plum',
            'Poinsettia', 'Poppy', 'Raspberry', 'Red', 'Rose', 'Rowan', 'Ruddy', 'Russet',
            'Saffron',
            'Scarlet', 'Scorch', 'Sierra', 'Singe', 'Smoulder', 'Spark', 'Strawberry',
            'Tiger',
            'Vixen'
        ],
        'SAND': ['Acorn', 'Beaver', 'Brown', 'Caribou', 'Chickadee', 'Chipmunk',
            'Cinnamon', 'Clay', 'Cougar', 'Coyote', 'Deer', 'Dirt', 'Doe', 'Dun', 'Dust',
            'Earth', 'Elk', 'Fallow', 'Gopher', 'Groundhog', 'Hare', 'Hazel', 'Heather',
            'Hedgehog', 'Moth', 'Mouse', 'Mushroom', 'Nut', 'Pale', 'Pika', 'Rabbit', 'Sepia',
            'Shrew', 'Silt', 'Snail', 'Sparrow', 'Stag', 'Timber'],
        
        'CARAMEL': ['Acorn', 'Beaver', 'Brown', 'Caribou', 'Chickadee', 'Chipmunk',
            'Cinnamon', 'Clay', 'Cougar', 'Coyote', 'Deer', 'Dirt', 'Doe', 'Dun', 'Dust',
            'Earth', 'Elk', 'Fallow', 'Gopher', 'Groundhog', 'Hare', 'Hazel', 'Heather',
            'Hedgehog', 'Moth', 'Mouse', 'Mushroom', 'Nut', 'Pale', 'Pika', 'Rabbit', 'Sepia',
            'Shrew', 'Silt', 'Snail', 'Sparrow', 'Stag', 'Timber'],
        
        'TOFFEE': ['Acorn', 'Beaver', 'Brown', 'Caribou', 'Chickadee', 'Chipmunk',
            'Cinnamon', 'Clay', 'Cougar', 'Coyote', 'Deer', 'Dirt', 'Doe', 'Dun', 'Dust',
            'Earth', 'Elk', 'Fallow', 'Gopher', 'Groundhog', 'Hare', 'Hazel', 'Heather',
            'Hedgehog', 'Moth', 'Mouse', 'Mushroom', 'Nut', 'Pale', 'Pika', 'Rabbit', 'Sepia',
            'Shrew', 'Silt', 'Snail', 'Sparrow', 'Stag', 'Timber', 'Acorn', 'Bat',
            'Bear', 'Beaver', 'Bison', 'Bog', 'Bronze', 'Brown',
             'Burrow', 'Chestnut', 'Clay', 'Dark', 'Doe', 'Dun', 'Dusk', 
             'Hickory', 'Log', 'Mahogany', 'Moose',
             'Mushroom',
             'Muskrat', 'Nightingale', 'Nut', 'Nutmeg', 'Oak', 'Otter', 'Owl', 'Porcupine',
             'Rat',
             'Sable', 'Sepia', 'Silt', 'Splinter', 'Swamp', 'Sycamore', 'Timber', 'Toad',
             'Truffle',
             'Umber', 'Walnut', 'Warren', 'Wolverine'],
        
        'FAWN': ['Acorn', 'Beaver', 'Brown', 'Caribou', 'Chickadee', 'Chipmunk',
            'Cinnamon', 'Clay', 'Cougar', 'Coyote', 'Deer', 'Dirt', 'Doe', 'Dun', 'Dust',
            'Earth', 'Elk', 'Fallow', 'Gopher', 'Groundhog', 'Hare', 'Hazel', 'Heather',
            'Hedgehog', 'Moth', 'Mouse', 'Mushroom', 'Nut', 'Pale', 'Pika', 'Rabbit', 'Sepia',
            'Shrew', 'Silt', 'Snail', 'Sparrow', 'Stag', 'Timber', 'Fawn', 'Acorn',
            'Bat', 'Bear', 'Beaver', 'Bison', 'Bog', 'Bronze', 'Brown',
             'Burrow', 'Chestnut', 'Clay', 'Dark', 'Doe', 'Dun', 'Dusk', 
             'Hickory', 'Log', 'Mahogany', 'Moose',
             'Mushroom',
             'Muskrat', 'Nightingale', 'Nut', 'Nutmeg', 'Oak', 'Otter', 'Owl', 'Porcupine',
             'Rat',
             'Sable', 'Sepia', 'Silt', 'Splinter', 'Swamp', 'Sycamore', 'Timber', 'Toad',
             'Truffle',
             'Umber', 'Walnut', 'Warren', 'Wolverine'],
        
        'MIDNIGHT': ['Berry','Violet', 'Iris', 'Wisteria', 'Plum', 'Amethyst', 'Royal', 'Lilac', 'Orchid', 'Lavender', 'Dawn',
                     'Basalt', 'Bat', 'Bear', 'Black', 'Blackberry', 'Cave', 'Cavern', 'Charcoal', 'Coal',
            'Crow', 'Dark', 'Dusk', 'Ebony', 'Eclipse', 'Evening',
            'Jackdaw', 'Magpie', 'Midnight', 'Night', 'Rat', 'Raven', 'Rook',
            'Sable',
            'Scorch', 'Shade', 'Shadow', 'Singe', 'Smoulder', 'Soot', 'Spider', 'Storm',
            'Twilight',
            'Umbra'],
    }

    eye_prefixes = {
       'YELLOW': ['Barley', 'Bee', 'Bumble', 'Buttercup', 'Canary', 'Daffodil', 'Daisy', 'Dawn', 'Day',
                   'Desert', 'Dune', 'Flash', 'Gold', 'Golden', 'Goldenrod', 'Hay', 'Honey', 'Hornet',
                   'Leopard',
                   'Light', 'Lightning', 'Lion', 'Maize', 'Oasis', 'Oat', 'Sun', 'Thunder', 'Wasp', 'Wheat',
                   'Yellow'],
       'PALEYELLOW': ['Barley', 'Bee', 'Bumble', 'Buttercup', 'Canary', 'Daffodil', 'Daisy', 'Dawn', 'Day',
                   'Desert', 'Dune', 'Flash', 'Gold', 'Golden', 'Goldenrod', 'Hay', 'Honey', 'Hornet',
                   'Leopard',
                   'Light', 'Lightning', 'Lion', 'Maize', 'Oasis', 'Oat', 'Sun', 'Thunder', 'Wasp', 'Wheat',
                   'Yellow'],
        'AMBER': ['Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar',
                  'Clementine', 'Copper', 'Dandelion', 'Dawn', 'Ember', 'Fire', 'Firefly', 'Flame',
                  'Flare', 'Flash', 'Flicker', 'Fox', 'Inferno', 'Jasper', 'Maple', 'Marigold', 'Morning',
                  'Orange', 'Saffron', 'Spark', 'Sun', 'Tangerine', 'Tiger'],
        'PUMPKIN': [ 'Bayou', 'Bog', 'Bullfrog', 'Bulrush', 'Fen', 'Frog', 'Grasshopper', 'Hazel',
                  'Kelp', 'Lichen', 'Lizard', 'Marsh', 'Mire', 'Moss','Mushroom', 'Olive',
                  'Sage', 'Thicket', 'Tortoise', 'Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar',
                  'Clementine', 'Copper', 'Dandelion', 'Dawn', 'Ember', 'Fire', 'Firefly', 'Flame',
                  'Flare', 'Flash', 'Flicker', 'Fox', 'Inferno', 'Jasper', 'Maple', 'Marigold', 'Morning',
                  'Orange', 'Saffron', 'Spark', 'Sun', 'Tangerine', 'Tiger'],
        'HAZEL': [ 'Bayou', 'Bog', 'Bullfrog', 'Bulrush', 'Fen', 'Frog', 'Grasshopper', 'Hazel',
                  'Kelp', 'Lichen', 'Lizard', 'Marsh', 'Mire', 'Moss','Mushroom', 'Olive',
                  'Sage', 'Thicket', 'Tortoise'],
        'PALEGREEN': ['Apple', 'Bush', 'Clove', 'Clover', 'Evergreen', 'Fern', 'Forest',
                      'Grass', 'Green', 'Grove', 'Iguana', 'Kelp', 'Leaf', 'Lichen', 'Lizard', 'Mantis',
                      'Meadow',
                      'Mint', 'Sage', 'Sprig', 'Sprout', 'Stem', 'Tree', 'Vine', ],
        'GREEN': ['Apple', 'Basil', 'Bayou', 'Bog', 'Bush', 'Clove', 'Clover',
                  'Evergreen', 'Fern', 'Forest', 'Frog', 'Grass', 'Green', 'Grove',
                  'Leaf',
                  'Lichen', 'Lizard', 'Mantis', 'Meadow', 'Moss', 'Parsley', 'Sprig', 'Sprout', 'Spruce',
                  'Stem',
                  'Thicket', 'Thistle', 'Tortoise', 'Tree', 'Turtle', 'Vine', 'Weed', 'Wintergreen'],
        'BLUE': ['Azure', 'Bay', 'Bluebell', 'Blueberry', 'Blue', 'Brook', 'Bubble', 'Cascade',
                 'Current', 'Cyclone', 'Dew', 'Drizzle', 'Estuary', 'Firth', 'Fjord', 'Flood', 'Frigid',
                 'Frost', 'Frozen', 'Geyser', 'Glacier', 'Gleam', 'Ice', 'Icicle', 'Jay', 'Lagoon', 'Lake',
                 'Ocean', 'Pond', 'Pool', 'Rain', 'River', 'Sea', 'Seafoam', 'Shallow', 'Shore', 'Sky',
                 'Splash',
                 'Stream', 'Teal', 'Tide', 'Torrent', 'Water', 'Wave'],
        'DARKBLUE': ['Azure', 'Bay', 'Bluebell', 'Blueberry', 'Blue', 'Brook', 'Bubble', 'Cascade',
                     'Current',
                     'Cyclone', 'Drizzle', 'Estuary', 'Firth', 'Flood', 'Geyser', 'Glacier',
                     'Indigo',
                     'Midnight', 'Ocean', 'Pond', 'Pool', 'Rain', 'River', 'Sea', 'Sky', 'Storm', 'Stream',
                     'Tide', 'Torrent', 'Twilight', 'Water', 'Wave'],
        'BLUEYELLOW': ['Aurora', 'Azure', 'Barley', 'Bay', 'Bee', 'Bluebell', 'Blueberry', 'Blue', 'Brook',
                       'Bubble', 'Buttercup', 'Butterfly', 'Canary', 'Cascade', 'Chalcedony', 'Current',
                       'Cyclone', 'Daffodil', 'Daisy', 'Dawn', 'Day', 'Dew', 'Drizzle', 'Dune', 'Echo',
                       'Estuary', 'Firth', 'Fjord', 'Flash', 'Flood', 'Frigid', 'Frost', 'Frozen', 'Geyser',
                       'Glacier', 'Gleam', 'Honey', 'Hornet', 'Ice', 'Icicle', 'Jay', 'Lagoon', 'Lake',
                       'Light',
                       'Lightning', 'Lion', 'Oasis', 'Ocean', 'Pond', 'Pool', 'Rain', 'River', 'Sea',
                       'Seafoam',
                       'Shallow', 'Shimmer', 'Shine', 'Shore', 'Sky', 'Splash', 'Stream', 'Sun', 'Teal',
                       'Tide',
                       'Torrent', 'Wasp', 'Water', 'Wave', 'Wheat', 'Yellow'],
        'AQUA': ['Apple', 'Aurora', 'Azure', 'Basil', 'Bay', 'Bluebell', 'Blueberry', 'Blue',
                      'Bog', 'Brook', 'Bubble', 'Bullfrog', 'Bush', 'Butterfly', 'Cascade', 'Chalcedony',
                      'Clove', 'Clover', 'Current', 'Cyclone', 'Delta', 'Dew', 'Drizzle', 'Echo',
                      'Evergreen', 'Fern', 'Firth', 'Fjord', 'Flood', 'Forest', 'Frigid',
                      'Frost', 'Frozen', 'Geyser', 'Glacier', 'Gleam', 'Grass', 'Green', 'Grove',
                      'Ice', 'Icicle', 'Jay', 'Kelp', 'Lagoon', 'Lake', 'Leaf', 'Lichen', 'Lizard',
                      'Mantis',
                      'Meadow', 'Moss', 'Ocean', 'Parsley', 'Pond', 'Pool', 'Rain', 'River', 'Sea',
                      'Seafoam',
                      'Shallow', 'Shimmer', 'Shine', 'Shore', 'Sky', 'Splash', 'Sprig', 'Sprout', 'Spruce',
                      'Stem', 'Stream', 'Teal', 'Thicket', 'Thistle', 'Tide', 'Torrent', 'Tortoise', 'Tree',
                      'Turtle', 'Vine', 'Water', 'Wave', 'Weed', 'Wintergreen'],
       'INDIGO': ['Apple', 'Aurora', 'Azure', 'Basil', 'Bay', 'Bluebell', 'Blueberry', 'Blue',
                      'Bog', 'Brook', 'Bubble', 'Bullfrog', 'Bush', 'Butterfly', 'Cascade', 'Chalcedony',
                      'Clove', 'Clover', 'Current', 'Cyclone', 'Delta', 'Dew', 'Drizzle', 'Echo',
                      'Evergreen', 'Fern', 'Firth', 'Fjord', 'Flood', 'Forest', 'Frigid',
                      'Frost', 'Frozen', 'Geyser', 'Glacier', 'Gleam', 'Grass', 'Green', 'Grove',
                      'Ice', 'Icicle', 'Jay', 'Kelp', 'Lagoon', 'Lake', 'Leaf', 'Lichen', 'Lizard',
                      'Mantis',
                      'Meadow', 'Moss', 'Ocean', 'Parsley', 'Pond', 'Pool', 'Rain', 'River', 'Sea',
                      'Seafoam',
                      'Shallow', 'Shimmer', 'Shine', 'Shore', 'Sky', 'Splash', 'Sprig', 'Sprout', 'Spruce',
                      'Stem', 'Stream', 'Teal', 'Thicket', 'Thistle', 'Tide', 'Torrent', 'Tortoise', 'Tree',
                      'Turtle', 'Vine', 'Water', 'Wave', 'Weed', 'Wintergreen'],
        'RED': ['Auburn', 'Bronze', 'Cinnamon', 'Clay', 'Copper', 'Crimson', 'Flicker', 'Inferno',
                   'Jasper', 'Mahogany', 'Plum', 'Poinsettia', 'Poppy', 'Rose', 'Ruddy', 'Robin', 'Russet',
                   'Salmon', 'Sap', 'Scorch', 'Sepia', 'Sienna', 'Sierra', 'Singe', 'Smoulder', 'Squirrel',
                   'Stoat', 'Tiger', 'Vixen', 'Weasel'],
        'AMARANTH': ['Rose', 'Blush', 'Carnation', 'Salmon', 'Pale', 'Peach'],
        'SCARLET': ['Auburn', 'Bronze', 'Cinnamon', 'Clay', 'Copper', 'Crimson', 'Flicker', 'Inferno',
                   'Jasper', 'Mahogany', 'Plum', 'Poinsettia', 'Poppy', 'Rose', 'Ruddy', 'Robin', 'Russet',
                   'Sap', 'Scorch', 'Sepia', 'Sienna', 'Sierra', 'Singe', 'Smoulder', 'Squirrel',
                   'Stoat', 'Tiger', 'Vixen', 'Weasel'],
        'SPRINGGREEN': ['Bayou', 'Bog', 'Chive', 'Clove', 'Cress', 'Fern',
                  'Frond','Leaf', 'Leech', 'Lichen', 'Moss', 'Gecko',
                  'Grass', 'Grasshopper', 'Green', 'Lizard', 'Meadow', 'Mantis', 'Olive',
                  'Pear', 'Prairie', 'Sage', 'Scrub', 'Snapper', 'Sprig', 'Sprout', 'Stem', 'Thicket',
                  'Thistle', 'Turtle', 'Vine',  'Willow'],
        'VIOLET': ['Violet', 'Iris', 'Wisteria', 'Plum', 'Amethyst', 'Royal', 'Lilac', 'Orchid', 'Lavender'],
        'PINKBLUE': ['Violet', 'Iris', 'Wisteria', 'Plum', 'Amethyst', 'Royal', 'Lilac', 'Orchid', 'Lavender'],
        'EMERALD': ['Green', 'Pale', 'Mint', 'Fern', 'Emerald'],
        'PINK': ['Rose', 'Blush', 'Carnation', 'Salmon', 'Pale', 'Peach'],
        'MINT': ['Blizzard', 'Bluebell', 'Brook', 'Bubble', 'Cascade', 'Cloud', 'Creek',
                     'Current', 'Cyclone', 'Day', 'Delta', 'Dew', 'Drizzle', 'Echo',
                     'Fjord', 'Fog', 'Frigid', 'Frozen', 'Frost', 'Gale', 'Gleam', 'Glacier', 'Hail', 'Ice',
                     'Icicle', 'Jay', 'Lake', 'Lagoon', 'Mist', 'Misty', 'Mistral', 'Moon', 'Ocean',
                     'Pale','Pond', 'Pool', 'Ripple', 'River', 'Sea', 'Shallow', 'Seafoam',
                     'Shine', 'Shimmer', 'Sky', 'Sleet', 'Silver', 'Snow', 'Snowdrop', 'Splash', 'Tempest',
                     'Tide', 'Water',  'Web', 'Wet', 'Wave', 'Wisteria', 'Zephyr'], 
        'PALEBLUE': ['Blizzard', 'Bluebell', 'Brook', 'Bubble', 'Cascade',  'Cloud', 'Creek',
                     'Current', 'Cyclone', 'Day', 'Delta', 'Dew', 'Drizzle', 'Echo', 
                     'Fjord', 'Fog', 'Frigid', 'Frozen', 'Frost', 'Gale', 'Gleam', 'Glacier', 'Hail', 'Ice',
                     'Icicle', 'Jay', 'Lake', 'Lagoon', 'Mist', 'Misty', 'Mistral', 'Moon', 'Ocean',
                     'Pale', 'Pond', 'Pool', 'Ripple', 'River', 'Sea', 'Shallow', 'Seafoam',
                     'Shine', 'Shimmer', 'Sky', 'Sleet', 'Silver', 'Snow', 'Snowdrop', 'Splash', 'Tempest',
                     'Tide', 'Tuna', 'Water', 'Web', 'Wet', 'Wave', 'Wisteria', 'Zephyr', 'Ice'],
        'BROWN':['Umber', 'Hickory', 'Cinnamon', 'Umber', 'Cedar', 'Walnut', 'Bark', 'Bison', 'Brown', 'Dark',
                  'Eagle', 'Hickory', 'Hollow',
                      'Moose', 'Otter', 'Oak',
                      'Owl', 'Rat', 'Sable', 'Scorpion', 'Sepia', 'Splinter', 'Swift',
                      'Sycamore','Timber',  'Umber', 'Walnut', 'Wolverine'],
        'PALEVIOLET': ['Violet', 'Iris', 'Wisteria', 'Plum', 'Amethyst', 'Royal', 'Lilac', 'Orchid', 'Lavender'],
        'SAGEGREEN': ['Green', 'Fern', 'Holly', 'Clover', 'Olive', 'Jade' 'Basil', 'Bayou', 'Bog',
                 'Clover', 'Clove', 'Cress', 
                      'Evergreen', 'Fern', 'Forest', 'Frond', 'Frog', 'Glade', 'Glen', 'Grass', 'Green',
                      'Grove', 'Ivy', 'Kelp', 'Leaf', 'Lichen', 'Meadow', 'Moss','Pine',
                      'Sapling', 'Snapper', 'Sprig', 'Sprout', 'Spruce', 'Stem', 'Thicket', 'Thistle',
                      'Thorn', 'Tortoise', 'Turtle', 'Vine', 'Willow', 'Wintergreen', 'Yarrow'],
        'DARKGREEN': ['Green', 'Fern', 'Holly', 'Clover', 'Olive', 'Jade' 'Basil', 'Bayou', 'Bog',
                 'Clover', 'Clove', 'Cress', 
                      'Evergreen', 'Fern', 'Forest', 'Frond', 'Frog', 'Glade', 'Glen', 'Grass', 'Green',
                      'Grove', 'Ivy', 'Kelp', 'Leaf', 'Lichen', 'Meadow', 'Moss','Pine',
                      'Sapling', 'Snapper', 'Sprig', 'Sprout', 'Spruce', 'Stem', 'Thicket', 'Thistle',
                      'Thorn', 'Tortoise', 'Turtle', 'Vine', 'Willow', 'Wintergreen', 'Yarrow'],
        'MAGENTA': ['Violet', 'Iris', 'Wisteria', 'Plum', 'Amethyst', 'Royal', 'Lilac', 'Orchid', 'Lavender'],
        'ROSEGOLD': ['Violet', 'Iris', 'Wisteria', 'Plum', 'Amethyst', 'Royal', 'Lilac', 'Orchid', 'Lavender'],
        'CORAL': ['Rose', 'Blush', 'Carnation', 'Salmon', 'Pale', 'Peach', 'Peach'],
        'COPPER': ['Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
                   'Coral', 'Inferno', 'Jasper', 'Marigold', 'Maple', 'Oriole', 'Orange', 'Singe',
                   'Cranberry', 'Crimson', 'Dawn', 'Flame', 'Flare', 'Firefly', 'Fire', 'Flicker', 'Fox',
                   'Ginger', 'Holly', 'Morning', 'Plum', 'Poinsettia', 'Poppy', 'Red',
                   'Raspberry',  'Rose', 'Robin', 'Salmon', 'Scorch', 'Sorrel', 'Squirrel',
                   'Strawberry', 'Tangerine', 'Tiger',  'Vixen'],
        'HONEY': ['Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
                   'Coral', 'Inferno', 'Jasper', 'Marigold', 'Maple', 'Oriole', 'Orange', 'Singe',
                   'Cranberry', 'Crimson', 'Dawn', 'Flame', 'Flare', 'Firefly', 'Fire', 'Flicker', 'Fox',
                   'Ginger', 'Holly', 'Morning', 'Plum', 'Poinsettia', 'Poppy', 'Red',
                   'Raspberry',  'Rose', 'Robin', 'Salmon', 'Scorch', 'Sorrel', 'Squirrel',
                   'Strawberry', 'Tangerine', 'Tiger',  'Vixen'],
       'DANDELION': ['Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
                   'Coral', 'Inferno', 'Jasper', 'Marigold', 'Maple', 'Oriole', 'Orange', 'Singe',
                   'Cranberry', 'Crimson', 'Dawn', 'Flame', 'Flare', 'Firefly', 'Fire', 'Flicker', 'Fox',
                   'Ginger', 'Holly', 'Morning', 'Plum', 'Poinsettia', 'Poppy', 'Red',
                   'Raspberry',  'Rose', 'Robin', 'Salmon', 'Scorch', 'Sorrel', 'Squirrel',
                   'Strawberry', 'Tangerine', 'Tiger',  'Vixen'],
       'GOLD': ['Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
                   'Coral', 'Inferno', 'Jasper', 'Marigold', 'Maple', 'Oriole', 'Orange', 'Singe',
                   'Cranberry', 'Crimson', 'Dawn', 'Flame', 'Flare', 'Firefly', 'Fire', 'Flicker', 'Fox',
                   'Ginger', 'Holly', 'Morning', 'Plum', 'Poinsettia', 'Poppy', 'Red',
                   'Raspberry',  'Rose', 'Robin', 'Salmon', 'Scorch', 'Sorrel', 'Squirrel',
                   'Strawberry', 'Tangerine', 'Tiger',  'Vixen'],
       'DARKAMBER': ['Amber', 'Apple', 'Blaze', 'Burn', 'Cardinal', 'Cherry', 'Cinnabar', 'Clementine',
                   'Coral', 'Inferno', 'Jasper', 'Marigold', 'Maple', 'Oriole', 'Orange', 'Singe',
                   'Cranberry', 'Crimson', 'Dawn', 'Flame', 'Flare', 'Firefly', 'Fire', 'Flicker', 'Fox',
                   'Ginger', 'Holly', 'Morning', 'Plum', 'Poinsettia', 'Poppy', 'Red',
                   'Raspberry',  'Rose', 'Robin', 'Salmon', 'Scorch', 'Sorrel', 'Squirrel',
                   'Strawberry', 'Tangerine', 'Tiger',  'Vixen'],
        'GREENGOLD' : ['Tawny', 'Hazel', 'Gold', 'Daisy', 'Sand']
    }

    loner_names = [
        "Haku", "Pichi", "Poki", "Nagi", "Jubie", "Bonbon", "Beans", "Aurora",
        "Maleficent", "Luna", "Eclipse", "Sol", "Star", "George", "Nightmare",
        "Bagel", "Monster", "Gargoyle", "Missile Launcher", "Rolo", "Rocket",
        "Void", "Abyss", "Vox", "Princess", "Noodle", "Duchess", "Cheesecake",
        "Callie", "Randy", "Ace", "Queeny", "Freddy", "Stella", "Rooster",
        "Sophie", "Maverick", "Seamus", 'Meowyman', "Pickles", "Lacy", "Lucy",
        "Knox", "Lugnut", "Bailey", "Azula", "Lucky", "Sunny", "Sadie", "Sox",
        "Bandit", "Onyx", "Quinn", "Grace", "Fang", "Ike", "Flower",
        "Whiskers", "Gust", "Peony", 'Human', "Minnie", "Buddy", "Mollie",
        "Jaxon", "Dunnock", "Firefly", "Cheese", "Sandwich", "Spam",
        "Broccoli", "Prickle", "Insect", "Grasshopper", "Coral", "Windy",
        "Sofa", "McChicken", "Purry", "Katy", "Mop", "Fishtail", "Roman",
        "Wishbone", "Nova", "Quimby", "Quest", "Nessie", "Niles", "Neil",
        "Nutella", "Nakeena", "Nuka", "Hughie", "Harvey", "Herc", "French",
        "Finch", "Frannie", "Flutie", "Purdy", "Free", "Glory", "Snek", "Indi",
        "Igor", "Jupiter", "Nintendo", "Jesse", "James", "Jethro", "Shampoo",
        "Joker", "Jinx", "Chaos", "Havoc", "Trouble", "Kingston", "King",
        "Kip", "Kong", "Ken", "Kendra", "Kisha", "Kermit", "Kelloggs",
        "Kodiak", "Klondike", "Ketchup", "KD", "Lupo", "Luigi", "Lily", "Lora",
        "Lee", "Lex", "Lester", "Makwa", "Madi", "Minna", "Moxie", "Mucha",
        "Manda", "Monte", "Riya", "Monzi", "Nisha", "Nemo", "Nitro", "Oops",
        "O'Leary", "Ophelia", "Olga", "Oscar", "Owen", "Porsche", "Ping",
        "Pong", "Quinzee", "Quickie", "Quagmire", "Quake", "Quinoa", "Roomba",
        "Riot", "Peanut Wigglebutt", "Ramble", "Rudolph", "Rum", "Reese",
        "Scotch", "Sneakers", "Schmidt", "Espresso", "Cocoa Puff", "Sonic",
        "Teufel", "Toni", "Torque", "Tempest", "Turbo", "Tetris", "Triscuit",
        "Tumble", "Voltage", "Vinnie", "Vaxx", "Venture", "Vida", "Guinness",
        "Polly", "Piper", "Pepper", "Lakota", "Dakota", "Bently", "Chinook",
        "Tiny", "Ula", "Union", "Uriel", "Orion", "Oakley", "Roselie",
        "Belle", "Benny", "Bumblebee", "Bluebell", "Chip", "Chocolate",
        "Cracker", "Dave", "Dolly", "Egg", "Frito", "Frank", "Gibby", "Jack",
        "Jenny", "Juliet", "Joob", "John", "Jimmy", "Jude", "Kenny", "Tom",
        "Oreo", "Mocha", "Ninja", "Cinderblock", "Pip", "Pipsqueak", "Milque",
        "Toast", "Molly Murder Mittens", "Flabby", "Crunchy", "Sorbet",
        "Vanilla", "Mint", "Nikki", "Pocket", "Tabbytha", "Gravy",
        "Potato", "Chewy", "Pumpernickel", "Pecan", "Old Man Sam", "Icecube",
        "Queso Ruby", "Pearl", "Jasper", "Stan", "Rose", "Mojo", "Kate",
        "Carmen", "Mange", "Chase", "Socks", "Tabby", "Jay", "Charlie", "L",
        "Poopy", "Crunchwrap", "Meow-meow", "Bede", "Smores", "Evilface",
        "Nick", "Mitski", "Ash", "Ah", "Violet", "Alcina", "Worm", "Monika",
        "Rat", "Bongo", "Bunny", "Viktor", "Steve", "Jewels", "Blu", "Rue",
        "Stinky", "Garnet", "Anita", "Sloane", "Emi", "Vivienne", "Amber",
        "Moon", "Twilight", "River", "Glass", "Goose", "Hunter", "Amity",
        "Stripes", "Cowbell", "Rory", "Lobster", "Slug", "Starfish", "Salmon",
        "Judy", "Johnny", "Kerry", "Evelyn", "Holly", "Bolt", "Millie",
        "Jessica", "Laku", "Dragonfly", "X'ek", "Silva", "Dreamy", "Decay",
        "Twister", "Shay", "Louis", "Oleander", "Spots", "Cream", "Omelet",
        "Gizmo", "Feather", "Twix", "Silver", "Ghost", "Wisp", "Obi Wan",
        "Pikachu", "Mango", "Via", "Olivia", "Mr. Whiskers", "Fluffy",
        "Shimmer", "Mimi", "Melody", "Leon", "Punk", "Mew", "Fern",
        "Marceline", "Whisper", "Skrunkly", "Stolas", "Rio", "Steven", "Pear",
        "Sekhmet", "Melon", "Ember", "Loona", "Saki", "Tiny", "Sandy",
        "Miles", "Mini", "Judas", "Zim", "Vinyl", "Rarity", "Trixie", "Sunset",
        "Anubis", "Armin", "Amy", "Alice", "Alec", "Baphomet", "Bean",
        "Bastet", "Birb", "Burm", "Chrissy", "Cherry", "Chief", "Crow",
        "Carrie", "Calvin", "Cookie", "Catie", "Charm", "Crab", "Charles",
        "Caroline", "Conan", "Cloud", "Charlie", "Cowboy", 'Burger', "Dune",
        "Dan", "Delilah", "Emerald", "Emy", "Erica", "Eddie", "Eda", "Ferret",
        "Fawn", "Fiver", "Fallow", "Ferry", "Gamble", "Grain", "Gir", "Hop",
        "Hot Sauce", "Habanero", "Taco Bell", "Cheetoman", "Queso", "Ruby",
        "Molly", "Murder", "Mittens", "Tabatha", "Sam", "Samantha", "Peanut",
        "Wigglebutt", "Zoe", "Cheeto", "Taco", "Max", "Sparky", "Cosmo", "Fred", 
        "Leo", "Tucker", "Minette", "Milo", "Fork", "Penny", "Zelda", "Jake", 
        "Felix", "Oliver", "Kitty", "Chloe", "Angel", "Samantha", "Muschi", 
        "Chicco", "Caramel", "Charlotte", "Chanel", "Lola", "Ollie", "Boo", 
        "Frankie", "Hotdog", "Beverly", "Mera", "Tasha"
    ]

    if os.path.exists('saves/prefixlist.txt'):
        with open('saves/prefixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if os.path.exists('saves/suffixlist.txt'):
        with open('saves/suffixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 eyes=None,
                 pelt=None,
                 tortiepattern=None):
        self.status = status
        self.prefix = prefix
        self.suffix = suffix
        
        # Set prefix
        if prefix is None:
            named_after_appearance = not random.getrandbits(3)  # Chance for True is '1/8'.
            possible_prefix_categories = []
            if named_after_appearance and (eyes is not None or colour is not None):
                if eyes in self.eye_prefixes:
                    possible_prefix_categories.append(self.eye_prefixes[eyes])
                if colour in self.colour_prefixes:
                    possible_prefix_categories.append(self.colour_prefixes[colour])
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(self.normal_prefixes)
                    
        # Set suffix
        while self.suffix is None or self.suffix == self.prefix.casefold():
            if pelt is None or pelt == 'SingleColour':
                self.suffix = random.choice(self.normal_suffixes)
            else:
                named_after_pelt = not random.getrandbits(3) # Chance for True is '1/8'.
                # Pelt name only gets used if there's an associated suffix.
                if (named_after_pelt
                    and pelt in ["Tortie", "Calico"]
                    and tortiepattern in self.tortie_pelt_suffixes):
                    self.suffix = random.choice(self.tortie_pelt_suffixes[tortiepattern])
                elif named_after_pelt and pelt in self.pelt_suffixes:
                    self.suffix = random.choice(self.pelt_suffixes[pelt])
                else:
                    self.suffix = random.choice(self.normal_suffixes)

    def __repr__(self):
        if self.status in ["deputy", "warrior", "medicine cat", "elder"]:
            return self.prefix + self.suffix
        else:
            return self.prefix + self.special_suffixes[self.status]


names = Name()


