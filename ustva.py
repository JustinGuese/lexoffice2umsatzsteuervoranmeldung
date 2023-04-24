from glob import glob

import pandas as pd


def pctStr2Digit(pctstr):
    return int(pctstr.replace("%", ""))

def floatify(floatstr):
    return float(floatstr.replace(".", "").replace(",", "."))

allFiles = glob("data/*.csv")
allTaxes = dict()
assert len(allFiles) == 2, "you should only have two files in the data folder, please check"
for file in allFiles:
    incomeSheet = "Export_RA" in file
        # rechnungsausgang == income
    df = pd.read_csv(file, delimiter=";", encoding="utf-16le")
    # drop all rows which have "Keine" in "Steuer" column
    df = df[~df["Steuer"].str.contains("Keine")]
    # convert "Steuer" column to pure int
    df["Steuer"] = df["Steuer"].apply(pctStr2Digit)
    df["Steuer"] = df["Steuer"].astype(int)
    df["Steuerbetrag"] = df["Steuerbetrag"].apply(floatify)
    df["Steuerbetrag"] = df["Steuerbetrag"].astype(float)
    # groupy
    steuer_sums = df.groupby("Steuer")["Steuerbetrag"].sum()
    allTaxes["einnahmen" if incomeSheet else "ausgaben"] = steuer_sums.to_dict()

revenue = sum(allTaxes["einnahmen"].values())
expenses = sum(allTaxes["ausgaben"].values())
earnings = revenue - expenses
# e.g. {'einnahmen': {19: 9786.65}, 'ausgaben': {19: 268.93}}
collection = []
print("-----")
print("Einkünfte: ")
for taxval, euro in allTaxes["einnahmen"].items():
    print("Steuersatz %2d Prozent: Steuer %10.2f€" % (taxval, euro))
    collection.append([True, taxval, euro])
print("-----")
print("Ausgaben")
for taxval, euro in allTaxes["ausgaben"].items():
    print("Steuersatz %2d Prozent: Steuer %10.2f€" % (taxval, euro))
    collection.append([False, taxval, euro])
print("-----")
print("total tax of revenue %10.2f€, total tax of expenses %10.2f€, remainer of taxes: %10.2f€" % (revenue, expenses, earnings))
if earnings > 0:
    print("this means you will have to pay %10.2f€ to the Finanzamt (no guarantee) :(" % earnings)
else:
    print("yay! this means the Finanzamt will have to pay you %10.2f€ back! (no guarantee)" % (earnings))