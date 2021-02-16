[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
![GitHub package.json version](https://img.shields.io/github/package-json/v/iqb-berlin/mdc-educational-standards?style=flat-square)

# Metadaten-Katalog Bildungsstandards

Dieses Repository enthält die Metadatendefinitionen, die das IQB für Aufgaben und Items im Rahmen des [Nationalen Bildungsmonitorings](https://www.kmk.org/themen/qualitaetssicherung-in-schulen/bildungsmonitoring.html) verwendet. Es handelt sich dabei nur um die Metadatendefinitionen, die sich auf die [Bildungsstandards](https://www.iqb.hu-berlin.de/bista) bzw. auf die [Kompetenzstufen](https://www.iqb.hu-berlin.de/bista/ksm/) beziehen.

Die Syntax des Katalogs basiert auf dem [Metadaten-System des IQB](https://github.com/iqb-berlin/mdc-schemadefinition). Der Katalog ist referenzierbar über die DOI `10.5159/IQB_MDR_EDUSTD_v1` und enthält Verweise auf den [Kernkatalog des IQB](https://doi.org/10.5159/IQB_MDR_Core_v1).   

Für eine bessere Lesbarkeit dieses Katalogs bitte [hier](docs/catalog.md) klicken.

Die Programmierungen dieses Repos basieren auf node.js. Sie dienen der Validierung und Umformung der ursprünglichen XML in andere Zielformate: [Markdown zur besseren Lesbarkeit](docs/catalog.md) und Turtle zur Veröffentlichung als SKOS im Rahmen der Projekte der [KIM OER Metadatengruppe](https://wiki.dnb.de/display/DINIAGKIM/OER-Metadatengruppe) (in Vorbereitung).
