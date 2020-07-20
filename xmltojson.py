import lxml.etree as xml

def parse(element):
    result = dict()

    if((type(element) != type(tuple()))):
        for item in element.items():
            if((type(result.get(str("@" + xml.QName(item[0]).localname).strip())) == type(None))):
                result[str("@" + xml.QName(item[0]).localname).strip()] = dict()
            if((type(item) != type(None))):
                result.get(str("@" + xml.QName(item[0]).localname).strip()).update(parse(item))
    if((type(element) != type(None))):
        if((type(element) != type(tuple()))):
            if((type(result.get(str("#" + "name").strip())) == type(None))):
                result[str("#" + "name").strip()] = str()
            if((type(xml.QName(element.tag).localname) != type(None))):
                result[str("#" + "name").strip()] += str(xml.QName(element.tag).localname).strip()
            if((type(result.get(str("#" + "text").strip())) == type(None))):
                result[str("#" + "text").strip()] = str()
            if((type(element.text) != type(None))):
                result[str("#" + "text").strip()] += str(element.text).strip()
            if((type(element.tail) != type(None))):
                result[str("#" + "text").strip()] += str(element.tail).strip()
            if((type(result.get(str("#" + "xmlns").strip())) == type(None))):
                result[str("#" + "xmlns").strip()] = str()
            if((type(xml.QName(element.tag).namespace) != type(None))):
                result[str("#" + "xmlns").strip()] += str(xml.QName(element.tag).namespace).strip()
        else:
            if((type(result.get(str("#" + "name").strip())) == type(None))):
                result[str("#" + "name").strip()] = str()
            if((type(xml.QName(element[0]).localname) != type(None))):
                result[str("#" + "name").strip()] += str(xml.QName(element[0]).localname).strip()
            if((type(result.get(str("#" + "text").strip())) == type(None))):
                result[str("#" + "text").strip()] = str()
            if((type(element[1]) != type(None))):
                result[str("#" + "text").strip()] += str(element[1]).strip()
            if((type(element[1]) != type(None))):
                result[str("#" + "text").strip()] += str(          ).strip()
            if((type(result.get(str("#" + "xmlns").strip())) == type(None))):
                result[str("#" + "xmlns").strip()] = str()
            if((type(xml.QName(element[0]).namespace) != type(None))):
                result[str("#" + "xmlns").strip()] += str(xml.QName(element[0]).namespace).strip()
    if((type(element) != type(tuple()))):
        for item in element.getchildren():
            if((type(result.get(str(" " + xml.QName(item.tag).localname).strip())) == type(None))):
                result[str(" " + xml.QName(item.tag).localname).strip()] = list()
            if((type(item) != type(None))):
                result.get(str(" " + xml.QName(item.tag).localname).strip()).append(parse(item))

    return(result)


def main():
    print(parse(xml.fromstring(open("d:/export.xml", "rb").read())))

    return


if((__name__ == "__main__")):
    main()
