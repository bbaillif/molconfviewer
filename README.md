# Mol Viewer

This is a simple package wrapping [py3dmol](https://github.com/avirshup/py3dmol) for a single command visualization of a RDKit molecule and its conformations (embed as Conformer objects in the Molecule)

## Installation

pip install molconfviewer

## Usage

```
from molconfviewer import MolConfViewer
mol_conf_viewer = MolConfViewer() 
mol_conf_viewer.view(mol=mol) # where mol is a rdkit mol
```

See the MolConfViewer object code to customize the visualization.
For more possibilities, please check py3dmol and 3dmol.js.
