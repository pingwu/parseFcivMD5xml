#!/usr/bin/python
"""
  This script will open Microsoft fciv genreated XML file, parse it then print the hexadecimal hash values 
    that are stored in base64 encoded format.
  Usage 
     rsyMD5xml.py [MD5.xml]
"""
from sys import stdin,stderr
import sys
from os import isatty
from binascii import a2b_base64,hexlify
from xml.dom.minidom import parse, parseString

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def handleMD5XML(dom) :
    handleFCIV(dom.getElementsByTagName("FCIV")[0])


def handleFCIV(fciv):
    handleFILE_ENTRY(fciv.getElementsByTagName("FILE_ENTRY"))
     

def handleFILE_ENTRY(files) :
    for f in files :
        name=handlename(f.getElementsByTagName("name")[0])
        md5=handleMD5(f.getElementsByTagName("MD5")[0])
  
        print "%s  %s" % (md5,name)

def handlename(name):
    return getText(name.childNodes)

def handleMD5(MD5):
    md5_base64=getText(MD5.childNodes)
    return hexlify(a2b_base64(md5_base64)) #"UTF-8" out put

def main(argv=sys.argv):

    if len(sys.argv) < 2:
        print __doc__
        sys.exit(2)

    xml_file = sys.argv[1] # auth or revoke

    dome1 = parse(xml_file)

    handleMD5XML(dome1)


if __name__=="__main__":
    sys.exit(main())

