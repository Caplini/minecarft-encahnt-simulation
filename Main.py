import random
import statistics

enchants = ["Aqua Affinity",
"Bane of Arthropods1",
"Bane of Arthropods2",
"Bane of Arthropods3",
"Bane of Arthropods4",
"Bane of Arthropods5",
"Blast Protection1",
"Blast Protection2",
"Blast Protection3",
"Blast Protection4",
"Channeling",
"Curse of Binding1",
"Curse of Vanishing2",
"Depth Strider1",
"Depth Strider2",
"Depth Strider3",
"Efficienc1y",
"Efficiency1",
"Effi3ciency",
"Effi4ciency",
"Efficie5ncy",
"Feather Fall4ing",
"Feather2 Falling",
"Feather Fall4ing",
"Feather F1alling",
"Fire Asp5ect",
"Fire A4spect",
"Fire 4Pro6tection",
"Fire Protection",
"Fire Prot345ection",
"Fire P56rotection",
"Fla5me",
"Fortune",
"For5tune",
"Fort5une",
"Frost Walker",
"Fros5t Walker",
"Impa5ling",
"Impa6ing",
"Imp5aling",
"Im6paling",
"Impal2ing",
"Infin1ity",
"Kno5ckback",
"Knoc34kback",
"Loot5ing",
"Loo6ting",
"Loot4ing",
"Loy2alty",
"Loy4alty",
"Loy6alty",
"Luck3 of the Sea",
"Luck4 of the Sea",
"Luck 5of the Sea",
"L3ure",
"Lu3re",
"Lu5re",
"Mend2ing",
"Mult56i3shot",
"Piercing",
"Pier57cing",
"Piercing",
"Pierc7ing",
"Po7wer",
"Po8wer",
"Po8wer",
"Po5wer",
"Power",
"Pro8jectile Protection",
"Projectile8Prot8tection",
"Projec8tile Protection",
"Protection",
"Protec8tion",
"Prote8ction",
"Prote8ction",
"P8unch",
"Pu9nch",
"Qui9ck Charge",
"Quick C5harge",
"Quic7k Charge",
"Respi6ration",
"Respirat5ion",
"Resp4iration",
"Rip6tide",
"Rip487tide",
"Sharp9ness",
"Shar87pness",
"Shar8pn9ess",
"Sh7arpness",
"Shar87pness",
"Sil9k Touch",
"Smi3te",
"Smi6te",
"Sm24ite",
"Smi67te",
"Sm89ite",
"Swe7eping Edge",
"Swe9eping Edge",
"Sweep5ing Edge",
"T8horns",
"Tho46rns",
"Tho88rns",
"Unb8reaking",
"Un9breaking",
"ME"]

x = 1
meancal = []

while True:
    if random.choice(enchants) == "ME":
        meancal.append(x)
        x = 0
        if len(meancal) == 1000000:
            break
    else:
        x+=1

print("mean amount of changes:", statistics.mean(meancal))
