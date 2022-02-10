import unittest
from rdkit import Chem
from rdkit.Chem.rdDistGeom import EmbedMultipleConfs
from molconfviewer import MolConfViewer

class MolViewerTest(unittest.TestCase):
    
    # only works in Jupyter
    def test_view(self):
        mol = Chem.MolFromSmiles('c1ccccc1')
        EmbedMultipleConfs(mol)
        MolConfViewer().view(mol)