import pandas as pd

# Данные для CPU
cpu_data_old = [
    {'Model': 'Intel Core i9-9900K', 'GHz': 3.6, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 98.88},
    {'Model': 'AMD Ryzen 9 3950X', 'GHz': 3.5, 'Cache L3 (MB)': 64, 'Cores': 16, 'GFLOPS': 226.19},
    {'Model': 'Intel Xeon Gold 6148', 'GHz': 2.4, 'Cache L3 (MB)': 27.5, 'Cores': 20, 'GFLOPS': 192.0},
    {'Model': 'AMD Ryzen 5 3600', 'GHz': 3.6, 'Cache L3 (MB)': 32, 'Cores': 6, 'GFLOPS': 86.4},
    {'Model': 'Intel Core i7-8700', 'GHz': 3.2, 'Cache L3 (MB)': 12, 'Cores': 6, 'GFLOPS': 76.8},
{'Model': 'Intel Core i3-9100', 'GHz': 3.6, 'Cache L3 (MB)': 6, 'Cores': 4, 'GFLOPS': 50.0},
{'Model': 'Intel Core i3-9300', 'GHz': 3.7, 'Cache L3 (MB)': 8, 'Cores': 4, 'GFLOPS': 52.0},
{'Model': 'Intel Core i3-10100', 'GHz': 3.6, 'Cache L3 (MB)': 6, 'Cores': 4, 'GFLOPS': 55.0},
{'Model': 'Intel Core i3-10300', 'GHz': 3.7, 'Cache L3 (MB)': 8, 'Cores': 4, 'GFLOPS': 58.0},
{'Model': 'Intel Core i5-9400', 'GHz': 2.9, 'Cache L3 (MB)': 9, 'Cores': 6, 'GFLOPS': 60.0},
{'Model': 'Intel Core i5-9600K', 'GHz': 3.7, 'Cache L3 (MB)': 9, 'Cores': 6, 'GFLOPS': 70.0},
{'Model': 'Intel Core i5-10400', 'GHz': 2.9, 'Cache L3 (MB)': 12, 'Cores': 6, 'GFLOPS': 65.0},
{'Model': 'Intel Core i5-10600K', 'GHz': 4.1, 'Cache L3 (MB)': 12, 'Cores': 6, 'GFLOPS': 80.0},
{'Model': 'Intel Core i7-9700K', 'GHz': 3.6, 'Cache L3 (MB)': 12, 'Cores': 8, 'GFLOPS': 90.0},
{'Model': 'Intel Core i7-10700K', 'GHz': 3.8, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 95.0},
{'Model': 'Intel Core i7-11700K', 'GHz': 3.6, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 100.0},
{'Model': 'Intel Core i9-9900K', 'GHz': 3.6, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 98.88},
{'Model': 'Intel Core i9-10900K', 'GHz': 3.7, 'Cache L3 (MB)': 20, 'Cores': 10, 'GFLOPS': 120.0},
{'Model': 'Intel Core i9-11900K', 'GHz': 3.5, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 110.0},
{'Model': 'Intel Core i9-12900K', 'GHz': 3.2, 'Cache L3 (MB)': 30, 'Cores': 16, 'GFLOPS': 200.0},
{'Model': 'AMD Ryzen 3 3100', 'GHz': 3.6, 'Cache L3 (MB)': 16, 'Cores': 4, 'GFLOPS': 60.0},
{'Model': 'AMD Ryzen 3 3300X', 'GHz': 3.8, 'Cache L3 (MB)': 16, 'Cores': 4, 'GFLOPS': 65.0},
{'Model': 'AMD Ryzen 3 4100', 'GHz': 3.8, 'Cache L3 (MB)': 4, 'Cores': 4, 'GFLOPS': 55.0},
{'Model': 'AMD Ryzen 5 3600', 'GHz': 3.6, 'Cache L3 (MB)': 32, 'Cores': 6, 'GFLOPS': 90.0},
{'Model': 'AMD Ryzen 5 5600X', 'GHz': 3.7, 'Cache L3 (MB)': 32, 'Cores': 6, 'GFLOPS': 100.0},
{'Model': 'AMD Ryzen 5 4600G', 'GHz': 3.7, 'Cache L3 (MB)': 8, 'Cores': 6, 'GFLOPS': 80.0},
{'Model': 'AMD Ryzen 7 3700X', 'GHz': 3.6, 'Cache L3 (MB)': 32, 'Cores': 8, 'GFLOPS': 120.0},
{'Model': 'AMD Ryzen 7 5800X', 'GHz': 3.8, 'Cache L3 (MB)': 32, 'Cores': 8, 'GFLOPS': 130.0},
{'Model': 'AMD Ryzen 7 5700G', 'GHz': 3.8, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 110.0},
{'Model': 'AMD Ryzen 9 3900X', 'GHz': 3.8, 'Cache L3 (MB)': 64, 'Cores': 12, 'GFLOPS': 180.0},
{'Model': 'AMD Ryzen 9 5900X', 'GHz': 3.7, 'Cache L3 (MB)': 64, 'Cores': 12, 'GFLOPS': 190.0},
{'Model': 'AMD Ryzen 9 5950X', 'GHz': 3.4, 'Cache L3 (MB)': 64, 'Cores': 16, 'GFLOPS': 240.0},
{'Model': 'AMD Ryzen Threadripper 3960X', 'GHz': 3.8, 'Cache L3 (MB)': 128, 'Cores': 24, 'GFLOPS': 400.0},
{'Model': 'AMD Ryzen Threadripper 3970X', 'GHz': 3.7, 'Cache L3 (MB)': 128, 'Cores': 32, 'GFLOPS': 500.0},
{'Model': 'AMD Ryzen Threadripper 3990X', 'GHz': 2.9, 'Cache L3 (MB)': 256, 'Cores': 64, 'GFLOPS': 800.0},
{'Model': 'Intel Core i5-11400', 'GHz': 2.6, 'Cache L3 (MB)': 12, 'Cores': 6, 'GFLOPS': 70.0},
{'Model': 'Intel Core i5-11600K', 'GHz': 3.9, 'Cache L3 (MB)': 12, 'Cores': 6, 'GFLOPS': 85.0},
{'Model': 'Intel Core i7-11700', 'GHz': 2.5, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 95.0},
{'Model': 'Intel Core i9-11900', 'GHz': 2.5, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 105.0},
{'Model': 'Intel Core i7-8700K', 'GHz': 3.7, 'Cache L3 (MB)': 12, 'Cores': 6, 'GFLOPS': 80.0},
{'Model': 'Intel Core i5-8600K', 'GHz': 3.6, 'Cache L3 (MB)': 9, 'Cores': 6, 'GFLOPS': 70.0},
{'Model': 'Intel Core i7-1185G7', 'GHz': 3.0, 'Cache L3 (MB)': 12, 'Cores': 4, 'GFLOPS': 60.0},
{'Model': 'Intel Core i5-1135G7', 'GHz': 2.4, 'Cache L3 (MB)': 8, 'Cores': 4, 'GFLOPS': 50.0},
{'Model': 'AMD Ryzen 5 3500X', 'GHz': 3.6, 'Cache L3 (MB)': 32, 'Cores': 6, 'GFLOPS': 85.0},
{'Model': 'AMD Ryzen 7 2700X', 'GHz': 3.7, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 100.0},
{'Model': 'AMD Ryzen 9 4900HS', 'GHz': 3.0, 'Cache L3 (MB)': 8, 'Cores': 8, 'GFLOPS': 90.0},
{'Model': 'AMD Ryzen 5 5600G', 'GHz': 3.9, 'Cache L3 (MB)': 16, 'Cores': 6, 'GFLOPS': 95.0},
{'Model': 'AMD Ryzen 7 5700X', 'GHz': 3.4, 'Cache L3 (MB)': 32, 'Cores': 8, 'GFLOPS': 120.0},
{'Model': 'AMD Ryzen 9 6900HX', 'GHz': 3.3, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 110.0},
{'Model': 'Intel Core i3-8100', 'GHz': 3.6, 'Cache L3 (MB)': 6, 'Cores': 4, 'GFLOPS': 45.0},
{'Model': 'Intel Core i5-7600K', 'GHz': 3.8, 'Cache L3 (MB)': 6, 'Cores': 4, 'GFLOPS': 55.0},
{'Model': 'AMD Ryzen 3 2200G', 'GHz': 3.5, 'Cache L3 (MB)': 4, 'Cores': 4, 'GFLOPS': 40.0},
{'Model': 'AMD Ryzen 5 2600', 'GHz': 3.4, 'Cache L3 (MB)': 16, 'Cores': 6, 'GFLOPS': 75.0},
{'Model': 'Intel Core i7-6700K', 'GHz': 4.0, 'Cache L3 (MB)': 8, 'Cores': 4, 'GFLOPS': 60.0},
{'Model': 'AMD Ryzen 7 1800X', 'GHz': 3.6, 'Cache L3 (MB)': 16, 'Cores': 8, 'GFLOPS': 90.0},
{'Model': 'Intel Core i9-7900X', 'GHz': 3.3, 'Cache L3 (MB)': 13.75, 'Cores': 10, 'GFLOPS': 120.0},
{'Model': 'AMD Ryzen 9 3950X', 'GHz': 3.5, 'Cache L3 (MB)': 64, 'Cores': 16, 'GFLOPS': 250.0},
{'Model': 'Intel Core i5-12400', 'GHz': 2.5, 'Cache L3 (MB)': 18, 'Cores': 6, 'GFLOPS': 80.0},
{'Model': 'AMD Ryzen 5 7600X', 'GHz': 4.7, 'Cache L3 (MB)': 32, 'Cores': 6, 'GFLOPS': 120.0},
{'Model': 'Intel Core i7-13700K', 'GHz': 3.4, 'Cache L3 (MB)': 30, 'Cores': 16, 'GFLOPS': 240.0},
{'Model': 'AMD Ryzen 7 7800X', 'GHz': 4.5, 'Cache L3 (MB)': 32, 'Cores': 8, 'GFLOPS': 160.0},
{'Model': 'Intel Core i9-13900K', 'GHz': 3.0, 'Cache L3 (MB)': 36, 'Cores': 24, 'GFLOPS': 350.0},
{'Model': 'AMD Ryzen 9 7950X', 'GHz': 4.5, 'Cache L3 (MB)': 64, 'Cores': 16, 'GFLOPS': 300.0},
{'Model': 'Intel Core i3-12100', 'GHz': 3.3, 'Cache L3 (MB)': 12, 'Cores': 4, 'GFLOPS': 60.0},
{'Model': 'AMD Ryzen 3 5300G', 'GHz': 4.0, 'Cache L3 (MB)': 8, 'Cores': 4, 'GFLOPS': 70.0},

]

cpu_df = pd.DataFrame(cpu_data)

# Данные для GPU
gpu_data_old = [
    {'Model': 'Tesla V100 SXM2 32Gb', 'Clock Speed (MHz)': 1380, 'VRAM (GB)': 32, 'Cores': 5120, 'GFLOPS': 15700},
    {'Model': 'GeForce RTX 2080 Ti', 'Clock Speed (MHz)': 1545, 'VRAM (GB)': 11, 'Cores': 4352, 'GFLOPS': 13400},
    {'Model': 'AMD Radeon VII', 'Clock Speed (MHz)': 1400, 'VRAM (GB)': 16, 'Cores': 3840, 'GFLOPS': 13800},
    {'Model': 'GeForce GTX 1080', 'Clock Speed (MHz)': 1607, 'VRAM (GB)': 8, 'Cores': 2560, 'GFLOPS': 8228},
    {'Model': 'NVIDIA Tesla T4', 'Clock Speed (MHz)': 1590, 'VRAM (GB)': 16, 'Cores': 2560, 'GFLOPS': 8140},
    {'Model': 'NVIDIA Quadro GV100', 'Clock Speed (MHz)': 1132, 'VRAM (GB)': 32, 'Cores': 5120, 'GFLOPS': 16660},
    {'Model': 'NVIDIA TITAN V', 'Clock Speed (MHz)': 1200, 'VRAM (GB)': 12, 'Cores': 5120, 'GFLOPS': 14900},
    {'Model': 'NVIDIA Quadro RTX 8000', 'Clock Speed (MHz)': 1395, 'VRAM (GB)': 48, 'Cores': 4608, 'GFLOPS': 16310},
    {'Model': 'GeForce GTX 1080 Ti', 'Clock Speed (MHz)': 1481, 'VRAM (GB)': 11, 'Cores': 3584, 'GFLOPS': 11340},
    {'Model': 'GeForce RTX 2080', 'Clock Speed (MHz)': 1515, 'VRAM (GB)': 8, 'Cores': 2944, 'GFLOPS': 10070},
    {'Model': 'NVIDIA Quadro P6000', 'Clock Speed (MHz)': 1506, 'VRAM (GB)': 24, 'Cores': 3840, 'GFLOPS': 12630},
    {'Model': 'NVIDIA TITAN Xp CE', 'Clock Speed (MHz)': 1405, 'VRAM (GB)': 12, 'Cores': 3840, 'GFLOPS': 12150},
    {'Model': 'NVIDIA Tesla P40', 'Clock Speed (MHz)': 1303, 'VRAM (GB)': 24, 'Cores': 3840, 'GFLOPS': 11760},
    {'Model': 'Tesla V100 SXM2 32Gb', 'Clock Speed (MHz)': 1380, 'VRAM (GB)': 32, 'Cores': 5120, 'GFLOPS': 15700},
    {'Model': 'NVIDIA GeForce RTX 3090', 'Clock Speed (MHz)': 1695, 'VRAM (GB)': 24, 'Cores': 10496, 'GFLOPS': 35500},
    {'Model': 'NVIDIA GeForce RTX 3080', 'Clock Speed (MHz)': 1710, 'VRAM (GB)': 10, 'Cores': 8704, 'GFLOPS': 29700},
    {'Model': 'NVIDIA GeForce RTX 3070', 'Clock Speed (MHz)': 1725, 'VRAM (GB)': 8, 'Cores': 5888, 'GFLOPS': 20300},
    {'Model': 'NVIDIA GeForce RTX 3060 Ti', 'Clock Speed (MHz)': 1665, 'VRAM (GB)': 8, 'Cores': 4864, 'GFLOPS': 16300},
    {'Model': 'NVIDIA GeForce GTX 1080 Ti', 'Clock Speed (MHz)': 1582, 'VRAM (GB)': 11, 'Cores': 3584, 'GFLOPS': 11300},
    {'Model': 'NVIDIA Quadro RTX 8000', 'Clock Speed (MHz)': 1770, 'VRAM (GB)': 48, 'Cores': 4608, 'GFLOPS': 16300},
    {'Model': 'NVIDIA A100 Tensor Core', 'Clock Speed (MHz)': 1410, 'VRAM (GB)': 40, 'Cores': 6912, 'GFLOPS': 19500},
    {'Model': 'AMD Radeon RX 6900 XT', 'Clock Speed (MHz)': 2250, 'VRAM (GB)': 16, 'Cores': 5120, 'GFLOPS': 23000},
    {'Model': 'AMD Radeon RX 6800 XT', 'Clock Speed (MHz)': 2250, 'VRAM (GB)': 16, 'Cores': 4608, 'GFLOPS': 20700},
    {'Model': 'AMD Radeon RX 6700 XT', 'Clock Speed (MHz)': 2581, 'VRAM (GB)': 12, 'Cores': 2560, 'GFLOPS': 13200},
    {'Model': 'AMD Radeon RX 580', 'Clock Speed (MHz)': 1340, 'VRAM (GB)': 8, 'Cores': 2304, 'GFLOPS': 6170},
    {'Model': 'AMD Radeon Pro W6800', 'Clock Speed (MHz)': 2320, 'VRAM (GB)': 32, 'Cores': 3840, 'GFLOPS': 17800},
    {'Model': 'AMD Radeon Instinct MI100', 'Clock Speed (MHz)': 1502, 'VRAM (GB)': 32, 'Cores': 7680, 'GFLOPS': 23000},
    {'Model': 'Intel Arc A770', 'Clock Speed (MHz)': 2100, 'VRAM (GB)': 16, 'Cores': 4096, 'GFLOPS': 17000},
    {'Model': 'Intel Iris Xe Graphics', 'Clock Speed (MHz)': 1300, 'VRAM (GB)': 0, 'Cores': 96, 'GFLOPS': 2500},  # Встроенная графика
    {'Model': 'NVIDIA GeForce MX450', 'Clock Speed (MHz)': 1395, 'VRAM (GB)': 2, 'Cores': 896, 'GFLOPS': 2500},  # Мобильная видеокарта
    {'Model': 'AMD Radeon RX 5500M', 'Clock Speed (MHz)': 1645, 'VRAM (GB)': 4, 'Cores': 1408, 'GFLOPS': 4630},  # Мобильная видеокарта
    {'Model': 'NVIDIA GeForce RTX 4090', 'Clock Speed (MHz)': 2520, 'VRAM (GB)': 24, 'Cores': 16384, 'GFLOPS': 82700},
    {'Model': 'NVIDIA GeForce RTX 4080', 'Clock Speed (MHz)': 2505, 'VRAM (GB)': 16, 'Cores': 9728, 'GFLOPS': 48700},
    {'Model': 'AMD Radeon RX 7900 XTX', 'Clock Speed (MHz)': 2500, 'VRAM (GB)': 24, 'Cores': 6144, 'GFLOPS': 61000},
    {'Model': 'AMD Radeon RX 7800 XT', 'Clock Speed (MHz)': 2430, 'VRAM (GB)': 16, 'Cores': 3840, 'GFLOPS': 37300},
    {'Model': 'NVIDIA GeForce RTX 4060', 'Clock Speed (MHz)': 2460, 'VRAM (GB)': 8, 'Cores': 3072, 'GFLOPS': 15100},
    {'Model': 'AMD Radeon RX 7600', 'Clock Speed (MHz)': 2655, 'VRAM (GB)': 8, 'Cores': 2048, 'GFLOPS': 10900},
    {'Model': 'Intel Arc A580', 'Clock Speed (MHz)': 2000, 'VRAM (GB)': 8, 'Cores': 3072, 'GFLOPS': 12300},
    {'Model': 'NVIDIA GeForce GTX 1660 Super', 'Clock Speed (MHz)': 1785, 'VRAM (GB)': 6, 'Cores': 1408, 'GFLOPS': 5030},
    {'Model': 'AMD Radeon RX 5700 XT', 'Clock Speed (MHz)': 1905, 'VRAM (GB)': 8, 'Cores': 2560, 'GFLOPS': 9750},
    {'Model': 'NVIDIA Quadro P6000', 'Clock Speed (MHz)': 1645, 'VRAM (GB)': 24, 'Cores': 3840, 'GFLOPS': 12700},
    {'Model': 'AMD Radeon Pro VII', 'Clock Speed (MHz)': 1700, 'VRAM (GB)': 16, 'Cores': 3840, 'GFLOPS': 13100},
    {'Model': 'NVIDIA Titan RTX', 'Clock Speed (MHz)': 1770, 'VRAM (GB)': 24, 'Cores': 4608, 'GFLOPS': 16300},
    {'Model': 'AMD Radeon RX 6600', 'Clock Speed (MHz)': 2491, 'VRAM (GB)': 8, 'Cores': 1792, 'GFLOPS': 8920},
    {'Model': 'NVIDIA GeForce RTX 3050', 'Clock Speed (MHz)': 1777, 'VRAM (GB)': 8, 'Cores': 2560, 'GFLOPS':910},
    {'Model': 'NVIDIA GeForce RTX 2080 Ti', 'Clock Speed (MHz)': 1635, 'VRAM (GB)': 11, 'Cores': 4352, 'GFLOPS': 14200},
    {'Model': 'NVIDIA GeForce RTX 2070 Super', 'Clock Speed (MHz)': 1770, 'VRAM (GB)': 8, 'Cores': 2560, 'GFLOPS': 9070},
    {'Model': 'NVIDIA GeForce GTX 1060', 'Clock Speed (MHz)': 1708, 'VRAM (GB)': 6, 'Cores': 1280, 'GFLOPS': 4370},
    {'Model': 'NVIDIA GeForce GTX 980 Ti', 'Clock Speed (MHz)': 1075, 'VRAM (GB)': 6, 'Cores': 2816, 'GFLOPS': 6060},
    {'Model': 'NVIDIA GeForce RTX 2060', 'Clock Speed (MHz)': 1680, 'VRAM (GB)': 6, 'Cores': 1920, 'GFLOPS': 6450},
    {'Model': 'AMD Radeon RX 570', 'Clock Speed (MHz)': 1244, 'VRAM (GB)': 4, 'Cores': 2048, 'GFLOPS': 5100},
    {'Model': 'AMD Radeon RX 5600 XT', 'Clock Speed (MHz)': 1560, 'VRAM (GB)': 6, 'Cores': 2304, 'GFLOPS': 7190},
    {'Model': 'AMD Radeon RX 550', 'Clock Speed (MHz)': 1183, 'VRAM (GB)': 4, 'Cores': 512, 'GFLOPS': 1210},
    {'Model': 'AMD Radeon Pro WX 8200', 'Clock Speed (MHz)': 1500, 'VRAM (GB)': 8, 'Cores': 3584, 'GFLOPS': 10800},
    {'Model': 'AMD Radeon Instinct MI50', 'Clock Speed (MHz)': 1725, 'VRAM (GB)': 32, 'Cores': 3840, 'GFLOPS': 13300},
    {'Model': 'Intel Arc A750', 'Clock Speed (MHz)': 2050, 'VRAM (GB)': 8, 'Cores': 3584, 'GFLOPS': 14700},
    {'Model': 'Intel Iris Plus Graphics 655', 'Clock Speed (MHz)': 1200, 'VRAM (GB)': 0, 'Cores': 48, 'GFLOPS': 1152},
    {'Model': 'NVIDIA GeForce MX350', 'Clock Speed (MHz)': 1354, 'VRAM (GB)': 2, 'Cores': 640, 'GFLOPS': 1730},
    {'Model': 'AMD Radeon RX 6800M', 'Clock Speed (MHz)': 2300, 'VRAM (GB)': 12, 'Cores': 2560, 'GFLOPS': 11800},
    {'Model': 'NVIDIA GeForce RTX 3080 Ti', 'Clock Speed (MHz)': 1665, 'VRAM (GB)': 12, 'Cores': 10240, 'GFLOPS': 34100},
    {'Model': 'NVIDIA GeForce RTX 4070', 'Clock Speed (MHz)': 2475, 'VRAM (GB)': 12, 'Cores': 5888, 'GFLOPS': 29100},
    {'Model': 'AMD Radeon RX 6950 XT', 'Clock Speed (MHz)': 2310, 'VRAM (GB)': 16, 'Cores': 5120, 'GFLOPS': 23600},
    {'Model': 'AMD Radeon RX 7700 XT', 'Clock Speed (MHz)': 2544, 'VRAM (GB)': 12, 'Cores': 3456, 'GFLOPS': 17600},
    {'Model': 'NVIDIA GeForce RTX 4050', 'Clock Speed (MHz)': 2640, 'VRAM (GB)': 6, 'Cores': 2560, 'GFLOPS': 13500},
    {'Model': 'AMD Radeon RX 7500', 'Clock Speed (MHz)': 2300, 'VRAM (GB)': 6, 'Cores': 1536, 'GFLOPS': 7100},
    {'Model': 'Intel Arc A380', 'Clock Speed (MHz)': 2000, 'VRAM (GB)': 6, 'Cores': 1024, 'GFLOPS': 4100},
    {'Model': 'NVIDIA GeForce GTX 1650', 'Clock Speed (MHz)': 1665, 'VRAM (GB)': 4, 'Cores': 896, 'GFLOPS': 2990},
    {'Model': 'AMD Radeon RX 6400', 'Clock Speed (MHz)': 2321, 'VRAM (GB)': 4, 'Cores': 768, 'GFLOPS': 3570},
    {'Model': 'NVIDIA Quadro RTX 6000', 'Clock Speed (MHz)': 1770, 'VRAM (GB)': 24, 'Cores': 4608, 'GFLOPS': 16300},
    {'Model': 'AMD Radeon Pro W5700', 'Clock Speed (MHz)': 1930, 'VRAM (GB)': 8, 'Cores': 2304, 'GFLOPS': 8900},
    {'Model': 'NVIDIA Titan V', 'Clock Speed (MHz)': 1455, 'VRAM (GB)': 12, 'Cores': 5120, 'GFLOPS': 14900},
    {'Model': 'AMD Radeon RX 6600 XT', 'Clock Speed (MHz)': 2589, 'VRAM (GB)': 8, 'Cores': 2048, 'GFLOPS': 10600},
    {'Model': 'NVIDIA GeForce RTX 3060', 'Clock Speed (MHz)': 1777, 'VRAM (GB)': 12, 'Cores': 3584, 'GFLOPS': 12700},
    {'Model': 'Intel UHD Graphics 630', 'Clock Speed (MHz)': 1150, 'VRAM (GB)': 0, 'Cores': 24, 'GFLOPS': 442},
    {'Model': 'AMD Radeon Vega 11', 'Clock Speed (MHz)': 1400, 'VRAM (GB)': 0, 'Cores': 704, 'GFLOPS': 1971},
]



gpu_df = pd.DataFrame(gpu_data)


import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # Создаем сетку 2x3
fig.suptitle('CPU Specifications')  # Заголовок группы графиков

# Первый ряд
sns.scatterplot(data=cpu_df, x='Cache L3 (MB)', y='GHz', ax=axes[0,0])
axes[0,0].set_title('GHz vs. Cache L3 (MB)')
sns.scatterplot(data=cpu_df, x='Cores', y='GHz', ax=axes[0,1])
axes[0,1].set_title('GHz vs. Cores')
sns.scatterplot(data=cpu_df, x='GFLOPS', y='GHz', ax=axes[0,2])
axes[0,2].set_title('GHz vs. GFLOPS')

# Второй ряд
sns.scatterplot(data=cpu_df, x='Cores', y='Cache L3 (MB)', ax=axes[1,0])
axes[1,0].set_title('Cache L3 (MB) vs. Cores')
sns.scatterplot(data=cpu_df, x='GFLOPS', y='Cache L3 (MB)', ax=axes[1,1])
axes[1,1].set_title('Cache L3 (MB) vs. GFLOPS')
sns.scatterplot(data=cpu_df, x='GFLOPS', y='Cores', ax=axes[1,2])
axes[1,2].set_title('Cores vs. GFLOPS')

plt.tight_layout()  # Автоматическая подстройка расстояний между графиками
plt.show()  # Отображение графиков для CPUs

# Графики для GPUs
fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # Создаем сетку 2x3
fig.suptitle('GPU Specifications')  # Заголовок группы графиков

# Первый ряд
sns.scatterplot(data=gpu_df, x='VRAM (GB)', y='Clock Speed (MHz)', ax=axes[0,0])
axes[0,0].set_title('Clock Speed (MHz) vs. VRAM (GB)')
sns.scatterplot(data=gpu_df, x='Cores', y='Clock Speed (MHz)', ax=axes[0,1])
axes[0,1].set_title('Clock Speed (MHz) vs. Cores')
sns.scatterplot(data=gpu_df, x='GFLOPS', y='Clock Speed (MHz)', ax=axes[0,2])
axes[0,2].set_title('Clock Speed (MHz) vs. GFLOPS')

# Второй ряд
sns.scatterplot(data=gpu_df, x='Cores', y='VRAM (GB)', ax=axes[1,0])
axes[1,0].set_title('VRAM (GB) vs. Cores')
sns.scatterplot(data=gpu_df, x='GFLOPS', y='VRAM (GB)', ax=axes[1,1])
axes[1,1].set_title('VRAM (GB) vs. GFLOPS')
sns.scatterplot(data=gpu_df, x='GFLOPS', y='Cores', ax=axes[1,2])
axes[1,2].set_title('Cores vs. GFLOPS')

plt.tight_layout()  # Автоматическая подстройка расстояний между графиками
plt.show()  # Отображение графиков для GPUs