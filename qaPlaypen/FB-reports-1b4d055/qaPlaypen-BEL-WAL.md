## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[8] PlaypenBELWAL-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2846 when it should be at most 2000 [code: bad-hhea-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen BEL WAL ExtraLight' / SUBFAMILY_NAME = 'Regular'

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

	- AE.cur.locl

	- F.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl

	- M_locl.au

	- OE.cur.locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- U_locl.au

	- Y_locl

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
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>

>
>This check heuristically looks for on-curve points which are close to, but do not sit on, significant boundary coordinates. For example, a point which has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as the baseline, here we also check for points near the x-height (but only for lowercase Latin letters), cap-height, ascender and descender Y coordinates.
>
>Not all such misaligned curve points are a mistake, and sometimes the design may call for points in locations near the boundaries. As this check is liable to generate significant numbers of false positives, it will pass if there are more than 100 reported misalignments.
>
* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* quotedbl (U+0022): X=50.0,Y=1403.0 (should be at cap-height 1405?)

	* quotedbl (U+0022): X=122.0,Y=1403.0 (should be at cap-height 1405?)

	* quotedbl (U+0022): X=196.0,Y=1403.0 (should be at cap-height 1405?)

	* quotedbl (U+0022): X=268.0,Y=1403.0 (should be at cap-height 1405?)

	* percent (U+0025): X=195.0,Y=0.5 (should be at baseline 0?)

	* quotesingle (U+0027): X=50.0,Y=1403.0 (should be at cap-height 1405?)

	* quotesingle (U+0027): X=122.0,Y=1403.0 (should be at cap-height 1405?)

	* four (U+0034): X=530.0,Y=1406.0 (should be at cap-height 1405?)

	* M (U+004D): X=278.0,Y=1403.0 (should be at cap-height 1405?)

	* M (U+004D): X=1259.0,Y=1403.0 (should be at cap-height 1405?)

	* Q (U+0051): X=823.0,Y=1.0 (should be at baseline 0?)

	* V (U+0056): X=99.0,Y=1406.0 (should be at cap-height 1405?)

	* V (U+0056): X=964.0,Y=1406.0 (should be at cap-height 1405?)

	* W (U+0057): X=48.5,Y=1407.0 (should be at cap-height 1405?)

	* W (U+0057): X=98.0,Y=1403.0 (should be at cap-height 1405?)

	* W (U+0057): X=1622.0,Y=1404.0 (should be at cap-height 1405?)

	* W (U+0057): X=1670.0,Y=1407.0 (should be at cap-height 1405?)

	* Y (U+0059): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* c (U+0063): X=387.5,Y=498.5 (should be at x-height 500?)

	* f (U+0066): X=75.0,Y=-924.0 (should be at descender -922?)

	* f (U+0066): X=354.0,Y=1407.0 (should be at cap-height 1405?)

	* f (U+0066): X=75.0,Y=-924.0 (should be at descender -922?)

	* g (U+0067): X=281.0,Y=-924.0 (should be at descender -922?)

	* j (U+006A): X=42.0,Y=-923.0 (should be at descender -922?)

	* j (U+006A): X=42.0,Y=-923.0 (should be at descender -922?)

	* p (U+0070): X=138.0,Y=-920.0 (should be at descender -922?)

	* p (U+0070): X=138.0,Y=-920.0 (should be at descender -922?)

	* q (U+0071): X=460.0,Y=-920.0 (should be at descender -922?)

	* s (U+0073): X=353.5,Y=499.0 (should be at x-height 500?)

	* t (U+0074): X=308.5,Y=1.0 (should be at baseline 0?)

	* x (U+0078): X=106.0,Y=499.0 (should be at x-height 500?)

	* y (U+0079): X=297.0,Y=-924.0 (should be at descender -922?)

	* yen (U+00A5): X=905.0,Y=1403.0 (should be at cap-height 1405?)

	* registered (U+00AE): X=241.0,Y=1407.0 (should be at cap-height 1405?)

	* ordmasculine (U+00BA): X=137.5,Y=1403.5 (should be at cap-height 1405?)

	* ordmasculine (U+00BA): X=318.0,Y=1403.5 (should be at cap-height 1405?)

	* Yacute (U+00DD): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* germandbls (U+00DF): X=159.0,Y=-920.0 (should be at descender -922?)

	* yacute (U+00FD): X=297.0,Y=-924.0 (should be at descender -922?)

	* thorn (U+00FE): X=138.0,Y=-920.0 (should be at descender -922?)

	* thorn (U+00FE): X=138.0,Y=-920.0 (should be at descender -922?)

	* ydieresis (U+00FF): X=297.0,Y=-924.0 (should be at descender -922?)

	* Aogonek (U+0104): X=1054.0,Y=1.0 (should be at baseline 0?)

	* dcaron (U+010F): X=511.0,Y=1407.0 (should be at cap-height 1405?)

	* gcircumflex (U+011D): X=281.0,Y=-924.0 (should be at descender -922?)

	* gbreve (U+011F): X=281.0,Y=-924.0 (should be at descender -922?)

	* gdotaccent (U+0121): X=281.0,Y=-924.0 (should be at descender -922?)

	* uni0123 (U+0123): X=281.0,Y=-924.0 (should be at descender -922?)

	* Iogonek (U+012E): X=279.0,Y=-2.0 (should be at baseline 0?)

	* ij (U+0133): X=343.0,Y=-923.0 (should be at descender -922?)

	* ij (U+0133): X=343.0,Y=-923.0 (should be at descender -922?)

	* jcircumflex (U+0135): X=42.0,Y=-923.0 (should be at descender -922?)

	* jcircumflex (U+0135): X=42.0,Y=-923.0 (should be at descender -922?)

	* Eng (U+014A): X=1029.0,Y=-2.0 (should be at baseline 0?)

	* uni0163 (U+0163): X=308.5,Y=1.0 (should be at baseline 0?)

	* tcaron (U+0165): X=308.5,Y=1.0 (should be at baseline 0?)

	* tbar (U+0167): X=308.5,Y=1.0 (should be at baseline 0?)

	* Wcircumflex (U+0174): X=48.5,Y=1407.0 (should be at cap-height 1405?)

	* Wcircumflex (U+0174): X=98.0,Y=1403.0 (should be at cap-height 1405?)

	* Wcircumflex (U+0174): X=1622.0,Y=1404.0 (should be at cap-height 1405?)

	* Wcircumflex (U+0174): X=1670.0,Y=1407.0 (should be at cap-height 1405?)

	* Ycircumflex (U+0176): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* ycircumflex (U+0177): X=297.0,Y=-924.0 (should be at descender -922?)

	* Ydieresis (U+0178): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* uni021B (U+021B): X=308.5,Y=1.0 (should be at baseline 0?)

	* uni0237 (U+0237): X=42.0,Y=-923.0 (should be at descender -922?)

	* uni0237 (U+0237): X=42.0,Y=-923.0 (should be at descender -922?)

	* Wgrave (U+1E80): X=48.5,Y=1407.0 (should be at cap-height 1405?)

	* Wgrave (U+1E80): X=98.0,Y=1403.0 (should be at cap-height 1405?)

	* Wgrave (U+1E80): X=1622.0,Y=1404.0 (should be at cap-height 1405?)

	* Wgrave (U+1E80): X=1670.0,Y=1407.0 (should be at cap-height 1405?)

	* Wacute (U+1E82): X=48.5,Y=1407.0 (should be at cap-height 1405?)

	* Wacute (U+1E82): X=98.0,Y=1403.0 (should be at cap-height 1405?)

	* Wacute (U+1E82): X=1622.0,Y=1404.0 (should be at cap-height 1405?)

	* Wacute (U+1E82): X=1670.0,Y=1407.0 (should be at cap-height 1405?)

	* Wdieresis (U+1E84): X=48.5,Y=1407.0 (should be at cap-height 1405?)

	* Wdieresis (U+1E84): X=98.0,Y=1403.0 (should be at cap-height 1405?)

	* Wdieresis (U+1E84): X=1622.0,Y=1404.0 (should be at cap-height 1405?)

	* Wdieresis (U+1E84): X=1670.0,Y=1407.0 (should be at cap-height 1405?)

	* Ygrave (U+1EF2): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* ygrave (U+1EF3): X=297.0,Y=-924.0 (should be at descender -922?)

	* uni1EF4 (U+1EF4): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* uni1EF5 (U+1EF5): X=297.0,Y=-924.0 (should be at descender -922?)

	* uni1EF6 (U+1EF6): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* uni1EF7 (U+1EF7): X=297.0,Y=-924.0 (should be at descender -922?)

	* uni1EF8 (U+1EF8): X=879.0,Y=1403.0 (should be at cap-height 1405?)

	* uni1EF9 (U+1EF9): X=297.0,Y=-924.0 (should be at descender -922?)

	* quoteleft (U+2018): X=166.0,Y=1403.0 (should be at cap-height 1405?)

	* quoteright (U+2019): X=86.0,Y=1404.0 (should be at cap-height 1405?)

	* quotedblleft (U+201C): X=166.0,Y=1403.0 (should be at cap-height 1405?)

	* quotedblleft (U+201C): X=342.0,Y=1403.0 (should be at cap-height 1405?)

	* quotedblright (U+201D): X=263.0,Y=1404.0 (should be at cap-height 1405?)

	* quotedblright (U+201D): X=86.0,Y=1404.0 (should be at cap-height 1405?)

	* minute (U+2032): X=79.0,Y=1403.0 (should be at cap-height 1405?)

	* second (U+2033): X=225.0,Y=1403.0 (should be at cap-height 1405?)

	* second (U+2033): X=79.0,Y=1403.0 (should be at cap-height 1405?)

	* integral (U+222B): X=203.5,Y=1.5 (should be at baseline 0?) [code: found-misalignments]
</div></details><br></div></details><details><summary><b>[7] PlaypenBELWAL-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2846 when it should be at most 2000 [code: bad-hhea-range]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen BEL WAL Light' / SUBFAMILY_NAME = 'Regular'

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

	- AE.cur.locl

	- F.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl

	- M_locl.au

	- OE.cur.locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- U_locl.au

	- Y_locl

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
</div></details><br></div></details><details><summary><b>[7] PlaypenBELWAL-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2846 when it should be at most 2000 [code: bad-hhea-range]
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

	- AE.cur.locl

	- F.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl

	- M_locl.au

	- OE.cur.locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- U_locl.au

	- Y_locl

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

	* ordfeminine (U+00AA): B<<339.0,1032.0>-<321.0,1048.0>-<315.0,1075.0>>/B<<315.0,1075.0>-<315.0,1074.0>-<314.5,1077.0>> = 12.528807709151492 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[6] PlaypenBELWAL-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2846 when it should be at most 2000 [code: bad-hhea-range]
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

	- AE.cur.locl

	- F.cur_locl

	- G_locl

	- G_locl.au

	- IJacute

	- I_locl

	- M_locl

	- M_locl.au

	- OE.cur.locl

	- Q.dec_pt

	- Q_locl

	- Q_locl.ini

	- U_locl.au

	- Y_locl

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
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 4 | 24 | 486 | 25 | 410 | 0 |
| 0% | 0% | 3% | 51% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
