# XML to JSON converter.
Project in this repository converts XML to its corresponding representation in Java and Python.
In Java corresponding representation is similar to XMLSlurper in Groovy.
With such converter it is quite easily to navigate in XML:
- attributes could be accessed as "@ + attribute name"
- nodes could be accessed as "node name"
There is some special names:
- #text - the text value of current node
- #xmlns - the namespace of current node
- #name - the local name of current node

Example is shown in corresponding Java or Python source.
