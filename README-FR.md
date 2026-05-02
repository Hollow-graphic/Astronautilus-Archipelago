## Installation

1. Récupère la fichier core de la dernière version sur https://github.com/dead-cells-core-modding/core
2. Extrait le dans le dossier du jeu
3. Récupère le archipelago mod zip de la dernière version sur [DeadCellsArchipelago](https://github.com/Maxlamenace572/DeadCellsArchipelago)
4. Extraite le mods.zip dans le dossier coremod

La structure de ton fichier doit ressembler à si dessous
```txt
<DeadCellsGameRoot>
|
+- coremod
|  |
|  +- core
|  |  |
|  |  +- native
|  |  |  |
|  |  |  +- ...
|  |  |
|  |  +- mdk
|  |  |	 |
|  |  |  +- install.ps1
|  |  |  |
|  |  |  +- uninstall.ps1
|  |  |  |
|  |  |  +- ...
|  |  |
|  |  +- host
|  |  |  |
|  |  |  +- startup
|  |  |  |  |
|  |  |  |  +- DeadCellsModding.exe
|  |  |  |  |
|  |  |  |  +- ...
|  |  |  +- ...
|  |  +- ...
|  +- ...
|
+- deadcells.exe
|
+- deadcells_gl.exe
|
+- ...
```