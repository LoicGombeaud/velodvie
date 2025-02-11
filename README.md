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

## Exemples

Sur des données factices :
![image](https://github.com/user-attachments/assets/913c2ff8-f860-43e6-aacc-23646874e11c)
![image](https://github.com/user-attachments/assets/8caf7671-c920-4531-bb52-a04f87b5d4fb)


## TODO

- visualisation de la répartition des distances (histogrammes ?)
- affinage des options de la heatmap, potentiellement à faire varier en fonction du nombre d'adresses récupérées et/ou mise en place d'un bouton/slider pour modifier les options en live sur la page HTML
- mise en place de persistence/cache pour éviter les appels répétés à Google Maps ($0,005 / appel API, mais $200 offerts par mois, à ne pas dépasser)
