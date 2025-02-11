# velodvie

Data viz pour les données employeurs de Vélo d'Vie à Cognac

## Données d'entrée

Liste de lieux de travail (nom + adresse précise), et pour chaque lieu de travail, liste d'adresses (nom de la rue uniquement) des employé⋅es.

## Données extraites

Pour chaque lieu de travail :
- distances domicile-travail, à vol d'oiseau et à vélo (via un itinéraire Google Maps)
- superpositions des itinéraires sous forme de heatmap, pour identifier visuellement les axes critiques

## Utilisation

```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 test_render.py
```

## TODO

- visualisation de la répartition des distances (histogrammes ?)
- affinage des options de la heatmap, potentiellement à faire varier en fonction du nombre d'adresses récupérées
