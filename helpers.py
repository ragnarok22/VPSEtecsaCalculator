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


def mb_to_gb(mb):
    return mb / 1024


def gb_to_mb(gb):
    return gb * 1024


def mbi_to_gbi(mb):
    return mb / 1000


def gbi_to_mbi(gb):
    return gb * 1000


def price_normalizer(price: float):
    # return round(price, 2)
    return float("{:.2f}".format(price))


def price_per_hours(cpu, ram, storage):
    return price_normalizer((cpu * PRICE_CPU) + (mb_to_gb(ram) * PRICE_RAM) + (storage * PRICE_STORAGE))


def price_per_day(cpu, ram, storage):
    return price_normalizer(price_per_hours(cpu, ram, storage) * 24)


def price_per_month(cpu, ram, storage):
    return price_normalizer(price_per_day(cpu, ram, storage) * 30)
