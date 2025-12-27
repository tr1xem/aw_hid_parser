from construct import (
    Struct,
    Int8ub,
    Int16ub,
    Switch,
    this,
    Enum,
    Array,
    Hex,
    Int24ub,
    GreedyBytes,
)

AW_DEVICE_INFO = Struct(
    "subcommand"
    / Enum(
        Int8ub,
        FIRMWARE_VERSION=0x00,
        DEVICE_STATUS=0x01,
        CONFIG=0x02,
        ANIMATION_COUNT=0x03,
        ANIMATION_ID=0x04,
        SERIES=0x05,
        ACTION=0x06,
        CALDERA=0x07,
    ),
)

AW_USER_CONTROL = Struct(
    "subcommand"
    / Enum(
        Int16ub,
        START_NEW=0x01,
        FINISH_AND_SAVE=0x02,
        FINISH_AND_PLAY=0x03,
        REMOVE=0x04,
        PLAY=0x05,
        SET_DEFAULT=0x06,
        SET_STARTUP=0x07,
    ),
    "animation_id"
    / Enum(
        Int16ub,
        STARTUP=0x0008,
        DEFAULT=0x0061,
        EPHEMERAL1=0x00FF,
        EPHEMERAL2=0xFFFF,
    ),
    "duration" / Int16ub,
)

AW_POWER_CONTROL = Struct(
    "subcommand"
    / Enum(
        Int16ub,
        START_NEW=0x01,
        FINISH_AND_SAVE=0x02,
        FINISH_AND_PLAY=0x03,
        REMOVE=0x04,
        PLAY=0x05,
        SET_DEFAULT=0x06,
        SET_STARTUP=0x07,
    ),
    "animation_id"
    / Enum(
        Int16ub,
        AC_SLEEP=0x005B,
        AC_ON_CHARGED=0x005C,
        AC_ON_CHARGING=0x005D,
        BATTERY_SLEEP=0x005E,
        BATTERY_ON=0x005F,
        BATTERY_CRITIAL=0x0060,
    ),
    "duration" / Int16ub,
)


AW_ZONE_SELECT = Struct(
    "loop" / Int8ub,
    "zones_size" / Int16ub,
    "zones" / Array(this.zones_size, Int8ub),
)

AW_SET_ANIMATION = Struct(
    "animation"
    / Enum(
        Int8ub,
        SOLID=0x00,
        PULSE=0x01,
        MORPH=0x02,
    ),
    "duration" / Int16ub,
    "tempo" / Int16ub,
    "RGB" / Hex(Int24ub),
)

AW_SET_DIM = Struct(
    "dim" / Int8ub,
    "zones_size" / Int16ub,
    "zones" / Array(this.zones_size, Int8ub),
)

AW_SET_STATIC_COLOR = Struct(
    "RGB" / Hex(Int24ub),
    "zones_size" / Int16ub,
    "zones" / Array(this.zones_size, Int8ub),
)

AW_RESET = Struct(
    "target" / Int8ub,
)

AW_REPORT = Struct(
    "command_type"
    / Enum(
        Int8ub,
        DEVICE_INFO=0x20,
        USER_CONTROL=0x21,
        POWER_CONTROL=0x22,
        ZONE_SELECT=0x23,
        SET_ANIMATION=0x24,
        SET_EVENT=0x25,
        SET_DIM=0x26,
        SET_STATIC_COLOR=0x27,
        RESET=0x28,
        ERASE_SPI_FLASH=0xFF,
    ),
    "command"
    / Switch(
        this.command_type,
        {
            "DEVICE_INFO": AW_DEVICE_INFO,
            "USER_CONTROL": AW_USER_CONTROL,
            "POWER_CONTROL": AW_POWER_CONTROL,
            "ZONE_SELECT": AW_ZONE_SELECT,
            "SET_ANIMATION": Array(3, AW_SET_ANIMATION),
            "SET_DIM": AW_SET_DIM,
            "SET_STATIC_COLOR": AW_SET_STATIC_COLOR,
            "AW_RESET": AW_RESET,
        },
    ),
    # "tail" / GreedyBytes,
)

DARFON_REPORT = Struct(
    "command_type"
    / Enum(
        Hex(Int8ub),
        SET_EFFECT=0x80,
        TURN_ON_SET=0x83,
        COLOR_CONTROL=0x8C,
        DEVICE_CONTROL=0x8B,
        DEV_INFO=0x93,
        DEVICE_CONFIG=0x94,
        DEVICE_CONFIG2=0x99,
    ),
    "tail" / GreedyBytes,
)

HID_REPORT = Struct(
    "hid_preamble"
    / Enum(
        Int8ub,
        AW_ELC=0x03,  # AW_ELC Preamble
        DARFON_RGB=0xCC,  # Darfon RGB Report ID
        DARFON_KB=0x01,  # Darfon KB Report ID
    ),
    "report"
    / Switch(
        this.hid_preamble,
        {
            "AW_ELC": AW_REPORT,
            "DARFON_RGB": DARFON_REPORT,
        },
    ),
)
