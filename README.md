
# notoglot-mini

Simple Python package and dataset that provides information about the world’s scripts (writing systems). 

Currently, the package is primarily tailored for the [Noto fonts](https://fonts.google.com/noto) project, but is already useful beyond it.

- This package is currently at “alpha stage”, though we believe that the quality of the data is good.

- Currently, this package is not published to PyPI.

- In future, this package will be replaced by a more comprehensive `notoglot` package, so the current API may change.

- Additional data points about each script will be published in future.


## Dataset

The [dataset](./notoglot_mini/data/notoglot_scripts.json) is a JSON file that contains information about the world’s scripts, keyed by the script’s [ISO 15924 code](https://en.wikipedia.org/wiki/ISO_15924), and structured like so:

```json
{
    "Armn": {
        "id": "Armn",
        "name": "Armenian",
        "status": "",
        "family": "European",
        "type": "alphabet",
        "summary": "Armenian (<span class='autonym'>Հայոց գրեր</span>) is a European bicameral alphabet, written left-to-right (12 million users). Created around 405 CE by Mesrop Mashtots. Used for the Armenian language to this day. Was widespread in the 18th–19th centuries CE in the Ottoman Empire. Armenia uses a reformed spelling introduced in the Soviet Union, the Armenian diaspora mostly uses the original Mesropian orthography.",
        "urls": {
            "ScriptSource": "https://scriptsource.org/scr/Armn",
            "Unicode": "https://www.unicode.org/versions/Unicode15.0.0/ch07.pdf#G3334",
            "Wikipedia": "https://en.wikipedia.org/wiki/ISO_15924:Armn",
            "Wiktionary": "https://en.wiktionary.org/wiki/Category:Armenian_script",
            "WiktionaryLangs": "https://en.wiktionary.org/wiki/Category:Armenian_script_languages",
            "r12a": "https://r12a.github.io/scripts/links?iso=Armn"
        }
    }
}
```

- The most unique data point in each script entry is `summary`, which contains a single-paragraph, hand-curated description of the script. 

## Python package

## Installation

```bash
python3 -m pip install --upgrade git+https://github.com/notofonts/notoglot-mini/
```

### Usage in Python

```python
import notoglot_mini
scripts = notoglot_mini.LoadScripts()
print(scripts["Armn"]["summary"])
```

### Other Python packages of interest

- [gflanguages](https://github.com/googlefonts/lang/): additional info about writing systems, languages and regions
- [fontTools.unicodedata](https://github.com/fonttools/fonttools/tree/main/Lib/fontTools/unicodedata): info about scripts and their code points
- [unicodedata2](https://github.com/fonttools/unicodedata2): info about the Unicode codepoints and their properties
- [aksharamukha](https://github.com/virtualvinodh/aksharamukha-python): transliteration between various scripts

## License

### Python code

Copyright 2021-2022 Noto Authors. Distributed under the [Apache 2](./LICENSE) license.

### Dataset

The dataset contains some information from:

- [The Noto project](https://github.com/notofonts/). Copyright 2021-2022 © Noto Authors. Distributed under the [Apache 2](./LICENSE) license.
- [ScriptSource](https://scriptsource.org/). Copyright © 2022 SIL International. Distributed under the [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license (CC-BY-SA).
- [ISO](https://www.unicode.org/iso15924/) and [Unicode, Inc.](https://www.unicode.org/). Copyright © 1991-2022 ISO, Unicode, Inc. All rights reserved. Distributed under the [Unicode Terms of Use](https://www.unicode.org/copyright.html) and [Unicode license agreement for data files and software](https://www.unicode.org/license.txt).
