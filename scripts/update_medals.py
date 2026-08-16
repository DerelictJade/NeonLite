import pandas as pd
import json

def convert_time(t):
    add60 = t.startswith("01:")
    t = t[3:]
    
    if add60:
        if t[0] == "0": t = "6" + t[1:]
        if t[0] == "1": t = "7" + t[1:]
        if t[0] == "2": t = "8" + t[1:]
    
    t = t.replace(".","") + "999"
    while t.startswith("0"):
        t = t[1:]
    
    return int(t)

def create_dict(times, cols):
    lists = [times.iloc[:, c].tolist() for c in cols]
    lists_T = [list(row) for row in zip(*lists)]
    out = {LEVEL_IDS[i]:lists_T[i] for i in range(len(LEVEL_IDS))}
    return out

def write_json(data, filename, metadata=None):
    if metadata:
        output = {
            "_metadata": metadata,
            **data
        }
    else:
        output = {**data}
        
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
        f.write("\n")

LEVEL_IDS = ['TUT_MOVEMENT', 'TUT_SHOOTINGRANGE', 'SLUGGER', 'TUT_FROG', 'TUT_JUMP', 'GRID_TUT_BALLOON', 'TUT_BOMB2', 'TUT_BOMBJUMP', 'TUT_FASTTRACK', 'GRID_PORT', 'GRID_PAGODA', 'TUT_RIFLE', 'TUT_RIFLEJOCK', 'TUT_DASHENEMY', 'GRID_JUMPDASH', 'GRID_SMACKDOWN', 'GRID_MEATY_BALLOONS', 'GRID_FAST_BALLOON', 'GRID_DRAGON2', 'GRID_DASHDANCE', 'TUT_GUARDIAN', 'TUT_UZI', 'TUT_JUMPER', 'TUT_BOMB', 'GRID_DESCEND', 'GRID_STAMPEROUT', 'GRID_CRUISE', 'GRID_SPRINT', 'GRID_MOUNTAIN', 'GRID_SUPERKINETIC', 'GRID_ARRIVAL', 'FLOATING', 'GRID_BOSS_YELLOW', 'GRID_HOPHOP', 'GRID_RINGER_TUTORIAL', 'GRID_RINGER_EXPLORATION', 'GRID_HOPSCOTCH', 'GRID_BOOM', 'GRID_SNAKE_IN_MY_BOOT', 'GRID_FLOCK', 'GRID_BOMBS_AHOY', 'GRID_ARCS', 'GRID_APARTMENT', 'TUT_TRIPWIRE', 'GRID_TANGLED', 'GRID_HUNT', 'GRID_CANNONS', 'GRID_FALLING', 'TUT_SHOCKER2', 'TUT_SHOCKER', 'GRID_PREPARE', 'GRID_TRIPMAZE', 'GRID_RACE', 'TUT_FORCEFIELD2', 'GRID_SHIELD', 'SA L VAGE2', 'GRID_VERTICAL', 'GRID_MINEFIELD', 'TUT_MIMIC', 'GRID_MIMICPOP', 'GRID_SWARM', 'GRID_SWITCH', 'GRID_TRAPS2', 'TUT_ROCKETJUMP', 'TUT_ZIPLINE', 'GRID_CLIMBANG', 'GRID_ROCKETUZI', 'GRID_CRASHLAND', 'GRID_ESCALATE', 'GRID_SPIDERCLAUS', 'GRID_FIRECRACKER_2', 'GRID_SPIDERMAN', 'GRID_DESTRUCTION', 'GRID_HEAT', 'GRID_BOLT', 'GRID_PON', 'GRID_CHARGE', 'GRID_MIMICFINALE', 'GRID_BARRAGE', 'GRID_1GUN', 'GRID_HECK', 'GRID_ANTFARM', 'GRID_FORTRESS', 'GRID_GODTEMPLE_ENTRY', 'GRID_BOSS_GODSDEATHTEMPLE', 'GRID_EXTERMINATOR', 'GRID_FEVER', 'GRID_SKIPSLIDE', 'GRID_CLOSER', 'GRID_HIKE', 'GRID_SKIP', 'GRID_CEILING', 'GRID_BOOP', 'GRID_TRIPRAP', 'GRID_ZIPRAP', 'TUT_ORIGIN', 'GRID_BOSS_RAPTURE', 'SIDEQUEST_OBSTACLE_PISTOL', 'SIDEQUEST_OBSTACLE_PISTOL_SHOOT', 'SIDEQUEST_OBSTACLE_MACHINEGUN', 'SIDEQUEST_OBSTACLE_RIFLE_2', 'SIDEQUEST_OBSTACLE_UZI2', 'SIDEQUEST_OBSTACLE_SHOTGUN', 'SIDEQUEST_OBSTACLE_ROCKETLAUNCHER', 'SIDEQUEST_RAPTURE_QUEST', 'SIDEQUEST_DODGER', 'GRID_GLASSPATH', 'GRID_GLASSPATH2', 'GRID_HELLVATOR', 'GRID_GLASSPATH3', 'SIDEQUEST_ALL_SEEING_EYE', 'SIDEQUEST_RESIDENTSAWB', 'SIDEQUEST_RESIDENTSAW', 'SIDEQUEST_SUNSET_FLIP_POWERBOMB', 'GRID_BALLOONLAIR', 'SIDEQUEST_BARREL_CLIMB', 'SIDEQUEST_FISHERMAN_SUPLEX', 'SIDEQUEST_STF', 'SIDEQUEST_ARENASIXNINE', 'SIDEQUEST_ATTITUDE_ADJUSTMENT', 'SIDEQUEST_ROCKETGODZ']
MEDALS_URL = "https://docs.google.com/spreadsheets/d/1CCShf6x4Nd2sQnsBnk788xu3AIUrVkdqzaeORB5UueQ/export?format=csv&gid=1606677618&range=Advanced!K3:O124"

topaz_meta = [
    {
        "medali": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MedalTopaz.png",
        "stampi": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MikeyTopaz.png",
        "crysti": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/CrystalTopaz.png",
        "popup": "NLEM/RESULTS_MEDAL_TOPAZ",
        "rank": 167,
        "color": "#f95700",
        "hidden": False
    }
]

bd_meta = [
    {
        "medali": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MedalBlud.png",
        "stampi": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MikeyBlud.png",
        "crysti": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/CrystalBlud.png",
        "popup": "NLEM/RESULTS_MEDAL_BD",
        "rank": 169,
        "color": "#ff55fc",
        "hidden": False
    }
]

both_meta =  [
    {
        "medali": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MedalTopaz.png",
        "stampi": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MikeyTopaz.png",
        "crysti": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/CrystalTopaz.png",
        "popup": "NLEM/RESULTS_MEDAL_TOPAZ",
        "rank": 167,
        "color": "#f95700",
        "hidden": False
    },
    {
        "medali": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MedalBlud.png",
        "stampi": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/MikeyBlud.png",
        "crysti": "https://raw.githubusercontent.com/DerelictJade/NeonLite/main/Assets/Sprites/CrystalBlud.png",
        "popup": "NLEM/RESULTS_MEDAL_BD",
        "rank": 169,
        "color": "#ff55fc",
        "hidden": False
    }
]

df = pd.read_csv(MEDALS_URL, header=None)
times = df.map(convert_time)

topaz1 = create_dict(times, [4, 3, 2, 1])
bd1 = create_dict(times, [4, 3, 2, 0])
both1 = create_dict(times, [4, 3, 2, 1, 0])

topaz2 = create_dict(times, [1])
bd2 = create_dict(times, [0])
both2 = create_dict(times, [1, 0])

# Update old sheets
write_json(topaz1, "Resources/communitymedals.json")
write_json(bd1, "Resources/blood_diamond.json")
write_json(both1, "Resources/topaz+bd.json")

# Update new sheets
write_json(topaz2, "Resources/topaz2.json", topaz_meta)
write_json(bd2, "Resources/bd2.json", bd_meta)
write_json(both2, "Resources/topaz+bd2.json", both_meta)


