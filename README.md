
# notoglot-mini

Simple Python package and dataset that provides information about the world’s scripts (writing systems). 

Currently, the package is tailored for the [Noto fonts](https://fonts.google.com/noto) project, but is already useful beyond it.

## Dataset

The [dataset](./notoglot_mini/data/notoglot_scripts.json) is a JSON file that contains information about the world’s scripts, structured like so: 

```
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
    },
```

Additional data points about each script will be published in future. 

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

## License

The code is licensed under the [Apache 2](./LICENSE) license. 

The dataset contains some information from: 

- [ScriptSource](https://scriptsource.org/), Copyright © 2022 SIL International, released under the [Creative Commons Attribution-ShareAlike 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license (CC-BY-SA).
- [Unicode.org](https://www.unicode.org/), licensed under the [Unicode, Inc. license agreement, data files and software](https://www.unicode.org/license.txt).
