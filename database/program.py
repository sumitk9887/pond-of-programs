import sys
import inspect

"""
    AbstractProgram for building a custom program.

    To build a custom program for execution via the REST API:
        - Create a new .py file in ./database/.
        - Import 
"""

def programInfo(program_name):
    if program_name == '':
        return None
    pass

class AbstractProgram(object):
    """
        AbstractProgram
        Defaults:
            Inputs: 1 Integer
            Outputs: 1 Integer
    """
    
    PROGRAM_NAME = ''
    N_INPUTS = [int]
    N_OUTPUTS = [int]

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    @property
    def inputs(self):        
        """
            Get a dictionary containing information of type of 
            inputs and no of inputs required for the program.
        """
        return {
            'n': len(self.N_INPUTS),
            'types': self.N_INPUTS
        }
    @property
    def outputs(self):
        """
            Get a dictionary containing information of type of 
            ouputs and no of outputs required for the program.
        """
        return {
            'n': len(self.N_OUPUTS),
            'types': self.N_OUPUTS
        }

    def execute(self, *args, **kwargs):
        raise NotImplementedError
