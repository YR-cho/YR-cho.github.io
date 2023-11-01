#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from vina import Vina

v = Vina ()

v.set_receptor("Protein_Receptor.pdbqt")
v.set_ligand_from_file("./NPASS_3/NPC123.pdbqt")


v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])
v.dock(exhaustiveness=8)
v.write_poses("Docking_result.pdbqt")
