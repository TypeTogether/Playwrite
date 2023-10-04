# Playwrite

*Playwrite* is a typeface engine that allows the creation of primary school cursive fonts. This typeface is the practical result of the Primarium research project [www.primarium.info] which studies handwriting instruction methodologies around the world. Its findings with regards to the calligraphic models currently in use, their development and rationale, informed the design of the *Playwrite* glyphs.

The shape of the handwritten Latin alphabethas developed following different currents, trends and colonial influences around the world. As a result, the very notion of what constitutes primary school cursive writing varies dramatically. It could be vertical or slanted, fully joined or semi-joined, uppercase letters can be ornate and decorative or simply borrowed from print styles, lowercase letters can be based on round or oval foundational shapes, and the proportion of the x-height vis-a-vis the ascenders and descenders can differ. 


## Build instructions

For complete build instructions refer to
`/sources/build-models-HowTo-README.md`



## Letter variations

Based on the Primarium study the TypeTogether team isolated a limited number of structural variations for the Latin letter shapes: 8 variation styles for lower cases and three for uppercases. With the help of a sturdy contextual alternate (CALT) opentype code these different veriation groups can be seamlessly combined.


* **Precursive**.  Default set of lower case letters. These are completely unjoined.

* **Modern cursive**.  
Same design as precursive in isolated shape but it istriggers a semi-connected typesetting.
Uses .mod suffix (eg. n.mod)
* **Fully joined odern cursive**.  Adds loops to descenders and connecting strokes to letters that do not connect in .mod.Uses .jmc suffix (eg. g.jmc)

* **Full Cursive**.  Construction os several glyphs change to match a continuous cursive style.Uses .ful suffix (eg. s.ful)

* **Speed loops**.  Adds speedloops to most letters with ascender strokes.Uses .lop suffix (eg. h.lop)

* **Curved entry stroke**.  Changes the lead-in connection at x-heigh level for several letters.Uses .cnt suffix (eg. n.cnt)

* **Mirrored loops**.  
Adds loops in to two letters and switches loop direction in “f”.Uses .mrr suffix (eg. f.mrr)

* **Microloops**.  Adds knots or small loops to mark stroke direction change in some letters.Uses .mlp suffix (eg. o.mlp)

* **Print**.  Default set of upper case letters. These are completely unjoined.

* **Cursive uppercases**.  Cursive capitals. SAlso enable connection with a number of lowercase lettersUses .cur suffix (eg. A.cur)

* **Decorative uppercases**.  Secondary set of decorative capitals to match certain handwriting models. These are semi-connected.Uses .dec suffix (eg. G.dec)



## Design variation axes

Playwrite's design space spans over four variation axes: the slant of the letters, ascender and descender length, typographic color, and a stroke speed axes that controls the tension of the curves and the direction and connection of the strokes.

Weight axis   
`wght
Min: 100
Max: 400`

Slant axis.  
`slnt
Min: 0
Max: 18`

Speed axis   
`SPED
Min: 0
Max: 100`

Extension axis.  
`YEXT
Min: 375
Max: 1000`



## Country recipes

Recipes for regional models of the Playwrite font arecreated by recipes that reside on a CSV file `Playwrite/sources/data/models-all.csv`. Each row of the file contains the data that names the font model, specifies a location in three of the founr axes (the weight axis always remains variable), and contains a selection of the of the letter variants that are preferred in that region.

Structure of each row is as follows:   
`Country;lang_tag;slnt;EXTD;SPED;UC;lc`

The classes UC and lc must contain the exact number of glyphs that is expected in the substitution classes, and in the correct order:   
`@UC = [A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AE Eth IJ Eng OE Thorn Germandbls];  ` 

`@lc = [a b c d e f g h i j k l m n o p q r s t u v w x y z ae eth ij eng oe thorn germandbls idotless jdotless];`

Here is an example of the recipe used for the Canada Playwrite Font:   
`Canada;CAN;18;496;100;A.cur_locl B.dec C.cur D.dec E.cur F.dec G.dec H.dec I.cur J.cur K.dec L.dec M.cur N.cur O.dec P.dec Q.cur R.dec S.cur T.dec U.cur V.cur W.cur X.cur Y.cur Z.cur AE.cur Eth IJ.cur Eng OE.cur Thorn Germandbls;a.mod b.lop c.mod d.mod e.ful f.mrr g.jmc h.lop i.mod j.jmc k.lop l.lop m.cnt n.cnt o.mod p.mrr_ca q.mrr r.ful s.ful t.mod u.mod v.cnt w.cnt x.ful y.cnt z.cnt ae.ful eth.mod ij.jmc eng oe.ful thorn.jmc germandbls.jmc idotless.mod jdotless.jmc `

## List of fonts by region

| Country | Tag | Variant | Family name |
| --- | --- | --- | --- |
| Argentina | ARG |  | Playwrite ARG |
| Australia | AUS | NSW | Playwrite AUS NSW |
| Australia | AUS | QLD | Playwrite AUS QLD |
| Australia | AUS | SA | Playwrite AUS SA |
| Australia | AUS | TAS | Playwrite AUS TAS |
| Australia | AUS | VIC | Playwrite AUS VIC |
| Belgium | BEL | WAL | Playwrite BEL WAL |
| Belgium | BEL | VLG | Playwrite BEL VLG |
| Brazil | BRA |  | Playwrite BRA |
| Canada | CAN |  | Playwrite CAN |
| Chile | CHI |  | Playwrite CHI |
| Colombia | COL |  | Playwrite COL |
| Croatia | HRV |  | Playwrite HRV |
| Croatia | HRV | Left Hand | Playwrite HRV Left Hand |
| Cuba | CUB |  | Playwrite CUB |
| Czech Republic | CZE |  | Playwrite CZE |
| Slovakia | SVK |  | Playwrite SVK |
| Denmark | DNK | Looped | Playwrite DNK Looped |
| Denmark | DNK | Unlooped | Playwrite DNK Unlooped |
| England | ENG | Semi Joined | Playwrite ENG Semi Joined |
| England | ENG | Joined | Playwrite ENG Joined |
| Finland | FIN |  | Playwrite FIN |
| France | FRA | Traditional | Playwrite FRA Traditional |
| France | FRA | Modern | Playwrite FRA Modern |
| Germany | DEU | Grundschrift | Playwrite DEU Grundschrift |
| Germany | DEU | LA | Playwrite DEU LA |
| Germany | DEU | SAS | Playwrite DEU SAS |
| Germany | DEU | VA | Playwrite DEU VA |
| Iceland | ISL |  | Playwrite ISL |
| Indonesia | IDN |  | Playwrite IDN |
| Ireland | IRL |  | Playwrite IRL |
| Italy | ITA | Traditional | Playwrite ITA Traditional |
| Italy | ITA | Modern | Playwrite ITA Modern |
| Mexico | MEX |  | Playwrite MEX |
| Netherlands | NLD |  | Playwrite NLD |
| New Zealand | NZL |  | Playwrite NZL |
| Norway | NOR |  | Playwrite NOR |
| Peru | PER |  | Playwrite PER |
| Poland | POL |  | Playwrite POL |
| Portugal | PRT |  | Playwrite PRT |
| Slovakia | SVK |  | Playwrite SVK |
| South Africa | ZAF |  | Playwrite ZAF |
| Spain | ESP |  | Playwrite ESP |
| Spain | ESP | Ornate Caps | Playwrite ESP Ornate Caps |
| Sweden | SWE |  | Playwrite SWE |
| Turkey | TUR |  | Playwrite TUR |
| USA | USA | Modern | Playwrite USA Modern |
| USA | USA | Traditional | Playwrite USA Traditional |
| Vietnam | VNM |  | Playwrite VNM |
 
## Create or edit handwriting models
After creating or editing glyphs and modifying the Recipe table you will need to prepare the files for font generation following these four steps.  
1. Write the model dictionary  
2. Write the feature file for models  
3. Update the design space  
4. Create UFOs from the Glyphpackage file

Now you are ready to build new fonts following the build instructions:
`/sources/build-models-HowTo-README.md`
