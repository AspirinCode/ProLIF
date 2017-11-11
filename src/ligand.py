"""
   Copyright 2017 Cédric BOUYSSET

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from rdkit import Chem
import os.path

class Ligand:
	"""Class for a ligand"""
	def __init__(self, file):
		"""Initialize the ligand from a file"""
		fileExtension = os.path.splitext(file)[1]
		if fileExtension == '.pdb':
			self.structure = Chem.MolFromPDBFile(file, sanitize=True, removeHs=False)
		elif fileExtension == '.mol2':
			self.structure = Chem.MolFromMol2File(file, sanitize=True, removeHs=False)
		elif fileExtension == '.sdf':
			self.structure = Chem.SDMolSupplier(file, sanitize=True, removeHs=False)[0]