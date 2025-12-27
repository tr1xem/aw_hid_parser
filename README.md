# Alienware RGB HID report parser

Simple and incomplete HID RGB report parser for Alienware laptops.

## Usage

Install the dependencies:

```
uv sync
```

Feed a pcapng file with a list of HID reports through stdin, e.g.

```
uv run python main.py /path/to/alienware-rgb-hid-report.pcapng
```

OR for stream input:

```
uv run python aw_hid_parser.py < report.txt
```

where `report.txt` is a list of HID reports in the format:

```
01 04 01 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
01 0e 01 01 00 81 40 a5 02 0a ff ff ff ff ff ff 02 00 00 01 81 40 a5 02 0a ff ff ff ff ff ff 02 00
01 0e 01 02 02 81 40 a5 02 0a ff ff ff ff ff ff 02 00 00 03 81 40 a5 02 0a ff ff ff ff ff ff 02 00
```
