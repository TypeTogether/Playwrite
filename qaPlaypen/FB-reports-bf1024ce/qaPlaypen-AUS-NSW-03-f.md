## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[13] PlaypenAUS_NSW-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

>
>There have been bugs rendering variable fonts with nested components. Additionally, some static fonts with nested components have been reported to have rendering and printing issues.
>
>For more info, see: * https://github.com/googlefonts/fontbakery/issues/2961 * https://github.com/arrowtype/recursive/issues/412
>
* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* uni1EAE
	* uni1EB0
	* uni1EB2
	* uni1EB4
	* uni1EA8
	* uni1EAA
	* Dcroat
	* uni1EC2
	* uni1EC4
	* IJacute
	* uni1ED4
	* uni1ED6
	* uni1EDA
	* uni1EE2
	* uni1EDC
	* uni1EDE
	* uni1EE0
	* uni1EE8
	* uni1EF0
	* uni1EEA
	* uni1EEC
	* uni1EEE
	* uni1EAF
	* uni1EB1
	* uni1EB3
	* uni1EB5
	* uni1EA5
	* uni1EA7
	* uni1EA9
	* uni1EAB
	* uni1EBF
	* uni1EC1
	* uni1EC3
	* uni1EC5
	* ijacute
	* uni1ED1
	* uni1ED3
	* uni1ED5
	* uni1ED7
	* uni1EDB
	* uni1EE3
	* uni1EDD
	* uni1EDF
	* uni1EE1
	* uni1EE9
	* uni1EF1
	* uni1EEB
	* uni1EED
	* uni1EEF
	* a.mod.fin
	* b.mod.ini
	* b.mod.med
	* b.mod.fin
	* c.mod.fin
	* d.mod.fin
	* f.mod.ini
	* f.mod.med
	* f.mod.fin
	* g.mod.ini
	* g.mod.med
	* g.mod.fin
	* h.mod.fin
	* i.mod.fin
	* j.mod.ini
	* j.mod.med
	* j.mod.fin
	* k.mod.fin
	* l.mod.fin
	* m.mod.fin
	* n.mod.fin
	* o.mod.ini
	* o.mod.med
	* o.mod.fin
	* p.mod.ini
	* p.mod.med
	* p.mod.fin
	* q.mod.ini
	* q.mod.med
	* q.mod.fin
	* r.mod.fin
	* s.mod.ini
	* u.mod.fin
	* v.mod.ini
	* v.mod.med
	* v.mod.fin
	* w.mod.ini
	* w.mod.med
	* w.mod.fin
	* x.mod.fin
	* y.mod.ini
	* y.mod.med
	* y.mod.fin
	* z.mod.fin
	* ae.mod.fin
	* oe.mod.fin
	* eth.mod.fin
	* ij.mod
	* ij.mod.ini
	* ij.mod.med
	* ij.mod.fin
	* b.jmc.fin
	* p.jmc
	* p.jmc.fin
	* q.jmc
	* q.jmc.fin
	* q.jmc_ar
	* q.jmc_ar.fin
	* s.jmc
	* germandbls.jmc.fin
	* ij.jmc.ini
	* ij.jmc.fin and thorn.jmc.fin [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted">com.google.fonts/check/integer_ppem_if_hinted</a>)</summary><div>

>
>Hinted fonts must have head table flag bit 3 set.
>
>Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of Head::flags decides whether PPEM should be rounded. This bit should always be set for hinted fonts.
>
>Note: Bit 3 = Force ppem to integer values for all internal scaler math; May use fractional ppem sizes if this bit is clear;
>
* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenv
python3 -m venv venv
# activate virtualenv
source venv/bin/activate
# install gftools
pip install git+https://www.github.com/googlefonts/tools [code: bad-flags]
</div></details><details><summary>🔥 <b>FAIL:</b> Check family name for GF Guide compliance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_name_compliance">com.google.fonts/check/name/family_name_compliance</a>)</summary><div>

>
>Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
>
>If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
>
>Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
>
>These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/googlefonts/fontbakery/
>
* 🔥 **FAIL** "Playpen AUS_NSW" contains the following characters which are not allowed: "_". [code: forbidden-characters]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1373, but got 900 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/googlefonts/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen AUS_NSW ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>

>
>The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
>
>- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font is designed for.
>
>- slng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font supports.
>
>The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
>
>The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
>
>The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
>
>This check ensures that the font has the meta table containing the slng and dlng structures.
>
>All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
>
>In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.
>
* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>

>
>Glyphs are either accessible directly through Unicode codepoints or through substitution rules.
>
>In Color Fonts, glyphs are also referenced by the COLR table.
>
>Any glyphs not accessible by either of these means are redundant and serve only to increase the font's file size.
>
* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- A.cur_locl

	- A.dec_locl

	- AE.cur

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- IJ.cur

	- IJacute

	- I_locl

	- M_locl

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

	- cnct.mod_e_z.ful

	- f.alt1.mrr

	- f.ful_pe

	- f.ful_pl

	- four.alt1

	- i.loclTRK

	- ijacute

	- k.lop_pe

	- l.alt1.lop

	- nine.alt1

	- one.alt1

	- p.mrr_ca

	- seven.alt1

	- t.lop_de

	- uni030C.alt_locl

	- uni0312.case

	- x.cnt_de 

	- y_de
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>

>
>Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
>
>However, a quotedbl should have 2 contours, unless the font belongs to a display family.
>
>This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.
>
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: itilde	Contours detected: 4	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 5	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: itilde	Contours detected: 4	Expected: 2

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 5	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>

>
>The dotted circle character (U+25CC) is inserted by shaping engines before mark glyphs which do not have an associated base, especially in the context of broken syllabic clusters.
>
>For fonts containing combining marks, it is recommended that the dotted circle character be included so that these isolated marks can be displayed properly; for fonts supporting complex scripts, this should be considered mandatory.
>
>Additionally, when a dotted circle glyph is present, it should be able to display all marks correctly, meaning that it should contain anchors for all attaching marks.
>
* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 periodcentered (U+00B7) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned if they have mark anchors.
>
>Only combining mark glyphs should be in that class. Any non-mark glyph must not be in that class, in particular spacing glyphs.
>
* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* b (U+0062): L<<353.0,893.0>--<179.0,293.0>>/B<<179.0,293.0>-<245.0,410.0>-<308.5,464.5>> = 13.255297387407163

	* eng (U+014B): L<<231.0,491.0>--<165.0,260.0>>/B<<165.0,260.0>-<214.0,355.0>-<265.5,412.0>> = 11.338811392700217

	* g (U+0067): L<<305.0,-194.0>--<421.0,206.0>>/B<<421.0,206.0>-<354.0,91.0>-<289.5,37.0>> = 14.053290709170858

	* gbreve (U+011F): L<<305.0,-194.0>--<421.0,206.0>>/B<<421.0,206.0>-<354.0,91.0>-<289.5,37.0>> = 14.053290709170858

	* gcircumflex (U+011D): L<<305.0,-194.0>--<421.0,206.0>>/B<<421.0,206.0>-<354.0,91.0>-<289.5,37.0>> = 14.053290709170858

	* gdotaccent (U+0121): L<<305.0,-194.0>--<421.0,206.0>>/B<<421.0,206.0>-<354.0,91.0>-<289.5,37.0>> = 14.053290709170858

	* h (U+0068): L<<353.0,892.0>--<171.0,262.0>>/B<<171.0,262.0>-<220.0,356.0>-<271.5,412.5>> = 11.418558515632983

	* hbar (U+0127): L<<353.0,892.0>--<171.0,262.0>>/B<<171.0,262.0>-<220.0,356.0>-<271.5,412.5>> = 11.418558515632983

	* hcircumflex (U+0125): L<<353.0,892.0>--<171.0,262.0>>/B<<171.0,262.0>-<220.0,356.0>-<271.5,412.5>> = 11.418558515632983

	* m (U+006D): L<<231.0,491.0>--<167.0,267.0>>/B<<167.0,267.0>-<238.0,403.0>-<312.5,461.0>> = 11.621811599992757

	* m (U+006D): L<<525.0,343.0>--<504.0,272.0>>/B<<504.0,272.0>-<575.0,405.0>-<648.5,462.0>> = 11.61796050767635

	* n (U+006E): L<<231.0,491.0>--<165.0,260.0>>/B<<165.0,260.0>-<214.0,355.0>-<265.5,412.0>> = 11.338811392700217

	* nacute (U+0144): L<<231.0,491.0>--<165.0,260.0>>/B<<165.0,260.0>-<214.0,355.0>-<265.5,412.0>> = 11.338811392700217

	* ncaron (U+0148): L<<231.0,491.0>--<165.0,260.0>>/B<<165.0,260.0>-<214.0,355.0>-<265.5,412.0>> = 11.338811392700217

	* ntilde (U+00F1): L<<231.0,491.0>--<165.0,260.0>>/B<<165.0,260.0>-<214.0,355.0>-<265.5,412.0>> = 11.338811392700217

	* p (U+0070): L<<238.0,492.0>--<180.0,293.0>>/B<<180.0,293.0>-<246.0,410.0>-<309.5,464.5>> = 13.178308387043325

	* q (U+0071): L<<249.0,-394.0>--<425.0,214.0>>/B<<425.0,214.0>-<357.0,94.0>-<292.0,38.5>> = 13.394443479274576

	* r (U+0072): L<<230.0,491.0>--<164.0,265.0>>/B<<164.0,265.0>-<214.0,365.0>-<259.5,420.0>> = 10.28537797494743

	* racute (U+0155): L<<230.0,491.0>--<164.0,265.0>>/B<<164.0,265.0>-<214.0,365.0>-<259.5,420.0>> = 10.28537797494743

	* rcaron (U+0159): L<<230.0,491.0>--<164.0,265.0>>/B<<164.0,265.0>-<214.0,365.0>-<259.5,420.0>> = 10.28537797494743

	* thorn (U+00FE): L<<353.0,892.0>--<179.0,293.0>>/B<<179.0,293.0>-<246.0,410.0>-<309.0,464.5>> = 13.599848289954492

	* u (U+0075): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uacute (U+00FA): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* ubreve (U+016D): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* ucircumflex (U+00FB): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* udieresis (U+00FC): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* ugrave (U+00F9): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uhorn (U+01B0): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uhungarumlaut (U+0171): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* umacron (U+016B): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni0123 (U+0123): L<<305.0,-194.0>--<421.0,206.0>>/B<<421.0,206.0>-<354.0,91.0>-<289.5,37.0>> = 14.053290709170858

	* uni0146 (U+0146): L<<231.0,491.0>--<165.0,260.0>>/B<<165.0,260.0>-<214.0,355.0>-<265.5,412.0>> = 11.338811392700217

	* uni0157 (U+0157): L<<230.0,491.0>--<164.0,265.0>>/B<<164.0,265.0>-<214.0,365.0>-<259.5,420.0>> = 10.28537797494743

	* uni01D4 (U+01D4): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni01D6 (U+01D6): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni01D8 (U+01D8): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni01DA (U+01DA): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni01DC (U+01DC): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EE5 (U+1EE5): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EE7 (U+1EE7): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EE9 (U+1EE9): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EEB (U+1EEB): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EED (U+1EED): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EEF (U+1EEF): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EF1 (U+1EF1): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uni1EF5 (U+1EF5): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216

	* uni1EF7 (U+1EF7): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216

	* uni1EF9 (U+1EF9): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216

	* uogonek (U+0173): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* uring (U+016F): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* utilde (U+0169): L<<411.0,111.0>--<448.0,241.0>>/B<<448.0,241.0>-<400.0,149.0>-<349.0,92.0>> = 11.66564307395382

	* y (U+0079): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216

	* yacute (U+00FD): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216

	* ycircumflex (U+0177): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216

	* ydieresis (U+00FF): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216 

	* ygrave (U+1EF3): L<<322.0,-194.0>--<449.0,245.0>>/B<<449.0,245.0>-<400.0,150.0>-<348.0,93.0>> = 11.149376082174216 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[13] PlaypenAUS_NSW-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

>
>There have been bugs rendering variable fonts with nested components. Additionally, some static fonts with nested components have been reported to have rendering and printing issues.
>
>For more info, see: * https://github.com/googlefonts/fontbakery/issues/2961 * https://github.com/arrowtype/recursive/issues/412
>
* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* uni1EAE
	* uni1EB0
	* uni1EB2
	* uni1EB4
	* uni1EA8
	* uni1EAA
	* Dcroat
	* uni1EC2
	* uni1EC4
	* IJacute
	* uni1ED4
	* uni1ED6
	* uni1EDA
	* uni1EE2
	* uni1EDC
	* uni1EDE
	* uni1EE0
	* uni1EE8
	* uni1EF0
	* uni1EEA
	* uni1EEC
	* uni1EEE
	* uni1EAF
	* uni1EB1
	* uni1EB3
	* uni1EB5
	* uni1EA5
	* uni1EA7
	* uni1EA9
	* uni1EAB
	* uni1EBF
	* uni1EC1
	* uni1EC3
	* uni1EC5
	* ijacute
	* uni1ED1
	* uni1ED3
	* uni1ED5
	* uni1ED7
	* uni1EDB
	* uni1EE3
	* uni1EDD
	* uni1EDF
	* uni1EE1
	* uni1EE9
	* uni1EF1
	* uni1EEB
	* uni1EED
	* uni1EEF
	* a.mod.fin
	* b.mod.ini
	* b.mod.med
	* b.mod.fin
	* c.mod.fin
	* d.mod.fin
	* f.mod.ini
	* f.mod.med
	* f.mod.fin
	* g.mod.ini
	* g.mod.med
	* g.mod.fin
	* h.mod.fin
	* i.mod.fin
	* j.mod.ini
	* j.mod.med
	* j.mod.fin
	* k.mod.fin
	* l.mod.fin
	* m.mod.fin
	* n.mod.fin
	* o.mod.ini
	* o.mod.med
	* o.mod.fin
	* p.mod.ini
	* p.mod.med
	* p.mod.fin
	* q.mod.ini
	* q.mod.med
	* q.mod.fin
	* r.mod.fin
	* s.mod.ini
	* u.mod.fin
	* v.mod.ini
	* v.mod.med
	* v.mod.fin
	* w.mod.ini
	* w.mod.med
	* w.mod.fin
	* x.mod.fin
	* y.mod.ini
	* y.mod.med
	* y.mod.fin
	* z.mod.fin
	* ae.mod.fin
	* oe.mod.fin
	* eth.mod.fin
	* ij.mod
	* ij.mod.ini
	* ij.mod.med
	* ij.mod.fin
	* b.jmc.fin
	* p.jmc
	* p.jmc.fin
	* q.jmc
	* q.jmc.fin
	* q.jmc_ar
	* q.jmc_ar.fin
	* s.jmc
	* germandbls.jmc.fin
	* ij.jmc.ini
	* ij.jmc.fin and thorn.jmc.fin [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted">com.google.fonts/check/integer_ppem_if_hinted</a>)</summary><div>

>
>Hinted fonts must have head table flag bit 3 set.
>
>Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of Head::flags decides whether PPEM should be rounded. This bit should always be set for hinted fonts.
>
>Note: Bit 3 = Force ppem to integer values for all internal scaler math; May use fractional ppem sizes if this bit is clear;
>
* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenv
python3 -m venv venv
# activate virtualenv
source venv/bin/activate
# install gftools
pip install git+https://www.github.com/googlefonts/tools [code: bad-flags]
</div></details><details><summary>🔥 <b>FAIL:</b> Check family name for GF Guide compliance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_name_compliance">com.google.fonts/check/name/family_name_compliance</a>)</summary><div>

>
>Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
>
>If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
>
>Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
>
>These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/googlefonts/fontbakery/
>
* 🔥 **FAIL** "Playpen AUS_NSW" contains the following characters which are not allowed: "_". [code: forbidden-characters]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1373, but got 900 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/googlefonts/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen AUS_NSW Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>

>
>The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
>
>- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font is designed for.
>
>- slng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font supports.
>
>The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
>
>The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
>
>The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
>
>This check ensures that the font has the meta table containing the slng and dlng structures.
>
>All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
>
>In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.
>
* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>

>
>Glyphs are either accessible directly through Unicode codepoints or through substitution rules.
>
>In Color Fonts, glyphs are also referenced by the COLR table.
>
>Any glyphs not accessible by either of these means are redundant and serve only to increase the font's file size.
>
* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- A.cur_locl

	- A.dec_locl

	- AE.cur

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- IJ.cur

	- IJacute

	- I_locl

	- M_locl

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

	- cnct.mod_e_z.ful

	- f.alt1.mrr

	- f.ful_pe

	- f.ful_pl

	- four.alt1

	- i.loclTRK

	- ijacute

	- k.lop_pe

	- l.alt1.lop

	- nine.alt1

	- one.alt1

	- p.mrr_ca

	- seven.alt1

	- t.lop_de

	- uni030C.alt_locl

	- uni0312.case

	- x.cnt_de 

	- y_de
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>

>
>Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
>
>However, a quotedbl should have 2 contours, unless the font belongs to a display family.
>
>This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.
>
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: itilde	Contours detected: 4	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 5	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: itilde	Contours detected: 4	Expected: 2

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 6	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 5	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>

>
>The dotted circle character (U+25CC) is inserted by shaping engines before mark glyphs which do not have an associated base, especially in the context of broken syllabic clusters.
>
>For fonts containing combining marks, it is recommended that the dotted circle character be included so that these isolated marks can be displayed properly; for fonts supporting complex scripts, this should be considered mandatory.
>
>Additionally, when a dotted circle glyph is present, it should be able to display all marks correctly, meaning that it should contain anchors for all attaching marks.
>
* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 periodcentered (U+00B7) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned if they have mark anchors.
>
>Only combining mark glyphs should be in that class. Any non-mark glyph must not be in that class, in particular spacing glyphs.
>
* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* eng (U+014B): L<<239.0,484.0>--<183.0,290.0>>/B<<183.0,290.0>-<249.0,410.0>-<321.5,464.5>> = 12.709491343814623

	* h (U+0068): L<<361.0,885.0>--<190.0,290.0>>/B<<190.0,290.0>-<256.0,410.0>-<328.0,464.5>> = 12.776409571781935

	* hbar (U+0127): L<<361.0,885.0>--<190.0,290.0>>/B<<190.0,290.0>-<256.0,410.0>-<328.0,464.5>> = 12.776409571781935

	* hcircumflex (U+0125): L<<361.0,885.0>--<190.0,290.0>>/B<<190.0,290.0>-<256.0,410.0>-<328.0,464.5>> = 12.776409571781935

	* m (U+006D): L<<239.0,484.0>--<185.0,298.0>>/B<<185.0,298.0>-<249.0,411.0>-<317.0,465.0>> = 13.336781054214766

	* m (U+006D): L<<529.0,334.0>--<518.0,299.0>>/B<<518.0,299.0>-<582.0,411.0>-<649.5,465.0>> = 12.29769287365997

	* n (U+006E): L<<239.0,484.0>--<183.0,290.0>>/B<<183.0,290.0>-<249.0,410.0>-<321.5,464.5>> = 12.709491343814623

	* nacute (U+0144): L<<239.0,484.0>--<183.0,290.0>>/B<<183.0,290.0>-<249.0,410.0>-<321.5,464.5>> = 12.709491343814623

	* ncaron (U+0148): L<<239.0,484.0>--<183.0,290.0>>/B<<183.0,290.0>-<249.0,410.0>-<321.5,464.5>> = 12.709491343814623

	* ntilde (U+00F1): L<<239.0,484.0>--<183.0,290.0>>/B<<183.0,290.0>-<249.0,410.0>-<321.5,464.5>> = 12.709491343814623

	* r (U+0072): L<<238.0,484.0>--<182.0,291.0>>/B<<182.0,291.0>-<249.0,415.0>-<312.0,467.0>> = 12.202980284542852

	* racute (U+0155): L<<238.0,484.0>--<182.0,291.0>>/B<<182.0,291.0>-<249.0,415.0>-<312.0,467.0>> = 12.202980284542852

	* rcaron (U+0159): L<<238.0,484.0>--<182.0,291.0>>/B<<182.0,291.0>-<249.0,415.0>-<312.0,467.0>> = 12.202980284542852

	* u (U+0075): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uacute (U+00FA): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* ubreve (U+016D): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* ucircumflex (U+00FB): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* udieresis (U+00FC): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* ugrave (U+00F9): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uhorn (U+01B0): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uhungarumlaut (U+0171): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* umacron (U+016B): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni0146 (U+0146): L<<239.0,484.0>--<183.0,290.0>>/B<<183.0,290.0>-<249.0,410.0>-<321.5,464.5>> = 12.709491343814623

	* uni0157 (U+0157): L<<238.0,484.0>--<182.0,291.0>>/B<<182.0,291.0>-<249.0,415.0>-<312.0,467.0>> = 12.202980284542852

	* uni01D4 (U+01D4): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni01D6 (U+01D6): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni01D8 (U+01D8): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni01DA (U+01DA): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni01DC (U+01DC): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EE5 (U+1EE5): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EE7 (U+1EE7): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EE9 (U+1EE9): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EEB (U+1EEB): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EED (U+1EED): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EEF (U+1EEF): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EF1 (U+1EF1): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uni1EF5 (U+1EF5): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496

	* uni1EF7 (U+1EF7): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496

	* uni1EF9 (U+1EF9): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496

	* uogonek (U+0173): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* uring (U+016F): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* utilde (U+0169): L<<407.0,127.0>--<431.0,211.0>>/B<<431.0,211.0>-<366.0,95.0>-<294.5,39.5>> = 13.318468697618158

	* y (U+0079): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496

	* yacute (U+00FD): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496

	* ycircumflex (U+0177): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496

	* ydieresis (U+00FF): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496 

	* ygrave (U+1EF3): L<<318.0,-183.0>--<433.0,217.0>>/B<<433.0,217.0>-<367.0,96.0>-<294.0,40.5>> = 12.570516359915496 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] PlaypenAUS_NSW-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

>
>There have been bugs rendering variable fonts with nested components. Additionally, some static fonts with nested components have been reported to have rendering and printing issues.
>
>For more info, see: * https://github.com/googlefonts/fontbakery/issues/2961 * https://github.com/arrowtype/recursive/issues/412
>
* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* uni1EAE
	* uni1EB0
	* uni1EB2
	* uni1EB4
	* uni1EA8
	* uni1EAA
	* Dcroat
	* uni1EC2
	* uni1EC4
	* IJacute
	* uni1ED4
	* uni1ED6
	* uni1EDA
	* uni1EE2
	* uni1EDC
	* uni1EDE
	* uni1EE0
	* uni1EE8
	* uni1EF0
	* uni1EEA
	* uni1EEC
	* uni1EEE
	* uni1EAF
	* uni1EB1
	* uni1EB3
	* uni1EB5
	* uni1EA5
	* uni1EA7
	* uni1EA9
	* uni1EAB
	* uni1EBF
	* uni1EC1
	* uni1EC3
	* uni1EC5
	* ijacute
	* uni1ED1
	* uni1ED3
	* uni1ED5
	* uni1ED7
	* uni1EDB
	* uni1EE3
	* uni1EDD
	* uni1EDF
	* uni1EE1
	* uni1EE9
	* uni1EF1
	* uni1EEB
	* uni1EED
	* uni1EEF
	* a.mod.fin
	* b.mod.ini
	* b.mod.med
	* b.mod.fin
	* c.mod.fin
	* d.mod.fin
	* f.mod.ini
	* f.mod.med
	* f.mod.fin
	* g.mod.ini
	* g.mod.med
	* g.mod.fin
	* h.mod.fin
	* i.mod.fin
	* j.mod.ini
	* j.mod.med
	* j.mod.fin
	* k.mod.fin
	* l.mod.fin
	* m.mod.fin
	* n.mod.fin
	* o.mod.ini
	* o.mod.med
	* o.mod.fin
	* p.mod.ini
	* p.mod.med
	* p.mod.fin
	* q.mod.ini
	* q.mod.med
	* q.mod.fin
	* r.mod.fin
	* s.mod.ini
	* u.mod.fin
	* v.mod.ini
	* v.mod.med
	* v.mod.fin
	* w.mod.ini
	* w.mod.med
	* w.mod.fin
	* x.mod.fin
	* y.mod.ini
	* y.mod.med
	* y.mod.fin
	* z.mod.fin
	* ae.mod.fin
	* oe.mod.fin
	* eth.mod.fin
	* ij.mod
	* ij.mod.ini
	* ij.mod.med
	* ij.mod.fin
	* b.jmc.fin
	* p.jmc
	* p.jmc.fin
	* q.jmc
	* q.jmc.fin
	* q.jmc_ar
	* q.jmc_ar.fin
	* s.jmc
	* germandbls.jmc.fin
	* ij.jmc.ini
	* ij.jmc.fin and thorn.jmc.fin [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted">com.google.fonts/check/integer_ppem_if_hinted</a>)</summary><div>

>
>Hinted fonts must have head table flag bit 3 set.
>
>Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of Head::flags decides whether PPEM should be rounded. This bit should always be set for hinted fonts.
>
>Note: Bit 3 = Force ppem to integer values for all internal scaler math; May use fractional ppem sizes if this bit is clear;
>
* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenv
python3 -m venv venv
# activate virtualenv
source venv/bin/activate
# install gftools
pip install git+https://www.github.com/googlefonts/tools [code: bad-flags]
</div></details><details><summary>🔥 <b>FAIL:</b> Check family name for GF Guide compliance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_name_compliance">com.google.fonts/check/name/family_name_compliance</a>)</summary><div>

>
>Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
>
>If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
>
>Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
>
>These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/googlefonts/fontbakery/
>
* 🔥 **FAIL** "Playpen AUS_NSW" contains the following characters which are not allowed: "_". [code: forbidden-characters]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1373, but got 900 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>

>
>The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
>
>- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font is designed for.
>
>- slng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font supports.
>
>The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
>
>The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
>
>The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
>
>This check ensures that the font has the meta table containing the slng and dlng structures.
>
>All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
>
>In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.
>
* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>

>
>Glyphs are either accessible directly through Unicode codepoints or through substitution rules.
>
>In Color Fonts, glyphs are also referenced by the COLR table.
>
>Any glyphs not accessible by either of these means are redundant and serve only to increase the font's file size.
>
* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- A.cur_locl

	- A.dec_locl

	- AE.cur

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- IJ.cur

	- IJacute

	- I_locl

	- M_locl

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

	- cnct.mod_e_z.ful

	- f.alt1.mrr

	- f.ful_pe

	- f.ful_pl

	- four.alt1

	- i.loclTRK

	- ijacute

	- k.lop_pe

	- l.alt1.lop

	- nine.alt1

	- one.alt1

	- p.mrr_ca

	- seven.alt1

	- t.lop_de

	- uni030C.alt_locl

	- uni0312.case

	- x.cnt_de 

	- y_de
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>

>
>Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
>
>However, a quotedbl should have 2 contours, unless the font belongs to a display family.
>
>This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.
>
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>

>
>The dotted circle character (U+25CC) is inserted by shaping engines before mark glyphs which do not have an associated base, especially in the context of broken syllabic clusters.
>
>For fonts containing combining marks, it is recommended that the dotted circle character be included so that these isolated marks can be displayed properly; for fonts supporting complex scripts, this should be considered mandatory.
>
>Additionally, when a dotted circle glyph is present, it should be able to display all marks correctly, meaning that it should contain anchors for all attaching marks.
>
* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 periodcentered (U+00B7) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned if they have mark anchors.
>
>Only combining mark glyphs should be in that class. Any non-mark glyph must not be in that class, in particular spacing glyphs.
>
* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* at (U+0040): B<<502.0,147.0>-<506.0,169.0>-<510.0,186.0>>/B<<510.0,186.0>-<509.0,183.0>-<507.5,177.5>> = 5.194428907734729

	* m (U+006D): L<<532.0,326.0>--<531.0,324.0>>/B<<531.0,324.0>-<588.0,419.0>-<651.0,469.0>> = 4.398705354995426 

	* ordfeminine (U+00AA): B<<415.0,606.5>-<419.0,629.0>-<424.0,646.0>>/B<<424.0,646.0>-<421.0,639.0>-<418.0,626.0>> = 6.809050179613362 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] PlaypenAUS_NSW-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

>
>There have been bugs rendering variable fonts with nested components. Additionally, some static fonts with nested components have been reported to have rendering and printing issues.
>
>For more info, see: * https://github.com/googlefonts/fontbakery/issues/2961 * https://github.com/arrowtype/recursive/issues/412
>
* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
	* uni1EAE
	* uni1EB0
	* uni1EB2
	* uni1EB4
	* uni1EA8
	* uni1EAA
	* Dcroat
	* uni1EC2
	* uni1EC4
	* IJacute
	* uni1ED4
	* uni1ED6
	* uni1EDA
	* uni1EE2
	* uni1EDC
	* uni1EDE
	* uni1EE0
	* uni1EE8
	* uni1EF0
	* uni1EEA
	* uni1EEC
	* uni1EEE
	* uni1EAF
	* uni1EB1
	* uni1EB3
	* uni1EB5
	* uni1EA5
	* uni1EA7
	* uni1EA9
	* uni1EAB
	* uni1EBF
	* uni1EC1
	* uni1EC3
	* uni1EC5
	* ijacute
	* uni1ED1
	* uni1ED3
	* uni1ED5
	* uni1ED7
	* uni1EDB
	* uni1EE3
	* uni1EDD
	* uni1EDF
	* uni1EE1
	* uni1EE9
	* uni1EF1
	* uni1EEB
	* uni1EED
	* uni1EEF
	* a.mod.fin
	* b.mod.ini
	* b.mod.med
	* b.mod.fin
	* c.mod.fin
	* d.mod.fin
	* f.mod.ini
	* f.mod.med
	* f.mod.fin
	* g.mod.ini
	* g.mod.med
	* g.mod.fin
	* h.mod.fin
	* i.mod.fin
	* j.mod.ini
	* j.mod.med
	* j.mod.fin
	* k.mod.fin
	* l.mod.fin
	* m.mod.fin
	* n.mod.fin
	* o.mod.ini
	* o.mod.med
	* o.mod.fin
	* p.mod.ini
	* p.mod.med
	* p.mod.fin
	* q.mod.ini
	* q.mod.med
	* q.mod.fin
	* r.mod.fin
	* s.mod.ini
	* u.mod.fin
	* v.mod.ini
	* v.mod.med
	* v.mod.fin
	* w.mod.ini
	* w.mod.med
	* w.mod.fin
	* x.mod.fin
	* y.mod.ini
	* y.mod.med
	* y.mod.fin
	* z.mod.fin
	* ae.mod.fin
	* oe.mod.fin
	* eth.mod.fin
	* ij.mod
	* ij.mod.ini
	* ij.mod.med
	* ij.mod.fin
	* b.jmc.fin
	* p.jmc
	* p.jmc.fin
	* q.jmc
	* q.jmc.fin
	* q.jmc_ar
	* q.jmc_ar.fin
	* s.jmc
	* germandbls.jmc.fin
	* ij.jmc.ini
	* ij.jmc.fin and thorn.jmc.fin [code: found-nested-components]
</div></details><details><summary>🔥 <b>FAIL:</b> PPEM must be an integer on hinted fonts. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/integer_ppem_if_hinted">com.google.fonts/check/integer_ppem_if_hinted</a>)</summary><div>

>
>Hinted fonts must have head table flag bit 3 set.
>
>Per https://docs.microsoft.com/en-us/typography/opentype/spec/head, bit 3 of Head::flags decides whether PPEM should be rounded. This bit should always be set for hinted fonts.
>
>Note: Bit 3 = Force ppem to integer values for all internal scaler math; May use fractional ppem sizes if this bit is clear;
>
* 🔥 **FAIL** This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.

This can be accomplished by using the 'gftools fix-hinting' command.

# create virtualenv
python3 -m venv venv
# activate virtualenv
source venv/bin/activate
# install gftools
pip install git+https://www.github.com/googlefonts/tools [code: bad-flags]
</div></details><details><summary>🔥 <b>FAIL:</b> Check family name for GF Guide compliance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_name_compliance">com.google.fonts/check/name/family_name_compliance</a>)</summary><div>

>
>Checks the family name for compliance with the Google Fonts Guide. https://googlefonts.github.io/gf-guide/onboarding.html#new-fonts
>
>If you want to have your family name added to the CamelCase exceptions list, please submit a pull request to the camelcased_familyname_exceptions.txt file.
>
>Similarly, abbreviations can be submitted to the abbreviations_familyname_exceptions.txt file.
>
>These are located in the Lib/fontbakery/data/googlefonts/ directory of the FontBakery source code currently hosted at https://github.com/googlefonts/fontbakery/
>
* 🔥 **FAIL** "Playpen AUS_NSW" contains the following characters which are not allowed: "_". [code: forbidden-characters]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1373, but got 900 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead. [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>

>
>The OpenType 'meta' table originated at Apple. Microsoft added it to OT with just two DataMap records:
>
>- dlng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font is designed for.
>
>- slng: comma-separated ScriptLangTags that indicate which scripts, or languages and scripts, with possible variants, the font supports.
>
>The slng structure is intended to describe which languages and scripts the font overall supports. For example, a Traditional Chinese font that also contains Latin characters, can indicate Hant,Latn, showing that it supports Hant, the Traditional Chinese variant of the Hani script, and it also supports the Latn script.
>
>The dlng structure is far more interesting. A font may contain various glyphs, but only a particular subset of the glyphs may be truly "leading" in the design, while other glyphs may have been included for technical reasons. Such a Traditional Chinese font could only list Hant there, showing that it’s designed for Traditional Chinese, but the font would omit Latn, because the developers don’t think the font is really recommended for purely Latin-script use.
>
>The tags used in the structures can comprise just script, or also language and script. For example, if a font has Bulgarian Cyrillic alternates in the locl feature for the cyrl BGR OT languagesystem, it could also indicate in dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages in meta use the ISO language and script codes, not the OpenType ones).
>
>This check ensures that the font has the meta table containing the slng and dlng structures.
>
>All families in the Google Fonts collection should contain the 'meta' table. Windows 10 already uses it when deciding on which fonts to fall back to. The Google Fonts API and also other environments could use the data for smarter filtering. Most importantly, those entries should be added to the Noto fonts.
>
>In the font making process, some environments store this data in external files already. But the meta table provides a convenient way to store this inside the font file, so some tools may add the data, and unrelated tools may read this data. This makes the solution much more portable and universal.
>
* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>

>
>Glyphs are either accessible directly through Unicode codepoints or through substitution rules.
>
>In Color Fonts, glyphs are also referenced by the COLR table.
>
>Any glyphs not accessible by either of these means are redundant and serve only to increase the font's file size.
>
* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- A.cur_locl

	- A.dec_locl

	- AE.cur

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- IJ.cur

	- IJacute

	- I_locl

	- M_locl

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

	- cnct.mod_e_z.ful

	- f.alt1.mrr

	- f.ful_pe

	- f.ful_pl

	- four.alt1

	- i.loclTRK

	- ijacute

	- k.lop_pe

	- l.alt1.lop

	- nine.alt1

	- one.alt1

	- p.mrr_ca

	- seven.alt1

	- t.lop_de

	- uni030C.alt_locl

	- uni0312.case

	- x.cnt_de 

	- y_de
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>

>
>Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
>
>However, a quotedbl should have 2 contours, unless the font belongs to a display family.
>
>This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.
>
* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uhorn	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: ohorn	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uhorn	Contours detected: 2	Expected: 1

	- Glyph name: uni1EDB	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDD	Contours detected: 4	Expected: 3

	- Glyph name: uni1EDF	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE1	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE3	Contours detected: 4	Expected: 3

	- Glyph name: uni1EE8	Contours detected: 3	Expected: 2

	- Glyph name: uni1EE9	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEA	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEB	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEC	Contours detected: 3	Expected: 2

	- Glyph name: uni1EED	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEE	Contours detected: 3	Expected: 2

	- Glyph name: uni1EEF	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF0	Contours detected: 3	Expected: 2

	- Glyph name: uni1EF1	Contours detected: 3	Expected: 2 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>

>
>The dotted circle character (U+25CC) is inserted by shaping engines before mark glyphs which do not have an associated base, especially in the context of broken syllabic clusters.
>
>For fonts containing combining marks, it is recommended that the dotted circle character be included so that these isolated marks can be displayed properly; for fonts supporting complex scripts, this should be considered mandatory.
>
>Additionally, when a dotted circle glyph is present, it should be able to display all marks correctly, meaning that it should contain anchors for all attaching marks.
>
* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 periodcentered (U+00B7) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check GDEF mark glyph class doesn't have characters that are not marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_non_mark_chars">com.google.fonts/check/gdef_non_mark_chars</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class become non-spacing and may be repositioned if they have mark anchors.
>
>Only combining mark glyphs should be in that class. Any non-mark glyph must not be in that class, in particular spacing glyphs.
>
* ⚠ **WARN** The following non-mark characters should not be in the GDEF mark glyph class:
	 U+00B7 [code: non-mark-chars]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* a (U+0061): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* aacute (U+00E1): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* abreve (U+0103): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* acircumflex (U+00E2): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* adieresis (U+00E4): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* agrave (U+00E0): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* amacron (U+0101): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* aogonek (U+0105): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* aring (U+00E5): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* at (U+0040): B<<529.5,191.5>-<536.0,214.0>-<543.0,240.0>>/B<<543.0,240.0>-<489.0,139.0>-<439.5,96.0>> = 13.062854204568824

	* atilde (U+00E3): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* b (U+0062): L<<345.0,901.0>--<159.0,263.0>>/B<<159.0,263.0>-<229.0,396.0>-<296.5,457.5>> = 11.50523318168949

	* d (U+0064): B<<419.5,167.0>-<431.0,206.0>-<441.0,244.0>>/B<<441.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.823644664444847

	* dcaron (U+010F): B<<419.5,167.0>-<431.0,206.0>-<441.0,244.0>>/B<<441.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.823644664444847

	* dcroat (U+0111): B<<419.5,167.0>-<431.0,206.0>-<441.0,244.0>>/B<<441.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.823644664444847

	* eng (U+014B): L<<224.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<201.0,340.0>-<257.0,403.0>> = 10.490002416762128

	* g (U+0067): L<<309.0,-205.0>--<438.0,237.0>>/B<<438.0,237.0>-<368.0,104.0>-<301.0,43.5>> = 11.488380931591527

	* gbreve (U+011F): L<<309.0,-205.0>--<438.0,237.0>>/B<<438.0,237.0>-<368.0,104.0>-<301.0,43.5>> = 11.488380931591527

	* gcircumflex (U+011D): L<<309.0,-205.0>--<438.0,237.0>>/B<<438.0,237.0>-<368.0,104.0>-<301.0,43.5>> = 11.488380931591527

	* gdotaccent (U+0121): L<<309.0,-205.0>--<438.0,237.0>>/B<<438.0,237.0>-<368.0,104.0>-<301.0,43.5>> = 11.488380931591527

	* h (U+0068): L<<345.0,899.0>--<152.0,233.0>>/B<<152.0,233.0>-<206.0,342.0>-<262.0,404.5>> = 10.193357308600827

	* hbar (U+0127): L<<345.0,899.0>--<152.0,233.0>>/B<<152.0,233.0>-<206.0,342.0>-<262.0,404.5>> = 10.193357308600827

	* hcircumflex (U+0125): L<<345.0,899.0>--<152.0,233.0>>/B<<152.0,233.0>-<206.0,342.0>-<262.0,404.5>> = 10.193357308600827

	* m (U+006D): L<<224.0,498.0>--<147.0,234.0>>/B<<147.0,234.0>-<201.0,342.0>-<255.5,404.5>> = 10.304846468765973

	* m (U+006D): L<<522.0,351.0>--<490.0,243.0>>/B<<490.0,243.0>-<542.0,348.0>-<596.0,408.0>> = 9.842004675899938

	* n (U+006E): L<<224.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<201.0,340.0>-<257.0,403.0>> = 10.490002416762128

	* nacute (U+0144): L<<224.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<201.0,340.0>-<257.0,403.0>> = 10.490002416762128

	* ncaron (U+0148): L<<224.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<201.0,340.0>-<257.0,403.0>> = 10.490002416762128

	* ntilde (U+00F1): L<<224.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<201.0,340.0>-<257.0,403.0>> = 10.490002416762128

	* ordfeminine (U+00AA): B<<452.5,653.0>-<459.0,677.0>-<467.0,703.0>>/B<<467.0,703.0>-<411.0,600.0>-<361.0,555.5>> = 11.42972423794491

	* p (U+0070): L<<230.0,500.0>--<160.0,263.0>>/B<<160.0,263.0>-<231.0,396.0>-<298.0,457.5>> = 11.639880518444423

	* q (U+0071): L<<255.0,-400.0>--<440.0,239.0>>/B<<440.0,239.0>-<371.0,105.0>-<303.5,44.0>> = 11.098571922765183

	* r (U+0072): L<<222.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<187.0,327.0>-<224.0,382.0>> = 8.627636407033576

	* racute (U+0155): L<<222.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<187.0,327.0>-<224.0,382.0>> = 8.627636407033576

	* rcaron (U+0159): L<<222.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<187.0,327.0>-<224.0,382.0>> = 8.627636407033576

	* thorn (U+00FE): L<<345.0,900.0>--<160.0,263.0>>/B<<160.0,263.0>-<231.0,396.0>-<298.0,457.5>> = 11.900283899582432

	* u (U+0075): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uacute (U+00FA): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* ubreve (U+016D): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* ucircumflex (U+00FB): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* udieresis (U+00FC): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* ugrave (U+00F9): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uhorn (U+01B0): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uhungarumlaut (U+0171): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* umacron (U+016B): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni0123 (U+0123): L<<309.0,-205.0>--<438.0,237.0>>/B<<438.0,237.0>-<368.0,104.0>-<301.0,43.5>> = 11.488380931591527

	* uni0146 (U+0146): L<<224.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<201.0,340.0>-<257.0,403.0>> = 10.490002416762128

	* uni0157 (U+0157): L<<222.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<187.0,327.0>-<224.0,382.0>> = 8.627636407033576

	* uni01CE (U+01CE): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni01D4 (U+01D4): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni01D6 (U+01D6): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni01D8 (U+01D8): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni01DA (U+01DA): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni01DC (U+01DC): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EA1 (U+1EA1): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EA3 (U+1EA3): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EA5 (U+1EA5): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EA7 (U+1EA7): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EA9 (U+1EA9): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EAB (U+1EAB): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EAD (U+1EAD): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EAF (U+1EAF): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EB1 (U+1EB1): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EB3 (U+1EB3): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EB5 (U+1EB5): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EB7 (U+1EB7): B<<418.5,165.5>-<430.0,205.0>-<440.0,244.0>>/B<<440.0,244.0>-<370.0,108.0>-<302.5,45.5>> = 12.853752108211893

	* uni1EE5 (U+1EE5): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EE7 (U+1EE7): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EE9 (U+1EE9): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EEB (U+1EEB): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EED (U+1EED): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EEF (U+1EEF): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EF1 (U+1EF1): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uni1EF5 (U+1EF5): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672

	* uni1EF7 (U+1EF7): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672

	* uni1EF9 (U+1EF9): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672

	* uogonek (U+0173): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* uring (U+016F): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* utilde (U+0169): L<<415.0,96.0>--<467.0,276.0>>/B<<467.0,276.0>-<413.0,164.0>-<357.0,100.0>> = 9.627290123143547

	* y (U+0079): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672

	* yacute (U+00FD): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672

	* ycircumflex (U+0177): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672

	* ydieresis (U+00FF): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672 

	* ygrave (U+1EF3): L<<327.0,-205.0>--<465.0,274.0>>/B<<465.0,274.0>-<411.0,164.0>-<355.0,101.0>> = 10.075139053697672 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 20 | 30 | 482 | 29 | 372 | 0 |
| 0% | 2% | 3% | 52% | 3% | 40% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
