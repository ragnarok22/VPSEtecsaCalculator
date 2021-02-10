"""
The helper file contains price constants and functions that help conversion and normalizations
"""
PRICE_CPU = 0.04
PRICE_RAM = 0.05
PRICE_STORAGE = 0.01

CPU_MIN = 1
CPU_MAX = 8

RAM_MIN = 512  # in MB
RAM_MAX = 16384  # 16GB in MB

STORAGE_MIN = 20  # GB
STORAGE_MAX = 500  # GB

BANDWIDTH = 100  # Mbps
BANDWIDTH_TRANSFER = 250  # gb


def mb_to_gb(mb: int) -> float:
    """
    Convert the given number from mega bytes to giga bytes
    :param mb: The MB to convert to GB
    :return: The GB
    """
    return mb / 1024


def gb_to_mb(gb: int) -> float:
    """
    Convert the given number from giga bytes to mega bytes
    :param gb: The GB to convert to MB
    :return: The MB
    """
    return gb * 1024


def mbi_to_gbi(mbit: int) -> float:
    """
    Convert the given number from mega bite to giga bite
    :param mbit: The MBit to convert to GBit
    :return: The GBit
    """
    return mbit / 1000


def gbi_to_mbi(gbit: int) -> float:
    """
    Convert the given number from giga bite to mega bite
    :param gbit: The GBit to convert to MBit
    :return: The MBit
    """
    return gbit * 1000


def price_normalizer(price: float) -> float:
    """
    Returns two digits after comma
    :param price: The price to normalize
    :return: the normalize price
    """
    return float("{:.2f}".format(price))


def price_per_hours(cpu, ram, storage):
    """
    Return the price of VPS in one hours
    :param cpu: amount of CPU
    :param ram: amount of RAM in MB
    :param storage: amount of storage in GB
    :return: The prices in CUP of VPS in one hour
    """
    return price_normalizer((cpu * PRICE_CPU) + (mb_to_gb(ram) * PRICE_RAM) + (storage * PRICE_STORAGE))


def price_per_day(cpu, ram, storage):
    """
    Return the price of VPS in one day (24 hours)
    :param cpu: amount of CPU
    :param ram: amount of RAM in MB
    :param storage: amount of storage in GB
    :return: The prices in CUP of VPS in one day (24 hours)
    """
    return price_normalizer(price_per_hours(cpu, ram, storage) * 24)


def price_per_month(cpu, ram, storage):
    """
    Return the price of VPS in one month (30 days)
    :param cpu: amount of CPU
    :param ram: amount of RAM in MB
    :param storage: amount of storage in GB
    :return: The prices in CUP of VPS in one month (30 days)
    """
    return price_normalizer(price_per_day(cpu, ram, storage) * 30)
