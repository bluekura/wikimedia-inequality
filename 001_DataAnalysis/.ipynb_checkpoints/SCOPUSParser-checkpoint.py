from __future__ import print_function
import sys
import xmltodict
import lxml.html
from xml.parsers.expat import ExpatError

def getTargetitem(sourcedict, itemlist):
    # input hierarchically as (level1.level2.level3...)
    cur_item = sourcedict
    for i in itemlist:
        if(not isinstance(cur_item, dict)):
            break
        cur_item = cur_item.setdefault(i, "ERR")
    if(cur_item == None):
        return "ERR"
    return cur_item

def getPubdate(sourcedict):
    # Get publication dates from the data
    PubDate = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 'source', 'publicationdate', 'year'])
    if(PubDate == "ERR"):
        PubDate = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 'source', 'publicationdate', 'year'])
    if(PubDate == "ERR"): 
        PubDate = getTargetitem(sourcedict, ['xocs:doc', 'xocs:meta', 'xocs:sort-year'])     
    return PubDate

def getEID(sourcedict):
    EID = getTargetitem(sourcedict, ['xocs:doc', 'xocs:meta', 'xocs:eid'])
    return EID

def getSrcID(sourcedict):
    SrcID = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 'source', '@srcid'])
    return SrcID

def getSrcTitle(sourcedict):
    SrcTitle = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 'source', 'sourcetitle'])
    return SrcTitle

def getSrcISSN(sourcedict, isPrinted):
    ISSN = ""
    if(isPrinted):
        listISSN = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 'source', 'issn'])
        if(isinstance(listISSN, list)):
            for vals in listISSN:
                if(vals.setdefault("@type", "###ERRMSG###") == "print"):
                    ISSN = vals.get("#text")
        elif(isinstance(listISSN, dict)):
            ISSN = listISSN.get("#text")
        else:
            pass 
         
    else:
        listISSN = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 'source', 'issn'])
        if(isinstance(listISSN, list)):
            for vals in listISSN:
                if(vals.setdefault("@type", "###ERRMSG###") == "electronic"):
                    ISSN = vals.get("#text")
        elif(isinstance(listISSN, dict)):
            ISSN = listISSN.get("#text")
        else:
            pass
    if(ISSN == "ERR"):
        return ""
    else:
        return ISSN

def getASJC(sourcedict):
    allTempcode = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head',
                                           'enhancement', 'classificationgroup', 'classifications'])
    if(allTempcode == "ERR"):
        ASJC = "-"
    elif(isinstance(allTempcode, list)):
        allCode = {}
        for i in allTempcode:
            allCode[i['@type']] = i['classification']
            ASJC = allCode.setdefault('ASJC', '-')
            if(isinstance(ASJC, list)):
                ASJC = ";".join(ASJC)
    else:
        Cur = allTempcode.setdefault('ASJC', '-')
        if(Cur == '-'):
            ASJC = "-"
        elif(isinstance(Cur, list)):
            ASJC = "::".join(Cur)
        else:
            ASJC = Cur
    return ASJC

def getMESH(sourcedict):
    allTempcode = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head',
                                           'enhancement', 'descriptorgroup', 'descriptors'])
    if(allTempcode == "ERR"):
        MESH = "-"
    elif(isinstance(allTempcode, list)):
        allTerm = {}
        for i in allTempcode:
            allTerm[i['@type']] = i['descriptor']
        Cur = allTerm.setdefault('MSH', '-')
        if(Cur == '-'):
            MESH = "-"
        elif(isinstance(Cur, list)):
            MESH = ":::".join([x['mainterm']['#text'] for x in Cur])
        else:
            MESH = Cur['mainterm']['#text']
    else:
        Cur = allTempcode.setdefault('MSH', '-')
        if(Cur == '-'):
            MESH = "-"
        elif(isinstance(Cur, list)):
            MESH = ":::".join([x['mainterm']['#text'] for x in Cur])
        else:
            MESH = Cur['mainterm']['#text']

def getTitle(sourcedict):
    TitleList = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head', 
                                          'citation-title', 'titletext', '#text'])
    if(isinstance(TitleList, unicode) or isinstance(TitleList, str)):
         return getStripTitle(TitleList)
    elif(isinstance(TitleList, list)):
        for val in TitleList:
            if(val.get('@original') == 'y'):
                return getStripTitle(val['#text'])
    else:
        return ""

def getStripTitle(orgtitle):
    nowtitle = orgtitle.lower().strip()
    filteredtitle = "".join([x for x in nowtitle if x.isalpha() or x.isnumeric() or x.isspace()])
    return filteredtitle

def getRegauthorkey(AuthorKeys):
    joinAuthorKey = ""
    NewList = []
    if(isinstance(AuthorKeys, list)):
        for i in range(len(AuthorKeys)):
            if(isinstance(AuthorKeys[i], dict)):
                if("#text" in AuthorKeys[i]):
                    NewList.append(getRegtext(AuthorKeys[i]['#text']))
                else:
                    pass
            else:
                NewList.append(AuthorKeys[i])
        joinAuthorKey = ":::".join([x for x in NewList if x is not None])
    elif(isinstance(AuthorKeys, str)):
        if(AuthorKeys=="ERR"):
            joinAuthorKey == ""
        else:
            joinAuthorKey == getRegtext(AuthorKeys)
    if(joinAuthorKey is not None):
        return joinAuthorKey.encode('utf8')
    else:
        return ""

def getRegtext(text):
    return " ".join("".join(text.splitlines()).split())

def getRegtitle(title):
    ArticleTitle = ""
    if(isinstance(title, list)):
        for i in title:
            if(i['@original'] == "y"):
                ArticleTitle = getRegtext(i["#text"])
    elif(title == "ERR"):
        ArticleTitles == ""
    else:
        ArticleTitle = getRegtext(title["#text"])
    return ArticleTitle.encode('utf8')


def getAuthorcoun(sourcedict):  
    GroupList = getTargetitem(sourcedict, ['xocs:doc', 'xocs:item', 'item', 'bibrecord', 'head',
                                          'author-group'])
    ResDict = []
    if(isinstance(GroupList, list)):
        for SubList in GroupList:
            AuidList = getTargetitem(SubList, ['author', '@auid'])
            AfCountry = getTargetitem(SubList, ['affiliation', '@country'])
            if(isinstance(AuidList, str) or isinstance(AuidList, unicode)):
                ResDict.append([AuidList, AfCountry])
            else:
                for auid in AuidList:
                    cur_auid = auid.setdefault('@auid', 'ERR')
                    ResDict.append([cur_auid, AfCountry])
    else:
        AuidList = getTargetitem(GroupList, ['author', '@auid'])
        AfCountry = getTargetitem(GroupList, ['affiliation', '@country'])
        if(isinstance(AuidList, str) or isinstance(AuidList, unicode)):
            ResDict.append([AuidList, AfCountry])
        else:
            for auid in AuidList:
                cur_auid = auid.setdefault('@auid', 'ERR')
                ResDict.append([cur_auid, AfCountry])
     
    return ResDict 

def openXml(xmlstring):
    try:
        tempdict = xmltodict.parse(xmlstring)
    except ExpatError as e:
        xmlstring = fixBadxml(xmlstring)
        tempdict = xmltodict.parse(xmlstring)
    return tempdict

def fixBadxml(xmlstring):
    try:
        lx = lxml.html.fromstring(xmlstring)
    except Exception as e:
        return "<xocs:doc><error>badxml</error></xocs:doc>"
    fixed = lxml.html.tostring(lx, method='xml')
    return fixed

if(__name__ == "__main__"):
    xmlbuffer = ""
    count = 0
    print('\'eid\'', '\'pubdate\'', '\'auid\'', '\'af_country\'', sep = "\t")
    for line in sys.stdin:
        lines = line.split("<?xml")
        xmlbuffer += lines[0]
        if(line.find("</xocs:doc") >= 0):
            tempdict = openXml(xmlbuffer)
            EID = getEID(tempdict)
            PubDate = getPubdate(tempdict)
            AuthorCountries = getAuthorcoun(tempdict)
            uniqAuthorCountries = [list(x) for x in set(tuple(x) for x in AuthorCountries)]
            for row in uniqAuthorCountries:
                print(EID, PubDate, row[0], row[1].upper(), sep = "\t")
            xmlbuffer = ""
