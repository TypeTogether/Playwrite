## Fontbakery report

Fontbakery version: 0.8.13

<details><summary><b>[12] PlaypenNZL-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1473, but got 1000 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 500 instead. [code: descent]
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
 FONT_FAMILY_NAME = 'Playpen NZL ExtraLight' / SUBFAMILY_NAME = 'Regular'

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

	* a (U+0061): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* aacute (U+00E1): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* abreve (U+0103): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* acircumflex (U+00E2): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* adieresis (U+00E4): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* agrave (U+00E0): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* amacron (U+0101): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* aogonek (U+0105): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* aring (U+00E5): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* atilde (U+00E3): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* b (U+0062): L<<409.0,993.0>--<180.0,293.0>>/B<<180.0,293.0>-<250.0,410.0>-<315.5,464.5>> = 12.776547544854221

	* d (U+0064): B<<405.5,163.0>-<414.0,190.0>-<423.0,216.0>>/B<<423.0,216.0>-<351.0,96.0>-<284.5,39.5>> = 11.870264531587885

	* dcaron (U+010F): B<<405.5,163.0>-<414.0,190.0>-<423.0,216.0>>/B<<423.0,216.0>-<351.0,96.0>-<284.5,39.5>> = 11.870264531587885

	* dcroat (U+0111): B<<405.5,163.0>-<414.0,190.0>-<423.0,216.0>>/B<<423.0,216.0>-<351.0,96.0>-<284.5,39.5>> = 11.870264531587885

	* eng (U+014B): L<<240.0,491.0>--<165.0,261.0>>/B<<165.0,261.0>-<218.0,355.0>-<271.5,411.5>> = 11.355126896896378

	* g (U+0067): L<<256.0,-295.0>--<420.0,208.0>>/B<<420.0,208.0>-<349.0,92.0>-<282.5,37.5>> = 13.411273252730515

	* gbreve (U+011F): L<<256.0,-295.0>--<420.0,208.0>>/B<<420.0,208.0>-<349.0,92.0>-<282.5,37.5>> = 13.411273252730515

	* gcircumflex (U+011D): L<<256.0,-295.0>--<420.0,208.0>>/B<<420.0,208.0>-<349.0,92.0>-<282.5,37.5>> = 13.411273252730515

	* gdotaccent (U+0121): L<<256.0,-295.0>--<420.0,208.0>>/B<<420.0,208.0>-<349.0,92.0>-<282.5,37.5>> = 13.411273252730515

	* h (U+0068): L<<410.0,991.0>--<172.0,263.0>>/B<<172.0,263.0>-<224.0,356.0>-<277.0,412.5>> = 11.107529223221462

	* hbar (U+0127): L<<410.0,991.0>--<172.0,263.0>>/B<<172.0,263.0>-<224.0,356.0>-<277.0,412.5>> = 11.107529223221462

	* hcircumflex (U+0125): L<<410.0,991.0>--<172.0,263.0>>/B<<172.0,263.0>-<224.0,356.0>-<277.0,412.5>> = 11.107529223221462

	* m (U+006D): L<<240.0,491.0>--<167.0,267.0>>/B<<167.0,267.0>-<243.0,402.0>-<319.0,460.5>> = 11.327480573951592

	* m (U+006D): L<<529.0,340.0>--<507.0,275.0>>/B<<507.0,275.0>-<582.0,405.0>-<656.0,462.0>> = 11.282656564668194

	* n (U+006E): L<<240.0,491.0>--<165.0,261.0>>/B<<165.0,261.0>-<218.0,355.0>-<271.5,411.5>> = 11.355126896896378

	* nacute (U+0144): L<<240.0,491.0>--<165.0,261.0>>/B<<165.0,261.0>-<218.0,355.0>-<271.5,411.5>> = 11.355126896896378

	* ncaron (U+0148): L<<240.0,491.0>--<165.0,261.0>>/B<<165.0,261.0>-<218.0,355.0>-<271.5,411.5>> = 11.355126896896378

	* ntilde (U+00F1): L<<240.0,491.0>--<165.0,261.0>>/B<<165.0,261.0>-<218.0,355.0>-<271.5,411.5>> = 11.355126896896378

	* ordfeminine (U+00AA): B<<489.0,749.5>-<493.0,762.0>-<498.0,777.0>>/B<<498.0,777.0>-<443.0,689.0>-<394.5,650.0>> = 13.570434385161475

	* p (U+0070): L<<247.0,492.0>--<181.0,293.0>>/B<<181.0,293.0>-<252.0,409.0>-<316.5,464.0>> = 13.12097698284665

	* q (U+0071): L<<193.0,-494.0>--<423.0,214.0>>/B<<423.0,214.0>-<351.0,94.0>-<285.0,38.5>> = 12.96691473187095

	* r (U+0072): L<<239.0,491.0>--<165.0,265.0>>/B<<165.0,265.0>-<218.0,365.0>-<265.0,420.0>> = 9.793402802637424

	* racute (U+0155): L<<239.0,491.0>--<165.0,265.0>>/B<<165.0,265.0>-<218.0,365.0>-<265.0,420.0>> = 9.793402802637424

	* rcaron (U+0159): L<<239.0,491.0>--<165.0,265.0>>/B<<165.0,265.0>-<218.0,365.0>-<265.0,420.0>> = 9.793402802637424

	* thorn (U+00FE): L<<409.0,992.0>--<181.0,293.0>>/B<<181.0,293.0>-<251.0,409.0>-<316.0,464.0>> = 13.043505067470157

	* u (U+0075): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uacute (U+00FA): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* ubreve (U+016D): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* ucircumflex (U+00FB): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* udieresis (U+00FC): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* ugrave (U+00F9): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uhorn (U+01B0): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uhungarumlaut (U+0171): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* umacron (U+016B): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni0123 (U+0123): L<<256.0,-295.0>--<420.0,208.0>>/B<<420.0,208.0>-<349.0,92.0>-<282.5,37.5>> = 13.411273252730515

	* uni0146 (U+0146): L<<240.0,491.0>--<165.0,261.0>>/B<<165.0,261.0>-<218.0,355.0>-<271.5,411.5>> = 11.355126896896378

	* uni0157 (U+0157): L<<239.0,491.0>--<165.0,265.0>>/B<<165.0,265.0>-<218.0,365.0>-<265.0,420.0>> = 9.793402802637424

	* uni01CE (U+01CE): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni01D4 (U+01D4): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni01D6 (U+01D6): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni01D8 (U+01D8): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni01DA (U+01DA): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni01DC (U+01DC): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EA1 (U+1EA1): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EA3 (U+1EA3): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EA5 (U+1EA5): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EA7 (U+1EA7): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EA9 (U+1EA9): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EAB (U+1EAB): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EAD (U+1EAD): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EAF (U+1EAF): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EB1 (U+1EB1): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EB3 (U+1EB3): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EB5 (U+1EB5): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EB7 (U+1EB7): B<<403.0,162.0>-<412.0,189.0>-<420.0,216.0>>/B<<420.0,216.0>-<349.0,95.0>-<283.5,39.0>> = 13.899063092750804

	* uni1EE5 (U+1EE5): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EE7 (U+1EE7): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EE9 (U+1EE9): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EEB (U+1EEB): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EED (U+1EED): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EEF (U+1EEF): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EF1 (U+1EF1): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uni1EF5 (U+1EF5): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692

	* uni1EF7 (U+1EF7): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692

	* uni1EF9 (U+1EF9): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692

	* uogonek (U+0173): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* uring (U+016F): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* utilde (U+0169): L<<406.0,115.0>--<447.0,240.0>>/B<<447.0,240.0>-<370.0,102.0>-<292.0,43.0>> = 11.000760309450268

	* y (U+0079): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692

	* yacute (U+00FD): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692

	* ycircumflex (U+0177): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692

	* ydieresis (U+00FF): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692 

	* ygrave (U+1EF3): L<<274.0,-295.0>--<449.0,245.0>>/B<<449.0,245.0>-<397.0,150.0>-<343.0,93.0>> = 10.738739226716692 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] PlaypenNZL-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1473, but got 1000 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 500 instead. [code: descent]
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

	* eng (U+014B): L<<248.0,483.0>--<185.0,290.0>>/B<<185.0,290.0>-<254.0,409.0>-<328.0,464.0>> = 12.028556648968657

	* h (U+0068): L<<417.0,984.0>--<191.0,291.0>>/B<<191.0,291.0>-<261.0,409.0>-<334.5,464.0>> = 12.615183502986987

	* hbar (U+0127): L<<417.0,984.0>--<191.0,291.0>>/B<<191.0,291.0>-<261.0,409.0>-<334.5,464.0>> = 12.615183502986987

	* hcircumflex (U+0125): L<<417.0,984.0>--<191.0,291.0>>/B<<191.0,291.0>-<261.0,409.0>-<334.5,464.0>> = 12.615183502986987

	* m (U+006D): L<<248.0,483.0>--<187.0,297.0>>/B<<187.0,297.0>-<254.0,409.0>-<323.0,464.0>> = 12.731200983404351

	* m (U+006D): L<<532.0,331.0>--<522.0,302.0>>/B<<522.0,302.0>-<588.0,411.0>-<656.5,465.0>> = 12.169491550306956

	* n (U+006E): L<<248.0,483.0>--<185.0,290.0>>/B<<185.0,290.0>-<254.0,409.0>-<328.0,464.0>> = 12.028556648968657

	* nacute (U+0144): L<<248.0,483.0>--<185.0,290.0>>/B<<185.0,290.0>-<254.0,409.0>-<328.0,464.0>> = 12.028556648968657

	* ncaron (U+0148): L<<248.0,483.0>--<185.0,290.0>>/B<<185.0,290.0>-<254.0,409.0>-<328.0,464.0>> = 12.028556648968657

	* ntilde (U+00F1): L<<248.0,483.0>--<185.0,290.0>>/B<<185.0,290.0>-<254.0,409.0>-<328.0,464.0>> = 12.028556648968657

	* ordfeminine (U+00AA): B<<478.0,744.5>-<479.0,747.0>-<481.0,751.0>>/B<<481.0,751.0>-<430.0,679.0>-<384.0,645.0>> = 8.74616226255517

	* r (U+0072): L<<247.0,483.0>--<184.0,290.0>>/B<<184.0,290.0>-<254.0,414.0>-<319.0,466.5>> = 11.367458337735862

	* racute (U+0155): L<<247.0,483.0>--<184.0,290.0>>/B<<184.0,290.0>-<254.0,414.0>-<319.0,466.5>> = 11.367458337735862

	* rcaron (U+0159): L<<247.0,483.0>--<184.0,290.0>>/B<<184.0,290.0>-<254.0,414.0>-<319.0,466.5>> = 11.367458337735862

	* u (U+0075): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uacute (U+00FA): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* ubreve (U+016D): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* ucircumflex (U+00FB): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* udieresis (U+00FC): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* ugrave (U+00F9): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uhorn (U+01B0): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uhungarumlaut (U+0171): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* umacron (U+016B): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni0146 (U+0146): L<<248.0,483.0>--<185.0,290.0>>/B<<185.0,290.0>-<254.0,409.0>-<328.0,464.0>> = 12.028556648968657

	* uni0157 (U+0157): L<<247.0,483.0>--<184.0,290.0>>/B<<184.0,290.0>-<254.0,414.0>-<319.0,466.5>> = 11.367458337735862

	* uni01D4 (U+01D4): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni01D6 (U+01D6): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni01D8 (U+01D8): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni01DA (U+01DA): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni01DC (U+01DC): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EE5 (U+1EE5): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EE7 (U+1EE7): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EE9 (U+1EE9): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EEB (U+1EEB): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EED (U+1EED): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EEF (U+1EEF): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EF1 (U+1EF1): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uni1EF5 (U+1EF5): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986

	* uni1EF7 (U+1EF7): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986

	* uni1EF9 (U+1EF9): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986

	* uogonek (U+0173): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* uring (U+016F): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* utilde (U+0169): L<<403.0,132.0>--<428.0,209.0>>/B<<428.0,209.0>-<360.0,95.0>-<288.0,39.5>> = 12.828371099667704

	* y (U+0079): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986

	* yacute (U+00FD): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986

	* ycircumflex (U+0177): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986

	* ydieresis (U+00FF): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986 

	* ygrave (U+1EF3): L<<270.0,-283.0>--<432.0,217.0>>/B<<432.0,217.0>-<362.0,97.0>-<288.0,41.0>> = 12.304112854168986 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] PlaypenNZL-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1473, but got 1000 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 500 instead. [code: descent]
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

	* at (U+0040): B<<508.0,142.0>-<511.0,163.0>-<516.0,180.0>>/B<<516.0,180.0>-<515.0,177.0>-<513.0,171.5>> = 2.045408488886837

	* m (U+006D): B<<554.5,426.5>-<555.0,383.0>-<537.0,328.0>>/B<<537.0,328.0>-<595.0,420.0>-<658.0,469.5>> = 14.106897187197198

	* u (U+0075): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uacute (U+00FA): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* ubreve (U+016D): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* ucircumflex (U+00FB): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* udieresis (U+00FC): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* ugrave (U+00F9): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uhorn (U+01B0): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uhungarumlaut (U+0171): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* umacron (U+016B): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni01D4 (U+01D4): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni01D6 (U+01D6): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni01D8 (U+01D8): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni01DA (U+01DA): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni01DC (U+01DC): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EE5 (U+1EE5): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EE7 (U+1EE7): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EE9 (U+1EE9): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EEB (U+1EEB): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EED (U+1EED): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EEF (U+1EEF): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uni1EF1 (U+1EF1): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uogonek (U+0173): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926

	* uring (U+016F): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926 

	* utilde (U+0169): L<<399.0,148.0>--<410.0,180.0>>/B<<410.0,180.0>-<349.0,86.0>-<282.5,35.5>> = 14.010589736968926 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[11] PlaypenNZL-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

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
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and abs(yMin) to accommodate vowel marks.
>
>When the win Metrics are significantly greater than the upm, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 typo values instead. This means the font developer can control the linespacing with the typo values, whilst avoiding clipping by setting the win values to values greater than the yMax and abs(yMin).
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1473, but got 1000 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 500 instead. [code: descent]
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

	* a (U+0061): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* aacute (U+00E1): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* abreve (U+0103): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* acircumflex (U+00E2): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* adieresis (U+00E4): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* agrave (U+00E0): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* amacron (U+0101): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* aogonek (U+0105): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* aring (U+00E5): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* at (U+0040): B<<531.0,183.0>-<537.0,202.0>-<544.0,223.0>>/B<<544.0,223.0>-<492.0,131.0>-<443.5,92.0>> = 11.040940180323686

	* atilde (U+00E3): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* b (U+0062): L<<401.0,1001.0>--<160.0,263.0>>/B<<160.0,263.0>-<234.0,396.0>-<303.0,457.5>> = 11.006290955448899

	* d (U+0064): B<<416.5,168.5>-<429.0,207.0>-<441.0,245.0>>/B<<441.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.671917672341593

	* dcaron (U+010F): B<<416.5,168.5>-<429.0,207.0>-<441.0,245.0>>/B<<441.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.671917672341593

	* dcroat (U+0111): B<<416.5,168.5>-<429.0,207.0>-<441.0,245.0>>/B<<441.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.671917672341593

	* eng (U+014B): L<<233.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<205.0,341.0>-<263.0,403.5>> = 10.159669810244182

	* g (U+0067): L<<260.0,-307.0>--<439.0,241.0>>/B<<439.0,241.0>-<364.0,107.0>-<295.0,45.0>> = 11.146574849335753

	* gbreve (U+011F): L<<260.0,-307.0>--<439.0,241.0>>/B<<439.0,241.0>-<364.0,107.0>-<295.0,45.0>> = 11.146574849335753

	* gcircumflex (U+011D): L<<260.0,-307.0>--<439.0,241.0>>/B<<439.0,241.0>-<364.0,107.0>-<295.0,45.0>> = 11.146574849335753

	* gdotaccent (U+0121): L<<260.0,-307.0>--<439.0,241.0>>/B<<439.0,241.0>-<364.0,107.0>-<295.0,45.0>> = 11.146574849335753

	* h (U+0068): L<<402.0,999.0>--<152.0,234.0>>/B<<152.0,234.0>-<210.0,343.0>-<268.0,405.0>> = 9.920636959741115

	* hbar (U+0127): L<<402.0,999.0>--<152.0,234.0>>/B<<152.0,234.0>-<210.0,343.0>-<268.0,405.0>> = 9.920636959741115

	* hcircumflex (U+0125): L<<402.0,999.0>--<152.0,234.0>>/B<<152.0,234.0>-<210.0,343.0>-<268.0,405.0>> = 9.920636959741115

	* m (U+006D): L<<233.0,498.0>--<147.0,234.0>>/B<<147.0,234.0>-<205.0,342.0>-<261.5,404.5>> = 10.194033532835965

	* m (U+006D): L<<526.0,350.0>--<491.0,246.0>>/B<<491.0,246.0>-<547.0,350.0>-<602.5,409.5>> = 9.700689879973245

	* n (U+006E): L<<233.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<205.0,341.0>-<263.0,403.5>> = 10.159669810244182

	* nacute (U+0144): L<<233.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<205.0,341.0>-<263.0,403.5>> = 10.159669810244182

	* ncaron (U+0148): L<<233.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<205.0,341.0>-<263.0,403.5>> = 10.159669810244182

	* ntilde (U+00F1): L<<233.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<205.0,341.0>-<263.0,403.5>> = 10.159669810244182

	* ordfeminine (U+00AA): B<<500.0,755.0>-<508.0,778.0>-<516.0,803.0>>/B<<516.0,803.0>-<457.0,700.0>-<405.0,655.5>> = 12.060079848123186

	* p (U+0070): L<<239.0,500.0>--<161.0,263.0>>/B<<161.0,263.0>-<236.0,396.0>-<304.5,457.5>> = 11.201980953923506

	* q (U+0071): L<<199.0,-500.0>--<440.0,239.0>>/B<<440.0,239.0>-<366.0,105.0>-<297.0,44.0>> = 10.847188255683562

	* r (U+0072): L<<231.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<190.0,328.0>-<229.0,383.0>> = 8.137886781323362

	* racute (U+0155): L<<231.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<190.0,328.0>-<229.0,383.0>> = 8.137886781323362

	* rcaron (U+0159): L<<231.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<190.0,328.0>-<229.0,383.0>> = 8.137886781323362

	* thorn (U+00FE): L<<401.0,1000.0>--<161.0,263.0>>/B<<161.0,263.0>-<236.0,396.0>-<304.5,457.5>> = 11.38152130388753

	* u (U+0075): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uacute (U+00FA): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* ubreve (U+016D): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* ucircumflex (U+00FB): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* udieresis (U+00FC): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* ugrave (U+00F9): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uhorn (U+01B0): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uhungarumlaut (U+0171): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* umacron (U+016B): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni0123 (U+0123): L<<260.0,-307.0>--<439.0,241.0>>/B<<439.0,241.0>-<364.0,107.0>-<295.0,45.0>> = 11.146574849335753

	* uni0146 (U+0146): L<<233.0,498.0>--<146.0,231.0>>/B<<146.0,231.0>-<205.0,341.0>-<263.0,403.5>> = 10.159669810244182

	* uni0157 (U+0157): L<<231.0,498.0>--<146.0,239.0>>/B<<146.0,239.0>-<190.0,328.0>-<229.0,383.0>> = 8.137886781323362

	* uni01CE (U+01CE): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni01D4 (U+01D4): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni01D6 (U+01D6): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni01D8 (U+01D8): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni01DA (U+01DA): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni01DC (U+01DC): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EA1 (U+1EA1): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EA3 (U+1EA3): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EA5 (U+1EA5): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EA7 (U+1EA7): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EA9 (U+1EA9): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EAB (U+1EAB): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EAD (U+1EAD): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EAF (U+1EAF): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EB1 (U+1EB1): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EB3 (U+1EB3): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EB5 (U+1EB5): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EB7 (U+1EB7): B<<415.0,167.0>-<428.0,206.0>-<440.0,245.0>>/B<<440.0,245.0>-<365.0,109.0>-<296.0,46.0>> = 11.772714427175737

	* uni1EE5 (U+1EE5): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EE7 (U+1EE7): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EE9 (U+1EE9): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EEB (U+1EEB): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EED (U+1EED): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EEF (U+1EEF): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EF1 (U+1EF1): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uni1EF5 (U+1EF5): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186

	* uni1EF7 (U+1EF7): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186

	* uni1EF9 (U+1EF9): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186

	* uogonek (U+0173): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* uring (U+016F): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* utilde (U+0169): L<<410.0,99.0>--<467.0,274.0>>/B<<467.0,274.0>-<409.0,163.0>-<351.0,99.5>> = 9.546911768910597

	* y (U+0079): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186

	* yacute (U+00FD): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186

	* ycircumflex (U+0177): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186

	* ydieresis (U+00FF): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186 

	* ygrave (U+1EF3): L<<278.0,-307.0>--<466.0,272.0>>/B<<466.0,272.0>-<408.0,163.0>-<349.5,100.5>> = 10.029396307304186 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 16 | 29 | 482 | 25 | 381 | 0 |
| 0% | 2% | 3% | 52% | 3% | 41% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
