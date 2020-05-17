#Program to implement simple XML parsing
import xml.etree.ElementTree as ET

data = '''<person>
     <name>Chuck</name>
     <phone type="intl">
     +1 947 1456 345
     </phone>
     <email hide="yes"/>
     </person>  '''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))