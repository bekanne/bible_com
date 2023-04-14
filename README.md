# README

This script opens a specific bible chapter or verse on the website www.bible.com.

<img src="bible_com.gif" alt="bible_com" />

## Installation

1. Clone or download the repository to a local directory.
2. Navigate to the directory containing the script.
3. Edit the config.cfg file with your preferred language.
4. Add a config_xx.cfg file if you want to add a new language setting (see *Edit config files* below).
5. Add the following alias to your shell configuration file:

```bash
# Bash (add to ~/.bashrc)
alias bible='/usr/bin/python3 /path/to/script/bible_com.py'

# Zsh (add to ~/.zshrc)
alias bible='/usr/bin/python3 /path/to/script/bible_com.py'

# Windows PowerShell (add to $PROFILE)
Set-Alias -Name bible -Value 'python3.exe C:\path\to\script\bible_com.py'
```
6. Replace /usr/bin/python with the path to your Python interpreter and /path/to/script with the path to the script directory.
Reload your shell configuration or open a new terminal.

> **ℹ️ Windows Users:**  
> In Windows, the PowerShell profile file is located at $PROFILE.CurrentUserAllHosts. You can edit this file to add the alias as described above.  
> Not tested in windows yet.

## Usage

The script requires the following arguments:

```text

bible_com.py [-h] -b BOOK -c CHAPTER [-v VERSE] [-t TRANSLATION] [-p PARALLEL]

  -h, --help - show this help message and exit
  -b, --book BOOK - Name of the book
  -c, --chapter CHAPTER - Chapter number
  -v, --verse VERSE - Verse number
  -t, --translation TRANSLATION - Translation version
  -p, --parallel PARALLEL - Translation for parallel view
```

### Examples

```bash

# Open Genesis 1
bible -b genesis -c 1

# Open John 3:16 in the ESV translation
bible -b john -c 3 -v 16 -t esv
```

## Edit/Add Config Files

### config.cfg
The config.cfg file contains in the langage section the string for the language. Depending on that string (e.g. "xx") the config file config_xx.cfg is used.
### config_xx.cfg
In the config_xx.cfg you have the **books** and **translations** sections. In the books section you define the book names with the aliases used by bible.com in the URL.  
**Example:**
```cfg
[books]
jesaja=ISA
jeremia=JER
```
For the translations the name of the translation and the id from bible.com is needed.  
**Example:**
```cfg
[translations]
esv=59
elberfelder=2351
```
