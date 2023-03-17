import json
import requests

# flagList is a list of tuples with flag name and search value
def url(*flagList):
    url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula." \
          "IScript_ClassSearch?institution=UVA01"
    for item in flagList:
        url += "&" + item[0] + "=" + item[1]
    r = requests.get(url)
    classList = []
    for c in r.json():
        classList.append((c['descr']))
    return classList

def main():
    flagList = [("term", 1228)]
    url(flagList)

