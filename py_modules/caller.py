import sys
import os

# pipeline modules are using relative importing
# so using sys.path hack here
from ecephys_spike_sorting import scripts
sys.path.append(os.path.dirname(scripts.__file__))

# import createInputJson for pipeline config
# this way users can see function args by py.help in matlab
from ecephys_spike_sorting.scripts.create_input_json import createInputJson

def call_helper():
    """
        TODO - Calling ecephys_spike_sorting.scripts.helpers.*
    """
    print("call_helper")