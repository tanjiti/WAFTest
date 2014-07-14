#! /usr/bin/env python 
# For Windows do a set path=%path%;C:\python27 to run properly (if not already done)

__version__ = "1.9.1"
__author__ = "Gerasimos Kassaras e-mail:g.kassaras@gmail.com"
__copyright__ = "Copyright(C) 2012 Gerasimos Kassaras (also known as lamehacker or rekcahemal Free Industries)"
__license__ = "GNU GPL v2"

# -*- coding: iso-8859-15 -*-

# Importing libraries
import urllib
import base64
import os
import re
import time
import sys

# ------------------------------------ Paths -----------------------------------------------------------

CD = os.getcwd()

CharPath = CD + "/CharContainer/"

# ------------------------------------ CharContainer ----------------------------------------------------

postfixFile = CharPath +"postfix_Container.lst"
fillerFile = CharPath +"space_Filler_Container.lst"
suffixFile = CharPath +"suffix_Container.lst"
sqlKeywordFile = CharPath + "sql_Keyword_Container.lst"

# ------------------------------------ Global time variables ---------------------------------------------

global tsleep 

tsleep = 3

# ------------------------------------ Print banner ------------------------------------------------------

def printBanner():
   
 print(' I am handsome turtle...')
 print('                                       ___-------___')
 print('                                   _-~~             ~~-_')
 print('                               _-~                    /~-_')
 print('             /^\__/^\         /~  \                   /    \'')
 print('           /|  O|| O|        /      \_______________/        \'')
 print('          | |___||__|      /       /                \          \'')
 print('          |          \    /      /                    \          \'')
 print('          |   (_______) /______/                        \_________ \'')
 print('          |         / /         \                      /            \'')
 print('           \         \^\\         \                  /               \     /')
 print('             \         ||           \______________/      _-_       //\__//')
 print('               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/')
 print('                 ~-----||====/~     |==================|       |/~~~~~')
 print('                  (_(__/  ./     /                    \_\      \.')
 print('                         (_(___/                         \_____)_)')
 print("------------------------------------------------------------------------------\n")
 print(" Author: rekcahemal Free Industries")
 print(" Feedback/Bugs : g.kassaras@gmail.com")
 print(" Blog : http://blog.elusivethoughts.org")
 print(" Twitter: @lamehacker")
 print("------------------------------------------------------------------------------\n")

#########################################################################################################
##                                      Exit functions
#########################################################################################################

def exitScript():
 
    print("Now fuzz an application...")

    sys.exit(0)
      
#########################################################################################################
##                                      Check functions
#########################################################################################################

def checkFileExitstance(_filename) :
    
 try:

    open(_filename)

    return True

 except:

    printFileDoesNotExist()

    return False

#----------------------------------------------------------------------------------------

def checkDirectoryExitstance() :
 
 if (os.path.isdir(CharPath)):

    return True

 else:

    printDirectoryDoesNotExist()

    return False

#########################################################################################################
##                                      Print functions
#########################################################################################################

def printEnter():

    print("\n")

#----------------------------------------------------------------------------------------

def printCleanUpMessage():

    print("Database has been cleaned up...\n")

#----------------------------------------------------------------------------------------

def printFileDoesNotExist():

    print("File does not exist please try gain...\n")

#----------------------------------------------------------------------------------------

def printDirectoryDoesNotExist():

    print("Directory CharContainer does not exist or you are in the wrong directory path\n")

#----------------------------------------------------------------------------------------

def printUsageMessage():

    print("Usage: Type a single option then press enter type filename press enter again for help type help for the turtle type ban!")

#----------------------------------------------------------------------------------------

def printErrorMessage():
    
    print("Invalid argumantes were provided, please try again....\n")

#----------------------------------------------------------------------------------------
 
def printVersion():
    
    print ("::::::: Teenage Mutant Turtles version is 1.9.1 :::::::")

#----------------------------------------------------------------------------------------

def printFinishMessage():
    
    time.sleep(tsleep)

    print("Payload mutation is finished enjoy...")

#----------------------------------------------------------------------------------------

def printGeneratePayloadMessage():
    
    time.sleep(tsleep)

    print("Payloads are being generated please wait...\n")

#----------------------------------------------------------------------------------------

def printCollectedPayloadMessage():
    
    time.sleep(tsleep)

    print("Payloads collected...\n")

#----------------------------------------------------------------------------------------
 
def printHelpMessage():
    
    print("help           :  Print help message for providing proper script arguments")    
    print("sfx            :  This option can be used for mutating SQL injection attack strings by adding suffixes to the payloads such as EXEC, %00 e.t.c") 
    print("pfx            :  This option can be used for mutating SQL injection attack strings by adding postfixes to the payloads e.g. --, );-- e.t.c")
    print("url            :  This option can be used for mutating SQL, Pathtraversal and XSS injection attack strings by url encoding the payloads")
    print("flr            :  This option can be used for mutating SQL injection attack strings by filling the gaps with SQL commends, url encoded space and other special characters")
    print("b64            :  This option can be used for mutating SQL, Pathtraversal and XSS injection attack strings by base 64 encoding the payloads")
    print("hex            :  This option can be used for mutating SQL and Pathtraversal injection attack strings by hex encoding the payload")
    print("concatMSSQL    :  This option can be used for mutating SQL injection attack strings by adding MSSQL concatenators within payload SQL keywords")
    print("concatOracle   :  This option can be used for mutating SQL injection attack strings by adding Oracle SQL concatenators within payload SQL keywords")
    print("concatMySQL    :  This option can be used for mutating SQL injection attack strings by adding MySQL concatenators within payload SQL keywords")
    print("utf8           :  This option can be used for mutating Pathtraversal attack strings by utf-8 encoding")
    print("utf16          :  This option can be used for mutating Pathtraversal attack strings by utf-16 encoding")
    print("utf32          :  This option can be used for mutating Pathtraversal attack strings by utf-32 encoding")
    print("gzip           :  This option can be used for mutating Pathtraversal attack strings by gzip encoding (Not tested thoroughly on Web Applications)")
    print("bzip           :  This option can be used for mutating Pathtraversal attack strings by bzip encoding (Not tested thoroughly on Web Applications)")
    print("ver            :  Print version of the script")
    print("ban            :  Print ThE script kiddy banner")
    print("allsql         :  Perform all SQL string injection mutations to the file provided as an input")
    print("XXSMe          :  Converts the payload given as an input to an xml file that XXSMe can import")
    print("SQLInjectMe    :  Converts the payload given as an input to an xml file that SQLInjectMe can import")
    print("var            :  This option can be used for mutating SQL injection attack strings by adding case variation to the payloads")
    print("clean          :  Clean payload the whole database from trailing,leading spaces,blank lines and double payloads")
    print("ded            :  Deduplicate all attack strings payloads to the file provided as an input")
    print("allxss         :  Collect all xss payloads from the payload database into a single file")
    print("allmssql       :  Collect all mssql payloads from the payload database into a single file")
    print("allaccess      :  Collect all payloads from the payload database into a single file")
    print("allpostgre     :  Collect all payloads from the payload database into a single file")
    print("alloracle      :  Collect all oracle payloads from the payload database into a single file")
    print("allldap        :  Collect all ldap payloads from the payload database into a single file")
    print("allxxe         :  Collect all external entity payloads from the payload database into a single file")
    print("allssi         :  Collect all server side include payloads from the payload database into a single file")
    print("allcmd         :  Collect all os command payloads from the payload database into a single file")
    print("alluseragent   :  Collect all useragent payloads from the payload database into a single file")
    print("allpaths       :  Collect all path traversal payloads from the payload database into a single file")
    print("allxpath       :  Collect all XPath payloads from the payload database into a single file")
    print("allxml         :  Collect all xml payloads from the payload database into a single file")
    print("allerrors      :  Collect all error payloads from the payload database into a single file")
    print("allhttpmethods :  Collect all http method payloads from the payload database into a single file")
    print("isdangerous    :  <TODO> Print warning if the payload file contains dangerous database SQL keywords")    

#########################################################################################################
##                                      Time functions
#########################################################################################################

def getTime():

    return time.strftime("%a%d%b%H_%M_%S", time.gmtime())

#----------------------------------------------------------------------------------------

def addDelay():
    
    time.sleep(tsleep)

    print("Processing")

#########################################################################################################
#-------------------------------- Database management --------------------------------------------------#
######################################################################################################### 

def getPayloadList(): # Reads through the payload database and collects all filenames with their paths
    
 _payloadFileList = []

 for _dirname, _dirnames, _filenames in os.walk('.'):
    
  for _filename in _filenames: # Get a file list with all payload files

      _payloadFileList.append(os.path.join(_dirname, _filename))

  for _payloadFileLine in _payloadFileList: # Save my turtles from being modified 

    if re.match(r'./tmntv...\.py',_payloadFileLine) or re.match(r'Readme.rtf',_payloadFileLine) or re.match(r'.\\tmntv...\.py',_payloadFileLine) or re.match(r'.\\Readme.rtf',_payloadFileLine):

        _payloadFileList.remove(_payloadFileLine)

 return _payloadFileList

#----------------------------------------------------------------------------------------

def cleanBlankLinesAndSpaces(_payloadFileList): # Remove all leading and trailing spaces, along with empty lines from the database 

 _filenamesMappedToPayloads = {} # Create that dictionary is going to pair filenames with their payloads (in the form of a list)

 for _payloadFilename in _payloadFileList: # Populate dictionary by mapping filenames to their list payloads
        
    _tmpFileObj1 = open(_payloadFilename,'r')
    
    _filenamesMappedToPayloads[_payloadFilename] = _tmpFileObj1.readlines() 
    
    _tmpFileObj1.close()
    
 for _filename, _payloads in _filenamesMappedToPayloads.iteritems(): # Write each sanitized payload back to the files
    
    _tmpFileObj2 = open(_filename,"w")
    
    for _payloadLine in _payloads:
        
        _tmpFileObj2.write((_payloadLine.strip()).rstrip()+"\n") # Remove trailing and leading spaces
        
    _tmpFileObj2.close()

#----------------------------------------------------------------------------------------

def cleanDoublesFromDb(_payloadFileList): # Does the actual cleaning if the double payloads for the whole database
    
 _filenamesMappedToPayloads = {} # Create a dictionary that is going to pair filenames with their payloads (in the form of a list)
 
 _compareList = []

 for _payloadFilename in _payloadFileList: # Populate dictionary by mapping filenames to their list payloads
        
    _tmpFileObj1 = open(_payloadFilename,'r')
    
    _filenamesMappedToPayloads[_payloadFilename] = _tmpFileObj1.readlines() 
    
    _tmpFileObj1.close()

 for _payloadFilename, _payloadFileList in _filenamesMappedToPayloads.iteritems(): # Write each sanitized payload back to the files
    
    _tmpFileObj2 = open(_payloadFilename,"w")
    
    for _payloadLine in _payloadFileList:
        
        if _payloadLine not in _compareList: # Deduplicate 
            
            _compareList.append(_payloadLine)
            
            _tmpFileObj2.write(_payloadLine) # Remove trailing and leading spaces
        
    _tmpFileObj2.close()   

#----------------------------------------------------------------------------------------

def cleandb(_payloadFileList): # Cleans trailing, leading spaces and double payloads
    
 cleanBlankLinesAndSpaces(_payloadFileList)

 cleanDoublesFromDb(_payloadFileList)

#----------------------------------------------------------------------------------------

def convertFileToList(_originalPayloadFileObj): # Converts the input payload file to a list

 return _originalPayloadFileObj.readlines()

#----------------------------------------------------------------------------------------

def deduplicate(_payloadList): # Deduplicate payloads from a single payload files
 
 currentTime = getTime()+'_'
 
 _mutatePayloadFile = currentTime+"deduplicatedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 _deduplictedList = list(set(_payloadList))
 
 for line in _deduplictedList:

  _mutatePayloadFileObj.write(line)
  
 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------

def getSelected(_option): # Return the selected argument

 if isallxss.match(_option):
    
    return "XSS"

 if isallmssql.match(_option):

    return "MSSQL"

 if isallaccess.match(_option):

    return "Access"

 if isallpostgre.match(_option):

    return "Postgre"

 if isalloracle.match(_option):

    return "Oracle"

 if isallldap.match(_option):

    return "LDAP"

 if isallxxe.match(_option):

    return "XXE"

 if isallssi.match(_option):

    return "SSI"

 if isallcmd.match(_option):

    return "CE"

 if isalluseragent.match(_option):

    return "UserAgent"

 if isallpaths.match(_option):

    return "Pathtraversal"

 if isallxml.match(_option):

    return "XML"

 if isallhttpmethods.match(_option):

    return "HttpMethod"

 if isallxpath.match(_option):

    return "XPath"

 if isallerror.match(_option):

    return "Errors"

#----------------------------------------------------------------------------------------

def collector(_option,_payloadFileList): # Collect all payloads of the same type 
    
 currentTime = getTime()+'_'
 
 _collectedPayloadFiles = currentTime+"collectedPayloads.lst"

 _collectedPayloadFilesObj = open(_collectedPayloadFiles,"a")

 for _payloadFile in _payloadFileList:
    
    _harvestFileObj = open(_payloadFile,"r")
    
    if re.search(getSelected(_option),_payloadFile):
        
        _collectedPayloadFilesObj.write(_harvestFileObj.read())

#----------------------------------------------------------------------------------------

def checkIfDangerous():
    
    print "TODO"

############################################################################################
#----------------------------------- Payload mutators -------------------------------------#
############################################################################################

def suffixAdder(_payloadList): # Adding suffixes
 
 checkDirectoryExitstance() 
 
 currentTime = getTime()+'_'
 
 _mutatePayloadFile = currentTime+"suffixedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")

 _suffixElementsFile = suffixFile

 _suffixElementObj = open(_suffixElementsFile,"r")
    
 _suffixList = _suffixElementObj.readlines()
 
 for _suffix in _suffixList: 

  for _payloadline in _payloadList:

   _mutatePayloadFileObj.write(str(_suffix).rstrip()+str(_payloadline).rstrip()+"\n")

 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------

def postfixAdder(_payloadList): # Adding postfixes
    
 checkDirectoryExitstance() 

 currentTime = getTime()+'_'

 _mutatePayloadFile = currentTime = getTime()+'_'+"postfixedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")

 _postfixElementsFile = postfixFile

 _postfixElementObj = open(_postfixElementsFile,"r")
    
 _postfixList = _postfixElementObj.readlines()
 
 for _postfix in _postfixList: 

  for _payloadline in _payloadList:

    _mutatePayloadFileObj.write(str(_payloadline).rstrip()+str(_postfix).rstrip()+"\n")
    
 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------

def replacer(_payloadList): # Filling the gaps 

 checkDirectoryExitstance() 

 currentTime = getTime()+'_'

 _mutatePayloadFile = currentTime+"spaceFilledPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")

 _space_FillerElementsFile = fillerFile

 _space_FillerElementObj = open(_space_FillerElementsFile,"r")
    
 _space_FillerList = _space_FillerElementObj.readlines()
 
 for _space_Filler in _space_FillerList: 

  for _payloadline in _payloadList:

   _mutatePayloadFileObj.write((str(_payloadline).rstrip()).replace(" ",(str(_space_Filler).rstrip()))+"\n")

 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------

def urlEncoder(_payloadList): # Do url encoding 

 currentTime = getTime()+'_'

 _mutatePayloadFile = currentTime = getTime()+'_'+"urlEncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((urllib.urlencode({'q':str(_payloadline).rstrip()})).replace("q=", "")+"\n")

 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------

def base64Encoder(_payloadList): # Base 64 encoding

 currentTime = getTime()+'_'
 
 _mutatePayloadFile = currentTime+"base64EncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write(base64.b64encode(str(_payloadline).rstrip())+"\n")

 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------

def hexEncoder(_payloadList): # ASCII Hex encoding for SQL and Path traversal 

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"hexEncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((str(_payloadline).rstrip()).encode("Hex")+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def utf32Encoder(_payloadList): # UTF-32 encoding for path traversal

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"utf32EncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((str(_payloadline).rstrip()).encode("utf_32")+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def utf16Encoder(_payloadList): # UTF-16 encoding for path traversal

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"utf16EncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((str(_payloadline).rstrip()).encode("utf_16")+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def utf8Encoder(_payloadList): # UTF-16 encoding for path traversal

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"utf8EncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((str(_payloadline).rstrip()).encode("utf_8")+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def gzipEncoder(_payloadList): # gzip encoding for path traversal

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"utf16EncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((str(_payloadline).rstrip()).encode("zlib_codec")+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def bz2Encoder(_payloadList): # bz2 encoding for path traversal

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"bz2codecEncodedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 for _payloadline in _payloadList:

  _mutatePayloadFileObj.write((str(_payloadline).rstrip()).encode("bz2_codec")+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def XSSMeFormater(_payloadList): # XSSMe formats the input payload file

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"XSSMeFormated.xml"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")
 
 _mutatePayloadFileObj.write("<exportedattacks><attacks><attack><attackString><![CDATA["+"\n")
 
 for _payloadline in _payloadList:
    
    _mutatePayloadFileObj.write((str(_payloadline).rstrip())+"\n"+"]]></attackString><signature>Script</signature></attack><attack><attackString><![CDATA["+"\n")
  
 _mutatePayloadFileObj.write("]]></attackString><signature>Script</signature></attack></attacks></exportedattacks>"+"\n")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def SQLInjectMeFormater(_payloadList):  # SQLInjectMe formats the input payload file

 currentTime = getTime()+'_'

 _mutatePayloadFile =  currentTime = getTime()+'_'+"SQLInjectMeFormated.xml"
 
 _mutatePayloadFileObj = open(_mutatePayloadFile,"w")

 _mutatePayloadFileObj.write("<exportedattacks><attacks><attack><attackString><![CDATA[")
 
 for _payloadline in _payloadList:
    
    _mutatePayloadFileObj.write((str(_payloadline).rstrip())+"]]></attackString><signature>TMNT</signature></attack><attack><![CDATA[")
  
 _mutatePayloadFileObj.write("</exportedattacks>")

 _mutatePayloadFileObj.close()
 
#----------------------------------------------------------------------------------------

def addCaseVarietionToKeyword(_sqlKeyword): # Adds case variation to a single keyword

 _sqlKeywordAsList = list(_sqlKeyword)

 for i in range(len(_sqlKeywordAsList)):

  if i % 2 == 0:

   _sqlKeywordAsList[i] = (_sqlKeywordAsList[i].upper())

  else:

   _sqlKeywordAsList[i] = (_sqlKeywordAsList[i].lower())

 _sqlKeyword = ''.join(_sqlKeywordAsList)

 return str(_sqlKeyword).rstrip()

#----------------------------------------------------------------------------------------

def searchPayloadLineUpperAndLower(_keywordList, _payloadLine):
    # Search payload line for all SQL keywords contained in file CharContainer
    for _keyword in _keywordList:

        if re.search(_keyword.upper(),_payloadLine):

            return True

        if re.search(_keyword.lower(),_payloadLine):

            return True

    else:

        return False 

#----------------------------------------------------------------------------------------

def caseVarietionAdder(_payloadList): # Adding case variation
 
 checkDirectoryExitstance() 

 currentTime = getTime()+'_'

 _mutatePayloadFile = currentTime+"caseVarietionPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"a")
 
 _sqlKeywordElementsFile = sqlKeywordFile

 _sqlKeywordElementsFileObj = open(_sqlKeywordElementsFile,"r")

 _sqlKeywordList = _sqlKeywordElementsFileObj.readlines()
 
 _sqlKeyWordDictionary = {} # Holding SQL keywords mapping them to SQL keywords with case variation

 _searchList = [] # Holding only SQL keywords for later searching
 
 # Populate dictionary with SQL keywords and equvalent SQL keyword values with case variation
 for _sqlKeyword in _sqlKeywordList:

    _sqlKeyWordDictionary[str(_sqlKeyword).rstrip()] = addCaseVarietionToKeyword(_sqlKeyword)

 # Populate list with SQL keywords for searching later on
 for _sqlKeywordKey, _sqlKeywordValue in _sqlKeyWordDictionary.iteritems():

    _searchList.append(_sqlKeywordKey)

 for _payloadLine in  _payloadList:

    for _sqlKeywordKey, _sqlKeywordValue  in _sqlKeyWordDictionary.iteritems():

        if re.search(_sqlKeywordKey.upper(),_payloadLine):

            _payloadLine = str(_payloadLine).replace(_sqlKeywordKey.upper(),_sqlKeywordValue)

            # Search for all keywords within the payload line
            if not searchPayloadLineUpperAndLower(_searchList,_payloadLine):

                _mutatePayloadFileObj.write(_payloadLine)
            
        if re.search(_sqlKeywordKey.lower(),_payloadLine):

            _payloadLine = str(_payloadLine).replace(_sqlKeywordKey.lower(),_sqlKeywordValue)

            # Search for all keywords within the payload line
            if not searchPayloadLineUpperAndLower(_searchList,_payloadLine):

                _mutatePayloadFileObj.write(_payloadLine)

 _mutatePayloadFileObj.close()

#----------------------------------------------------------------------------------------
 
def addConcatenationToKeyword(_option,_sqlKeyword): # Add concatenation to a single SQL kerword

 isConcatMSSQL = re.compile("concatMSSQL")
 isConcatOracle = re.compile("concatOracle")
 isConcatMySQL = re.compile("concatMYSQL")
    
 _sqlKeywordAsList = list(_sqlKeyword)

 if isConcatMSSQL.match(_option):# Add the concatenator between the second and third character
    
    _sqlKeywordAsList.insert(1,"\'+\'")

 if isConcatOracle.match(_option):
    
    _sqlKeywordAsList.insert(1,"\'| |\'")

 if isConcatMySQL.match(_option):
    
    _sqlKeywordAsList.insert(1,"\' \'")

 _sqlKeyword = ''.join(_sqlKeywordAsList)

 return str(_sqlKeyword).rstrip()
 
#----------------------------------------------------------------------------------------

def concatenationAdder(_option,_payloadList): # Adding concatenators
 
 checkDirectoryExitstance() 

 currentTime = getTime()+'_'

 _mutatePayloadFile = currentTime+"concatenatedPayloads.lst"

 _mutatePayloadFileObj = open(_mutatePayloadFile,"a")
 
 _sqlKeywordElementsFile = sqlKeywordFile

 _sqlKeywordElementsFileObj = open(_sqlKeywordElementsFile,"r")

 _sqlKeywordList = _sqlKeywordElementsFileObj.readlines()
 
 _sqlKeyWordDictionary = {} # Holding SQL keywords mapping 

 _searchList = [] # Holding only SQL keywords for later searching
 
 # Populate dictionary with SQL keywords and equvalent SQL keyword values
 for _sqlKeyword in _sqlKeywordList:

    _sqlKeyWordDictionary[str(_sqlKeyword).rstrip()] = addConcatenationToKeyword(option,_sqlKeyword)

 # Populate list with SQL keywords for searching later on
 for _sqlKeywordKey, _sqlKeywordValue in _sqlKeyWordDictionary.iteritems():

    _searchList.append(_sqlKeywordKey)

 for _payloadLine in  _payloadList:

    for _sqlKeywordKey, _sqlKeywordValue  in _sqlKeyWordDictionary.iteritems():

        if re.search(_sqlKeywordKey.upper(),_payloadLine):

            _payloadLine = str(_payloadLine).replace(_sqlKeywordKey.upper(),_sqlKeywordValue)

            # Search for all keywords within the payload line
            if not searchPayloadLineUpperAndLower(_searchList,_payloadLine):

                _mutatePayloadFileObj.write(_payloadLine)
            
        if re.search(_sqlKeywordKey.lower(),_payloadLine):

            _payloadLine = str(_payloadLine).replace(_sqlKeywordKey.lower(),_sqlKeywordValue)

            # Search for all keywords within the payload line
            if not searchPayloadLineUpperAndLower(_searchList,_payloadLine):

                _mutatePayloadFileObj.write(_payloadLine)

 _mutatePayloadFileObj.close()
 
#########################################################################################################
####################################### Argument handling...#############################################
#########################################################################################################

printUsageMessage()

option = raw_input("Enter option: ")

optionIsValid = re.compile("(hex)|(sfx)|(flr)|(url)|(pfx)|(b64)|(allsql)|(help)|(ban)|(ver)|(var)|(ded)|(clean)|(XSSMe)|(SQLInjectMe)|(allxss)|(allxxe)|(allxml)|(alloracle)|(allldap)|(allssi)|(allpaths)|(allxpath)|(allhttpmethods)|(alluseragent)|(allmssql)|(allcmd)|(allaccess)|(allpostgre)|(allerror)|(concatMSSQL)|(concatOracle)|(concatMySQL)|(isdangerous)|(utf32)|(utf16)|(utf8)|(gzip)|(bz2)")

#------------------------------- Commands that have to do with the single file input ---------------------

isSuffix = re.compile("sfx")
isPostfix = re.compile("pfx")
isAll = re.compile("allsql")
isUrl = re.compile("url")
isVariation = re.compile("var")
isBase64 = re.compile("b64")
isFiller = re.compile("flr")
isHex = re.compile("hex")
isUtf32 = re.compile("utf32")
isUtf16 = re.compile("utf16")
isUtf8 = re.compile("utf8")
isGzip = re.compile("gzip")
isBz2 = re.compile("bz2")
isConcatMSSQL = re.compile("concatMSSQL")
isConcatOracle = re.compile("concatOracle")
isConcatMySQL = re.compile("concatMYSQL")
isXSSMe = re.compile("XSSMe")
isSQLInjectMe = re.compile("SQLInjectMe")

#------------------------------- Commands that have to do with the tool ---------------------------------

isHelp = re.compile("help")
isBanner = re.compile("ban")
isVersion = re.compile("ver")

#------------------------------- Commands that have to do with db/payload cleanup ------------------------

isClean = re.compile("clean")
isDeduplicate = re.compile("ded")

#------------------------------- Commands that have to do with db payload collection ---------------------

isallxss = re.compile("allxss")
isallmssql = re.compile("allmssql")
isallaccess = re.compile("allaccess")
isallpostgre = re.compile("allpostgre")
isalloracle = re.compile("alloracle")
isallldap = re.compile("allldap")
isallxxe = re.compile("allxxe")
isallssi = re.compile("allssi")
isallcmd = re.compile("allcmd")
isalluseragent = re.compile("alluseragent")
isallpaths = re.compile("allpaths")
isallxpath = re.compile("allxpath")
isallxml = re.compile("allxml")
isallhttpmethods = re.compile("allhttpmethods")
isallerror = re.compile("allerror")
isDangerous = re.compile("isdangerous")

#------------------------------- Execute options that require a file as an input --------------------------

if not (optionIsValid.match(option)):

   printErrorMessage()

   exitScript()
 
if  isHelp.match(option):

    printHelpMessage()

    exitScript()

if  isClean.match(option):

    cleandb(getPayloadList())

    printCleanUpMessage()

    exitScript()
    
if  isBanner.match(option):

    printBanner()

    exitScript()

if  isVersion.match(option):

    printVersion()

    exitScript()

if getSelected(option):
    
    collector(option,getPayloadList())

    printCollectedPayloadMessage()
    
    exitScript()

#----------------- Supply file input --------------------------------------------

filename = raw_input("Enter filename: ")

if not checkFileExitstance(filename) :

    exitScript()

#################################################################################
############################### Open payload file ###############################
#################################################################################

originalPayloadFileObj = open(filename,"r")

payloadList = convertFileToList(originalPayloadFileObj)

### Close input file up ###  
originalPayloadFileObj.close()

#################################################################################
############################# Generating mutation file ##########################
#################################################################################

printGeneratePayloadMessage()

#---------------------------------------------------------------------------------

if isAll.match(option):
    
    postfixAdder(payloadList)

    addDelay()

    concatenationAdder("concatMSSQL",payloadList)
    concatenationAdder("concatOracle",payloadList)
    concatenationAdder("concatMYSQL",payloadList)

    addDelay()

    suffixAdder(payloadList)

    addDelay()

    replacer(payloadList)

    addDelay()

    urlEncoder(payloadList)

    addDelay()

    base64Encoder(payloadList)

    addDelay()

    hexEncoder(payloadList)

    addDelay()

    caseVarietionAdder(payloadList)

    addDelay()

    SQLInjectMeFormater(payloadList)

    addDelay()

    XSSMeFormater(payloadList)

#---------------------------------------------------------------------------------

if  isSuffix.match(option):

    suffixAdder(payloadList)

if  isFiller.match(option):

    replacer(payloadList)

if  isUtf32.match(option):

    utf32Encoder(payloadList)

if  isUtf16.match(option):

    utf16Encoder(payloadList)

if  isUtf8.match(option):

    utf8Encoder(payloadList)

if  isGzip.match(option):

    gzipEncoder(payloadList)

if  isBz2.match(option):

    bz2Encoder(payloadList)

if  isPostfix.match(option):

    postfixAdder(payloadList)

if  isVariation.match(option):

    caseVarietionAdder(payloadList)

if  isHex.match(option):

    hexEncoder(payloadList)

if  isBase64.match(option):

    base64Encoder(payloadList)

if  isUrl.match(option):

    urlEncoder(payloadList)

if  isDeduplicate.match(option):

    deduplicate(payloadList)
    
if  isXSSMe.match(option):

    XSSMeFormater(payloadList)
    
if  isSQLInjectMe.match(option):

    SQLInjectMeFormater(payloadList)

if  isConcatOracle.match(option):
    
    concatenationAdder(option,payloadList)

#------------------------ Handle concatination mutation -------------------------------------

if  isConcatMSSQL.match(option) or isConcatMySQL.match(option) or isConcatOracle.match(option):
    
    concatenationAdder(option,payloadList)

#---------------------------------------------------------------------------------------------

if  isDangerous.match(option):
    
    checkIfDangerous(payloadList)

printFinishMessage()

exitScript()
    
#---------------------------------------------------------------------------------

