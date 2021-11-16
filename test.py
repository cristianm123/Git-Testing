import tqdm
import time

from tools.Cristian import addCristianToParty
from tools.Nini import addNiniToParty
from tools.Julian import addJulianToParty
from tools.Jonathan import addJonathanToParty
from tools.JuanDavid import addJuanDavidToParty
from tools.MaryAnn import addMaryAnnToParty
from tools.Mayra import addMayraToParty
from tools.JuanPablo import addJuanPabloToParty
from tools.Lady import addLadyToParty
from tools.Stephanie import addStephanieToParty
from tools.Wilson import addWilsonToParty
from tools.Diego import addDiegoToParty
from tools.Monica import addMonicaToParty
from tools.Jhonatan import addJhonatanToParty
from tools.Gamarra import addGamarraToParty

party = addNiniToParty(party)
party = addJulianToParty(party)
party = addJonathanToParty(party)
party = addJuanDavidToParty(party)
party = addMaryAnnToParty(party)
party = addMayraToParty(party)
party = addJuanPabloToParty(party)
party = addLadyToParty(party)
party = addStephanieToParty(party)
party = addWilsonToParty(party)
party = addDiegoToParty(party)
party = addMonicaToParty(party)
party = addJhonatanToParty(party)
party = addGamarraToParty(party)
party = addCristianToParty(party)

for x in tqdm.tqdm(party, position=0, leave=True):
    print("")
    print(x + " está entrando a la fiesta")
    time.sleep(2)

print(", ".join(party), "están en la fiesta")