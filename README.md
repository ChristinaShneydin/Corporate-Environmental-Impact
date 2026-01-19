# Corporate-Environmental-Impact Analysis
# Emissions-Intensitätsanalyse mit dem Impact-Weighted Accounts Dataset

## Projektüberblick

Dieses Projekt analysiert Umweltkennzahlen von Unternehmen, um sektorale Emissionstrends sichtbar zu machen und vergleichbar aufzubereiten. Ziel ist es, den umfangreichen Datensatz zu strukturieren, auszuwerten und in verständlicher Form zu visualisieren, sodass er als Grundlage für Berichte und Entscheidungsprozesse genutzt werden können.

Der Fokus liegt auf der Kombination aus Datenaufbereitung, Analyse und nachvollziehbarer Ergebnisdarstellung.

## Allgemeine Information

Über 6.000 Unternehmen weltweit;
Etwa 50 Branchen (Industry);
Betrachtungszeitraum: 2018–2022;
Teilweise maschinell geschätzte Werte (Machine Learning basiert);
Emissionen in monetarisierter Form dargestellt (300 USD Umweltschadenskosten pro Tonne Emissionen)

## Zielsetzung

Analyse der Treibhausgasintensität nach Branche und Unternehmen auf Basis der Scope-3-Daten von Harvard IWA;
Visualisierung der Ergebnisse für Berichts- und Präsentationszwecke 

## Fragestellungen 

- Welche Branchen verursachen die höchsten/niedrigsten Emissionen
- Wie Entwickeln sich die Emissionen im zeitlichen Verlauf der TOP Branchen?
- Welche Branchen sind am effizientesten? (Höchster Umsatz, bei niedrigsten Emissionen)

## Verwendete Technologien

- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn
- HTML für Visualisierungsexporte

## Workflow

1. Import und Sichtung der Rohdaten  
2. Datenbereinigung und Vereinheitlichung von Formaten  
3. Explorative Datenanalyse zur Identifikation relevanter Muster  
4. Berechnung zentraler Kennzahlen nach Branche und Unternehmen  
5. Erstellung von Visualisierungen zur Ergebnisdarstellung  
6. Export der Ergebnisse für Weiterverwendung in Berichten

Alle Schritte sind in den Notebooks dokumentiert und reproduzierbar.

## Download Dataset

https://ifvi.org/wp-content/uploads/2023/10/Scope-3-Environmental-Impact-Data-2022.xlsx 
alternativ: https://ifvi.org/impact-accounting-in-practice/resources/ -> Scope 3 Environmental Impact Data (2022)


## Fazit: 

Die Analyse zeigt Unterschiede in Emissionsintensitäten zwischen Branchen sowie Entwicklungstrends über Zeiträume hinweg. Die Visualisierungen ermöglichen einen schnellen Überblick und können für Präsentationen oder Reporting-Zwecke weiterverwendet werden.

Es gibt eine PDF Präsentation mit eingebetteten Abbildungen (Corporate_Environmental_Impact_Praesentation.pdf). Diese kann für einen Überblick heruntergeladen werden. 
(Detaillierte Codes sind unter "notebooks" als ipynb Dateien zu finden.)

Ableitungen:
- leichter Emissions-Rückgang bei den emissionsstärksten Unternehmen zu beobachten (vermutlich auf stärkere Regulierungen und gesellschaftlichen Druck zurückzuführen)
- starke Schwankungen lassen sich durch geringe Anzahl an Unternehmen innerhalb der Branche erklären (teilweise gibt es nur Daten von nur 2 bis 10 Unternehmen pro Branche -> zwar sind zahlreiche Unternehmen gemeldet, jedoch sind die Branchenkategorien zu stark verzweigt)
- Höherer Umsatz geht tendenziell mit höheren Emissionen einher, spannend ist wie viele Emissionen pro USD Umsatz entstehen -> die Unternehmen mit niedrigeren Emissionen bei gleichem Umsatz sollten näher betrachtet werden, innerhalb der Branche miteinander vergleichen  
