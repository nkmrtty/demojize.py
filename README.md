# demojize.py
This script decodes emoji icons in an input file to emoji alias, e.g. 👍(`\U0001F44D`) => `:thumbs_up_sign:`.


## Example
### Input file: `input.txt`
```
demojize.py is cool! 👍👍👍
```
### Run
```bash
python demojize.py input.txt
```
### Output file: `demojized_input.txt`
```
demojize.py is cool! :thumbs_up_sign::thumbs_up_sign::thumbs_up_sign:
```


## Requirements
* Python 2.7+
* emoji (from pip)


## Usage
### For a single file

```
python demojize.py /path/to/file
```

### For multiple files in a directory (like batch)

```
ls -1 /path/to/file_dir/ | xargs python demojize.py /path/to/file_dir/
```
