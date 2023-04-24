# lexoffice2umsatzsteuervoranmeldung

takes a lexoffice export and calculates your "umsatzsteuervoranmeldung" values that you need to enter in ELSTER
not at all official, I'm no tax guy, just scripted a youtube video for my own purposes.

lexoffice csv format: text/plain; charset=utf-16le

# how?

1. Head over to Lexoffice Export https://app.lexoffice.de/export/#/ 
2. Select the Date Range you have to submit to the government, in my case quarterly (Q1)
3. Export the "Listen im CSV-Format", under "weitere exporte"
4. This will download two csv files, move them into the "data" folder
5. (onetime) `pip install -r requirements.txt`
6. run `python ustva.py`

Will output something along the lines of 

```
-----
Einkünfte: 
Steuersatz 19 Prozent: Steuer    9786.65€
-----
Ausgaben
Steuersatz 19 Prozent: Steuer     268.93€
-----
total tax of revenue    9786.65€, total tax of expenses     268.93€, remainer of taxes:    9517.72€
this means you will have to pay    9517.72€ to the Finanzamt (no guarantee) :(
```