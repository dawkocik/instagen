
# Instagen

Generating an image with DALL·E 2, slicing it in 9 parts and posting it on Instagram


## Installation

Clone project and install dependencies

```bash
git clone https://github.com/dawkocik/instagen.git
```
```bash
cd instagen & python3 -m pip install -r requirements.txt
```
    
## Usage

Run this to generate a config file
```ps
python3 instagen.py
```


Example config file
```ini
[openai]
api-key = sk-Nts2jClblai5IpL4dkrzT3BblablaNpfmYbC6Vsvs
prompt = cat modern space alien future chaos hd --chaos 100

[instagram]
username = knuieiey
password = verypowerfulpassword
```

Then run again
```ps
python3 instagen.py
```
## Authors

- [@kn](https://www.github.com/dawkocik)

