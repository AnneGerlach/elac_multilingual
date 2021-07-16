<?xml version="1.0" encoding="UTF-8"?>

<p:declare-step version="1.0" xmlns:p="http://www.w3.org/ns/xproc"
    xmlns:c="http://www.w3.org/ns/xproc-step" exclude-inline-prefixes="#all" name="main">


    <!-- create context for p:variable with base-uri pointing to the location of this file -->
    <p:input port="source">
        <p:inline>
            <x/>
        </p:inline>
    </p:input>
    
    <!-- any params passed in from outside get passed through to p:xslt automatically! -->
    <p:input port="parameters" kind="parameter"/>
    <p:output port="result" primary="true"/>
    
    <!-- configuration options for steering input and output -->
    <p:option name="input-dir" select="'./bundle_blams_eng/'"/>
    <p:option name="input-filter" select="'.*\.xml$'"/>
    <p:option name="output-dir" select="'./translate_pattern/'"/>
 
    <!-- resolve any path to base uri of this file, to make sure they are absolute -->
    <p:variable name="abs-input-dir" select="resolve-uri($input-dir, base-uri(/))"/>
    <p:variable name="abs-output-dir" select="resolve-uri($output-dir, base-uri(/))"/>

    <!-- first step: get list of all files in input-dir -->
    <p:directory-list>
        <p:with-option name="path" select="$abs-input-dir"/>
    </p:directory-list>

    <!-- iterate over each file to load it -->
    <p:for-each>
        <p:iteration-source select="//c:file[matches(@name, $input-filter)]"/>
        <p:variable name="filename" select="tokenize(resolve-uri(/c:file/@name, $abs-input-dir), '/')[last()]"/>
        <p:load>
            <p:with-option name="href" select="resolve-uri(/c:file/@name, $abs-input-dir)"/>
        </p:load>
        <p:xslt>
            <p:input port="stylesheet">
                <p:pipe step="style" port="result"/>
            </p:input>
        </p:xslt> 
        <p:store>
            <p:with-option name="href" select="concat($output-dir, replace($filename, '\.xml', '_translate.xml'))"/>
        </p:store>
    </p:for-each>
   
    <!-- loading of the stylesheet.. -->
    <p:load href="generatetranslationsheets.xsl" name="style"/>

</p:declare-step>

