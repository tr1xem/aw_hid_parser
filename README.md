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
