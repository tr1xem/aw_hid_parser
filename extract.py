import pyshark
from hidparser import HID_REPORT


def extract_hid_bytes(pcap_file):
    """
    Extract raw HID payload bytes from a pcapng file where
    usbhid.setup.wLength == 33 || usb.setup.wLength == 33.
    Prints space-separated hex for each matching DATA fragment.
    """
    cap = pyshark.FileCapture(
        pcap_file,
        display_filter="usbhid.setup.wLength == 33 || usb.setup.wLength == 33",
        keep_packets=False,
    )

    for pkt in cap:
        data_fields = getattr(pkt, "data", None)
        if not data_fields:
            continue

        all_fields = getattr(data_fields, "_all_fields", {})
        if not all_fields:
            continue
        if (
            all_fields.get("usbhid.setup.wLength") == "33"
            or all_fields.get("usb.setup.wLength") == "33"
        ):
            usb_fragment = all_fields.get("usb.data_fragment")
            if usb_fragment:
                print("\n---------------------------------------------")
                print("USB COMMAND BUFFER: " + usb_fragment + "\n")
                raw = bytes.fromhex(usb_fragment.replace(":", ""))
                print(HID_REPORT.parse(raw))
