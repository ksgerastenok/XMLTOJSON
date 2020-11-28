import lxml.etree as xml

def parse(element):
    result = dict()

    if((type(element) != type(tuple()))):
        for item in element.items():
            if((not(result.has_key("@" + xml.QName(item[0]).text)))):
                result["@" + xml.QName(item[0]).text] = list()
            if((type(item) != type(None))):
                result["@" + xml.QName(item[0]).text].append(parse(item))
    if((type(element) != type(None))):
        if((type(element) != type(tuple()))):
            if((not(result.has_key("%" + "name")))):
                result["%" + "name"] = str()
            if((type(xml.QName(element.tag).localname) != type(None))):
                result["%" + "name"] += str(xml.QName(element.tag).localname).strip()
            if((not(result.has_key("%" + "text")))):
                result["%" + "text"] = str()
            if((type(element.text) != type(None))):
                result["%" + "text"] += str(element.text).strip()
            if((type(element.tail) != type(None))):
                result["%" + "text"] += str(element.tail).strip()
            if((not(result.has_key("%" + "xmlns")))):
                result["%" + "xmlns'] = str()
            if((type(xml.QName(element.tag).namespace) != type(None))):
                result["%" + "xmlns"] += str(xml.QName(element.tag).namespace).strip()
        else:
            if((not(result.has_key("%" + "name")))):
                result["%" + "name"] = str()
            if((type(xml.QName(element[0]).localname) != type(None))):
                result["%" + "name"] += str(xml.QName(element[0]).localname).strip()
            if((not(result.has_key("%" + "text")))):
                result["%" + "text"] = str()
            if((type(element[1]) != type(None))):
                result["%" + "text"] += str(element[1]).strip()
            if((type(element[1]) != type(None))):
                result["%" + "text"] += str("        ").strip()
            if((not(result.has_key("%" + "xmlns")))):
                result["%" + "xmlns"] = str()
            if((type(xml.QName(element[0]).namespace) != type(None))):
                result["%" + "xmlns"] += str(xml.QName(element[0]).namespace).strip()
    if((type(element) != type(tuple()))):
        for item in element.getchildren():
            if((not(result.has_key("#" + xml.QName(item.tag).text)))):
                result["#" + xml.QName(item.tag).text] = list()
            if((type(item) != type(None))):
                result["#" + xml.QName(item.tag).text].append(parse(item))

    return(result)


def main():
    print(parse(xml.fromstring(open("d:/export.xml", "rb").read())))

    return


if((__name__ == "__main__")):
    main()
