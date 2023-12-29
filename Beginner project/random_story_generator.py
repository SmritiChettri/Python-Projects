# So to start with this project we are going to pick phrases randomly
import random

when = ["Once upon a time", "Yesterday", "A long time ago", "Last Night", "A few years ago"]
who = ["Zhongli", "Nahida", "Raiden Shogun", "Furina", "Venti", "Neuviellette", "An otter", "A dragon"]
where = ["Liyue", "Inazuma", "Mondstadt", "Fontaine", "Sumeru"]
what = ["darnk lots of Osmanthus Wine.", "tried to get hold the vison holders.", "tried to protect civilians.", "was too drunk to know anything."]
print(random.choice(when)+ ', ' + random.choice(who)+ ' who lived in ' +random.choice(where), random.choice(what))