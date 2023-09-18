## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[9] PlaypenARG-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2079 when it should be at most 2000 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1541, but got 1534 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 588 instead [code: descent]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen ARG ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/fonttools/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
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

	- M_locl

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

	- cnct.cnt_r_r.ful

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

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
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* quotedbl (U+0022): X=50.0,Y=1063.0 (should be at cap-height 1065?)

	* quotedbl (U+0022): X=122.0,Y=1063.0 (should be at cap-height 1065?)

	* quotedbl (U+0022): X=194.0,Y=1063.0 (should be at cap-height 1065?)

	* quotedbl (U+0022): X=266.0,Y=1063.0 (should be at cap-height 1065?)

	* quotesingle (U+0027): X=50.0,Y=1063.0 (should be at cap-height 1065?)

	* quotesingle (U+0027): X=122.0,Y=1063.0 (should be at cap-height 1065?)

	* asterisk (U+002A): X=158.0,Y=1066.0 (should be at cap-height 1065?)

	* asterisk (U+002A): X=199.0,Y=1066.0 (should be at cap-height 1065?)

	* one (U+0031): X=250.0,Y=1067.0 (should be at cap-height 1065?)

	* two (U+0032): X=264.5,Y=1063.0 (should be at cap-height 1065?)

	* seven (U+0037): X=155.0,Y=0.5 (should be at baseline 0?)

	* M (U+004D): X=229.0,Y=1063.0 (should be at cap-height 1065?)

	* M (U+004D): X=996.0,Y=1063.0 (should be at cap-height 1065?)

	* N (U+004E): X=811.0,Y=2.0 (should be at baseline 0?)

	* S (U+0053): X=526.0,Y=1063.0 (should be at cap-height 1065?)

	* W (U+0057): X=85.0,Y=1063.0 (should be at cap-height 1065?)

	* W (U+0057): X=1302.0,Y=1064.0 (should be at cap-height 1065?)

	* W (U+0057): X=1351.0,Y=1067.0 (should be at cap-height 1065?)

	* Y (U+0059): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* Y (U+0059): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* c (U+0063): X=387.5,Y=498.5 (should be at x-height 500?)

	* f (U+0066): X=354.0,Y=1067.0 (should be at cap-height 1065?)

	* s (U+0073): X=353.5,Y=499.0 (should be at x-height 500?)

	* t (U+0074): X=308.5,Y=1.0 (should be at baseline 0?)

	* x (U+0078): X=106.0,Y=499.0 (should be at x-height 500?)

	* yen (U+00A5): X=89.0,Y=1066.0 (should be at cap-height 1065?)

	* yen (U+00A5): X=694.0,Y=1064.0 (should be at cap-height 1065?)

	* registered (U+00AE): X=241.0,Y=1067.0 (should be at cap-height 1065?)

	* ordmasculine (U+00BA): X=137.5,Y=1063.5 (should be at cap-height 1065?)

	* ordmasculine (U+00BA): X=318.0,Y=1063.5 (should be at cap-height 1065?)

	* questiondown (U+00BF): X=171.0,Y=-2.0 (should be at baseline 0?)

	* AE (U+00C6): X=79.0,Y=1.0 (should be at baseline 0?)

	* Ntilde (U+00D1): X=811.0,Y=2.0 (should be at baseline 0?)

	* Yacute (U+00DD): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* Yacute (U+00DD): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* Aogonek (U+0104): X=842.0,Y=2.0 (should be at baseline 0?)

	* dcaron (U+010F): X=677.0,Y=1064.0 (should be at cap-height 1065?)

	* dcaron (U+010F): X=506.0,Y=1063.0 (should be at cap-height 1065?)

	* Iogonek (U+012E): X=225.0,Y=-1.0 (should be at baseline 0?)

	* Nacute (U+0143): X=811.0,Y=2.0 (should be at baseline 0?)

	* uni0145 (U+0145): X=811.0,Y=2.0 (should be at baseline 0?)

	* Ncaron (U+0147): X=811.0,Y=2.0 (should be at baseline 0?)

	* Eng (U+014A): X=813.0,Y=-2.0 (should be at baseline 0?)

	* Sacute (U+015A): X=526.0,Y=1063.0 (should be at cap-height 1065?)

	* Scircumflex (U+015C): X=526.0,Y=1063.0 (should be at cap-height 1065?)

	* Scedilla (U+015E): X=526.0,Y=1063.0 (should be at cap-height 1065?)

	* Scaron (U+0160): X=526.0,Y=1063.0 (should be at cap-height 1065?)

	* uni0163 (U+0163): X=308.5,Y=1.0 (should be at baseline 0?)

	* tcaron (U+0165): X=308.5,Y=1.0 (should be at baseline 0?)

	* tbar (U+0167): X=308.5,Y=1.0 (should be at baseline 0?)

	* Wcircumflex (U+0174): X=85.0,Y=1063.0 (should be at cap-height 1065?)

	* Wcircumflex (U+0174): X=1302.0,Y=1064.0 (should be at cap-height 1065?)

	* Wcircumflex (U+0174): X=1351.0,Y=1067.0 (should be at cap-height 1065?)

	* Ycircumflex (U+0176): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* Ycircumflex (U+0176): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* Ydieresis (U+0178): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* Ydieresis (U+0178): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* AEacute (U+01FC): X=79.0,Y=1.0 (should be at baseline 0?)

	* uni0218 (U+0218): X=526.0,Y=1063.0 (should be at cap-height 1065?)

	* uni021B (U+021B): X=308.5,Y=1.0 (should be at baseline 0?)

	* Wgrave (U+1E80): X=85.0,Y=1063.0 (should be at cap-height 1065?)

	* Wgrave (U+1E80): X=1302.0,Y=1064.0 (should be at cap-height 1065?)

	* Wgrave (U+1E80): X=1351.0,Y=1067.0 (should be at cap-height 1065?)

	* Wacute (U+1E82): X=85.0,Y=1063.0 (should be at cap-height 1065?)

	* Wacute (U+1E82): X=1302.0,Y=1064.0 (should be at cap-height 1065?)

	* Wacute (U+1E82): X=1351.0,Y=1067.0 (should be at cap-height 1065?)

	* Wdieresis (U+1E84): X=85.0,Y=1063.0 (should be at cap-height 1065?)

	* Wdieresis (U+1E84): X=1302.0,Y=1064.0 (should be at cap-height 1065?)

	* Wdieresis (U+1E84): X=1351.0,Y=1067.0 (should be at cap-height 1065?)

	* uni1EB0 (U+1EB0): X=338.0,Y=1507.0 (should be at ascender 1508?)

	* Ygrave (U+1EF2): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* Ygrave (U+1EF2): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* uni1EF4 (U+1EF4): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* uni1EF4 (U+1EF4): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* uni1EF6 (U+1EF6): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* uni1EF6 (U+1EF6): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* uni1EF8 (U+1EF8): X=62.0,Y=1066.0 (should be at cap-height 1065?)

	* uni1EF8 (U+1EF8): X=667.0,Y=1064.0 (should be at cap-height 1065?)

	* quoteleft (U+2018): X=167.0,Y=1063.0 (should be at cap-height 1065?)

	* quoteright (U+2019): X=84.0,Y=1064.0 (should be at cap-height 1065?)

	* quotedblleft (U+201C): X=167.0,Y=1063.0 (should be at cap-height 1065?)

	* quotedblleft (U+201C): X=332.0,Y=1063.0 (should be at cap-height 1065?)

	* quotedblright (U+201D): X=249.0,Y=1064.0 (should be at cap-height 1065?)

	* quotedblright (U+201D): X=84.0,Y=1064.0 (should be at cap-height 1065?)

	* minute (U+2032): X=79.0,Y=1063.0 (should be at cap-height 1065?)

	* second (U+2033): X=225.0,Y=1063.0 (should be at cap-height 1065?)

	* second (U+2033): X=79.0,Y=1063.0 (should be at cap-height 1065?)

	* integral (U+222B): X=200.0,Y=-1.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><br></div></details><details><summary><b>[8] PlaypenARG-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2079 when it should be at most 2000 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1541, but got 1534 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 588 instead [code: descent]
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

	- M_locl

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

	- cnct.cnt_r_r.ful

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

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
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* quotedbl (U+0022): X=47.0,Y=1066.0 (should be at cap-height 1065?)

	* quotedbl (U+0022): X=128.0,Y=1066.0 (should be at cap-height 1065?)

	* quotedbl (U+0022): X=200.0,Y=1066.0 (should be at cap-height 1065?)

	* quotedbl (U+0022): X=281.0,Y=1066.0 (should be at cap-height 1065?)

	* quotesingle (U+0027): X=47.0,Y=1066.0 (should be at cap-height 1065?)

	* quotesingle (U+0027): X=128.0,Y=1066.0 (should be at cap-height 1065?)

	* one (U+0031): X=240.0,Y=1063.0 (should be at cap-height 1065?)

	* K (U+004B): X=756.0,Y=1067.0 (should be at cap-height 1065?)

	* V (U+0056): X=94.0,Y=1066.0 (should be at cap-height 1065?)

	* V (U+0056): X=752.0,Y=1066.0 (should be at cap-height 1065?)

	* V (U+0056): X=816.5,Y=1063.5 (should be at cap-height 1065?)

	* X (U+0058): X=692.0,Y=-2.0 (should be at baseline 0?)

	* X (U+0058): X=108.0,Y=-2.0 (should be at baseline 0?)

	* X (U+0058): X=126.0,Y=1067.0 (should be at cap-height 1065?)

	* X (U+0058): X=687.0,Y=1067.0 (should be at cap-height 1065?)

	* Y (U+0059): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* b (U+0062): X=254.5,Y=500.5 (should be at x-height 500?)

	* c (U+0063): X=388.5,Y=499.5 (should be at x-height 500?)

	* f (U+0066): X=361.0,Y=1066.5 (should be at cap-height 1065?)

	* k (U+006B): X=471.0,Y=501.0 (should be at x-height 500?)

	* m (U+006D): X=249.0,Y=498.0 (should be at x-height 500?)

	* p (U+0070): X=254.5,Y=500.5 (should be at x-height 500?)

	* q (U+0071): X=346.0,Y=1.5 (should be at baseline 0?)

	* t (U+0074): X=310.0,Y=-0.5 (should be at baseline 0?)

	* x (U+0078): X=487.5,Y=0.5 (should be at baseline 0?)

	* x (U+0078): X=46.0,Y=-1.0 (should be at baseline 0?)

	* x (U+0078): X=47.0,Y=501.5 (should be at x-height 500?)

	* yen (U+00A5): X=683.0,Y=1064.0 (should be at cap-height 1065?)

	* ordfeminine (U+00AA): X=322.0,Y=1067.0 (should be at cap-height 1065?)

	* ordfeminine (U+00AA): X=386.0,Y=1067.0 (should be at cap-height 1065?)

	* registered (U+00AE): X=238.0,Y=1064.0 (should be at cap-height 1065?)

	* ordmasculine (U+00BA): X=135.5,Y=1063.0 (should be at cap-height 1065?)

	* ordmasculine (U+00BA): X=319.0,Y=1063.0 (should be at cap-height 1065?)

	* questiondown (U+00BF): X=169.0,Y=-0.5 (should be at baseline 0?)

	* AE (U+00C6): X=88.0,Y=1.0 (should be at baseline 0?)

	* Yacute (U+00DD): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* uni0136 (U+0136): X=756.0,Y=1067.0 (should be at cap-height 1065?)

	* uni0163 (U+0163): X=310.0,Y=-0.5 (should be at baseline 0?)

	* tcaron (U+0165): X=310.0,Y=-0.5 (should be at baseline 0?)

	* tbar (U+0167): X=310.0,Y=-0.5 (should be at baseline 0?)

	* Ycircumflex (U+0176): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* Ydieresis (U+0178): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* Uhorn (U+01AF): X=982.0,Y=1066.5 (should be at cap-height 1065?)

	* uni01DA (U+01DA): X=476.0,Y=1067.0 (should be at cap-height 1065?)

	* uni01DA (U+01DA): X=130.0,Y=1067.0 (should be at cap-height 1065?)

	* AEacute (U+01FC): X=88.0,Y=1.0 (should be at baseline 0?)

	* uni021B (U+021B): X=310.0,Y=-0.5 (should be at baseline 0?)

	* uni1EAE (U+1EAE): X=515.0,Y=1509.0 (should be at ascender 1508?)

	* uni1EB0 (U+1EB0): X=362.0,Y=1509.0 (should be at ascender 1508?)

	* uni1EB1 (U+1EB1): X=232.0,Y=1067.0 (should be at cap-height 1065?)

	* uni1EB4 (U+1EB4): X=349.0,Y=1510.0 (should be at ascender 1508?)

	* uni1EE8 (U+1EE8): X=982.0,Y=1066.5 (should be at cap-height 1065?)

	* uni1EEA (U+1EEA): X=982.0,Y=1066.5 (should be at cap-height 1065?)

	* uni1EEC (U+1EEC): X=982.0,Y=1066.5 (should be at cap-height 1065?)

	* uni1EEE (U+1EEE): X=982.0,Y=1066.5 (should be at cap-height 1065?)

	* uni1EF0 (U+1EF0): X=982.0,Y=1066.5 (should be at cap-height 1065?)

	* Ygrave (U+1EF2): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* uni1EF4 (U+1EF4): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* uni1EF6 (U+1EF6): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* uni1EF8 (U+1EF8): X=655.0,Y=1064.0 (should be at cap-height 1065?)

	* quoteleft (U+2018): X=174.5,Y=1066.0 (should be at cap-height 1065?)

	* quotedblleft (U+201C): X=174.5,Y=1066.0 (should be at cap-height 1065?)

	* quotedblleft (U+201C): X=346.5,Y=1066.0 (should be at cap-height 1065?)

	* minute (U+2032): X=75.0,Y=1066.0 (should be at cap-height 1065?)

	* second (U+2033): X=232.0,Y=1066.0 (should be at cap-height 1065?)

	* second (U+2033): X=75.0,Y=1066.0 (should be at cap-height 1065?)

	* integral (U+222B): X=208.0,Y=-1.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><br></div></details><details><summary><b>[8] PlaypenARG-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2079 when it should be at most 2000 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1541, but got 1534 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 588 instead [code: descent]
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

	- M_locl

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

	- cnct.cnt_r_r.ful

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

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

	* ordfeminine (U+00AA): B<<339.0,692.0>-<321.0,708.0>-<315.0,735.0>>/B<<315.0,735.0>-<315.0,734.0>-<314.5,737.0>> = 12.528807709151492 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[7] PlaypenARG-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2079 when it should be at most 2000 [code: bad-hhea-range]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1541, but got 1534 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 588 instead [code: descent]
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

	- M_locl

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

	- cnct.cnt_r_r.ful

	- cnct.cnt_r_v.mod

	- cnct.cnt_r_x.mod

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

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
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 24 | 486 | 25 | 406 | 0 |
| 0% | 1% | 3% | 51% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
