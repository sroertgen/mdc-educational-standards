from collections import namedtuple

from lxml import etree
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, SKOS
from pathlib import Path

ConceptScheme = namedtuple("ConceptScheme", ["conceptScheme", "concepts"])
SchemeData = namedtuple("SchemeData", ["id", "label", "definition"])
LangString = namedtuple("LangString", ["value", "lang"])

output_folder = Path("./data")
if not output_folder.exists():
    output_folder.mkdir()

def getValues(entry):
    if entry is not None:
        lang = entry.get("{http://www.w3.org/XML/1998/namespace}lang")
        value = entry.text
        return LangString(value, lang)
    else:
        return 

def parseXml():
    tree = etree.parse("mdc-educational-standards.xml")
    md_lists = tree.xpath("//MDDef")

    conceptSchemes = []
    # get labels and values
    for item in md_lists:
        # get concept scheme id
        _id = str(item.get("id"))
        # get label
        label = getValues(item.find("Label"))
        definition = getValues(item.find("Description"))
        # get values
        # <Value id="1"><Label xml:lang="de">K1</Label><Description xml:lang="de">Mathematisch argumentieren</Description></Value>
        conceptScheme = SchemeData(_id, label, definition)

        values = item.findall("Value")
        concepts = []
        for value in values:
            _id = str(value.get("id"))
            label = getValues(value.find("Label"))
            definition = getValues(value.find("Description"))
            concepts.append(SchemeData(_id, label, definition))
        conceptSchemes.append(ConceptScheme(conceptScheme=conceptScheme, concepts=concepts))

    return conceptSchemes


def buildGraph(cs):
    conceptScheme = cs.conceptScheme
    concepts = cs.concepts

    g = Graph()
    base_url = URIRef("http://example.org/iqb/cs_" + conceptScheme.id + "/")
    
    g.add((base_url, RDF.type, SKOS.ConceptScheme))
    g.add((base_url, DCTERMS.title, Literal(conceptScheme.label.value, lang=conceptScheme.label.lang )))

    for concept in concepts:
        concept_url = base_url + concept.id
        g.add((concept_url, RDF.type, SKOS.Concept))
        g.add((concept_url, SKOS.prefLabel, Literal(concept.label.value, lang=concept.label.lang)))
        if concept.definition:
            g.add((concept_url, SKOS.definition, Literal(concept.definition.value, lang=concept.definition.lang)))
        # add topConceptOf
        g.add((concept_url, SKOS.topConceptOf, base_url))
        g.add((base_url, SKOS.hasTopConcept, concept_url))
    
    g.bind("skos", SKOS)
    g.bind("dct", DCTERMS)

    outfile_path = output_folder / ("iqb_cs" + conceptScheme.id + ".ttl")
    g.serialize(str(outfile_path), format="turtle", base=base_url, encoding="utf-8")

conceptSchemes = parseXml()

for item in conceptSchemes:
    buildGraph(item)
