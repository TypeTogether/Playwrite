## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[11] PlaypenISL-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1348, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
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
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ISL ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/fonttools/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* ⚠ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.65x (1650) [code: bad-hhea-range]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check if uppercase glyphs are vertically centered. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/caps_vertically_centered">com.google.fonts/check/caps_vertically_centered</a>)</summary><div>

>
>This check suggests one possible approach to designing vertical metrics, but can be ingnored if you follow a different approach. In order to center text in buttons, lists, and grid systems with minimal additional CSS work, the uppercase glyphs should be vertically centered in the em box. This check mainly applies to Latin, Greek, Cyrillic, and other similar scripts. For non-latin scripts like Arabic, this check might not be applicable. There is a detailed description of this subject at: https://x.com/romanshamin_en/status/1562801657691672576
>
* ⚠ **WARN** Uppercase glyphs are not vertically centered in the em box. [code: vertical-metrics-not-centered]
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

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- U_locl.au

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mod_e_z.ful

	- cnct.mod_r_z.cnt

	- cnct.mod_v_n.cnt

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

	- q.jmc_ar

	- q.mod_au

	- seven.alt1

	- t.lop_de

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

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 cnct.mod_r_z.cnt (unencoded) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>

>
>This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
>
>This check is not run for variable fonts, as they may legitimately have colinear vectors.
>
* ⚠ **WARN** The following glyphs have colinear vectors:

	* ae (U+00E6): L<<501.0,422.0>--<501.0,422.0>> -> L<<501.0,422.0>--<501.0,422.0>>

	* aeacute (U+01FD): L<<501.0,422.0>--<501.0,422.0>> -> L<<501.0,422.0>--<501.0,422.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* a (U+0061): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* aacute (U+00E1): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* abreve (U+0103): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* acircumflex (U+00E2): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* adieresis (U+00E4): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* agrave (U+00E0): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* amacron (U+0101): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* aogonek (U+0105): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* aring (U+00E5): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* atilde (U+00E3): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* b (U+0062): L<<323.0,869.0>--<177.0,293.0>>/B<<177.0,293.0>-<239.0,411.0>-<301.0,465.0>> = 13.495170565543694

	* eng (U+014B): L<<222.0,492.0>--<164.0,260.0>>/B<<164.0,260.0>-<210.0,356.0>-<260.0,412.5>> = 11.565944083515308

	* h (U+0068): L<<323.0,867.0>--<170.0,261.0>>/B<<170.0,261.0>-<216.0,356.0>-<266.0,412.5>> = 11.667109880681993

	* hbar (U+0127): L<<323.0,867.0>--<170.0,261.0>>/B<<170.0,261.0>-<216.0,356.0>-<266.0,412.5>> = 11.667109880681993

	* hcircumflex (U+0125): L<<323.0,867.0>--<170.0,261.0>>/B<<170.0,261.0>-<216.0,356.0>-<266.0,412.5>> = 11.667109880681993

	* m (U+006D): L<<222.0,492.0>--<166.0,267.0>>/B<<166.0,267.0>-<210.0,358.0>-<258.0,413.5>> = 11.828221733920218

	* m (U+006D): L<<521.0,345.0>--<502.0,270.0>>/B<<502.0,270.0>-<547.0,360.0>-<594.5,414.5>> = 12.349197703404412

	* n (U+006E): L<<222.0,492.0>--<164.0,260.0>>/B<<164.0,260.0>-<210.0,356.0>-<260.0,412.5>> = 11.565944083515308

	* nacute (U+0144): L<<222.0,492.0>--<164.0,260.0>>/B<<164.0,260.0>-<210.0,356.0>-<260.0,412.5>> = 11.565944083515308

	* ncaron (U+0148): L<<222.0,492.0>--<164.0,260.0>>/B<<164.0,260.0>-<210.0,356.0>-<260.0,412.5>> = 11.565944083515308

	* ntilde (U+00F1): L<<222.0,492.0>--<164.0,260.0>>/B<<164.0,260.0>-<210.0,356.0>-<260.0,412.5>> = 11.565944083515308

	* p (U+0070): L<<229.0,493.0>--<178.0,293.0>>/B<<178.0,293.0>-<240.0,411.0>-<302.0,465.0>> = 13.412949781561384

	* q (U+0071): L<<278.0,-370.0>--<426.0,214.0>>/B<<426.0,214.0>-<363.0,93.0>-<299.5,38.0>> = 13.283471822625618

	* r (U+0072): L<<221.0,492.0>--<164.0,265.0>>/B<<164.0,265.0>-<209.0,365.0>-<253.0,420.0>> = 10.132128006500182

	* racute (U+0155): L<<221.0,492.0>--<164.0,265.0>>/B<<164.0,265.0>-<209.0,365.0>-<253.0,420.0>> = 10.132128006500182

	* rcaron (U+0159): L<<221.0,492.0>--<164.0,265.0>>/B<<164.0,265.0>-<209.0,365.0>-<253.0,420.0>> = 10.132128006500182

	* thorn (U+00FE): L<<323.0,868.0>--<178.0,293.0>>/B<<178.0,293.0>-<240.0,411.0>-<302.0,465.0>> = 13.565089040331943

	* u (U+0075): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uacute (U+00FA): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* ubreve (U+016D): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* ucircumflex (U+00FB): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* udieresis (U+00FC): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* ugrave (U+00F9): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uhorn (U+01B0): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uhungarumlaut (U+0171): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* umacron (U+016B): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni0146 (U+0146): L<<222.0,492.0>--<164.0,260.0>>/B<<164.0,260.0>-<210.0,356.0>-<260.0,412.5>> = 11.565944083515308

	* uni0157 (U+0157): L<<221.0,492.0>--<164.0,265.0>>/B<<164.0,265.0>-<209.0,365.0>-<253.0,420.0>> = 10.132128006500182

	* uni01CE (U+01CE): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni01D4 (U+01D4): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni01D6 (U+01D6): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni01D8 (U+01D8): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni01DA (U+01DA): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni01DC (U+01DC): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EA1 (U+1EA1): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EA3 (U+1EA3): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EA5 (U+1EA5): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EA7 (U+1EA7): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EA9 (U+1EA9): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EAB (U+1EAB): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EAD (U+1EAD): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EAF (U+1EAF): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EB1 (U+1EB1): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EB3 (U+1EB3): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EB5 (U+1EB5): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EB7 (U+1EB7): B<<409.0,158.5>-<416.0,187.0>-<423.0,216.0>>/B<<423.0,216.0>-<360.0,95.0>-<297.5,39.0>> = 13.933807737652076

	* uni1EE5 (U+1EE5): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EE7 (U+1EE7): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EE9 (U+1EE9): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EEB (U+1EEB): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EED (U+1EED): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EEF (U+1EEF): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EF1 (U+1EF1): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uni1EF5 (U+1EF5): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* uni1EF7 (U+1EF7): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* uni1EF9 (U+1EF9): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* uogonek (U+0173): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* uring (U+016F): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* utilde (U+0169): L<<416.0,107.0>--<450.0,243.0>>/B<<450.0,243.0>-<404.0,149.0>-<354.5,92.0>> = 12.039112116022293

	* y (U+0079): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* yacute (U+00FD): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* ycircumflex (U+0177): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* ydieresis (U+00FF): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148

	* ygrave (U+1EF3): L<<345.0,-167.0>--<449.0,246.0>>/B<<449.0,246.0>-<403.0,150.0>-<353.0,92.5>> = 11.46805845065148 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] PlaypenISL-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1348, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* ⚠ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.65x (1650) [code: bad-hhea-range]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check if uppercase glyphs are vertically centered. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/caps_vertically_centered">com.google.fonts/check/caps_vertically_centered</a>)</summary><div>

>
>This check suggests one possible approach to designing vertical metrics, but can be ingnored if you follow a different approach. In order to center text in buttons, lists, and grid systems with minimal additional CSS work, the uppercase glyphs should be vertically centered in the em box. This check mainly applies to Latin, Greek, Cyrillic, and other similar scripts. For non-latin scripts like Arabic, this check might not be applicable. There is a detailed description of this subject at: https://x.com/romanshamin_en/status/1562801657691672576
>
* ⚠ **WARN** Uppercase glyphs are not vertically centered in the em box. [code: vertical-metrics-not-centered]
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

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- U_locl.au

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mod_e_z.ful

	- cnct.mod_r_z.cnt

	- cnct.mod_v_n.cnt

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

	- q.jmc_ar

	- q.mod_au

	- seven.alt1

	- t.lop_de

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

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 cnct.mod_r_z.cnt (unencoded) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* eng (U+014B): L<<230.0,485.0>--<181.0,290.0>>/B<<181.0,290.0>-<244.0,412.0>-<315.0,465.5>> = 13.206175987431887

	* h (U+0068): L<<332.0,861.0>--<188.0,290.0>>/B<<188.0,290.0>-<250.0,411.0>-<321.0,465.0>> = 12.9762187379373

	* hbar (U+0127): L<<332.0,861.0>--<188.0,290.0>>/B<<188.0,290.0>-<250.0,411.0>-<321.0,465.0>> = 12.9762187379373

	* hcircumflex (U+0125): L<<332.0,861.0>--<188.0,290.0>>/B<<188.0,290.0>-<250.0,411.0>-<321.0,465.0>> = 12.9762187379373

	* m (U+006D): L<<230.0,485.0>--<183.0,297.0>>/B<<183.0,297.0>-<244.0,412.0>-<310.5,465.5>> = 13.906790955456463

	* m (U+006D): L<<525.0,338.0>--<515.0,296.0>>/B<<515.0,296.0>-<575.0,412.0>-<642.0,465.5>> = 13.957378026318773

	* n (U+006E): L<<230.0,485.0>--<181.0,290.0>>/B<<181.0,290.0>-<244.0,412.0>-<315.0,465.5>> = 13.206175987431887

	* nacute (U+0144): L<<230.0,485.0>--<181.0,290.0>>/B<<181.0,290.0>-<244.0,412.0>-<315.0,465.5>> = 13.206175987431887

	* ncaron (U+0148): L<<230.0,485.0>--<181.0,290.0>>/B<<181.0,290.0>-<244.0,412.0>-<315.0,465.5>> = 13.206175987431887

	* ntilde (U+00F1): L<<230.0,485.0>--<181.0,290.0>>/B<<181.0,290.0>-<244.0,412.0>-<315.0,465.5>> = 13.206175987431887

	* r (U+0072): L<<230.0,485.0>--<181.0,291.0>>/B<<181.0,291.0>-<243.0,416.0>-<304.5,467.5>> = 12.20626943170575

	* racute (U+0155): L<<230.0,485.0>--<181.0,291.0>>/B<<181.0,291.0>-<243.0,416.0>-<304.5,467.5>> = 12.20626943170575

	* rcaron (U+0159): L<<230.0,485.0>--<181.0,291.0>>/B<<181.0,291.0>-<243.0,416.0>-<304.5,467.5>> = 12.20626943170575

	* u (U+0075): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uacute (U+00FA): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* ubreve (U+016D): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* ucircumflex (U+00FB): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* udieresis (U+00FC): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* ugrave (U+00F9): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uhorn (U+01B0): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uhungarumlaut (U+0171): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* umacron (U+016B): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni0146 (U+0146): L<<230.0,485.0>--<181.0,290.0>>/B<<181.0,290.0>-<244.0,412.0>-<315.0,465.5>> = 13.206175987431887

	* uni0157 (U+0157): L<<230.0,485.0>--<181.0,291.0>>/B<<181.0,291.0>-<243.0,416.0>-<304.5,467.5>> = 12.20626943170575

	* uni01D4 (U+01D4): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni01D6 (U+01D6): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni01D8 (U+01D8): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni01DA (U+01DA): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni01DC (U+01DC): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EE5 (U+1EE5): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EE7 (U+1EE7): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EE9 (U+1EE9): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EEB (U+1EEB): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EED (U+1EED): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EEF (U+1EEF): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EF1 (U+1EF1): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uni1EF5 (U+1EF5): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* uni1EF7 (U+1EF7): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* uni1EF9 (U+1EF9): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* uogonek (U+0173): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* uring (U+016F): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* utilde (U+0169): L<<411.0,122.0>--<433.0,212.0>>/B<<433.0,212.0>-<371.0,94.0>-<301.0,39.0>> = 13.98223332256077

	* y (U+0079): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* yacute (U+00FD): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* ycircumflex (U+0177): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* ydieresis (U+00FF): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689

	* ygrave (U+1EF3): L<<339.0,-157.0>--<434.0,217.0>>/B<<434.0,217.0>-<371.0,95.0>-<300.0,40.0>> = 13.059216715414689 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] PlaypenISL-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1348, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* ⚠ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.65x (1650) [code: bad-hhea-range]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check if uppercase glyphs are vertically centered. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/caps_vertically_centered">com.google.fonts/check/caps_vertically_centered</a>)</summary><div>

>
>This check suggests one possible approach to designing vertical metrics, but can be ingnored if you follow a different approach. In order to center text in buttons, lists, and grid systems with minimal additional CSS work, the uppercase glyphs should be vertically centered in the em box. This check mainly applies to Latin, Greek, Cyrillic, and other similar scripts. For non-latin scripts like Arabic, this check might not be applicable. There is a detailed description of this subject at: https://x.com/romanshamin_en/status/1562801657691672576
>
* ⚠ **WARN** Uppercase glyphs are not vertically centered in the em box. [code: vertical-metrics-not-centered]
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

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- U_locl.au

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mod_e_z.ful

	- cnct.mod_r_z.cnt

	- cnct.mod_v_n.cnt

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

	- q.jmc_ar

	- q.mod_au

	- seven.alt1

	- t.lop_de

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

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 cnct.mod_r_z.cnt (unencoded) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* m (U+006D): L<<529.0,332.0>--<526.0,321.0>>/B<<526.0,321.0>-<581.0,419.0>-<643.5,469.0>> = 14.047088779080896 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] PlaypenISL-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1348, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking post.italicAngle value. (derived from com.google.fonts/check/italic_angle) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/post.html#com.google.fonts/check/italic_angle">com.google.fonts/check/italic_angle</a>)</summary><div>

>
>The 'post' table italicAngle property should be a reasonable amount, likely not more than 30°. Note that in the OpenType specification, the value is negative for a rightward lean.
>
>https://docs.microsoft.com/en-us/typography/opentype/spec/post
>
* 🔥 **FAIL** Font is not italic, so post.italicAngle should be equal to zero. [code: non-zero-upright]
</div></details><details><summary>⚠ <b>WARN:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* ⚠ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.65x (1650) [code: bad-hhea-range]
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
</div></details><details><summary>⚠ <b>WARN:</b> Check if uppercase glyphs are vertically centered. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/caps_vertically_centered">com.google.fonts/check/caps_vertically_centered</a>)</summary><div>

>
>This check suggests one possible approach to designing vertical metrics, but can be ingnored if you follow a different approach. In order to center text in buttons, lists, and grid systems with minimal additional CSS work, the uppercase glyphs should be vertically centered in the em box. This check mainly applies to Latin, Greek, Cyrillic, and other similar scripts. For non-latin scripts like Arabic, this check might not be applicable. There is a detailed description of this subject at: https://x.com/romanshamin_en/status/1562801657691672576
>
* ⚠ **WARN** Uppercase glyphs are not vertically centered in the em box. [code: vertical-metrics-not-centered]
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

	- AE.cur.locl

	- F.cur_locl

	- G.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- U_locl.au

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mod_e_z.ful

	- cnct.mod_r_z.cnt

	- cnct.mod_v_n.cnt

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

	- q.jmc_ar

	- q.mod_au

	- seven.alt1

	- t.lop_de

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

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: Tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 cnct.mod_r_z.cnt (unencoded) and tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* a (U+0061): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* aacute (U+00E1): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* abreve (U+0103): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* acircumflex (U+00E2): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* adieresis (U+00E4): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* agrave (U+00E0): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* amacron (U+0101): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* aogonek (U+0105): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* aring (U+00E5): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* at (U+0040): B<<538.0,192.5>-<544.0,217.0>-<550.0,243.0>>/B<<550.0,243.0>-<499.0,141.0>-<450.0,97.0>> = 13.570434385161475

	* atilde (U+00E3): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* b (U+0062): L<<314.0,876.0>--<159.0,263.0>>/B<<159.0,263.0>-<224.0,397.0>-<289.5,458.0>> = 11.686759912415228

	* d (U+0064): B<<422.0,164.5>-<432.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 13.042143424517748

	* dcaron (U+010F): B<<422.0,164.5>-<432.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 13.042143424517748

	* dcroat (U+0111): B<<422.0,164.5>-<432.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 13.042143424517748

	* eng (U+014B): L<<215.0,498.0>--<147.0,231.0>>/B<<147.0,231.0>-<198.0,340.0>-<252.0,403.0>> = 10.785995374189115

	* g (U+0067): L<<333.0,-177.0>--<438.0,234.0>>/B<<438.0,234.0>-<372.0,103.0>-<307.0,43.0>> = 12.408659540181475

	* gbreve (U+011F): L<<333.0,-177.0>--<438.0,234.0>>/B<<438.0,234.0>-<372.0,103.0>-<307.0,43.0>> = 12.408659540181475

	* gcircumflex (U+011D): L<<333.0,-177.0>--<438.0,234.0>>/B<<438.0,234.0>-<372.0,103.0>-<307.0,43.0>> = 12.408659540181475

	* gdotaccent (U+0121): L<<333.0,-177.0>--<438.0,234.0>>/B<<438.0,234.0>-<372.0,103.0>-<307.0,43.0>> = 12.408659540181475

	* h (U+0068): L<<315.0,874.0>--<153.0,232.0>>/B<<153.0,232.0>-<202.0,341.0>-<256.5,404.0>> = 10.043716989183576

	* hbar (U+0127): L<<315.0,874.0>--<153.0,232.0>>/B<<153.0,232.0>-<202.0,341.0>-<256.5,404.0>> = 10.043716989183576

	* hcircumflex (U+0125): L<<315.0,874.0>--<153.0,232.0>>/B<<153.0,232.0>-<202.0,341.0>-<256.5,404.0>> = 10.043716989183576

	* m (U+006D): L<<214.0,498.0>--<147.0,233.0>>/B<<147.0,233.0>-<197.0,342.0>-<250.0,404.5>> = 10.452901288908567

	* m (U+006D): L<<517.0,351.0>--<488.0,241.0>>/B<<488.0,241.0>-<538.0,347.0>-<590.0,407.5>> = 10.483964864282214

	* n (U+006E): L<<215.0,498.0>--<147.0,231.0>>/B<<147.0,231.0>-<198.0,340.0>-<252.0,403.0>> = 10.785995374189115

	* nacute (U+0144): L<<215.0,498.0>--<147.0,231.0>>/B<<147.0,231.0>-<198.0,340.0>-<252.0,403.0>> = 10.785995374189115

	* ncaron (U+0148): L<<215.0,498.0>--<147.0,231.0>>/B<<147.0,231.0>-<198.0,340.0>-<252.0,403.0>> = 10.785995374189115

	* ntilde (U+00F1): L<<215.0,498.0>--<147.0,231.0>>/B<<147.0,231.0>-<198.0,340.0>-<252.0,403.0>> = 10.785995374189115

	* ordfeminine (U+00AA): B<<432.0,626.5>-<438.0,651.0>-<444.0,677.0>>/B<<444.0,677.0>-<393.0,575.0>-<344.0,530.5>> = 13.570434385161475

	* p (U+0070): L<<220.0,500.0>--<160.0,263.0>>/B<<160.0,263.0>-<226.0,397.0>-<291.0,458.0>> = 12.015200659794086

	* q (U+0071): L<<285.0,-375.0>--<441.0,239.0>>/B<<441.0,239.0>-<375.0,104.0>-<309.5,43.5>> = 11.797896943705565

	* r (U+0072): L<<213.0,498.0>--<147.0,239.0>>/B<<147.0,239.0>-<184.0,327.0>-<219.0,382.0>> = 8.508336085291484

	* racute (U+0155): L<<213.0,498.0>--<147.0,239.0>>/B<<147.0,239.0>-<184.0,327.0>-<219.0,382.0>> = 8.508336085291484

	* rcaron (U+0159): L<<213.0,498.0>--<147.0,239.0>>/B<<147.0,239.0>-<184.0,327.0>-<219.0,382.0>> = 8.508336085291484

	* thorn (U+00FE): L<<315.0,875.0>--<160.0,263.0>>/B<<160.0,263.0>-<226.0,397.0>-<291.0,458.0>> = 12.009632340390764

	* u (U+0075): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uacute (U+00FA): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* ubreve (U+016D): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* ucircumflex (U+00FB): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* udieresis (U+00FC): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* ugrave (U+00F9): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uhorn (U+01B0): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uhungarumlaut (U+0171): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* umacron (U+016B): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni0123 (U+0123): L<<333.0,-177.0>--<438.0,234.0>>/B<<438.0,234.0>-<372.0,103.0>-<307.0,43.0>> = 12.408659540181475

	* uni0146 (U+0146): L<<215.0,498.0>--<147.0,231.0>>/B<<147.0,231.0>-<198.0,340.0>-<252.0,403.0>> = 10.785995374189115

	* uni0157 (U+0157): L<<213.0,498.0>--<147.0,239.0>>/B<<147.0,239.0>-<184.0,327.0>-<219.0,382.0>> = 8.508336085291484

	* uni01CE (U+01CE): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni01D4 (U+01D4): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni01D6 (U+01D6): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni01D8 (U+01D8): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni01DA (U+01DA): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni01DC (U+01DC): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EA1 (U+1EA1): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EA3 (U+1EA3): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EA5 (U+1EA5): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EA7 (U+1EA7): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EA9 (U+1EA9): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EAB (U+1EAB): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EAD (U+1EAD): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EAF (U+1EAF): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EB1 (U+1EB1): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EB3 (U+1EB3): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EB5 (U+1EB5): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EB7 (U+1EB7): B<<421.0,164.0>-<431.0,204.0>-<441.0,244.0>>/B<<441.0,244.0>-<375.0,107.0>-<309.0,45.0>> = 11.6862834484111

	* uni1EE5 (U+1EE5): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EE7 (U+1EE7): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EE9 (U+1EE9): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EEB (U+1EEB): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EED (U+1EED): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EEF (U+1EEF): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EF1 (U+1EF1): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uni1EF5 (U+1EF5): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* uni1EF7 (U+1EF7): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* uni1EF9 (U+1EF9): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* uogonek (U+0173): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* uring (U+016F): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* utilde (U+0169): L<<421.0,92.0>--<467.0,277.0>>/B<<467.0,277.0>-<416.0,165.0>-<362.0,100.5>> = 10.519137783872264

	* y (U+0079): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* yacute (U+00FD): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* ycircumflex (U+0177): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* ydieresis (U+00FF): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181

	* ygrave (U+1EF3): L<<350.0,-177.0>--<465.0,274.0>>/B<<465.0,274.0>-<415.0,164.0>-<360.5,100.5>> = 10.138999361000181 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 30 | 490 | 25 | 396 | 0 |
| 0% | 1% | 3% | 52% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
