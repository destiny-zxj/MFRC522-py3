# MFRC522-python


## Requirements
1. Raspberry 
```bash
sudo raspi-config
# Interfacing Options -> SPI
```
2. python3-spidev
```bash
sudo apt-get install python3-spidev
```
3. SPI-Py
```bash
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python3 setup.py install
```

## Pins

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

## Usage

> demo