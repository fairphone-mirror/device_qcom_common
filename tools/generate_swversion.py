from xml.dom.minidom import Document, Element
import sys, os

def ensure_directory_exists(filename):
    dir = os.path.dirname(filename)
    try:
        os.stat(dir)
    except:
        os.makedirs(dir)

def main(filename, version):
    doc = Document()
    root = doc.createElement('data')
    child = Element('parameter')
    child.setAttribute('version',version)
    root.appendChild(child)
    doc.appendChild(root)
    #doc.toprettyxml(encoding='utf-8',indent="  ")
    ensure_directory_exists(filename)
    f = open(filename, 'w')
    f.write(doc.toprettyxml(encoding='utf-8',indent="  "))
    f.close

if __name__ == "__main__":
    if len(sys.argv) != 3:
        exit()
    main(sys.argv[1], sys.argv[2])