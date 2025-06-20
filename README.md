# Corporate-Environmental-Impact
# Emissions-Intensitätsanalyse mit dem Impact-Weighted Accounts Dataset

## Ziel
Analyse der Treibhausgasintensität nach Branche und Unternehmen auf Basis der Scope-3-Daten von Harvard IWA.

## Download Dataset

https://ifvi.org/wp-content/uploads/2023/10/Scope-3-Environmental-Impact-Data-2022.xlsx 
alternativ: https://ifvi.org/impact-accounting-in-practice/resources/ -> Scope 3 Environmental Impact Data (2022)

## Allgemeine Information
Über 6.000 Unternehmen weltweit;
Etwa 50 Branchen (Industry);
Betrachtungszeitraum: 2018–2022;
Teilweise maschinell geschätzte Werte (Machine Learning basiert);
Emissionen in monetarisierter Form dargestellt (300 USD Umweltschadenskosten pro Tonne Emissionen)

Es gibt eine PDF Präsentation mit eingebetteten Abbildungen (Corporate_Environmental_Impact_Praesentation.pdf). Diese kann für einen Überblick heruntergeladen werden. 
Detaillierte Codes sind unter "notebooks" als ipynb Dateien zu finden.

## Fragestellungen 
- Welche Branchen verursachen die höchsten/niedrigsten Emissionen
- Wie Entwickeln sich die Emissionen im zeitlichen Verlauf der TOP Branchen?
- Welche Branchen sind am effizientesten? (Höchster Umsatz, bei niedrigsten Emissionen)


## Fazit: 
- leichter Emissions-Rückgang bei den emissionsstärksten Unternehmen zu beobachten (vermutlich auf stärkere Regulierungen und gesellschaftlichen Druck zurückzuführen)
- starke Schwankungen lassen sich durch geringe Anzahl an Unternehmen innerhalb der Branche erklären (teilweise gibt es nur Daten von nur 2 bis 10 Unternehmen pro Branche -> zwar sind zahlreiche Unternehmen gemeldet, jedoch sind die Branchenkategorien zu stark verzweigt)
- Höherer Umsatz geht tendenziell mit höheren Emissionen einher, spannend ist wie viele Emissionen pro USD Umsatz entstehen -> die Unternehmen mit niedrigeren Emissionen bei gleichem Umsatz sollten näher betrachtet werden, innerhalb der Branche miteinander vergleichen  
