# Data
Dans le dossier debug il y a un `script.py` qui permet de parser le dataset (un geojson valide), et d'extraire les features dans un fichier `data/data.json`.
ce script, va créer le `data/data.json` qui est le fichier **incorrect** (mais trompe l'oeil lors de la présentation).

Il créé aussi un fichier correct_data.json qui sera utilisé à l'étape 5 avec pydantic (celui là ne crachera pas).
