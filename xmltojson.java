package event.xml2json;

import org.w3c.dom.*;
import java.util.*;
import javax.xml.parsers.*;

public class XmlJson extends Object {

    private static Map<String, Object> XmlToJson(Node doc) {
        Integer i;
        Map<String, Object> result;

        result = new HashMap<>();

        if ((doc != null)) {
            if ((doc.hasChildNodes())) {
                for (i = 0; i != doc.getChildNodes().getLength(); i += 1) {
                    if ((doc.getChildNodes().item(i).getNodeType() == Node.ELEMENT_NODE)) {
                        if ((!(result.containsKey("" + doc.getChildNodes().item(i).getLocalName())))) {
                            result.put("" + doc.getChildNodes().item(i).getLocalName(), new ArrayList<>());
                        }
                        if ((doc.getChildNodes().item(i) != null)) {
                            ((List) (result.get("" + doc.getChildNodes().item(i).getLocalName()))).add(XmlJson.XmlToJson(doc.getChildNodes().item(i)));
                        }
                    }
                }
            }
            if ((doc.getNodeType() == Node.ELEMENT_NODE)) {
                if ((!(result.containsKey("#" + "name")))) {
                    result.put("#" + "name", "");
                }
                if ((doc.getLocalName() != null)) {
                    result.replace("#" + "name", doc.getLocalName().trim());
                }
                if ((!(result.containsKey("#" + "text")))) {
                    result.put("#" + "text", "");
                }
                if ((doc.getFirstChild() != null)) {
                    result.replace("#" + "text", doc.getFirstChild().getNodeValue().trim());
                }
                if ((!(result.containsKey("#" + "xmlns")))) {
                    result.put("#" + "xmlns", "");
                }
                if ((doc.getNamespaceURI() != null)) {
                    result.replace("#" + "xmlns", doc.getNamespaceURI().trim());
                }
            }
            if ((doc.getNodeType() == Node.ATTRIBUTE_NODE)) {
                if ((!(result.containsKey("#" + "name")))) {
                    result.put("#" + "name", "");
                }
                if ((doc.getLocalName() != null)) {
                    result.replace("#" + "name", doc.getLocalName().trim());
                }
                if ((!(result.containsKey("#" + "text")))) {
                    result.put("#" + "text", "");
                }
                if ((doc.getNodeValue() != null)) {
                    result.replace("#" + "text", doc.getNodeValue().trim());
                }
                if ((!(result.containsKey("#" + "xmlns")))) {
                    result.put("#" + "xmlns", "");
                }
                if ((doc.getNamespaceURI() != null)) {
                    result.replace("#" + "xmlns", doc.getNamespaceURI().trim());
                }
            }
            if ((doc.hasAttributes())) {
                for (i = 0; i != doc.getAttributes().getLength(); i += 1) {
                    if ((doc.getAttributes().item(i).getNodeType() == Node.ATTRIBUTE_NODE)) {
                        if ((!(result.containsKey("@" + doc.getAttributes().item(i).getLocalName())))) {
                            result.put("@" + doc.getAttributes().item(i).getLocalName(), new HashMap<>());
                        }
                        if ((doc.getAttributes().item(i) != null)) {
                            ((Map) (result.get("@" + doc.getAttributes().item(i).getLocalName()))).putAll(XmlJson.XmlToJson(doc.getAttributes().item(i)));
                        }
                    }
                }
            }
        }

        return (result);
    }

    public static void main(String[] args) throws Throwable {
        DocumentBuilderFactory fuck;
        fuck = DocumentBuilderFactory.newInstance();
        fuck.setNamespaceAware(true);

        System.out.println(((Map) (((Map) (((List) (((Map) (((List) (XmlJson.XmlToJson(fuck.newDocumentBuilder().parse("d:/export.xml").getDocumentElement()).get("files"))).get(0))).get("file"))).get(0))).get("@name"))).get("#text"));

        return;
    }
}
