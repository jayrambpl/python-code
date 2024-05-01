
def EmailBody_new(supply_file,report_date, bench_count, upcoming_bench_count, total_count, available_within_15_days,available_in_16_to_30_days , available_in_31_to_60_days, available_in_61_to_90_days, available_after_90_days):
    msg = f"""
        <html xmlns:v="urn:schemas-microsoft-com:vml"
        xmlns:o="urn:schemas-microsoft-com:office:office"
        xmlns:w="urn:schemas-microsoft-com:office:word"
        xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
        xmlns="http://www.w3.org/TR/REC-html40">

        <head>
        <meta http-equiv=Content-Type content="text/html; charset=windows-1252">
        <meta name=ProgId content=Word.Document>
        <meta name=Generator content="Microsoft Word 15">
        <meta name=Originator content="Microsoft Word 15">
        <link rel=File-List href="email_temp_files/filelist.xml">
        <!--[if gte mso 9]><xml>
        <o:DocumentProperties>
        <o:Author>JAYRAM SINGH</o:Author>
        <o:LastAuthor>JAYRAM SINGH</o:LastAuthor>
        <o:Revision>1</o:Revision>
        <o:TotalTime>3</o:TotalTime>
        <o:Created>2024-01-08T08:14:00Z</o:Created>
        <o:LastSaved>2024-01-08T08:20:00Z</o:LastSaved>
        <o:Pages>1</o:Pages>
        <o:Words>80</o:Words>
        <o:Characters>461</o:Characters>
        <o:Company>IBM Corporation</o:Company>
        <o:Lines>3</o:Lines>
        <o:Paragraphs>1</o:Paragraphs>
        <o:CharactersWithSpaces>540</o:CharactersWithSpaces>
        <o:Version>16.00</o:Version>
        </o:DocumentProperties>
        <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        </o:OfficeDocumentSettings>
        </xml><![endif]-->
        <link rel=themeData href="email_temp_files/themedata.thmx">
        <link rel=colorSchemeMapping href="email_temp_files/colorschememapping.xml">
        <!--[if gte mso 9]><xml>
        <w:WordDocument>
        <w:SpellingState>Clean</w:SpellingState>
        <w:GrammarState>Clean</w:GrammarState>
        <w:TrackMoves>false</w:TrackMoves>
        <w:TrackFormatting/>
        <w:PunctuationKerning/>
        <w:ValidateAgainstSchemas/>
        <w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
        <w:IgnoreMixedContent>false</w:IgnoreMixedContent>
        <w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
        <w:DoNotPromoteQF/>
        <w:LidThemeOther>EN-IN</w:LidThemeOther>
        <w:LidThemeAsian>X-NONE</w:LidThemeAsian>
        <w:LidThemeComplexScript>HI</w:LidThemeComplexScript>
        <w:Compatibility>
        <w:BreakWrappedTables/>
        <w:SnapToGridInCell/>
        <w:WrapTextWithPunct/>
        <w:UseAsianBreakRules/>
        <w:DontGrowAutofit/>
        <w:SplitPgBreakAndParaMark/>
        <w:EnableOpenTypeKerning/>
        <w:DontFlipMirrorIndents/>
        <w:OverrideTableStyleHps/>
        </w:Compatibility>
        <m:mathPr>
        <m:mathFont m:val="Cambria Math"/>
        <m:brkBin m:val="before"/>
        <m:brkBinSub m:val="&#45;-"/>
        <m:smallFrac m:val="off"/>
        <m:dispDef/>
        <m:lMargin m:val="0"/>
        <m:rMargin m:val="0"/>
        <m:defJc m:val="centerGroup"/>
        <m:wrapIndent m:val="1440"/>
        <m:intLim m:val="subSup"/>
        <m:naryLim m:val="undOvr"/>
        </m:mathPr></w:WordDocument>
        </xml><![endif]--><!--[if gte mso 9]><xml>
        <w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="false"
        DefSemiHidden="false" DefQFormat="false" DefPriority="99"
        LatentStyleCount="376">
        <w:LsdException Locked="false" Priority="0" QFormat="true" Name="Normal"/>
        <w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 1"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 2"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 3"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 4"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 5"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 6"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 7"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 8"/>
        <w:LsdException Locked="false" Priority="9" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="heading 9"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 6"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 7"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 8"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index 9"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 1"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 2"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 3"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 4"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 5"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 6"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 7"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 8"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" Name="toc 9"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Normal Indent"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="footnote text"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="annotation text"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="header"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="footer"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="index heading"/>
        <w:LsdException Locked="false" Priority="35" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="caption"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="table of figures"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="envelope address"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="envelope return"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="footnote reference"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="annotation reference"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="line number"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="page number"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="endnote reference"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="endnote text"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="table of authorities"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="macro"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="toa heading"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Bullet"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Number"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Bullet 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Bullet 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Bullet 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Bullet 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Number 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Number 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Number 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Number 5"/>
        <w:LsdException Locked="false" Priority="10" QFormat="true" Name="Title"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Closing"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Signature"/>
        <w:LsdException Locked="false" Priority="1" SemiHidden="true"
        UnhideWhenUsed="true" Name="Default Paragraph Font"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text Indent"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Continue"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Continue 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Continue 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Continue 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="List Continue 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Message Header"/>
        <w:LsdException Locked="false" Priority="11" QFormat="true" Name="Subtitle"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Salutation"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Date"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text First Indent"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text First Indent 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Note Heading"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text Indent 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Body Text Indent 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Block Text"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Hyperlink"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="FollowedHyperlink"/>
        <w:LsdException Locked="false" Priority="22" QFormat="true" Name="Strong"/>
        <w:LsdException Locked="false" Priority="20" QFormat="true" Name="Emphasis"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Document Map"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Plain Text"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="E-mail Signature"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Top of Form"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Bottom of Form"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Normal (Web)"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Acronym"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Address"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Cite"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Code"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Definition"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Keyboard"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Preformatted"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Sample"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Typewriter"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="HTML Variable"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Normal Table"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="annotation subject"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="No List"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Outline List 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Outline List 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Outline List 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Simple 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Simple 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Simple 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Classic 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Classic 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Classic 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Classic 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Colorful 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Colorful 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Colorful 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Columns 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Columns 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Columns 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Columns 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Columns 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 6"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 7"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Grid 8"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 4"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 5"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 6"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 7"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table List 8"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table 3D effects 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table 3D effects 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table 3D effects 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Contemporary"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Elegant"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Professional"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Subtle 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Subtle 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Web 1"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Web 2"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Web 3"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Balloon Text"/>
        <w:LsdException Locked="false" Priority="39" Name="Table Grid"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Table Theme"/>
        <w:LsdException Locked="false" SemiHidden="true" Name="Placeholder Text"/>
        <w:LsdException Locked="false" Priority="1" QFormat="true" Name="No Spacing"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 1"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List Accent 1"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 1"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 1"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 1"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 1"/>
        <w:LsdException Locked="false" SemiHidden="true" Name="Revision"/>
        <w:LsdException Locked="false" Priority="34" QFormat="true"
        Name="List Paragraph"/>
        <w:LsdException Locked="false" Priority="29" QFormat="true" Name="Quote"/>
        <w:LsdException Locked="false" Priority="30" QFormat="true"
        Name="Intense Quote"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 1"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 1"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 1"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 1"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 1"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 1"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 1"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 1"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 2"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List Accent 2"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 2"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 2"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 2"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 2"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 2"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 2"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 2"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 2"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 2"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 2"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 2"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 2"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 3"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List Accent 3"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 3"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 3"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 3"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 3"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 3"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 3"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 3"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 3"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 3"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 3"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 3"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 3"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 4"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List Accent 4"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 4"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 4"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 4"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 4"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 4"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 4"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 4"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 4"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 4"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 4"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 4"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 4"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 5"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List Accent 5"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 5"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 5"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 5"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 5"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 5"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 5"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 5"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 5"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 5"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 5"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 5"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 5"/>
        <w:LsdException Locked="false" Priority="60" Name="Light Shading Accent 6"/>
        <w:LsdException Locked="false" Priority="61" Name="Light List Accent 6"/>
        <w:LsdException Locked="false" Priority="62" Name="Light Grid Accent 6"/>
        <w:LsdException Locked="false" Priority="63" Name="Medium Shading 1 Accent 6"/>
        <w:LsdException Locked="false" Priority="64" Name="Medium Shading 2 Accent 6"/>
        <w:LsdException Locked="false" Priority="65" Name="Medium List 1 Accent 6"/>
        <w:LsdException Locked="false" Priority="66" Name="Medium List 2 Accent 6"/>
        <w:LsdException Locked="false" Priority="67" Name="Medium Grid 1 Accent 6"/>
        <w:LsdException Locked="false" Priority="68" Name="Medium Grid 2 Accent 6"/>
        <w:LsdException Locked="false" Priority="69" Name="Medium Grid 3 Accent 6"/>
        <w:LsdException Locked="false" Priority="70" Name="Dark List Accent 6"/>
        <w:LsdException Locked="false" Priority="71" Name="Colorful Shading Accent 6"/>
        <w:LsdException Locked="false" Priority="72" Name="Colorful List Accent 6"/>
        <w:LsdException Locked="false" Priority="73" Name="Colorful Grid Accent 6"/>
        <w:LsdException Locked="false" Priority="19" QFormat="true"
        Name="Subtle Emphasis"/>
        <w:LsdException Locked="false" Priority="21" QFormat="true"
        Name="Intense Emphasis"/>
        <w:LsdException Locked="false" Priority="31" QFormat="true"
        Name="Subtle Reference"/>
        <w:LsdException Locked="false" Priority="32" QFormat="true"
        Name="Intense Reference"/>
        <w:LsdException Locked="false" Priority="33" QFormat="true" Name="Book Title"/>
        <w:LsdException Locked="false" Priority="37" SemiHidden="true"
        UnhideWhenUsed="true" Name="Bibliography"/>
        <w:LsdException Locked="false" Priority="39" SemiHidden="true"
        UnhideWhenUsed="true" QFormat="true" Name="TOC Heading"/>
        <w:LsdException Locked="false" Priority="41" Name="Plain Table 1"/>
        <w:LsdException Locked="false" Priority="42" Name="Plain Table 2"/>
        <w:LsdException Locked="false" Priority="43" Name="Plain Table 3"/>
        <w:LsdException Locked="false" Priority="44" Name="Plain Table 4"/>
        <w:LsdException Locked="false" Priority="45" Name="Plain Table 5"/>
        <w:LsdException Locked="false" Priority="40" Name="Grid Table Light"/>
        <w:LsdException Locked="false" Priority="46" Name="Grid Table 1 Light"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark"/>
        <w:LsdException Locked="false" Priority="51" Name="Grid Table 6 Colorful"/>
        <w:LsdException Locked="false" Priority="52" Name="Grid Table 7 Colorful"/>
        <w:LsdException Locked="false" Priority="46"
        Name="Grid Table 1 Light Accent 1"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 1"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 1"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 1"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 1"/>
        <w:LsdException Locked="false" Priority="51"
        Name="Grid Table 6 Colorful Accent 1"/>
        <w:LsdException Locked="false" Priority="52"
        Name="Grid Table 7 Colorful Accent 1"/>
        <w:LsdException Locked="false" Priority="46"
        Name="Grid Table 1 Light Accent 2"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 2"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 2"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 2"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 2"/>
        <w:LsdException Locked="false" Priority="51"
        Name="Grid Table 6 Colorful Accent 2"/>
        <w:LsdException Locked="false" Priority="52"
        Name="Grid Table 7 Colorful Accent 2"/>
        <w:LsdException Locked="false" Priority="46"
        Name="Grid Table 1 Light Accent 3"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 3"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 3"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 3"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 3"/>
        <w:LsdException Locked="false" Priority="51"
        Name="Grid Table 6 Colorful Accent 3"/>
        <w:LsdException Locked="false" Priority="52"
        Name="Grid Table 7 Colorful Accent 3"/>
        <w:LsdException Locked="false" Priority="46"
        Name="Grid Table 1 Light Accent 4"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 4"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 4"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 4"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 4"/>
        <w:LsdException Locked="false" Priority="51"
        Name="Grid Table 6 Colorful Accent 4"/>
        <w:LsdException Locked="false" Priority="52"
        Name="Grid Table 7 Colorful Accent 4"/>
        <w:LsdException Locked="false" Priority="46"
        Name="Grid Table 1 Light Accent 5"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 5"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 5"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 5"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 5"/>
        <w:LsdException Locked="false" Priority="51"
        Name="Grid Table 6 Colorful Accent 5"/>
        <w:LsdException Locked="false" Priority="52"
        Name="Grid Table 7 Colorful Accent 5"/>
        <w:LsdException Locked="false" Priority="46"
        Name="Grid Table 1 Light Accent 6"/>
        <w:LsdException Locked="false" Priority="47" Name="Grid Table 2 Accent 6"/>
        <w:LsdException Locked="false" Priority="48" Name="Grid Table 3 Accent 6"/>
        <w:LsdException Locked="false" Priority="49" Name="Grid Table 4 Accent 6"/>
        <w:LsdException Locked="false" Priority="50" Name="Grid Table 5 Dark Accent 6"/>
        <w:LsdException Locked="false" Priority="51"
        Name="Grid Table 6 Colorful Accent 6"/>
        <w:LsdException Locked="false" Priority="52"
        Name="Grid Table 7 Colorful Accent 6"/>
        <w:LsdException Locked="false" Priority="46" Name="List Table 1 Light"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark"/>
        <w:LsdException Locked="false" Priority="51" Name="List Table 6 Colorful"/>
        <w:LsdException Locked="false" Priority="52" Name="List Table 7 Colorful"/>
        <w:LsdException Locked="false" Priority="46"
        Name="List Table 1 Light Accent 1"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 1"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 1"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 1"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 1"/>
        <w:LsdException Locked="false" Priority="51"
        Name="List Table 6 Colorful Accent 1"/>
        <w:LsdException Locked="false" Priority="52"
        Name="List Table 7 Colorful Accent 1"/>
        <w:LsdException Locked="false" Priority="46"
        Name="List Table 1 Light Accent 2"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 2"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 2"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 2"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 2"/>
        <w:LsdException Locked="false" Priority="51"
        Name="List Table 6 Colorful Accent 2"/>
        <w:LsdException Locked="false" Priority="52"
        Name="List Table 7 Colorful Accent 2"/>
        <w:LsdException Locked="false" Priority="46"
        Name="List Table 1 Light Accent 3"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 3"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 3"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 3"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 3"/>
        <w:LsdException Locked="false" Priority="51"
        Name="List Table 6 Colorful Accent 3"/>
        <w:LsdException Locked="false" Priority="52"
        Name="List Table 7 Colorful Accent 3"/>
        <w:LsdException Locked="false" Priority="46"
        Name="List Table 1 Light Accent 4"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 4"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 4"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 4"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 4"/>
        <w:LsdException Locked="false" Priority="51"
        Name="List Table 6 Colorful Accent 4"/>
        <w:LsdException Locked="false" Priority="52"
        Name="List Table 7 Colorful Accent 4"/>
        <w:LsdException Locked="false" Priority="46"
        Name="List Table 1 Light Accent 5"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 5"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 5"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 5"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 5"/>
        <w:LsdException Locked="false" Priority="51"
        Name="List Table 6 Colorful Accent 5"/>
        <w:LsdException Locked="false" Priority="52"
        Name="List Table 7 Colorful Accent 5"/>
        <w:LsdException Locked="false" Priority="46"
        Name="List Table 1 Light Accent 6"/>
        <w:LsdException Locked="false" Priority="47" Name="List Table 2 Accent 6"/>
        <w:LsdException Locked="false" Priority="48" Name="List Table 3 Accent 6"/>
        <w:LsdException Locked="false" Priority="49" Name="List Table 4 Accent 6"/>
        <w:LsdException Locked="false" Priority="50" Name="List Table 5 Dark Accent 6"/>
        <w:LsdException Locked="false" Priority="51"
        Name="List Table 6 Colorful Accent 6"/>
        <w:LsdException Locked="false" Priority="52"
        Name="List Table 7 Colorful Accent 6"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Mention"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Smart Hyperlink"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Hashtag"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Unresolved Mention"/>
        <w:LsdException Locked="false" SemiHidden="true" UnhideWhenUsed="true"
        Name="Smart Link"/>
        </w:LatentStyles>
        </xml><![endif]-->
        <style>
        <!--
        /* Font Definitions */
        @font-face
            {{font-family:"Cambria Math";
            panose-1:2 4 5 3 5 4 6 3 2 4;
            mso-font-charset:0;
            mso-generic-font-family:roman;
            mso-font-pitch:variable;
            mso-font-signature:-536869121 1107305727 33554432 0 415 0;}}
        @font-face
            {{font-family:Calibri;
            panose-1:2 15 5 2 2 2 4 3 2 4;
            mso-font-charset:0;
            mso-generic-font-family:swiss;
            mso-font-pitch:variable;
            mso-font-signature:-469750017 -1040178053 9 0 511 0;}}
        @font-face
            {{font-family:"IBM Plex Sans";
            panose-1:2 11 5 3 5 2 3 0 2 3;
            mso-font-charset:0;
            mso-generic-font-family:swiss;
            mso-font-pitch:variable;
            mso-font-signature:-1610611985 1342185531 0 0 415 0;}}
        /* Style Definitions */
        p.MsoNormal, li.MsoNormal, div.MsoNormal
            {{mso-style-unhide:no;
            mso-style-qformat:yes;
            mso-style-parent:"";
            margin:0cm;
            mso-pagination:widow-orphan;
            font-size:11.0pt;
            font-family:"Calibri",sans-serif;
            mso-fareast-font-family:Calibri;
            mso-fareast-theme-font:minor-latin;}}
        span.SpellE
            {{mso-style-name:"";
            mso-spl-e:yes;}}
        .MsoChpDefault
            {{mso-style-type:export-only;
            mso-default-props:yes;
            mso-bidi-font-size:11.0pt;
            font-family:"Calibri",sans-serif;
            mso-ascii-font-family:Calibri;
            mso-ascii-theme-font:minor-latin;
            mso-fareast-font-family:Calibri;
            mso-fareast-theme-font:minor-latin;
            mso-hansi-font-family:Calibri;
            mso-hansi-theme-font:minor-latin;
            mso-bidi-font-family:Mangal;
            mso-bidi-theme-font:minor-bidi;
            mso-fareast-language:EN-US;
            mso-bidi-language:AR-SA;}}
        .MsoPapDefault
            {{mso-style-type:export-only;
            margin-bottom:8.0pt;
            line-height:107%;}}
        @page WordSection1
            {{size:595.3pt 841.9pt;
            margin:72.0pt 72.0pt 72.0pt 72.0pt;
            mso-header-margin:35.4pt;
            mso-footer-margin:35.4pt;
            mso-paper-source:0;}}
        div.WordSection1
            {{page:WordSection1;}}
        -->
        </style>
        <!--[if gte mso 10]>
        <style>
        /* Style Definitions */
        table.MsoNormalTable
            {{mso-style-name:"Table Normal";
            mso-tstyle-rowband-size:0;
            mso-tstyle-colband-size:0;
            mso-style-noshow:yes;
            mso-style-priority:99;
            mso-style-parent:"";
            mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
            mso-para-margin-top:0cm;
            mso-para-margin-right:0cm;
            mso-para-margin-bottom:8.0pt;
            mso-para-margin-left:0cm;
            line-height:107%;
            mso-pagination:widow-orphan;
            font-size:11.0pt;
            font-family:"Calibri",sans-serif;
            mso-ascii-font-family:Calibri;
            mso-ascii-theme-font:minor-latin;
            mso-hansi-font-family:Calibri;
            mso-hansi-theme-font:minor-latin;
            mso-bidi-font-family:Mangal;
            mso-bidi-theme-font:minor-bidi;
            mso-font-kerning:1.0pt;
            mso-ligatures:standardcontextual;
            mso-fareast-language:EN-US;
            mso-bidi-language:AR-SA;}}
        table.MsoTable15Grid4Accent1
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-tstyle-rowband-size:1;
            mso-tstyle-colband-size:1;
            mso-style-priority:49;
            mso-style-unhide:no;
            border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;
            mso-border-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;
            mso-border-themecolor:accent1;
            mso-border-themetint:153;
            mso-padding-alt:0cm 5.4pt 0cm 5.4pt;
            mso-border-insideh:.5pt solid #8EAADB;
            mso-border-insideh-themecolor:accent1;
            mso-border-insideh-themetint:153;
            mso-border-insidev:.5pt solid #8EAADB;
            mso-border-insidev-themecolor:accent1;
            mso-border-insidev-themetint:153;
            mso-para-margin:0cm;
            mso-pagination:widow-orphan;
            font-size:11.0pt;
            font-family:"Calibri",sans-serif;
            mso-ascii-font-family:Calibri;
            mso-ascii-theme-font:minor-latin;
            mso-hansi-font-family:Calibri;
            mso-hansi-theme-font:minor-latin;
            mso-bidi-font-family:Mangal;
            mso-bidi-theme-font:minor-bidi;
            mso-font-kerning:1.0pt;
            mso-ligatures:standardcontextual;
            mso-fareast-language:EN-US;
            mso-bidi-language:AR-SA;}}
        table.MsoTable15Grid4Accent1FirstRow
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-table-condition:first-row;
            mso-style-priority:49;
            mso-style-unhide:no;
            mso-tstyle-shading:#4472C4;
            mso-tstyle-shading-themecolor:accent1;
            mso-tstyle-border-top:.5pt solid #4472C4;
            mso-tstyle-border-top-themecolor:accent1;
            mso-tstyle-border-left:.5pt solid #4472C4;
            mso-tstyle-border-left-themecolor:accent1;
            mso-tstyle-border-bottom:.5pt solid #4472C4;
            mso-tstyle-border-bottom-themecolor:accent1;
            mso-tstyle-border-right:.5pt solid #4472C4;
            mso-tstyle-border-right-themecolor:accent1;
            mso-tstyle-border-insideh:cell-none;
            mso-tstyle-border-insidev:cell-none;
            color:white;
            mso-themecolor:background1;
            mso-ansi-font-weight:bold;
            mso-bidi-font-weight:bold;}}
        table.MsoTable15Grid4Accent1LastRow
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-table-condition:last-row;
            mso-style-priority:49;
            mso-style-unhide:no;
            mso-tstyle-border-top:1.5pt double #4472C4;
            mso-tstyle-border-top-themecolor:accent1;
            mso-ansi-font-weight:bold;
            mso-bidi-font-weight:bold;}}
        table.MsoTable15Grid4Accent1FirstCol
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-table-condition:first-column;
            mso-style-priority:49;
            mso-style-unhide:no;
            mso-ansi-font-weight:bold;
            mso-bidi-font-weight:bold;}}
        table.MsoTable15Grid4Accent1LastCol
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-table-condition:last-column;
            mso-style-priority:49;
            mso-style-unhide:no;
            mso-ansi-font-weight:bold;
            mso-bidi-font-weight:bold;}}
        table.MsoTable15Grid4Accent1OddColumn
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-table-condition:odd-column;
            mso-style-priority:49;
            mso-style-unhide:no;
            mso-tstyle-shading:#D9E2F3;
            mso-tstyle-shading-themecolor:accent1;
            mso-tstyle-shading-themetint:51;}}
        table.MsoTable15Grid4Accent1OddRow
            {{mso-style-name:"Grid Table 4 - Accent 1";
            mso-table-condition:odd-row;
            mso-style-priority:49;
            mso-style-unhide:no;
            mso-tstyle-shading:#D9E2F3;
            mso-tstyle-shading-themecolor:accent1;
            mso-tstyle-shading-themetint:51;}}
        </style>
        <![endif]--><!--[if gte mso 9]><xml>
        <o:shapedefaults v:ext="edit" spidmax="1026"/>
        </xml><![endif]--><!--[if gte mso 9]><xml>
        <o:shapelayout v:ext="edit">
        <o:idmap v:ext="edit" data="1"/>
        </o:shapelayout></xml><![endif]-->
        </head>

        <body lang=EN-IN style='tab-interval:36.0pt;word-wrap:break-word'>

        <div class=WordSection1>

        <table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 align=left
        width=528 style='width:396.0pt;background:#F2F2F2;mso-background-themecolor:
        background1;mso-background-themeshade:242;border-collapse:collapse;mso-yfti-tbllook:
        1184;mso-table-lspace:2.25pt;mso-table-rspace:2.25pt;mso-table-anchor-vertical:
        paragraph;mso-table-anchor-horizontal:column;mso-table-left:left;mso-padding-alt:
        0cm 0cm 0cm 0cm'>
        <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:12.0pt'>
        <td style='padding:0cm 0cm 0cm 0cm;height:12.0pt'>
        <p class=MsoNormal style='line-height:.75pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:1.0pt;mso-fareast-font-family:
        "Times New Roman";color:black;mso-color-alt:windowtext'>&nbsp;</span><span
        style='font-size:1.0pt;mso-fareast-font-family:"Times New Roman"'><o:p></o:p></span></p>
        </td>
        </tr>
        <tr style='mso-yfti-irow:1'>
        <td valign=top style='padding:0cm 0cm 0cm 0cm'>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><b><span style='font-size:18.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'>IoT Bench Data</span></b><span
        style='font-size:14.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
        "Times New Roman";color:#525252'> </span><u><span style='font-size:12.0pt;
        font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
        color:#525252'></span></u><span style='font-size:12.0pt;
        font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
        color:#525252'><o:p></o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'><o:p>&nbsp;</o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'>As on <b>{report_date}</b><o:p></o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'><o:p>&nbsp;</o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'>Team,&nbsp; <br>
        <br>
        Please find attached IoT bench data report as on today based on [{supply_file}]. <br>
        <br>
        Summary:<o:p></o:p></span></p>
        <table class=MsoTable15Grid4Accent1 border=1 cellspacing=0 cellpadding=0
        style='border-collapse:collapse;border:none;mso-border-alt:solid #8EAADB .5pt;
        mso-border-themecolor:accent1;mso-border-themetint:153;mso-yfti-tbllook:
        1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
        <tr style='mso-yfti-irow:-1;mso-yfti-firstrow:yes;mso-yfti-lastfirstrow:
            yes'>
            <td width=59 valign=top style='width:44.25pt;border:solid #4472C4 1.0pt;
            mso-border-themecolor:accent1;border-right:none;mso-border-top-alt:solid #4472C4 .5pt;
            mso-border-top-themecolor:accent1;mso-border-left-alt:solid #4472C4 .5pt;
            mso-border-left-themecolor:accent1;mso-border-bottom-alt:solid #4472C4 .5pt;
            mso-border-bottom-themecolor:accent1;background:#4472C4;mso-background-themecolor:
            accent1;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:5;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:white;mso-themecolor:background1'>Sn.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:solid #4472C4 1.0pt;
            mso-border-top-themecolor:accent1;border-left:none;border-bottom:solid #4472C4 1.0pt;
            mso-border-bottom-themecolor:accent1;border-right:none;mso-border-top-alt:
            solid #4472C4 .5pt;mso-border-top-themecolor:accent1;mso-border-bottom-alt:
            solid #4472C4 .5pt;mso-border-bottom-themecolor:accent1;background:#4472C4;
            mso-background-themecolor:accent1;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:1;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:white;mso-themecolor:background1'>Head<o:p></o:p></span></b></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border:solid #4472C4 1.0pt;
            mso-border-themecolor:accent1;border-left:none;mso-border-top-alt:solid #4472C4 .5pt;
            mso-border-top-themecolor:accent1;mso-border-bottom-alt:solid #4472C4 .5pt;
            mso-border-bottom-themecolor:accent1;mso-border-right-alt:solid #4472C4 .5pt;
            mso-border-right-themecolor:accent1;background:#4472C4;mso-background-themecolor:
            accent1;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:1;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:white;mso-themecolor:background1'>Count<o:p></o:p></span></b></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:0'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;background:#D9E2F3;mso-background-themecolor:
            accent1;mso-background-themetint:51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:68;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>1.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><b><span style='font-size:12.0pt;
            font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'>Bench Count<o:p></o:p></span></b></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{bench_count}<o:p></o:p></span></b></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:1'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:4;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>2.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
            mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
            mso-height-rule:exactly'><b><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
            mso-fareast-font-family:"Times New Roman";color:#525252'>Upcoming Bench
            Count<o:p></o:p></span></b></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{upcoming_bench_count}<o:p></o:p></span></b></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:2'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;background:#D9E2F3;mso-background-themecolor:
            accent1;mso-background-themetint:51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:68;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>3.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><b><span style='font-size:12.0pt;
            font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'>Total Count<o:p></o:p></span></b></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{total_count}<o:p></o:p></span></b></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:3'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:4;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>4.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
            mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
            mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
            mso-fareast-font-family:"Times New Roman";color:#525252'>Available within
            15 days<o:p></o:p></span></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{available_within_15_days}<o:p></o:p></span></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:4'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;background:#D9E2F3;mso-background-themecolor:
            accent1;mso-background-themetint:51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:68;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>5.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:
            "IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'>Available in 16 to 30 days<o:p></o:p></span></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{available_in_16_to_30_days}<o:p></o:p></span></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:5'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:4;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>6.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
            mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
            mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
            mso-fareast-font-family:"Times New Roman";color:#525252'>Available in 31 to
            60 days<o:p></o:p></span></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{available_in_31_to_60_days}<o:p></o:p></span></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:6'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;background:#D9E2F3;mso-background-themecolor:
            accent1;mso-background-themetint:51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:68;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>7.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:
            "IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'>Available in 61 to 90 days<o:p></o:p></span></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{available_in_61_to_90_days}<o:p></o:p></span></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:7'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-yfti-cnfc:4;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><b><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>8.<o:p></o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
            mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
            mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
            mso-fareast-font-family:"Times New Roman";color:#525252'>Available after 90
            days<o:p></o:p></span></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal align=center style='text-align:center;line-height:18.0pt;
            mso-line-height-rule:exactly;mso-element:frame;mso-element-frame-hspace:
            2.25pt;mso-element-wrap:around;mso-element-anchor-vertical:paragraph;
            mso-element-anchor-horizontal:column;mso-height-rule:exactly'><span
            style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
            "Times New Roman";color:#525252'>{available_after_90_days}<o:p></o:p></span></p>
            </td>
        </tr>
        <tr style='mso-yfti-irow:8;mso-yfti-lastrow:yes'>
            <td width=59 valign=top style='width:44.25pt;border:solid #8EAADB 1.0pt;
            mso-border-themecolor:accent1;mso-border-themetint:153;border-top:none;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:
            accent1;mso-border-themetint:153;background:#D9E2F3;mso-background-themecolor:
            accent1;mso-background-themetint:51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:68;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><b><span style='font-size:12.0pt;
            font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'><o:p>&nbsp;</o:p></span></b></p>
            </td>
            <td width=331 valign=top style='width:248.05pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:
            "IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'><o:p>&nbsp;</o:p></span></p>
            </td>
            <td width=137 valign=top style='width:102.9pt;border-top:none;border-left:
            none;border-bottom:solid #8EAADB 1.0pt;mso-border-bottom-themecolor:accent1;
            mso-border-bottom-themetint:153;border-right:solid #8EAADB 1.0pt;
            mso-border-right-themecolor:accent1;mso-border-right-themetint:153;
            mso-border-top-alt:solid #8EAADB .5pt;mso-border-top-themecolor:accent1;
            mso-border-top-themetint:153;mso-border-left-alt:solid #8EAADB .5pt;
            mso-border-left-themecolor:accent1;mso-border-left-themetint:153;
            mso-border-alt:solid #8EAADB .5pt;mso-border-themecolor:accent1;mso-border-themetint:
            153;background:#D9E2F3;mso-background-themecolor:accent1;mso-background-themetint:
            51;padding:0cm 5.4pt 0cm 5.4pt'>
            <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
            mso-yfti-cnfc:64;mso-element:frame;mso-element-frame-hspace:2.25pt;
            mso-element-wrap:around;mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:
            column;mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:
            "IBM Plex Sans",sans-serif;mso-fareast-font-family:"Times New Roman";
            color:#525252'><o:p>&nbsp;</o:p></span></p>
            </td>
        </tr>
        </table>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'><o:p>&nbsp;</o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'>THANK YOU. <o:p></o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'>Jayram Singh<o:p></o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'>DevOps<o:p></o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;
        mso-fareast-font-family:"Times New Roman";color:#525252'><o:p>&nbsp;</o:p></span></p>
        <p class=MsoNormal style='line-height:18.0pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:9.0pt;font-family:"IBM Plex Sans",sans-serif;
        color:#525252;letter-spacing:.4pt'>This is a communication generated from code.</span><span
        style='font-size:12.0pt;font-family:"IBM Plex Sans",sans-serif;mso-fareast-font-family:
        "Times New Roman";color:#525252'><o:p></o:p></span></p>
        </td>
        </tr>
        <tr style='mso-yfti-irow:2;height:6.0pt'>
        <td style='padding:0cm 0cm 0cm 0cm;height:6.0pt'>
        <p class=MsoNormal style='line-height:.75pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:1.0pt;mso-fareast-font-family:
        "Times New Roman";color:black;mso-color-alt:windowtext;display:none;
        mso-hide:all'>&nbsp;</span><span style='font-size:1.0pt;mso-fareast-font-family:
        "Times New Roman";display:none;mso-hide:all'><o:p></o:p></span></p>
        </td>
        </tr>
        <tr style='mso-yfti-irow:3'>
        <td valign=top style='padding:0cm 0cm 0cm 0cm'>
        <table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 align=left
        width=240 style='width:180.0pt;border-collapse:collapse;display:none;
        mso-yfti-tbllook:1184;margin-left:-2.25pt;margin-right:-2.25pt;mso-table-anchor-vertical:
        paragraph;mso-table-anchor-horizontal:column;mso-table-left:left;mso-padding-alt:
        0cm 0cm 0cm 0cm'>
        <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
            display:none'>
            <td style='padding:0cm 0cm 0cm 0cm'></td>
        </tr>
        </table>
        </td>
        </tr>
        <tr style='mso-yfti-irow:4;mso-yfti-lastrow:yes'>
        <td style='padding:0cm 0cm 0cm 0cm'>
        <p class=MsoNormal style='line-height:.75pt;mso-line-height-rule:exactly;
        mso-element:frame;mso-element-frame-hspace:2.25pt;mso-element-wrap:around;
        mso-element-anchor-vertical:paragraph;mso-element-anchor-horizontal:column;
        mso-height-rule:exactly'><span style='font-size:1.0pt;mso-fareast-font-family:
        "Times New Roman";color:black;mso-color-alt:windowtext'>&nbsp;</span><span
        style='font-size:1.0pt;mso-fareast-font-family:"Times New Roman"'><o:p></o:p></span></p>
        </td>
        </tr>
        </table>

        <p class=MsoNormal><o:p>&nbsp;</o:p></p>

        </div>

        </body>

        </html> """
    return(msg)
