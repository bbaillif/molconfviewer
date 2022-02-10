import ipywidgets
import py3Dmol

from ipywidgets import interact, fixed
from rdkit import Chem
from rdkit.Chem.rdchem import Mol
from typing import Tuple

class MolConfViewer():
    
    def __init__(self, 
                 widget_size: Tuple[int, int] = (300, 300), 
                 style: str = "stick", 
                 draw_surface: bool = False, 
                 opacity: float = 0.5):
        """Setup the viewer parameter
        Args:
            size: tuple(int, int), canvas size
            style: str, type of drawing molecule, see 3dmol.js
                   style can be 'line', 'stick', 'sphere', 'cartoon'
            surface: bool, display SAS
            opacity: float, opacity of surface, ranging from 0 to 1
        """
        self.widget_size = widget_size
        assert style in ('line', 'stick', 'sphere', 'cartoon')
        self.style = style
        self.draw_surface = draw_surface
        self.opacity = opacity
    
    def view(self, mol: Mol) :
        """View a RDKit molecule in 3D, with a slider to explore conformations
        Largely inspired from 
        https://birdlet.github.io/2019/10/02/py3dmol_example/
        Args:
            mol: rdMol, molecule to show
        Returns:
            Nothing, prints a jupyter widget to show the molecule
        """

        max_conf_id = mol.GetNumConformers() - 1
        conf_id_slider = ipywidgets.IntSlider(min=0, 
                                              max=max_conf_id, 
                                              step=1)
        interact(self.get_viewer, 
                 mol=fixed(mol), 
                 conf_id=conf_id_slider)
        
    def get_viewer(self, 
                    mol: Mol, 
                    conf_id: int = -1) -> py3Dmol.view:
        """Draw a given conformation for a molecule in 3D
        Args:
            mol: Mol, molecule to show
            conf_id: int, id of the RDKit Conformer in the Mol to visualize
        Returns:
            viewer: py3Dmol.view, a class for constructing embedded 3Dmol.js
                views in Jupyter.
        """
        
        mblock = Chem.MolToMolBlock(mol, confId=conf_id)
        viewer = py3Dmol.view(width=self.widget_size[0], 
                              height=self.widget_size[1])
        viewer.addModel(mblock, 'mol')
        viewer.setStyle({self.style:{}})
        if self.draw_surface:
            viewer.addSurface(py3Dmol.SAS, {'opacity': self.opacity})
        viewer.zoomTo()
        return viewer