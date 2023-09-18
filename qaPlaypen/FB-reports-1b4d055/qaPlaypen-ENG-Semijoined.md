## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[9] PlaypenENGSemijoined-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined ExtraLight' / SUBFAMILY_NAME = 'Regular'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* r (U+0072): L<<159.0,496.0>--<159.0,301.0>>/B<<159.0,301.0>-<179.0,386.0>-<209.0,433.5>> = 13.24051991518721

	* racute (U+0155): L<<159.0,496.0>--<159.0,301.0>>/B<<159.0,301.0>-<179.0,386.0>-<209.0,433.5>> = 13.24051991518721

	* rcaron (U+0159): L<<159.0,496.0>--<159.0,301.0>>/B<<159.0,301.0>-<179.0,386.0>-<209.0,433.5>> = 13.24051991518721

	* uni0157 (U+0157): L<<159.0,496.0>--<159.0,301.0>>/B<<159.0,301.0>-<179.0,386.0>-<209.0,433.5>> = 13.24051991518721 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] PlaypenENGSemijoined-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined ExtraLight' / SUBFAMILY_NAME = 'Italic'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* exclam (U+0021): X=177.5,Y=1.0 (should be at baseline 0?)

	* quotedbl (U+0022): X=128.0,Y=873.0 (should be at cap-height 875?)

	* quotedbl (U+0022): X=270.0,Y=873.0 (should be at cap-height 875?)

	* quotesingle (U+0027): X=128.0,Y=873.0 (should be at cap-height 875?)

	* asterisk (U+002A): X=236.0,Y=877.0 (should be at cap-height 875?)

	* asterisk (U+002A): X=278.0,Y=876.0 (should be at cap-height 875?)

	* one (U+0031): X=283.0,Y=873.0 (should be at cap-height 875?)

	* question (U+003F): X=200.5,Y=1.0 (should be at baseline 0?)

	* M (U+004D): X=279.0,Y=873.0 (should be at cap-height 875?)

	* M (U+004D): X=924.0,Y=873.0 (should be at cap-height 875?)

	* N (U+004E): X=278.0,Y=874.0 (should be at cap-height 875?)

	* N (U+004E): X=660.0,Y=2.0 (should be at baseline 0?)

	* X (U+0058): X=560.0,Y=1.0 (should be at baseline 0?)

	* X (U+0058): X=66.0,Y=-2.0 (should be at baseline 0?)

	* X (U+0058): X=186.0,Y=876.0 (should be at cap-height 875?)

	* c (U+0063): X=415.0,Y=499.0 (should be at x-height 500?)

	* e (U+0065): X=341.5,Y=-1.0 (should be at baseline 0?)

	* f (U+0066): X=-65.0,Y=-374.5 (should be at descender -375?)

	* f (U+0066): X=431.0,Y=877.0 (should be at cap-height 875?)

	* h (U+0068): X=330.5,Y=498.5 (should be at x-height 500?)

	* h (U+0068): X=479.0,Y=502.0 (should be at x-height 500?)

	* j (U+006A): X=-89.0,Y=-375.5 (should be at descender -375?)

	* k (U+006B): X=464.0,Y=-1.0 (should be at baseline 0?)

	* m (U+006D): X=319.5,Y=498.5 (should be at x-height 500?)

	* m (U+006D): X=654.5,Y=498.5 (should be at x-height 500?)

	* n (U+006E): X=324.5,Y=498.5 (should be at x-height 500?)

	* n (U+006E): X=473.5,Y=502.0 (should be at x-height 500?)

	* y (U+0079): X=144.0,Y=0.5 (should be at baseline 0?)

	* braceleft (U+007B): X=182.0,Y=877.0 (should be at cap-height 875?)

	* braceright (U+007D): X=194.5,Y=-2.0 (should be at baseline 0?)

	* registered (U+00AE): X=295.0,Y=877.0 (should be at cap-height 875?)

	* ordmasculine (U+00BA): X=386.0,Y=877.0 (should be at cap-height 875?)

	* guillemotright (U+00BB): X=88.0,Y=-1.0 (should be at baseline 0?)

	* guillemotright (U+00BB): X=338.0,Y=-1.0 (should be at baseline 0?)

	* AE (U+00C6): X=44.0,Y=1.0 (should be at baseline 0?)

	* Ntilde (U+00D1): X=278.0,Y=874.0 (should be at cap-height 875?)

	* Ntilde (U+00D1): X=660.0,Y=2.0 (should be at baseline 0?)

	* ae (U+00E6): X=705.0,Y=-1.0 (should be at baseline 0?)

	* egrave (U+00E8): X=341.5,Y=-1.0 (should be at baseline 0?)

	* eacute (U+00E9): X=341.5,Y=-1.0 (should be at baseline 0?)

	* ecircumflex (U+00EA): X=341.5,Y=-1.0 (should be at baseline 0?)

	* edieresis (U+00EB): X=341.5,Y=-1.0 (should be at baseline 0?)

	* yacute (U+00FD): X=144.0,Y=0.5 (should be at baseline 0?)

	* ydieresis (U+00FF): X=144.0,Y=0.5 (should be at baseline 0?)

	* emacron (U+0113): X=341.5,Y=-1.0 (should be at baseline 0?)

	* ebreve (U+0115): X=341.5,Y=-1.0 (should be at baseline 0?)

	* edotaccent (U+0117): X=341.5,Y=-1.0 (should be at baseline 0?)

	* eogonek (U+0119): X=341.5,Y=-1.0 (should be at baseline 0?)

	* ecaron (U+011B): X=341.5,Y=-1.0 (should be at baseline 0?)

	* Iogonek (U+012E): X=161.0,Y=-1.0 (should be at baseline 0?)

	* ij (U+0133): X=213.0,Y=-375.5 (should be at descender -375?)

	* jcircumflex (U+0135): X=-88.0,Y=-376.0 (should be at descender -375?)

	* uni0137 (U+0137): X=464.0,Y=-1.0 (should be at baseline 0?)

	* Nacute (U+0143): X=278.0,Y=874.0 (should be at cap-height 875?)

	* Nacute (U+0143): X=660.0,Y=2.0 (should be at baseline 0?)

	* uni0145 (U+0145): X=278.0,Y=874.0 (should be at cap-height 875?)

	* uni0145 (U+0145): X=660.0,Y=2.0 (should be at baseline 0?)

	* Ncaron (U+0147): X=278.0,Y=874.0 (should be at cap-height 875?)

	* Ncaron (U+0147): X=660.0,Y=2.0 (should be at baseline 0?)

	* Eng (U+014A): X=660.0,Y=1.0 (should be at baseline 0?)

	* Eng (U+014A): X=278.0,Y=874.0 (should be at cap-height 875?)

	* oe (U+0153): X=718.5,Y=-1.0 (should be at baseline 0?)

	* ycircumflex (U+0177): X=144.0,Y=0.5 (should be at baseline 0?)

	* uni01D8 (U+01D8): X=356.0,Y=874.0 (should be at cap-height 875?)

	* uni01D9 (U+01D9): X=721.0,Y=1273.0 (should be at ascender 1275?)

	* uni01D9 (U+01D9): X=364.0,Y=1274.0 (should be at ascender 1275?)

	* uni01DC (U+01DC): X=405.0,Y=876.0 (should be at cap-height 875?)

	* AEacute (U+01FC): X=44.0,Y=1.0 (should be at baseline 0?)

	* aeacute (U+01FD): X=705.0,Y=-1.0 (should be at baseline 0?)

	* uni0237 (U+0237): X=-88.0,Y=-376.0 (should be at descender -375?)

	* uni1EA6 (U+1EA6): X=544.0,Y=1274.0 (should be at ascender 1275?)

	* uni1EAA (U+1EAA): X=386.0,Y=1277.0 (should be at ascender 1275?)

	* uni1EAE (U+1EAE): X=600.0,Y=1277.0 (should be at ascender 1275?)

	* uni1EB0 (U+1EB0): X=350.0,Y=1276.0 (should be at ascender 1275?)

	* uni1EB9 (U+1EB9): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EBB (U+1EBB): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EBD (U+1EBD): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EBF (U+1EBF): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EC0 (U+1EC0): X=560.0,Y=1274.0 (should be at ascender 1275?)

	* uni1EC1 (U+1EC1): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EC3 (U+1EC3): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EC4 (U+1EC4): X=402.0,Y=1277.0 (should be at ascender 1275?)

	* uni1EC5 (U+1EC5): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1EC7 (U+1EC7): X=341.5,Y=-1.0 (should be at baseline 0?)

	* uni1ED2 (U+1ED2): X=637.0,Y=1274.0 (should be at ascender 1275?)

	* uni1ED6 (U+1ED6): X=479.0,Y=1277.0 (should be at ascender 1275?)

	* ygrave (U+1EF3): X=144.0,Y=0.5 (should be at baseline 0?)

	* uni1EF5 (U+1EF5): X=144.0,Y=0.5 (should be at baseline 0?)

	* uni1EF7 (U+1EF7): X=144.0,Y=0.5 (should be at baseline 0?)

	* uni1EF9 (U+1EF9): X=144.0,Y=0.5 (should be at baseline 0?)

	* quoteright (U+2019): X=159.0,Y=873.0 (should be at cap-height 875?)

	* quotedblright (U+201D): X=317.0,Y=873.0 (should be at cap-height 875?)

	* quotedblright (U+201D): X=159.0,Y=873.0 (should be at cap-height 875?)

	* minute (U+2032): X=144.0,Y=873.0 (should be at cap-height 875?)

	* second (U+2033): X=290.0,Y=873.0 (should be at cap-height 875?)

	* second (U+2033): X=144.0,Y=873.0 (should be at cap-height 875?)

	* guilsinglright (U+203A): X=88.0,Y=-1.0 (should be at baseline 0?)

	* integral (U+222B): X=111.0,Y=-2.0 (should be at baseline 0?)

	* integral (U+222B): X=437.5,Y=875.5 (should be at cap-height 875?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* eng (U+014B): L<<191.0,494.0>--<167.0,296.0>>/B<<167.0,296.0>-<199.0,380.0>-<240.5,429.0>> = 13.943230920553646

	* h (U+0068): L<<244.0,869.0>--<172.0,295.0>>/B<<172.0,295.0>-<205.0,380.0>-<246.5,429.0>> = 14.06838385566361

	* hbar (U+0127): L<<244.0,869.0>--<172.0,295.0>>/B<<172.0,295.0>-<205.0,380.0>-<246.5,429.0>> = 14.06838385566361

	* hcircumflex (U+0125): L<<244.0,869.0>--<172.0,295.0>>/B<<172.0,295.0>-<205.0,380.0>-<246.5,429.0>> = 14.06838385566361

	* n (U+006E): L<<191.0,494.0>--<167.0,296.0>>/B<<167.0,296.0>-<199.0,380.0>-<240.5,429.0>> = 13.943230920553646

	* nacute (U+0144): L<<191.0,494.0>--<167.0,296.0>>/B<<167.0,296.0>-<199.0,380.0>-<240.5,429.0>> = 13.943230920553646

	* ncaron (U+0148): L<<191.0,494.0>--<167.0,296.0>>/B<<167.0,296.0>-<199.0,380.0>-<240.5,429.0>> = 13.943230920553646

	* ntilde (U+00F1): L<<191.0,494.0>--<167.0,296.0>>/B<<167.0,296.0>-<199.0,380.0>-<240.5,429.0>> = 13.943230920553646

	* r (U+0072): L<<190.0,494.0>--<166.0,301.0>>/B<<166.0,301.0>-<197.0,386.0>-<232.5,433.5>> = 12.948734491046945

	* racute (U+0155): L<<190.0,494.0>--<166.0,301.0>>/B<<166.0,301.0>-<197.0,386.0>-<232.5,433.5>> = 12.948734491046945

	* rcaron (U+0159): L<<190.0,494.0>--<166.0,301.0>>/B<<166.0,301.0>-<197.0,386.0>-<232.5,433.5>> = 12.948734491046945

	* uni0146 (U+0146): L<<191.0,494.0>--<167.0,296.0>>/B<<167.0,296.0>-<199.0,380.0>-<240.5,429.0>> = 13.943230920553646

	* uni0157 (U+0157): L<<190.0,494.0>--<166.0,301.0>>/B<<166.0,301.0>-<197.0,386.0>-<232.5,433.5>> = 12.948734491046945

	* uni1EF5 (U+1EF5): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* uni1EF7 (U+1EF7): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* uni1EF9 (U+1EF9): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* y (U+0079): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* yacute (U+00FD): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* ycircumflex (U+0177): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* ydieresis (U+00FF): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003

	* ygrave (U+1EF3): L<<399.0,-160.0>--<445.0,209.0>>/B<<445.0,209.0>-<413.0,124.0>-<371.5,74.5>> = 13.523974930576003 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[10] PlaypenENGSemijoined-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>

>
>Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families
>
* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Playpen ENG Semijoined Regular | Playpen ENG Semijoined |
| Subfamily Name | Italic | Italic |
| Full Name | Playpen ENG Semijoined Italic | Playpen ENG Semijoined Italic |
| Poscript Name | PlaypenENGSemijoined-Italic | PlaypenENGSemijoined-Italic |
| Typographic Family Name | Playpen ENG Semijoined | N/A |
| Typographic Subfamily Name | Italic | N/A | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Does full font name begin with the font family name? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/name.html#com.google.fonts/check/name/match_familyname_fullfont">com.google.fonts/check/name/match_familyname_fullfont</a>)</summary><div>

>
>The FULL_FONT_NAME entry in the ‘name’ table should start with the same string as the Family Name (FONT_FAMILY_NAME, TYPOGRAPHIC_FAMILY_NAME or WWS_FAMILY_NAME).
>
>If the Family Name is not included as the first part of the Full Font Name, and the user embeds the font in a document using a Microsoft Office app, the app will fail to render the font when it opens the document again.
>
>NOTE: Up until version 1.5, the OpenType spec included the following exception in the definition of Full Font Name:
>
>"An exception to the [above] definition of Full font name is for Microsoft platform strings for CFF OpenType fonts: in this case, the Full font name string must be identical to the PostScript FontName in the CFF Name INDEX."
>
>https://docs.microsoft.com/en-us/typography/opentype/otspec150/name#name-ids
>
* 🔥 **FAIL** On the 'name' table, the full font name 'Playpen ENG Semijoined Italic' does not begin with the font family name 'Playpen ENG Semijoined Regular' in platformID 3, encodingID 1, languageID 1033(0409), and nameID 1. [code: mismatch-font-names]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined Regular' / SUBFAMILY_NAME = 'Italic'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><br></div></details><details><summary><b>[8] PlaypenENGSemijoined-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined Light' / SUBFAMILY_NAME = 'Regular'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><br></div></details><details><summary><b>[9] PlaypenENGSemijoined-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined Light' / SUBFAMILY_NAME = 'Italic'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* quotedbl (U+0022): X=124.0,Y=876.0 (should be at cap-height 875?)

	* quotedbl (U+0022): X=206.0,Y=876.0 (should be at cap-height 875?)

	* quotedbl (U+0022): X=275.0,Y=876.0 (should be at cap-height 875?)

	* quotedbl (U+0022): X=357.0,Y=876.0 (should be at cap-height 875?)

	* quotesingle (U+0027): X=124.0,Y=876.0 (should be at cap-height 875?)

	* quotesingle (U+0027): X=206.0,Y=876.0 (should be at cap-height 875?)

	* asterisk (U+002A): X=233.0,Y=876.0 (should be at cap-height 875?)

	* seven (U+0037): X=86.5,Y=2.0 (should be at baseline 0?)

	* A (U+0041): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* J (U+004A): X=174.0,Y=1.5 (should be at baseline 0?)

	* X (U+0058): X=647.0,Y=873.0 (should be at cap-height 875?)

	* c (U+0063): X=414.5,Y=499.5 (should be at x-height 500?)

	* f (U+0066): X=-66.0,Y=-375.5 (should be at descender -375?)

	* f (U+0066): X=435.0,Y=876.5 (should be at cap-height 875?)

	* h (U+0068): X=334.5,Y=499.5 (should be at x-height 500?)

	* k (U+006B): X=503.0,Y=499.0 (should be at x-height 500?)

	* x (U+0078): X=454.0,Y=-2.0 (should be at baseline 0?)

	* x (U+0078): X=16.5,Y=-0.5 (should be at baseline 0?)

	* x (U+0078): X=518.5,Y=501.5 (should be at x-height 500?)

	* section (U+00A7): X=484.5,Y=874.5 (should be at cap-height 875?)

	* ordfeminine (U+00AA): X=398.0,Y=874.0 (should be at cap-height 875?)

	* ordfeminine (U+00AA): X=462.0,Y=874.0 (should be at cap-height 875?)

	* guillemotleft (U+00AB): X=329.0,Y=-0.5 (should be at baseline 0?)

	* guillemotleft (U+00AB): X=579.0,Y=-0.5 (should be at baseline 0?)

	* registered (U+00AE): X=292.0,Y=874.0 (should be at cap-height 875?)

	* ordmasculine (U+00BA): X=387.0,Y=876.5 (should be at cap-height 875?)

	* guillemotright (U+00BB): X=80.0,Y=1.0 (should be at baseline 0?)

	* guillemotright (U+00BB): X=330.0,Y=1.0 (should be at baseline 0?)

	* Agrave (U+00C0): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Aacute (U+00C1): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Acircumflex (U+00C2): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Atilde (U+00C3): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Adieresis (U+00C4): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Aring (U+00C5): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* AE (U+00C6): X=56.0,Y=1.0 (should be at baseline 0?)

	* Oslash (U+00D8): X=833.0,Y=877.0 (should be at cap-height 875?)

	* ae (U+00E6): X=276.5,Y=1.0 (should be at baseline 0?)

	* Amacron (U+0100): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Abreve (U+0102): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* Aogonek (U+0104): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* IJ (U+0132): X=512.0,Y=1.5 (should be at baseline 0?)

	* Jcircumflex (U+0134): X=174.0,Y=1.5 (should be at baseline 0?)

	* jcircumflex (U+0135): X=-86.5,Y=-375.5 (should be at descender -375?)

	* uni01CD (U+01CD): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni01D8 (U+01D8): X=323.5,Y=873.0 (should be at cap-height 875?)

	* uni01D9 (U+01D9): X=364.0,Y=1276.5 (should be at ascender 1275?)

	* uni01DC (U+01DC): X=434.5,Y=874.5 (should be at cap-height 875?)

	* AEacute (U+01FC): X=56.0,Y=1.0 (should be at baseline 0?)

	* aeacute (U+01FD): X=276.5,Y=1.0 (should be at baseline 0?)

	* uni0237 (U+0237): X=-86.5,Y=-375.5 (should be at descender -375?)

	* uni0338 (U+0338): X=-218.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA0 (U+1EA0): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA2 (U+1EA2): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA4 (U+1EA4): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA4 (U+1EA4): X=735.0,Y=1275.5 (should be at ascender 1275?)

	* uni1EA6 (U+1EA6): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA6 (U+1EA6): X=574.0,Y=1273.0 (should be at ascender 1275?)

	* uni1EA8 (U+1EA8): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EA9 (U+1EA9): X=520.0,Y=874.0 (should be at cap-height 875?)

	* uni1EAA (U+1EAA): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EAC (U+1EAC): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EAE (U+1EAE): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EAF (U+1EAF): X=307.0,Y=874.0 (should be at cap-height 875?)

	* uni1EB0 (U+1EB0): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EB0 (U+1EB0): X=343.0,Y=1277.0 (should be at ascender 1275?)

	* uni1EB1 (U+1EB1): X=434.0,Y=874.0 (should be at cap-height 875?)

	* uni1EB2 (U+1EB2): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EB2 (U+1EB2): X=470.0,Y=1273.0 (should be at ascender 1275?)

	* uni1EB4 (U+1EB4): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EB6 (U+1EB6): X=-3.0,Y=-2.0 (should be at baseline 0?)

	* uni1EBE (U+1EBE): X=750.0,Y=1275.5 (should be at ascender 1275?)

	* uni1EC0 (U+1EC0): X=589.0,Y=1273.0 (should be at ascender 1275?)

	* uni1EC3 (U+1EC3): X=509.0,Y=874.0 (should be at cap-height 875?)

	* uni1ED0 (U+1ED0): X=828.0,Y=1275.5 (should be at ascender 1275?)

	* uni1ED2 (U+1ED2): X=667.0,Y=1273.0 (should be at ascender 1275?)

	* uni1ED5 (U+1ED5): X=506.0,Y=874.0 (should be at cap-height 875?)

	* quoteright (U+2019): X=241.0,Y=876.0 (should be at cap-height 875?)

	* quoteright (U+2019): X=156.0,Y=877.0 (should be at cap-height 875?)

	* quotedblright (U+201D): X=408.0,Y=876.0 (should be at cap-height 875?)

	* quotedblright (U+201D): X=323.0,Y=877.0 (should be at cap-height 875?)

	* quotedblright (U+201D): X=241.0,Y=876.0 (should be at cap-height 875?)

	* quotedblright (U+201D): X=156.0,Y=877.0 (should be at cap-height 875?)

	* minute (U+2032): X=142.0,Y=876.0 (should be at cap-height 875?)

	* second (U+2033): X=299.0,Y=876.0 (should be at cap-height 875?)

	* second (U+2033): X=142.0,Y=876.0 (should be at cap-height 875?)

	* guilsinglleft (U+2039): X=329.0,Y=-0.5 (should be at baseline 0?)

	* guilsinglright (U+203A): X=80.0,Y=1.0 (should be at baseline 0?)

	* integral (U+222B): X=434.5,Y=876.0 (should be at cap-height 875?) [code: found-misalignments]
</div></details><br></div></details><details><summary><b>[8] PlaypenENGSemijoined-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined' / SUBFAMILY_NAME = 'Regular'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><br></div></details><details><summary><b>[9] PlaypenENGSemijoined-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined Thin' / SUBFAMILY_NAME = 'Regular'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* eng (U+014B): L<<150.0,500.0>--<150.0,271.0>>/B<<150.0,271.0>-<173.0,366.0>-<211.0,420.5>> = 13.609731895812178

	* h (U+0068): L<<155.0,875.0>--<155.0,266.0>>/B<<155.0,266.0>-<177.0,364.0>-<215.5,419.0>> = 12.652556500557967

	* hbar (U+0127): L<<155.0,875.0>--<155.0,266.0>>/B<<155.0,266.0>-<177.0,364.0>-<215.5,419.0>> = 12.652556500557967

	* hcircumflex (U+0125): L<<155.0,875.0>--<155.0,266.0>>/B<<155.0,266.0>-<177.0,364.0>-<215.5,419.0>> = 12.652556500557967

	* m (U+006D): L<<149.0,500.0>--<149.0,272.0>>/B<<149.0,272.0>-<172.0,368.0>-<209.0,421.5>> = 13.47315811273114

	* m (U+006D): L<<486.0,351.0>--<486.0,269.0>>/B<<486.0,269.0>-<508.0,366.0>-<545.0,420.5>> = 12.778733188406045

	* n (U+006E): L<<150.0,500.0>--<150.0,271.0>>/B<<150.0,271.0>-<173.0,366.0>-<211.0,420.5>> = 13.609731895812178

	* nacute (U+0144): L<<150.0,500.0>--<150.0,271.0>>/B<<150.0,271.0>-<173.0,366.0>-<211.0,420.5>> = 13.609731895812178

	* ncaron (U+0148): L<<150.0,500.0>--<150.0,271.0>>/B<<150.0,271.0>-<173.0,366.0>-<211.0,420.5>> = 13.609731895812178

	* ntilde (U+00F1): L<<150.0,500.0>--<150.0,271.0>>/B<<150.0,271.0>-<173.0,366.0>-<211.0,420.5>> = 13.609731895812178

	* r (U+0072): L<<149.0,500.0>--<149.0,279.0>>/B<<149.0,279.0>-<168.0,375.0>-<198.0,427.0>> = 11.19511142629998

	* racute (U+0155): L<<149.0,500.0>--<149.0,279.0>>/B<<149.0,279.0>-<168.0,375.0>-<198.0,427.0>> = 11.19511142629998

	* rcaron (U+0159): L<<149.0,500.0>--<149.0,279.0>>/B<<149.0,279.0>-<168.0,375.0>-<198.0,427.0>> = 11.19511142629998

	* u (U+0075): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uacute (U+00FA): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* ubreve (U+016D): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* ucircumflex (U+00FB): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* udieresis (U+00FC): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* ugrave (U+00F9): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uhorn (U+01B0): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uhungarumlaut (U+0171): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* umacron (U+016B): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni0146 (U+0146): L<<150.0,500.0>--<150.0,271.0>>/B<<150.0,271.0>-<173.0,366.0>-<211.0,420.5>> = 13.609731895812178

	* uni0157 (U+0157): L<<149.0,500.0>--<149.0,279.0>>/B<<149.0,279.0>-<168.0,375.0>-<198.0,427.0>> = 11.19511142629998

	* uni01D4 (U+01D4): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni01D6 (U+01D6): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni01D8 (U+01D8): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni01DA (U+01DA): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni01DC (U+01DC): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EE5 (U+1EE5): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EE7 (U+1EE7): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EE9 (U+1EE9): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EEB (U+1EEB): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EED (U+1EED): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EEF (U+1EEF): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EF1 (U+1EF1): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uni1EF5 (U+1EF5): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* uni1EF7 (U+1EF7): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* uni1EF9 (U+1EF9): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* uogonek (U+0173): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* uring (U+016F): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* utilde (U+0169): L<<459.0,71.0>--<459.0,230.0>>/B<<459.0,230.0>-<436.0,134.0>-<398.0,80.0>> = 13.47315811273114

	* y (U+0079): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* yacute (U+00FD): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* ycircumflex (U+0177): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* ydieresis (U+00FF): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152

	* ygrave (U+1EF3): L<<460.0,-159.0>--<460.0,236.0>>/B<<460.0,236.0>-<438.0,137.0>-<399.5,82.0>> = 12.52880770915152 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[9] PlaypenENGSemijoined-ThinItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1347, but got 1313 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 400 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ENG Semijoined Thin' / SUBFAMILY_NAME = 'Italic'

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

	- IJacute

	- I_locl

	- M_locl.au

	- OE.cur.locl

	- Q.cur_locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- T.cur_locl

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

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

	- q.jmc_ar

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
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* at (U+0040): B<<544.0,172.5>-<546.0,194.0>-<549.0,216.0>>/B<<549.0,216.0>-<514.0,129.0>-<471.0,91.0>> = 14.149700308766363

	* b (U+0062): L<<235.0,876.0>--<162.0,299.0>>/B<<162.0,299.0>-<209.0,419.0>-<266.5,469.0>> = 14.178072216036286

	* eng (U+014B): L<<182.0,499.0>--<154.0,272.0>>/B<<154.0,272.0>-<188.0,367.0>-<232.0,421.0>> = 12.66021919942755

	* h (U+0068): L<<235.0,875.0>--<159.0,270.0>>/B<<159.0,270.0>-<193.0,366.0>-<237.0,420.5>> = 12.342467284448388

	* hbar (U+0127): L<<235.0,875.0>--<159.0,270.0>>/B<<159.0,270.0>-<193.0,366.0>-<237.0,420.5>> = 12.342467284448388

	* hcircumflex (U+0125): L<<235.0,875.0>--<159.0,270.0>>/B<<159.0,270.0>-<193.0,366.0>-<237.0,420.5>> = 12.342467284448388

	* m (U+006D): L<<182.0,499.0>--<153.0,275.0>>/B<<153.0,275.0>-<187.0,369.0>-<230.0,422.0>> = 12.508439106910126

	* m (U+006D): L<<500.0,347.0>--<491.0,275.0>>/B<<491.0,275.0>-<525.0,369.0>-<568.0,422.5>> = 12.760148764953595

	* n (U+006E): L<<182.0,499.0>--<154.0,272.0>>/B<<154.0,272.0>-<188.0,367.0>-<232.0,421.0>> = 12.66021919942755

	* nacute (U+0144): L<<182.0,499.0>--<154.0,272.0>>/B<<154.0,272.0>-<188.0,367.0>-<232.0,421.0>> = 12.66021919942755

	* ncaron (U+0148): L<<182.0,499.0>--<154.0,272.0>>/B<<154.0,272.0>-<188.0,367.0>-<232.0,421.0>> = 12.66021919942755

	* ntilde (U+00F1): L<<182.0,499.0>--<154.0,272.0>>/B<<154.0,272.0>-<188.0,367.0>-<232.0,421.0>> = 12.66021919942755

	* r (U+0072): L<<181.0,499.0>--<153.0,279.0>>/B<<153.0,279.0>-<185.0,377.0>-<221.5,429.0>> = 10.830250770323287

	* racute (U+0155): L<<181.0,499.0>--<153.0,279.0>>/B<<153.0,279.0>-<185.0,377.0>-<221.5,429.0>> = 10.830250770323287

	* rcaron (U+0159): L<<181.0,499.0>--<153.0,279.0>>/B<<153.0,279.0>-<185.0,377.0>-<221.5,429.0>> = 10.830250770323287

	* u (U+0075): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uacute (U+00FA): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* ubreve (U+016D): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* ucircumflex (U+00FB): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* udieresis (U+00FC): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* ugrave (U+00F9): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uhorn (U+01B0): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uhungarumlaut (U+0171): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* umacron (U+016B): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni0146 (U+0146): L<<182.0,499.0>--<154.0,272.0>>/B<<154.0,272.0>-<188.0,367.0>-<232.0,421.0>> = 12.66021919942755

	* uni0157 (U+0157): L<<181.0,499.0>--<153.0,279.0>>/B<<153.0,279.0>-<185.0,377.0>-<221.5,429.0>> = 10.830250770323287

	* uni01D4 (U+01D4): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni01D6 (U+01D6): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni01D8 (U+01D8): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni01DA (U+01DA): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni01DC (U+01DC): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EE5 (U+1EE5): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EE7 (U+1EE7): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EE9 (U+1EE9): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EEB (U+1EEB): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EED (U+1EED): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EEF (U+1EEF): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EF1 (U+1EF1): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uni1EF5 (U+1EF5): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* uni1EF7 (U+1EF7): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* uni1EF9 (U+1EF9): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* uogonek (U+0173): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* uring (U+016F): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* utilde (U+0169): L<<441.0,84.0>--<459.0,235.0>>/B<<459.0,235.0>-<425.0,138.0>-<380.5,83.0>> = 12.51847031921777

	* y (U+0079): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* yacute (U+00FD): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* ycircumflex (U+0177): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* ydieresis (U+00FF): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244

	* ygrave (U+1EF3): L<<406.0,-165.0>--<457.0,233.0>>/B<<457.0,233.0>-<423.0,136.0>-<379.0,82.0>> = 12.014224887856244 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 10 | 62 | 970 | 51 | 788 | 0 |
| 0% | 1% | 3% | 52% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
