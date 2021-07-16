import xml.etree.ElementTree as ET
import os
from os import listdir
from os.path import isfile, join, exists
import re

#needed folders for the script
engblamsfolder = ('./bundle_blams_eng/') #english blams
transfolder = ('./translated_pattern/') #translated pattern
outputfolder =('./bundle_blams_multiling/') #output folder for the generated files


#STEP 2: iterate through the englisch blams and parse the englisch files and translated file. Take needed elements and write them in new files
def iteratefolder(filetranslist, mylisttrans):
  for filename in os.listdir(engblamsfolder):
    
    mylist = [engblamsfolder + filename for filename in listdir(engblamsfolder) if isfile(join(engblamsfolder, filename))]
    filenamesplitted = filename.split('.')
    filenamecompare = filenamesplitted[0]
    filenamecompare = filenamecompare.replace('_', ' ')
    for filetrans in filetranslist:
        filetranssplitted = filetrans.split('_translate.')
        filetranscompare = (filetranssplitted[0])
        filetranscompare = filetranscompare.replace('_', ' ')
        if filename.endswith(".xml"):
            for s in mylist:
                tree = ET.parse(s)
                root = tree.getroot()
                for child in root:
                    fileinlist= child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleGeneralInfo/{http://www.clarin.eu/cmd/}BundleDisplayTitle')
                    for t in mylisttrans:
                        
                        translisttitle= t.split('/')
                        if translisttitle[2] == filetrans:
                            print (fileinlist, filenamecompare, filetranscompare)
                            if fileinlist == filenamecompare == filetranscompare:
                                print('TEST')
                                treetrans = ET.parse(t)
                                roottrans = treetrans.getroot()
                                for transchild in roottrans:
                                        
                                        test= transchild.findtext('BundleDisplayTitle')
                                        print(fileinlist, test)

                                        #file beginning tag 
                                        cmdtag = ('<CMD xmlns="http://www.clarin.eu/cmd/" xmlns:cmd="http://www.clarin.eu/cmd/" xmlns:dcr="http://www.isocat.org/ns/dcr" xmlns:ann="http://www.clarin.eu" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.clarin.eu/cmd/ https://catalog.clarin.eu/ds/ComponentRegistry/rest/registry/1.1/profiles/clarin.eu:cr1:p_1475136016193/xsd" CMDVersion="1.1">')
                                        #mdselflink
                                        mdselfl = root.findtext('.//{http://www.clarin.eu/cmd/}MdSelfLink')
                                        #header tag
                                        headertag =('<Header>'+ '\n' + '<MdSelfLink>' + '\n' + mdselfl + '\n' +'</MdSelfLink>' +'\n' +'</Header>')
                                        #resource tag
                                        resourcestag = ('<Resources><ResourceProxyList></ResourceProxyList><JournalFileProxyList></JournalFileProxyList><ResourceRelationList></ResourceRelationList></Resources>')
                                        #getbundleid
                                        bundleid = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleGeneralInfo/{http://www.clarin.eu/cmd/}BundleID')
                                        #component beginning tag
                                        startcomp = ('<Components><BLAM-bundle-repository-v0.14><BundleGeneralInfo><BundleID IdentifierType="Handle">' + bundleid + '</BundleID>')
                                        #displayTitle
                                        distit=transchild.findtext('BundleDisplayTitle')
                                        distittag= ('<BundleDisplayTitle>'+ '\n' +distit+ '\n' + '</BundleDisplayTitle>')
                                        #BundleDescription
                                        descrip=transchild.findtext('BundleDescription')
                                        descripttag= ('<BundleDescription>'+ '\n' +descrip+ '\n' + '</BundleDescription>')
                                        #RecordingDate
                                        recorddate =child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleGeneralInfo/{http://www.clarin.eu/cmd/}BundleRecordingDate')
                                        recorddatetag=('<BundleRecordingDate>'+ '\n' + recorddate+ '\n' +'</BundleRecordingDate>')
                                        
                                        #Get Keywords
                                        keywords=transchild.findall('BundleKeywords/BundleKeyword') 
                                        mylistkey= [('<BundleKeyword>') +keyword.text for keyword in keywords]
                                        keywordstring = ('</BundleKeyword>' + '\n').join(mylistkey)
                                    
                                        keywordsstart = ('<BundleKeywords>')
                                        keywordsend = ('</BundleKeyword></BundleKeywords>')


                                        #Objlangstart und end tag
                                        objstart = "<BundleObjectLanguages><BundleObjectLanguage>"
                                        objend ="</BundleObjectLanguage></BundleObjectLanguages>"
                                        #get ObjectLanguageDisplayName
                                        objlangdis = transchild.findtext('./BundleObjectLanguages/BundleObjectLanguage/ObjectLanguageDisplayName')
                                        if objlangdis == '':
                                            objlangdisnam=('<ObjectLanguageDisplayName/>')
                                        else: 
                                            objlangdisnam=('<ObjectLanguageDisplayName>' + objlangdis + '</ObjectLanguageDisplayName>')

                                        #get ObjectLanguageName
                                        objlangname = transchild.findtext('./BundleObjectLanguages/BundleObjectLanguage/ObjectLanguageName')
                                        objlangnametag = ('<ObjectLanguageName>' + objlangname + '</ObjectLanguageName>')

                                        #get ISO 
                                        iso = transchild.findtext('./BundleObjectLanguages/BundleObjectLanguage/ObjectLanguageISO639-3Code')
                                        isotag = ('<ObjectLanguageISO639-3Code>' + iso + '</ObjectLanguageISO639-3Code>')

                                        #get Glotto
                                        glotto = transchild.findtext('./BundleObjectLanguages/BundleObjectLanguage/ObjectLanguageGlottologCode')
                                        glottotag = ('<ObjectLanguageGlottologCode>' + glotto + '</ObjectLanguageGlottologCode>')

                                        #get AlternativeNames
                                        anames=transchild.findall('./BundleObjectLanguages/BundleObjectLanguage/ObjectLanguageAlternativeNames/ObjectLanguageAlternativeName') 
                                        mylistalt= [('<ObjectLanguageAlternativeName>') +aname.text for aname in anames]
                                        altnamestring = ('</ObjectLanguageAlternativeName>' + '\n').join(mylistalt)
                                        altnamessstart = ('<ObjectLanguageAlternativeNames>')
                                        altnamesend = ('</ObjectLanguageAlternativeName></ObjectLanguageAlternativeNames>')

                                        #gettaxonomy
                                        taxonomy=transchild.findall('./BundleObjectLanguages/BundleObjectLanguage/ObjectLanguageTaxonomy/ObjectLanguageLanguageFamily') 
                                        mylisttax= [('<ObjectLanguageLanguageFamily>') +tax.text for tax in taxonomy]
                                        taxstring = ('</ObjectLanguageLanguageFamily>' + '\n').join(mylisttax)
                                       
                                        if taxstring == '':
                                            taxstringfin=('')
                                        else: 
                                            taxstart = ('<ObjectLanguageTaxonomy>')
                                            taxend = ('</ObjectLanguageLanguageFamily></ObjectLanguageTaxonomy>')
                                            taxstringfin=(taxstart + taxstring + taxend)

                                        #Get BundleLocation
                                        #geolocation
                                        #bundloc = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleGeneralInfo/{http://www.clarin.eu/cmd/}BundleLocation/{http://www.clarin.eu/cmd/}BundleGeoLocation')
                                        #bundloctag = ('<BundleLocation><BundleGeoLocation>'+ bundloc + '</BundleGeoLocation>')
                                            #getlocationname
                                        bundloctag = ('<BundleLocation>')
                                        locname = transchild.findtext('./BundleLocation/BundleLocationName')
                                        if locname == '':
                                            locname=('<BundleLocationName/>')
                                        else: 
                                            locname=('<BundleLocationName>' + locname + '</BundleLocationName>')
                                            #getlocfacet
                                        locfacet=transchild.findtext('./BundleLocation/BundleLocationFacet')
                                        locfacettag = ('<BundleLocationFacet>' + locfacet + '</BundleLocationFacet>')
                                            #getRegionName
                                        regname = transchild.findtext('./BundleLocation/BundleRegionName')
                                        if regname == '':
                                            regname=('<BundleRegionName/>')
                                        else: 
                                            regname=('<BundleRegionName>' + regname + '</BundleRegionName>')
                                            #getRegionFacet
                                        regfacet=transchild.findtext('./BundleLocation/BundleRegionFacet')
                                        regfacettag = ('<BundleRegionFacet>' + regfacet + '</BundleRegionFacet>')

                                            #getCountryName
                                        countryname = transchild.findtext('./BundleLocation/BundleCountryName')
                                        if countryname == '':
                                            countryname=('<BundleCountryName/>')
                                        else: 
                                            countryname=('<BundleCountryName>' + countryname + '</BundleCountryName>')
                                            #getCountryFacet
                                        countryfacet=transchild.findtext('./BundleLocation/BundleCountryFacet')
                                        countryfacettag = ('<BundleCountryFacet>' + countryfacet + '</BundleCountryFacet>')
                                            #getCountryCode
                                        countrycode=transchild.findtext('./BundleLocation/BundleCountryCode')
                                        countrycodetag = ('<BundleCountryCode>' + countrycode + '</BundleCountryCode>')

                                        bundlocfin ='</BundleLocation></BundleGeneralInfo>'

                                        #BundlePublicationInfo
                                            #pubyear
                                        pubyear = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundlePublicationInfo/{http://www.clarin.eu/cmd/}BundlePublicationYear')
                                        pubyeartag =('<BundlePublicationInfo><BundlePublicationYear>' + pubyear+ '</BundlePublicationYear>')

                                            #bundledataProvider
                                        datapr = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundlePublicationInfo/{http://www.clarin.eu/cmd/}BundleDataProvider')
                                        dataprtag =('<BundleDataProvider>' + datapr+ '</BundleDataProvider>')

                                            #bundlecreators
                                                #bundlecreator
                                                #creatornameidentifier
                                        creatorstarttag = "<BundleCreators><BundleCreator>"

                                        creatorid = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundlePublicationInfo/{http://www.clarin.eu/cmd/}BundleCreators/{http://www.clarin.eu/cmd/}BundleCreator/{http://www.clarin.eu/cmd/}CreatorNameIdentifier')
                                        creatoraff = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundlePublicationInfo/{http://www.clarin.eu/cmd/}BundleCreators/{http://www.clarin.eu/cmd/}BundleCreator/{http://www.clarin.eu/cmd/}CreatorAffiliation')
                                        if (creatorid == ''):
                                            creatorid=('<CreatorNameIdentifier/>')
                                        else: 
                                            creatorid=('<CreatorNameIdentifier>' + creatorid + '</CreatorNameIdentifier>')

                                        if (creatoraff ==''):
                                            creatoraff=('<CreatorAffiliation/>')
                                        else:
                                            creatoraff=('<CreatorAffiliation>' + creatoraff + '</CreatorAffiliation>')
                                        
                                        #get Creatorname

                                        creatorfam = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundlePublicationInfo/{http://www.clarin.eu/cmd/}BundleCreators/{http://www.clarin.eu/cmd/}BundleCreator/{http://www.clarin.eu/cmd/}CreatorName/{http://www.clarin.eu/cmd/}CreatorFamilyName')
                                        creatorgive = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundlePublicationInfo/{http://www.clarin.eu/cmd/}BundleCreators/{http://www.clarin.eu/cmd/}BundleCreator/{http://www.clarin.eu/cmd/}CreatorName/{http://www.clarin.eu/cmd/}CreatorGivenName')
                                        
                                        if (creatorfam == ''):
                                            creatorfam=('<CreatorFamilyName/>')
                                        else: 
                                            creatorfam=('<CreatorFamilyName>' + creatorfam + '</CreatorFamilyName>')
                                                                           
                                        if (creatorgive ==''):
                                            creatorgive=('<CreatorGivenName/>')
                                        else:
                                            creatorgive=('<CreatorGivenName>' + creatorgive + '</CreatorGivenName>')
                                        creatorstart=('<CreatorName>')
                                        creatorend =('</CreatorName></BundleCreator></BundleCreators></BundlePublicationInfo>')

                                        #ProjectInfo
                                        projstart=('<ProjectInfo><Project>')
                                        projend=('</Project></ProjectInfo>')
                                        #projdisplayname
                                        projdisname = transchild.findtext('./ProjectDisplayName')
                                        projdisname =('<ProjectDisplayName>' + projdisname+ '</ProjectDisplayName>')
                                        #projdesc
                                        projdesc = transchild.findtext('./ProjectDescription')
                                        projdesc =('<ProjectDescription>' + projdesc+ '</ProjectDescription>')

                                        #BundleAdministriveInfo
                                        startad="<BundleAdministrativeInfo>"

                                        #access
                                        access = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleAdministrativeInfo/{http://www.clarin.eu/cmd/}Access') 
                                        if (access == ''):
                                            access=('<Access/>')
                                        else: 
                                            access=('<Access>' + access + '</Access>')
                                        
                                        #availabilitydate
                                        ava = child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleAdministrativeInfo/{http://www.clarin.eu/cmd/}AvailabilityDate')
                                        if (ava == ''):
                                            ava=('<AvailabilityDate/>')
                                        else: 
                                            ava=('<AvailabilityDate>' + ava + '</AvailabilityDate>')

                                        #licensetag
                                        lictag="<License><LicenseName/><LicenseIdentifier/></License>"

                                        #rightsholder
                                        rightsholder= child.findtext('.//{http://www.clarin.eu/cmd/}BLAM-bundle-repository-v0.14/{http://www.clarin.eu/cmd/}BundleAdministrativeInfo/{http://www.clarin.eu/cmd/}RightsHolder/{http://www.clarin.eu/cmd/}RightsHolderName')
                                        rightsholder =('<RightsHolder><RightsHolderName>' + rightsholder+ '</RightsHolderName></RightsHolder></BundleAdministrativeInfo>')

                                        #BundleStructuralInfo
                                        structinfo=("<BundleStructuralInfo><BundleIsMemberOfCollection></BundleIsMemberOfCollection><BundleResources/></BundleStructuralInfo></BLAM-bundle-repository-v0.14></Components></CMD>")

                                        #Variabel which contains all input
                                        a = (cmdtag+ '\n' + headertag+'\n'+ resourcestag+'\n'+startcomp +'\n'+distittag+
                                        '\n'+descripttag+'\n'+recorddatetag+'\n'+keywordsstart+'\n'
                                        +keywordstring+'\n'+keywordsend+'\n'+objstart+'\n'+objlangdisnam+'\n'+ objlangnametag+'\n'+isotag+'\n'+glottotag+'\n'
                                        + '\n' + altnamessstart + '\n' + altnamestring + '\n' + altnamesend + '\n' +taxstringfin+ '\n' + objend+'\n'
                                        + bundloctag  + '\n' +locname+ '\n' + locfacettag + '\n' + regname+ '\n' +regfacettag+ '\n' 
                                        + countryname+ '\n'+countryfacettag+ '\n'+ countrycodetag+ '\n'+ bundlocfin+
                                        '\n' + pubyeartag+'\n'+dataprtag+'\n'+creatorstarttag+'\n'+creatorid+'\n'+creatoraff+'\n'
                                        +'\n'+ creatorstart +'\n'+ creatorfam +'\n'+creatorgive +'\n'+creatorend +'\n'+
                                        projstart +'\n'+projdisname+'\n'+projdesc+ '\n'+projend +'\n'+
                                        startad +'\n'+ access +'\n'+ ava +'\n'+lictag +'\n'+ rightsholder +'\n'+ structinfo)
                                       
                                        print(a)
                                        #Write var a in several files
                                        filetest = filename.split('.')
                                        fileoutfile= outputfolder +filetest[0] + '_spa.' + filetest[1]
                                        if os.path.exists(fileoutfile):
                                                file1 = fileoutfile.split('_spa.')
                                                fileoutfile = file1[0] + '_yuz.' + file1[1]
                                        
                                        with open(fileoutfile, 'w',encoding="utf-8") as f_out:
                                            f_out.write('{}\n'.format(a))

                                        
                                        
                                   
#FIRST STEP: Iterate through the translated_pattern files and give filenames and filenames+directory to Step 2: iteratefolder
def iteratetrans():
    for filetrans in os.listdir(transfolder):
        filetranslist = [filetrans for filetrans in os.listdir(transfolder)]
        mylisttrans = [transfolder + filetrans for filetrans in listdir(transfolder) if isfile(join(transfolder, filetrans))]  
    return filetranslist, mylisttrans
   

filetranslist, mylisttrans = iteratetrans()

iteratefolder(filetranslist, mylisttrans)