## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[13] PlaypenAUS_VIC-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
* 🔥 **FAIL** "Playpen AUS_VIC" contains the following characters which are not allowed: "_". [code: forbidden-characters]
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
 FONT_FAMILY_NAME = 'Playpen AUS_VIC ExtraLight' / SUBFAMILY_NAME = 'Regular'

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

	- M_locl.au

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

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

	* a (U+0061): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* aacute (U+00E1): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* abreve (U+0103): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* acircumflex (U+00E2): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* adieresis (U+00E4): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* agrave (U+00E0): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* amacron (U+0101): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* aogonek (U+0105): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* aring (U+00E5): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* atilde (U+00E3): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* eng (U+014B): L<<241.0,491.0>--<178.0,298.0>>/B<<178.0,298.0>-<225.0,380.0>-<274.5,428.0>> = 11.742102173284042

	* h (U+0068): L<<377.0,891.0>--<184.0,300.0>>/B<<184.0,300.0>-<231.0,380.0>-<280.0,428.0>> = 12.349002503215463

	* hbar (U+0127): L<<377.0,891.0>--<184.0,300.0>>/B<<184.0,300.0>-<231.0,380.0>-<280.0,428.0>> = 12.349002503215463

	* hcircumflex (U+0125): L<<377.0,891.0>--<184.0,300.0>>/B<<184.0,300.0>-<231.0,380.0>-<280.0,428.0>> = 12.349002503215463

	* m (U+006D): L<<240.0,491.0>--<180.0,305.0>>/B<<180.0,305.0>-<249.0,420.0>-<319.0,469.5>> = 13.08505993623217

	* m (U+006D): L<<527.0,334.0>--<519.0,311.0>>/B<<519.0,311.0>-<587.0,423.0>-<656.0,471.0>> = 12.08472366856666

	* n (U+006E): L<<241.0,491.0>--<178.0,298.0>>/B<<178.0,298.0>-<225.0,380.0>-<274.5,428.0>> = 11.742102173284042

	* nacute (U+0144): L<<241.0,491.0>--<178.0,298.0>>/B<<178.0,298.0>-<225.0,380.0>-<274.5,428.0>> = 11.742102173284042

	* ncaron (U+0148): L<<241.0,491.0>--<178.0,298.0>>/B<<178.0,298.0>-<225.0,380.0>-<274.5,428.0>> = 11.742102173284042

	* ntilde (U+00F1): L<<241.0,491.0>--<178.0,298.0>>/B<<178.0,298.0>-<225.0,380.0>-<274.5,428.0>> = 11.742102173284042

	* r (U+0072): L<<239.0,490.0>--<177.0,301.0>>/B<<177.0,301.0>-<225.0,386.0>-<269.0,433.5>> = 11.2919926404038

	* racute (U+0155): L<<239.0,490.0>--<177.0,301.0>>/B<<177.0,301.0>-<225.0,386.0>-<269.0,433.5>> = 11.2919926404038

	* rcaron (U+0159): L<<239.0,490.0>--<177.0,301.0>>/B<<177.0,301.0>-<225.0,386.0>-<269.0,433.5>> = 11.2919926404038

	* u (U+0075): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uacute (U+00FA): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* ubreve (U+016D): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* ucircumflex (U+00FB): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* udieresis (U+00FC): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* ugrave (U+00F9): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uhorn (U+01B0): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uhungarumlaut (U+0171): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* umacron (U+016B): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni0146 (U+0146): L<<241.0,491.0>--<178.0,298.0>>/B<<178.0,298.0>-<225.0,380.0>-<274.5,428.0>> = 11.742102173284042

	* uni0157 (U+0157): L<<239.0,490.0>--<177.0,301.0>>/B<<177.0,301.0>-<225.0,386.0>-<269.0,433.5>> = 11.2919926404038

	* uni01CE (U+01CE): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni01D4 (U+01D4): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni01D6 (U+01D6): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni01D8 (U+01D8): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni01DA (U+01DA): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni01DC (U+01DC): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EA1 (U+1EA1): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EA3 (U+1EA3): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EA5 (U+1EA5): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EA7 (U+1EA7): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EA9 (U+1EA9): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EAB (U+1EAB): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EAD (U+1EAD): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EAF (U+1EAF): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EB1 (U+1EB1): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EB3 (U+1EB3): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EB5 (U+1EB5): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EB7 (U+1EB7): B<<398.0,142.0>-<405.0,163.0>-<412.0,184.0>>/B<<412.0,184.0>-<345.0,77.0>-<283.0,30.0>> = 13.61854166144103

	* uni1EE5 (U+1EE5): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EE7 (U+1EE7): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EE9 (U+1EE9): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EEB (U+1EEB): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EED (U+1EED): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EEF (U+1EEF): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EF1 (U+1EF1): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uni1EF5 (U+1EF5): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123

	* uni1EF7 (U+1EF7): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123

	* uni1EF9 (U+1EF9): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123

	* uogonek (U+0173): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* uring (U+016F): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* utilde (U+0169): L<<408.0,121.0>--<434.0,199.0>>/B<<434.0,199.0>-<364.0,83.0>-<292.0,33.5>> = 12.673860005623105

	* y (U+0079): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123

	* yacute (U+00FD): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123

	* ycircumflex (U+0177): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123

	* ydieresis (U+00FF): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123 

	* ygrave (U+1EF3): L<<309.0,-191.0>--<437.0,206.0>>/B<<437.0,206.0>-<389.0,124.0>-<340.0,75.5>> = 12.472986200093123 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[13] PlaypenAUS_VIC-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
* 🔥 **FAIL** "Playpen AUS_VIC" contains the following characters which are not allowed: "_". [code: forbidden-characters]
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
 FONT_FAMILY_NAME = 'Playpen AUS_VIC Light' / SUBFAMILY_NAME = 'Regular'

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

	- M_locl.au

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

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

	* eng (U+014B): L<<248.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,425.0>-<327.5,472.0>> = 13.633972789404336

	* m (U+006D): B<<540.0,467.0>-<560.0,415.0>-<532.0,331.0>>/B<<532.0,331.0>-<593.0,426.0>-<657.5,472.5>> = 14.269784754079812

	* n (U+006E): L<<248.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,425.0>-<327.5,472.0>> = 13.633972789404336

	* nacute (U+0144): L<<248.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,425.0>-<327.5,472.0>> = 13.633972789404336

	* ncaron (U+0148): L<<248.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,425.0>-<327.5,472.0>> = 13.633972789404336

	* ntilde (U+00F1): L<<248.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,425.0>-<327.5,472.0>> = 13.633972789404336

	* r (U+0072): L<<247.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,428.0>-<320.0,473.5>> = 13.222980359434512

	* racute (U+0155): L<<247.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,428.0>-<320.0,473.5>> = 13.222980359434512

	* rcaron (U+0159): L<<247.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,428.0>-<320.0,473.5>> = 13.222980359434512

	* uni0146 (U+0146): L<<248.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,425.0>-<327.5,472.0>> = 13.633972789404336

	* uni0157 (U+0157): L<<247.0,483.0>--<195.0,322.0>>/B<<195.0,322.0>-<259.0,428.0>-<320.0,473.5>> = 13.222980359434512

	* uni1EF5 (U+1EF5): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504

	* uni1EF7 (U+1EF7): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504

	* uni1EF9 (U+1EF9): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504

	* y (U+0079): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504

	* yacute (U+00FD): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504

	* ycircumflex (U+0177): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504

	* ydieresis (U+00FF): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504 

	* ygrave (U+1EF3): L<<303.0,-181.0>--<421.0,182.0>>/B<<421.0,182.0>-<357.0,80.0>-<289.0,32.5>> = 14.098525408165504 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] PlaypenAUS_VIC-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
* 🔥 **FAIL** "Playpen AUS_VIC" contains the following characters which are not allowed: "_". [code: forbidden-characters]
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

	- M_locl.au

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

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

	* d (U+0064): B<<381.5,135.0>-<382.0,138.0>-<383.0,140.0>>/B<<383.0,140.0>-<322.0,58.0>-<263.5,20.5>> = 10.080597987542275

	* dcaron (U+010F): B<<381.5,135.0>-<382.0,138.0>-<383.0,140.0>>/B<<383.0,140.0>-<322.0,58.0>-<263.5,20.5>> = 10.080597987542275 

	* dcroat (U+0111): B<<381.5,135.0>-<382.0,138.0>-<383.0,140.0>>/B<<383.0,140.0>-<322.0,58.0>-<263.5,20.5>> = 10.080597987542275 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[12] PlaypenAUS_VIC-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
* 🔥 **FAIL** "Playpen AUS_VIC" contains the following characters which are not allowed: "_". [code: forbidden-characters]
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

	- M_locl.au

	- OE.cur

	- OE.cur.locl

	- Q.cur_locl

	- Q.cur_locl.ini

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

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

	* a (U+0061): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* aacute (U+00E1): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* abreve (U+0103): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* acircumflex (U+00E2): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* adieresis (U+00E4): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* agrave (U+00E0): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* amacron (U+0101): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* aogonek (U+0105): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* aring (U+00E5): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* at (U+0040): B<<521.5,177.0>-<527.0,194.0>-<534.0,214.0>>/B<<534.0,214.0>-<483.0,127.0>-<434.5,90.0>> = 11.089079792179602

	* atilde (U+00E3): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* b (U+0062): L<<368.0,901.0>--<173.0,301.0>>/B<<173.0,301.0>-<241.0,417.0>-<305.5,468.0>> = 12.374964405454921

	* d (U+0064): B<<410.0,147.5>-<420.0,177.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<293.5,35.0>> = 13.224085520519898

	* dcaron (U+010F): B<<410.0,147.5>-<420.0,177.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<293.5,35.0>> = 13.224085520519898

	* dcroat (U+0111): B<<410.0,147.5>-<420.0,177.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<293.5,35.0>> = 13.224085520519898

	* eng (U+014B): L<<233.0,498.0>--<160.0,274.0>>/B<<160.0,274.0>-<213.0,368.0>-<266.0,421.5>> = 11.365179669758035

	* g (U+0067): L<<296.0,-200.0>--<427.0,202.0>>/B<<427.0,202.0>-<358.0,85.0>-<293.0,34.0>> = 12.480437127206173

	* gbreve (U+011F): L<<296.0,-200.0>--<427.0,202.0>>/B<<427.0,202.0>-<358.0,85.0>-<293.0,34.0>> = 12.480437127206173

	* gcircumflex (U+011D): L<<296.0,-200.0>--<427.0,202.0>>/B<<427.0,202.0>-<358.0,85.0>-<293.0,34.0>> = 12.480437127206173

	* gdotaccent (U+0121): L<<296.0,-200.0>--<427.0,202.0>>/B<<427.0,202.0>-<358.0,85.0>-<293.0,34.0>> = 12.480437127206173

	* h (U+0068): L<<369.0,899.0>--<166.0,277.0>>/B<<166.0,277.0>-<218.0,370.0>-<271.0,423.0>> = 11.136341178642768

	* hbar (U+0127): L<<369.0,899.0>--<166.0,277.0>>/B<<166.0,277.0>-<218.0,370.0>-<271.0,423.0>> = 11.136341178642768

	* hcircumflex (U+0125): L<<369.0,899.0>--<166.0,277.0>>/B<<166.0,277.0>-<218.0,370.0>-<271.0,423.0>> = 11.136341178642768

	* m (U+006D): L<<233.0,498.0>--<162.0,279.0>>/B<<162.0,279.0>-<213.0,371.0>-<265.0,423.5>> = 11.038957872371492

	* m (U+006D): L<<523.0,343.0>--<505.0,288.0>>/B<<505.0,288.0>-<556.0,377.0>-<606.5,427.5>> = 11.692302489897308

	* n (U+006E): L<<233.0,498.0>--<160.0,274.0>>/B<<160.0,274.0>-<213.0,368.0>-<266.0,421.5>> = 11.365179669758035

	* nacute (U+0144): L<<233.0,498.0>--<160.0,274.0>>/B<<160.0,274.0>-<213.0,368.0>-<266.0,421.5>> = 11.365179669758035

	* ncaron (U+0148): L<<233.0,498.0>--<160.0,274.0>>/B<<160.0,274.0>-<213.0,368.0>-<266.0,421.5>> = 11.365179669758035

	* ntilde (U+00F1): L<<233.0,498.0>--<160.0,274.0>>/B<<160.0,274.0>-<213.0,368.0>-<266.0,421.5>> = 11.365179669758035

	* ordfeminine (U+00AA): B<<463.5,638.0>-<469.0,656.0>-<475.0,676.0>>/B<<475.0,676.0>-<423.0,588.0>-<374.5,549.5>> = 13.879982638495386

	* p (U+0070): L<<239.0,500.0>--<173.0,301.0>>/B<<173.0,301.0>-<243.0,417.0>-<307.0,468.0>> = 12.760278913714693

	* q (U+0071): L<<232.0,-400.0>--<427.0,200.0>>/B<<427.0,200.0>-<359.0,85.0>-<294.5,34.0>> = 12.591847861149269

	* r (U+0072): L<<231.0,498.0>--<160.0,280.0>>/B<<160.0,280.0>-<213.0,380.0>-<259.0,431.5>> = 9.883777934723865

	* racute (U+0155): L<<231.0,498.0>--<160.0,280.0>>/B<<160.0,280.0>-<213.0,380.0>-<259.0,431.5>> = 9.883777934723865

	* rcaron (U+0159): L<<231.0,498.0>--<160.0,280.0>>/B<<160.0,280.0>-<213.0,380.0>-<259.0,431.5>> = 9.883777934723865

	* thorn (U+00FE): L<<369.0,900.0>--<173.0,301.0>>/B<<173.0,301.0>-<243.0,417.0>-<307.0,468.0>> = 12.99009039949364

	* u (U+0075): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uacute (U+00FA): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* ubreve (U+016D): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* ucircumflex (U+00FB): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* udieresis (U+00FC): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* ugrave (U+00F9): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uhorn (U+01B0): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uhungarumlaut (U+0171): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* umacron (U+016B): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni0123 (U+0123): L<<296.0,-200.0>--<427.0,202.0>>/B<<427.0,202.0>-<358.0,85.0>-<293.0,34.0>> = 12.480437127206173

	* uni0146 (U+0146): L<<233.0,498.0>--<160.0,274.0>>/B<<160.0,274.0>-<213.0,368.0>-<266.0,421.5>> = 11.365179669758035

	* uni0157 (U+0157): L<<231.0,498.0>--<160.0,280.0>>/B<<160.0,280.0>-<213.0,380.0>-<259.0,431.5>> = 9.883777934723865

	* uni01CE (U+01CE): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni01D4 (U+01D4): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni01D6 (U+01D6): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni01D8 (U+01D8): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni01DA (U+01DA): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni01DC (U+01DC): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EA1 (U+1EA1): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EA3 (U+1EA3): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EA5 (U+1EA5): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EA7 (U+1EA7): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EA9 (U+1EA9): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EAB (U+1EAB): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EAD (U+1EAD): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EAF (U+1EAF): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EB1 (U+1EB1): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EB3 (U+1EB3): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EB5 (U+1EB5): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EB7 (U+1EB7): B<<409.0,145.5>-<419.0,176.0>-<429.0,206.0>>/B<<429.0,206.0>-<359.0,87.0>-<294.0,35.0>> = 12.030596096537815

	* uni1EE5 (U+1EE5): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EE7 (U+1EE7): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EE9 (U+1EE9): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EEB (U+1EEB): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EED (U+1EED): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EEF (U+1EEF): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EF1 (U+1EF1): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uni1EF5 (U+1EF5): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673

	* uni1EF7 (U+1EF7): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673

	* uni1EF9 (U+1EF9): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673

	* uogonek (U+0173): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* uring (U+016F): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* utilde (U+0169): L<<412.0,105.0>--<452.0,228.0>>/B<<452.0,228.0>-<400.0,133.0>-<347.0,80.0>> = 10.680210461138158

	* y (U+0079): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673

	* yacute (U+00FD): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673

	* ycircumflex (U+0177): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673

	* ydieresis (U+00FF): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673 

	* ygrave (U+1EF3): L<<314.0,-200.0>--<453.0,229.0>>/B<<453.0,229.0>-<400.0,135.0>-<346.5,81.5>> = 11.46279105176673 [code: found-jaggy-segments]
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
