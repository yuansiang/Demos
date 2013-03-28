from xml.dom import minidom

xml = """<?xml version = "1.0" ?>
<ProductData>
    <Item Id = "P01">
        <Image>apple.jpg</Image>
        <Description>This an apple</Description>
</ProductData>
<ProductData>
    <Item Id = "P02">
        <Image>pear.jpg</Image>
        <Description>Hey</Description>
</ProductData>
"""

#get XML as text string
xml_data = minidom.parseString(xml).getElementsByTagName("ProductData")

#get all items
parts = xml_data[0].getElementsByTagName("Item")

#loop for all items
for part in parts:
    #get ID
    pid = part.attributes["Id"].value.strip()
    #get image
    image = part.getElementsByTagName("Image")[0].firstChild.nodeValue.strip
    #get description
    image = part.getElementsByTagName("Description")[0].firstChild.nodeValue.strip
    print(pid)
