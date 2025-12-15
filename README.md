# Alienware RGB HID report parser

Simple and incomplete HID RGB report parser for Alienware laptops.

## Usage

Feed a file with a list of HID reports through stdin, e.g.

```
./aw_hid_parser < reports.txt
```

Where `reports.txt` is formated like:

```
03 21 00 01 ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
03 23 01 00 01 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```
