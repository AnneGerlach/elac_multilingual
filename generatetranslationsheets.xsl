<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:cmd="http://www.clarin.eu/cmd/"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="2.0">

    <!-- modify language attribute: Translation lang ="spa" or "yuz" depending on which language you want -->
    
    <xsl:template match="/">
        <xsl:call-template name="starter"/>
    </xsl:template>

    <xsl:template name="starter">
        <TranslatedElements>
            <Translation lang="spa">
                <BundleDisplayTitle>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleDisplayTitle"
                    />
                </BundleDisplayTitle>
                <BundleDescription>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleDescription"
                    />
                </BundleDescription>
                <BundleKeywords>
                    <xsl:for-each
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleKeywords/cmd:BundleKeyword">
                        <BundleKeyword>
                            <xsl:value-of select="."/>
                        </BundleKeyword>
                    </xsl:for-each>
                </BundleKeywords>
                <BundleObjectLanguages>
                    <xsl:for-each
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleObjectLanguages">
                        <xsl:call-template name="ObjectLanguage"/>
                    </xsl:for-each>
                </BundleObjectLanguages>
               
                <BundleLocation>
                    <BundleGeoLocation>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleGeoLocation"
                        />
                    </BundleGeoLocation>
                    <BundleLocationName>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleLocationName"
                        />
                    </BundleLocationName>
                    <BundleLocationFacet>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleLocationFacet"
                        />
                    </BundleLocationFacet>
                    <BundleRegionName>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleRegionName"
                        />
                    </BundleRegionName>
                    <BundleRegionFacet>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleRegionFacet"
                        />
                    </BundleRegionFacet>
                    <BundleCountryName>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleCountryName"
                        />
                    </BundleCountryName>
                    <BundleCountryFacet>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleCountryFacet"
                        />
                    </BundleCountryFacet>
                    <BundleCountryCode>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleCountryCode"
                        />
                    </BundleCountryCode>
                </BundleLocation>
                <ProjectDisplayName>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:ProjectInfo/cmd:Project/cmd:ProjectDisplayName"
                    />
                </ProjectDisplayName>
                
                <ProjectDescription>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:ProjectInfo/cmd:Project/cmd:ProjectDescription"
                    />
                </ProjectDescription>
            </Translation>
            
            <Translation lang="yuz">
                <BundleDisplayTitle>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleDisplayTitle"
                    />
                </BundleDisplayTitle>
                <BundleDescription>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleDescription"
                    />
                </BundleDescription>
                <BundleKeywords>
                    <xsl:for-each
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleKeywords/cmd:BundleKeyword">
                        <BundleKeyword>
                            <xsl:value-of select="."/>
                        </BundleKeyword>
                    </xsl:for-each>
                </BundleKeywords>
                <BundleObjectLanguages>
                    <xsl:for-each
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleObjectLanguages">
                        <xsl:call-template name="ObjectLanguage"/>
                    </xsl:for-each>
                </BundleObjectLanguages>
                
                <BundleLocation>
                    <BundleLocationName>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleLocationName"
                        />
                    </BundleLocationName>
                    <BundleLocationFacet>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleLocationFacet"
                        />
                    </BundleLocationFacet>
                    <BundleRegionName>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleRegionName"
                        />
                    </BundleRegionName>
                    <BundleRegionFacet>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleRegionFacet"
                        />
                    </BundleRegionFacet>
                    <BundleCountryName>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleCountryName"
                        />
                    </BundleCountryName>
                    <BundleCountryFacet>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleCountryFacet"
                        />
                    </BundleCountryFacet>
                    <BundleCountryCode>
                        <xsl:value-of
                            select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleLocation/cmd:BundleCountryCode"
                        />
                    </BundleCountryCode>
                </BundleLocation>
                <ProjectDisplayName>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:ProjectInfo/cmd:Project/cmd:ProjectDisplayName"
                    />
                </ProjectDisplayName>
                
                <ProjectDescription>
                    <xsl:value-of
                        select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:ProjectInfo/cmd:Project/cmd:ProjectDescription"
                    />
                </ProjectDescription>
            </Translation>
        </TranslatedElements>
    </xsl:template>

    <xsl:template name="ObjectLanguage">
        <BundleObjectLanguage>
            <xsl:for-each
                select="/cmd:CMD/cmd:Components/cmd:BLAM-bundle-repository-v0.14/cmd:BundleGeneralInfo/cmd:BundleObjectLanguages/cmd:BundleObjectLanguage">
                <ObjectLanguageDisplayName>
                    <xsl:value-of select="./cmd:ObjectLanguageDisplayName"/>
                </ObjectLanguageDisplayName>
                <ObjectLanguageName>
                    <xsl:value-of select="./cmd:ObjectLanguageName"/>
                </ObjectLanguageName>
                <ObjectLanguageISO639-3Code>
                    <xsl:value-of select="./cmd:ObjectLanguageISO639-3Code"/>
                </ObjectLanguageISO639-3Code>
                <ObjectLanguageGlottologCode>
                    <xsl:value-of select="./cmd:ObjectLanguageGlottologCode"/>
                </ObjectLanguageGlottologCode>
                <ObjectLanguageAlternativeNames>
                    <xsl:for-each
                        select="./cmd:ObjectLanguageAlternativeNames/cmd:ObjectLanguageAlternativeName">
                        <ObjectLanguageAlternativeName>
                            <xsl:value-of select="."/>
                        </ObjectLanguageAlternativeName>
                    </xsl:for-each>
                </ObjectLanguageAlternativeNames>
                <ObjectLanguageTaxonomy>
                    <xsl:for-each
                        select="./cmd:ObjectLanguageTaxonomy/cmd:ObjectLanguageLanguageFamily">
                        <ObjectLanguageLanguageFamily>
                            <xsl:value-of select="."/>
                        </ObjectLanguageLanguageFamily>
                    </xsl:for-each>
                </ObjectLanguageTaxonomy>
            </xsl:for-each>
        </BundleObjectLanguage>
    </xsl:template>
</xsl:stylesheet>
