# valorant.py provides some powerful helper functions
# for filtering data from the API. These snippets cover
# both simple and advanced use cases.

import os
import valorant

from valorant.query import exp

KEY = os.environ["VALPY-KEY"]
client = valorant.Client(KEY, locale=None)

# Find the Phantom among the list of weapons.
# `.find` is an alias for `.get`, provided for semantics.
test = client.get_user("2356676jE87TjzCOtE-uo-ckphx8WerDSydy3GxClpAih4dVdoyrXoutht66k8BGrdNMpigxNADHA").matchlist()

print("Match List: ", test)
