import json
import requests
from .models import Course

# flagList is a list of tuples with flag name and search value

def url(flagList):
    url = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula." \
          "IScript_ClassSearch?institution=UVA01&term=1228"
    for item in flagList:
        url += "&" + item[0] + "=" + str(item[1])
    r = requests.get(url)
    classList = []
    for c in r.json():
        courseMnemonic = c['subject']
        courseNumber = c['catalog_nbr']
        courseTitle = c['descr']
        courseName = courseMnemonic + " " + courseNumber + ": " + courseTitle
        if courseName not in classList:

            c = Course(mnem = courseMnemonic, num = courseNumber, descr = courseTitle)
            c.save()
            classList.append(courseName)
    return classList

def main():

    for i in range(90):
        flagList = [("term", 1228), ("page", str(i))]
        list = url(flagList)
main()
