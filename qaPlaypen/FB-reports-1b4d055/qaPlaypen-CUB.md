## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[10] PlaypenCUB-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2192 when it should be at most 2000 [code: bad-hhea-range]
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
 FONT_FAMILY_NAME = 'Playpen CUB ExtraLight' / SUBFAMILY_NAME = 'Regular'

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
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>

>
>This check looks for consecutive line segments which have the same angle. This normally happens if an outline point has been added by accident.
>
>This check is not run for variable fonts, as they may legitimately have colinear vectors.
>
* ⚠ **WARN** The following glyphs have colinear vectors:

	* ampersand (U+0026): L<<704.0,188.0>--<465.0,583.0>> -> L<<465.0,583.0>--<464.0,585.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>

>
>This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.
>
* ⚠ **WARN** The following glyphs have jaggy segments:

	* eng (U+014B): L<<241.0,491.0>--<190.0,336.0>>/B<<190.0,336.0>-<233.0,404.0>-<278.0,444.0>> = 14.09446118465354

	* h (U+0068): L<<447.0,1106.0>--<196.0,337.0>>/B<<196.0,337.0>-<239.0,405.0>-<283.5,444.5>> = 14.230759563624021

	* hbar (U+0127): L<<447.0,1106.0>--<196.0,337.0>>/B<<196.0,337.0>-<239.0,405.0>-<283.5,444.5>> = 14.230759563624021

	* hcircumflex (U+0125): L<<447.0,1106.0>--<196.0,337.0>>/B<<196.0,337.0>-<239.0,405.0>-<283.5,444.5>> = 14.230759563624021

	* n (U+006E): L<<241.0,491.0>--<190.0,336.0>>/B<<190.0,336.0>-<233.0,404.0>-<278.0,444.0>> = 14.09446118465354

	* nacute (U+0144): L<<241.0,491.0>--<190.0,336.0>>/B<<190.0,336.0>-<233.0,404.0>-<278.0,444.0>> = 14.09446118465354

	* ncaron (U+0148): L<<241.0,491.0>--<190.0,336.0>>/B<<190.0,336.0>-<233.0,404.0>-<278.0,444.0>> = 14.09446118465354

	* ntilde (U+00F1): L<<241.0,491.0>--<190.0,336.0>>/B<<190.0,336.0>-<233.0,404.0>-<278.0,444.0>> = 14.09446118465354

	* r (U+0072): L<<239.0,490.0>--<190.0,337.0>>/B<<190.0,337.0>-<232.0,408.0>-<273.0,447.5>> = 12.848148548866796

	* racute (U+0155): L<<239.0,490.0>--<190.0,337.0>>/B<<190.0,337.0>-<232.0,408.0>-<273.0,447.5>> = 12.848148548866796

	* rcaron (U+0159): L<<239.0,490.0>--<190.0,337.0>>/B<<190.0,337.0>-<232.0,408.0>-<273.0,447.5>> = 12.848148548866796

	* uni0146 (U+0146): L<<241.0,491.0>--<190.0,336.0>>/B<<190.0,336.0>-<233.0,404.0>-<278.0,444.0>> = 14.09446118465354

	* uni0157 (U+0157): L<<239.0,490.0>--<190.0,337.0>>/B<<190.0,337.0>-<232.0,408.0>-<273.0,447.5>> = 12.848148548866796

	* uni1EF5 (U+1EF5): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* uni1EF7 (U+1EF7): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* uni1EF9 (U+1EF9): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* y (U+0079): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* yacute (U+00FD): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* ycircumflex (U+0177): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* ydieresis (U+00FF): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182

	* ygrave (U+1EF3): L<<240.0,-402.0>--<424.0,166.0>>/B<<424.0,166.0>-<382.0,98.0>-<337.0,58.0>> = 13.75202667659182 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[8] PlaypenCUB-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2192 when it should be at most 2000 [code: bad-hhea-range]
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

	* d (U+0064): B<<387.0,121.0>-<389.0,129.0>-<392.0,137.0>>/B<<392.0,137.0>-<333.0,52.0>-<275.5,17.5>> = 14.209152016993317

	* dcaron (U+010F): B<<387.0,121.0>-<389.0,129.0>-<392.0,137.0>>/B<<392.0,137.0>-<333.0,52.0>-<275.5,17.5>> = 14.209152016993317

	* dcroat (U+0111): B<<387.0,121.0>-<389.0,129.0>-<392.0,137.0>>/B<<392.0,137.0>-<333.0,52.0>-<275.5,17.5>> = 14.209152016993317 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[7] PlaypenCUB-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2192 when it should be at most 2000 [code: bad-hhea-range]
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
</div></details><br></div></details><details><summary><b>[8] PlaypenCUB-Thin.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>

>
>This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be between 120% and 200% of UPM * Warning if sum is over 150% of UPM
>
>The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
>
>Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics
>
* 🔥 **FAIL** The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2192 when it should be at most 2000 [code: bad-hhea-range]
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

	* OE (U+0152): B<<1093.0,778.0>-<1093.0,764.0>-<1092.0,750.0>>/L<<1092.0,750.0>--<1204.0,1095.0>> = 13.89976671324127

	* at (U+0040): B<<536.5,162.0>-<540.0,174.0>-<545.0,189.0>>/B<<545.0,189.0>-<500.0,116.0>-<454.5,84.5>> = 13.216324063790571

	* eng (U+014B): L<<234.0,499.0>--<175.0,318.0>>/B<<175.0,318.0>-<222.0,396.0>-<270.0,440.0>> = 13.017406489351075

	* h (U+0068): L<<440.0,1114.0>--<180.0,319.0>>/B<<180.0,319.0>-<227.0,397.0>-<275.0,440.5>> = 12.961634560945768

	* hbar (U+0127): L<<440.0,1114.0>--<180.0,319.0>>/B<<180.0,319.0>-<227.0,397.0>-<275.0,440.5>> = 12.961634560945768

	* hcircumflex (U+0125): L<<440.0,1114.0>--<180.0,319.0>>/B<<180.0,319.0>-<227.0,397.0>-<275.0,440.5>> = 12.961634560945768

	* m (U+006D): L<<233.0,499.0>--<176.0,323.0>>/B<<176.0,323.0>-<221.0,399.0>-<268.0,442.0>> = 12.684745255027904

	* m (U+006D): L<<521.0,336.0>--<518.0,329.0>>/B<<518.0,329.0>-<563.0,403.0>-<609.0,444.5>> = 8.10553298194283

	* n (U+006E): L<<234.0,499.0>--<175.0,318.0>>/B<<175.0,318.0>-<222.0,396.0>-<270.0,440.0>> = 13.017406489351075

	* nacute (U+0144): L<<234.0,499.0>--<175.0,318.0>>/B<<175.0,318.0>-<222.0,396.0>-<270.0,440.0>> = 13.017406489351075

	* ncaron (U+0148): L<<234.0,499.0>--<175.0,318.0>>/B<<175.0,318.0>-<222.0,396.0>-<270.0,440.0>> = 13.017406489351075

	* ntilde (U+00F1): L<<234.0,499.0>--<175.0,318.0>>/B<<175.0,318.0>-<222.0,396.0>-<270.0,440.0>> = 13.017406489351075

	* ordfeminine (U+00AA): B<<529.0,836.0>-<533.0,849.0>-<538.0,864.0>>/B<<538.0,864.0>-<492.0,791.0>-<446.5,758.5>> = 13.781597235653596

	* r (U+0072): L<<232.0,497.0>--<174.0,321.0>>/B<<174.0,321.0>-<220.0,403.0>-<263.0,446.0>> = 11.051961324333073

	* racute (U+0155): L<<232.0,497.0>--<174.0,321.0>>/B<<174.0,321.0>-<220.0,403.0>-<263.0,446.0>> = 11.051961324333073

	* rcaron (U+0159): L<<232.0,497.0>--<174.0,321.0>>/B<<174.0,321.0>-<220.0,403.0>-<263.0,446.0>> = 11.051961324333073

	* u (U+0075): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uacute (U+00FA): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* ubreve (U+016D): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* ucircumflex (U+00FB): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* udieresis (U+00FC): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* ugrave (U+00F9): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uhorn (U+01B0): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uhungarumlaut (U+0171): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* umacron (U+016B): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni0146 (U+0146): L<<234.0,499.0>--<175.0,318.0>>/B<<175.0,318.0>-<222.0,396.0>-<270.0,440.0>> = 13.017406489351075

	* uni0157 (U+0157): L<<232.0,497.0>--<174.0,321.0>>/B<<174.0,321.0>-<220.0,403.0>-<263.0,446.0>> = 11.051961324333073

	* uni01D4 (U+01D4): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni01D6 (U+01D6): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni01D8 (U+01D8): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni01DA (U+01DA): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni01DC (U+01DC): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EE5 (U+1EE5): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EE7 (U+1EE7): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EE9 (U+1EE9): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EEB (U+1EEB): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EED (U+1EED): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EEF (U+1EEF): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EF1 (U+1EF1): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uni1EF5 (U+1EF5): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* uni1EF7 (U+1EF7): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* uni1EF9 (U+1EF9): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* uogonek (U+0173): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* uring (U+016F): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* utilde (U+0169): L<<414.0,112.0>--<437.0,184.0>>/B<<437.0,184.0>-<391.0,105.0>-<343.0,61.5>> = 12.495529679457876

	* y (U+0079): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* yacute (U+00FD): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* ycircumflex (U+0177): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* ydieresis (U+00FF): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757

	* ygrave (U+1EF3): L<<246.0,-409.0>--<439.0,184.0>>/B<<439.0,184.0>-<392.0,106.0>-<343.5,62.5>> = 13.043467573248757 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 25 | 490 | 25 | 401 | 0 |
| 0% | 1% | 3% | 52% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
