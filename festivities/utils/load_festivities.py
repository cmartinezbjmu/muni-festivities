import json
import datetime
import xml.etree.ElementTree as ET

class todict(dict):
  def __str__(self):
    return json.dumps(self)

def parseXML():
  """Parse XML with ElementTree."""

  tree = ET.ElementTree(file='../../static/files/festivities.xml')
  root = tree.getroot()
  users = root.getchildren()
  festivities = dict()
  print("[")
  for festivity_count,festivity in enumerate(users):
    festivity_children = festivity.getchildren()
    for festivity_child in festivity_children:
      if festivity_child.tag == "name":
        festivities["name"] = festivity_child.text
      if festivity_child.tag == "start":
        festivities["start_date"] = festivity_child.text
      if festivity_child.tag == "end":
        festivities["end_date"] = festivity_child.text
      if festivity_child.tag == "place":
        festivities["place"] = festivity_child.text
    festivities["created_at"] = str(datetime.datetime.now())
    festivities["updated_at"] = str(datetime.datetime.now())
    print(todict({"model": "festivities.Festivity", "fields": festivities}))
    if (festivity_count!=len(users)-1):
      print(",")
  print("]")

parseXML()