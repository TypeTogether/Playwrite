## FontBakery report

fontbakery version: 0.9.0

<details><summary><b>[17] PlaypenPER[wght].ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Checking file is named canonically. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/canonical_filename">com.google.fonts/check/canonical_filename</a>)</summary><div>

>
>A font's filename must be composed as "<familyname>-<stylename>.ttf":
>
>- Nunito-Regular.ttf
>
>- Oswald-BoldItalic.ttf
>
>Variable fonts must list the axis tags in alphabetical order in square brackets and separated by commas:
>
>- Roboto[wdth,wght].ttf
>
>- Familyname-Italic[wght].ttf
>
* 🔥 **FAIL** Expected "Playpen[wght].ttf. Got PlaypenPER[wght].ttf. [code: bad-filename]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>

>
>Google Fonts has several rules which need to be adhered to when setting a font's name table. Please read: https://googlefonts.github.io/gf-guide/statics.html#supported-styles https://googlefonts.github.io/gf-guide/statics.html#style-linking https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles https://googlefonts.github.io/gf-guide/statics.html#single-weight-families
>
* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Playpen Rg 00 Short Slow | Playpen |
| Subfamily Name | Regular | Regular |
| Full Name | Playpen Rg 00 Short Slow | Playpen Regular |
| Poscript Name | Playpen-Rg00ShortSlow | Playpen-Regular |
| Typographic Family Name | Playpen | N/A |
| Typographic Subfamily Name | Rg 00 Short Slow | N/A | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Check glyphs do not have components which are themselves components. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyf_nested_components">com.google.fonts/check/glyf_nested_components</a>)</summary><div>

>
>There have been bugs rendering variable fonts with nested components. Additionally, some static fonts with nested components have been reported to have rendering and printing issues.
>
>For more info, see: * https://github.com/fonttools/fontbakery/issues/2961 * https://github.com/arrowtype/recursive/issues/412
>
* 🔥 **FAIL** The following glyphs have components which themselves are component glyphs:
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

This can be accomplished by using the 'gftools fix-hinting' command:

```
# create virtualenv
python3 -m venv venv
# activate virtualenv
source venv/bin/activate
# install gftools
pip install git+https://www.github.com/googlefonts/tools
```
 [code: bad-flags]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>

>
>A font's winAscent and winDescent values should be greater than or equal to the head table's yMax, abs(yMin) values. If they are less than these values, clipping can occur on Windows platforms (https://github.com/RedHatBrand/Overpass/issues/33).
>
>If the font includes tall/deep writing systems such as Arabic or Devanagari, the winAscent and winDescent can be greater than the yMax and absolute yMin values to accommodate vowel marks.
>
>When the 'win' Metrics are significantly greater than the UPM, the linespacing can appear too loose. To counteract this, enabling the OS/2 fsSelection bit 7 (Use_Typo_Metrics), will force Windows to use the OS/2 'typo' values instead. This means the font developer can control the linespacing with the 'typo' values, whilst avoiding clipping by setting the 'win' values to values greater than the yMax and absolute yMin.
>
* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1475, but got 1458 instead [code: ascent]
* 🔥 **FAIL** OS/2.usWinDescent value should be equal or greater than 626, but got 524 instead [code: descent]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 Metrics match hhea Metrics. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/os2_metrics_match_hhea">com.google.fonts/check/os2_metrics_match_hhea</a>)</summary><div>

>
>OS/2 and hhea vertical metric values should match. This will produce the same linespacing on Mac, GNU+Linux and Windows.
>
>- Mac OS X uses the hhea values. - Windows uses OS/2 or Win, depending on the OS or fsSelection bit value.
>
>When OS/2 and hhea vertical metrics match, the same linespacing results on macOS, GNU+Linux and Windows. Note that fixing this issue in a previously released font may cause reflow in user documents and unhappy users.
>
* 🔥 **FAIL** OS/2 sTypoAscender (1428) and hhea ascent (1275) must be equal. [code: ascender]
</div></details><details><summary>🔥 <b>FAIL:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.google.fonts/check/varfont/bold_wght_coord">com.google.fonts/check/varfont/bold_wght_coord</a>)</summary><div>

>
>The Open-Type spec's registered design-variation tag 'wght' available at https://docs.microsoft.com/en-gb/typography/opentype/spec/dvaraxistag_wght does not specify a required value for the 'Bold' instance of a variable font.
>
>But Dave Crossland suggested that we should enforce a required value of 700 in this case (NOTE: a distinction is made between "no bold instance present" vs "bold instance is present but its wght coordinate is not == 700").
>
* 🔥 **FAIL** "Bold" instance not present. [code: no-bold-instance]
</div></details><details><summary>🔥 <b>FAIL:</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to a name ID whose string is equal to the string of either name ID 2 or 17, and its postScriptNameID value is set to a name ID whose string is equal to the string of name ID 6. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/fvar.html#com.adobe.fonts/check/varfont/valid_default_instance_nameids">com.adobe.fonts/check/varfont/valid_default_instance_nameids</a>)</summary><div>

>
>According to the 'fvar' documentation in OpenType spec v1.9.1 https://docs.microsoft.com/en-us/typography/opentype/spec/fvar
>
>The default instance of a font is that instance for which the coordinate value of each axis is the defaultValue specified in the corresponding variation axis record. An instance record is not required for the default instance, though an instance record can be provided. When enumerating named instances, the default instance should be enumerated even if there is no corresponding instance record. If an instance record is included for the default instance (that is, an instance record has coordinates set to default values), then the nameID value should be set to either 2 or 17 or to a name ID with the same value as name ID 2 or 17. Also, if a postScriptNameID is included in instance records, and the postScriptNameID value should be set to 6 or to a name ID with the same value as name ID 6.
>
* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its subfamily name should be 'Rg 00 Short Slow' [code: invalid-default-instance-subfamily-name]
* 🔥 **FAIL** 'Regular' instance has the same coordinates as the default instance; its postscript name should be 'Playpen-Rg00ShortSlow', instead of 'PlaypenPER-Regular'. [code: invalid-default-instance-postscript-name]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>

>
>According to a GlyphsApp tutorial [1], in order to make sure all versions of Windows recognize it as a valid font file, we must make sure that the concatenated length of the familyname (NameID.FONT_FAMILY_NAME) and style (NameID.FONT_SUBFAMILY_NAME) strings in the name table do not exceed 20 characters.
>
>After discussing the problem in more detail at FontBakery issue #2179 [2] we decided that allowing up to 27 chars would still be on the safe side, though.
>
>[1] https://glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances [2] https://github.com/fonttools/fontbakery/issues/2179
>
* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Playpen Rg 00 Short Slow' / SUBFAMILY_NAME = 'Regular'

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
</div></details><details><summary>⚠ <b>WARN:</b> Ensure variable fonts include an avar table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/mandatory_avar_table">com.google.fonts/check/mandatory_avar_table</a>)</summary><div>

>
>Most variable fonts should include an avar table to correctly define axes progression rates.
>
>For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000, because a 10% progression from 0% may be too much to define the 200, while 90% may be too little to define the 900.
>
>If the progression rates of axes is linear, this check can be ignored. Fontmake will also skip adding an avar table if the progression rates are linear. However, we still recommend designers visually proof each instance is at the expected weight, width etc.
>
* ⚠ **WARN** This variable font does not have an avar table. [code: missing-avar]
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

	- U_locl.au

	- X.dec_locl

	- Y_locl

	- Z.dec_locl

	- _circle

	- b.jmc_dk

	- caroncomb_locl

	- cnct.ful_t.lop_de_e

	- cnct.mlp_b_s.mod

	- cnct.mod_e_z.ful

	- f.alt1.mrr

	- f.ful_pl

	- four.alt1

	- i.loclTRK

	- ijacute

	- l.alt1.lop

	- nine.alt1

	- one.alt1

	- p.mrr_ca

	- seven.alt1

	- t.lop_de

	- uni0312.case

	- x.cnt_de

	- y_de
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Detect any interpolation issues in the font. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/interpolation_issues">com.google.fonts/check/interpolation_issues</a>)</summary><div>

>
>When creating a variable font, the designer must make sure that corresponding paths have the same start points across masters, as well as that corresponding component shapes are placed in the same order within a glyph across masters. If this is not done, the glyph will not interpolate correctly.
>
>Here we check for the presence of potential interpolation errors using the fontTools.varLib.interpolatable module.
>
* ⚠ **WARN** Interpolation issues were found in the font: 	- Contour 0 start point differs in glyph 'cnct.cnt_G_z' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 0 start point differs in glyph 'x.cnt_de.med' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 1 start point differs in glyph 'x.cnt_de.med' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 0 start point differs in glyph 'cnct.mlp_b_z.mod' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 0 start point differs in glyph 'cnct.mod_G_t' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 0 start point differs in glyph 'x.cnt_de.ini' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 1 start point differs in glyph 'x.cnt_de.ini' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 0 start point differs in glyph 'x.cnt_de.fin' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90>

	- Contour 1 start point differs in glyph 'x.cnt_de.fin' between location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6d900> and location <fontTools.ttLib.ttGlyphSet._TTGlyphSetGlyf object at 0x115a6dc90> [code: interpolation-issues]
</div></details><details><summary>⚠ <b>WARN:</b> Check if OS/2 xAvgCharWidth is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/xavgcharwidth">com.google.fonts/check/xavgcharwidth</a>)</summary><div>


* ⚠ **WARN** OS/2 xAvgCharWidth is 647 but it should be 675 which corresponds to the average of the widths of all glyphs in the font. [code: xAvgCharWidth-wrong]
</div></details><details><summary>⚠ <b>WARN:</b> Check glyphs in mark glyph class are non-spacing. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/gdef.html#com.google.fonts/check/gdef_spacing_marks">com.google.fonts/check/gdef_spacing_marks</a>)</summary><div>

>
>Glyphs in the GDEF mark glyph class should be non-spacing.
>
>Spacing glyphs in the GDEF mark glyph class may have incorrect anchor positioning that was only intended for building composite glyphs during design.
>
* ⚠ **WARN** The following spacing glyphs may be in the GDEF mark glyph class by mistake:
	 tildeshortcomb (unencoded) [code: spacing-mark-glyphs]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 8 | 9 | 102 | 7 | 124 | 0 |
| 0% | 3% | 4% | 41% | 3% | 50% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
