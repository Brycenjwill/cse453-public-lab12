########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

# you may need to put something here...

# SECURITY_LEVELS dictionary
SECURITY_LEVELS = {
    'Public': 0,
    'Confidential': 1,
    'Privileged': 2,
    'Secret': 3
}
 
# USER_SECURITY_LEVELS dictionary
USER_SECURITY_LEVELS = {
    'AdmiralAbe': SECURITY_LEVELS['Secret'],
    'CaptainCharlie': SECURITY_LEVELS['Privileged'],
    'SeamanSam': SECURITY_LEVELS['Confidential'],
    'SeamanSue': SECURITY_LEVELS['Confidential'],
    'SeamanSly': SECURITY_LEVELS['Confidential'],
    'default': SECURITY_LEVELS['Public']
}

def readSecurityCondition(username, assetSecurityLevel):
    
    return USER_SECURITY_LEVELS[username] >= SECURITY_LEVELS[assetSecurityLevel]