import numpy as np
import math

####################

# Q u b i t s

###########################

# 2-qubit states

# | 0 } = [[ 1 ], = | 0  0 }
#          [ 0 ],
#          [ 0 ],
#          [ 0 ]]
state0 = np.array([[1, 0, 0, 0]])

#################################

# | 1 } = [[ 0 ], = | 0 1 }
#          [ 1 ],
#          [ 0 ],
#          [ 0 ]]
state1 = np.array([[0, 1, 0, 0]])

#################################

# | 2 } = [[ 0 ], = | 1 0 }
# #        [ 0 ]
#          [ 1 ]
#          [ 0 ]]
state2 = np.array([[0,0,1,0]])

#################################

# | 3 } = [[ 0 ], = | 1 1 }
# #        [ 0 ]
#          [ 0 ]
#          [ 1 ]]
state3 = np.array([[0,0,0,1]])

