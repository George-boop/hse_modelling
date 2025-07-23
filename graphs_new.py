gpu_data = [
    {'Model': 'Tesla V100 SXM2 32Gb', 'Cores': 5120, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 900, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 15.7, 'VRAM (GB)': 32},
    {'Model': 'Tesla V100 SXM2 16Gb', 'Cores': 5120, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 900, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 15.7, 'VRAM (GB)': 16},
    {'Model': 'Tesla V100 PCIE 32Gb', 'Cores': 5120, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 900, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 14.1, 'VRAM (GB)': 32},
    {'Model': 'Tesla V100 PCIE 16Gb', 'Cores': 5120, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 900, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 14.1, 'VRAM (GB)': 16},
    {'Model': 'NVIDIA Quadro GV100', 'Cores': 5120, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 900, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 15.7, 'VRAM (GB)': 32},
    {'Model': 'NVIDIA TITAN V', 'Cores': 5120, 'L2-Cache (MB)': 4.5, 'Memory Bandwidth (GB/s)': 652.8, 'Memory Bus (bit)': 3072, 'Performance (FP32 TFLOPS)': 14.9, 'VRAM (GB)': 12},
    {'Model': 'NVIDIA TITAN RTX', 'Cores': 4608, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 672, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 16.3, 'VRAM (GB)': 24},
    {'Model': 'GeForce RTX 2080 Ti', 'Cores': 4352, 'L2-Cache (MB)': 5.5, 'Memory Bandwidth (GB/s)': 616, 'Memory Bus (bit)': 352, 'Performance (FP32 TFLOPS)': 14.2, 'VRAM (GB)': 11},
    {'Model': 'NVIDIA Quadro RTX 8000', 'Cores': 4608, 'L2-Cache (MB)': 6, 'Memory Bandwidth (GB/s)': 672, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 16.3, 'VRAM (GB)': 48},
    {'Model': 'NVIDIA Quadro GP100', 'Cores': 3584, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 732, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 10.3, 'VRAM (GB)': 16},
    {'Model': 'NVIDIA TITAN Xp', 'Cores': 3840, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 547.7, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 12.1, 'VRAM (GB)': 12},
    {'Model': 'GeForce GTX 1080 Ti', 'Cores': 3584, 'L2-Cache (MB)': 2.75, 'Memory Bandwidth (GB/s)': 484, 'Memory Bus (bit)': 352, 'Performance (FP32 TFLOPS)': 11.3, 'VRAM (GB)': 11},
    {'Model': 'GeForce RTX 2080 SUPER', 'Cores': 3072, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 496, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 11.2, 'VRAM (GB)': 8},
    {'Model': 'GeForce RTX 2070 SUPER', 'Cores': 2560, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 9.1, 'VRAM (GB)': 8},
    {'Model': 'GeForce RTX 2080', 'Cores': 2944, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 10.1, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA Tesla P100', 'Cores': 3584, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 732, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 10.6, 'VRAM (GB)': 16},
    {'Model': 'NVIDIA Quadro RTX 5000', 'Cores': 3072, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 11.2, 'VRAM (GB)': 16},
    {'Model': 'NVIDIA Quadro P6000', 'Cores': 3840, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 432, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 12.0, 'VRAM (GB)': 24},
    {'Model': 'GeForce RTX 2070', 'Cores': 2304, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 7.5, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA TITAN Xp CE', 'Cores': 3840, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 547.7, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 12.1, 'VRAM (GB)': 12},
    {'Model': 'NVIDIA TITAN X Pascal', 'Cores': 3584, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 480, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 11.0, 'VRAM (GB)': 12},
    {'Model': 'GeForce RTX 2060 SUPER', 'Cores': 2176, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 7.2, 'VRAM (GB)': 8},
    {'Model': 'AMD Radeon VII', 'Cores': 3840, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 1024, 'Memory Bus (bit)': 4096, 'Performance (FP32 TFLOPS)': 13.8, 'VRAM (GB)': 16},
    {'Model': 'NVIDIA Quadro RTX 4000', 'Cores': 2304, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 416, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 7.1, 'VRAM (GB)': 8},
    {'Model': 'GeForce RTX 2060', 'Cores': 1920, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 336, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 6.5, 'VRAM (GB)': 6},
    {'Model': 'NVIDIA Tesla P40', 'Cores': 3840, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 346, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 12.0, 'VRAM (GB)': 24},
    {'Model': 'GeForce RTX 2070 SUPER Laptop', 'Cores': 2560, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 9.1, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX 1080', 'Cores': 2560, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 320, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.9, 'VRAM (GB)': 8},
    {'Model': 'GeForce RTX 2080 Max-Q', 'Cores': 2944, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 384, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.8, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX 1080 Laptop', 'Cores': 2560, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 320, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.9, 'VRAM (GB)': 8},
    {'Model': 'GeForce RTX 2070 Max-Q', 'Cores': 2304, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 384, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 6.8, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA Quadro RTX 5000 Max-Q', 'Cores': 3072, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 384, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 9.5, 'VRAM (GB)': 16},
    {'Model': 'NVIDIA Quadro P5000', 'Cores': 2560, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.9, 'VRAM (GB)': 16},
    {'Model': 'GeForce GTX 980 Ti', 'Cores': 2816, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 336, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 6.1, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 1070 Ti', 'Cores': 2432, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 256, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.1, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX TITAN X', 'Cores': 3072, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 336, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 7.0, 'VRAM (GB)': 12},
    {'Model': 'GeForce RTX 2070 Laptop', 'Cores': 2304, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 448, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 7.5, 'VRAM (GB)': 8},
    {'Model': 'GeForce RTX 2060 Laptop', 'Cores': 1920, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 336, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 6.5, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 1070', 'Cores': 1920, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 256, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 6.5, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA Tesla T4', 'Cores': 2560, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 300, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.1, 'VRAM (GB)': 16},
    {'Model': 'GeForce GTX 1660 Ti Laptop', 'Cores': 1536, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 288, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 5.0, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 1070 Max-Q', 'Cores': 2048, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 256, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 6.0, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA Quadro P4000', 'Cores': 1792, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 243, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 5.2, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX 1080 Max-Q', 'Cores': 2560, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 320, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 8.2, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX 1660 SUPER', 'Cores': 1408, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 336, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 5.0, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 1060', 'Cores': 1280, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 4.4, 'VRAM (GB)': 6},
    {'Model': 'NVIDIA Tesla P4', 'Cores': 2560, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 5.5, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX 1060 Laptop', 'Cores': 1280, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 4.4, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 970', 'Cores': 1664, 'L2-Cache (MB)': 1.75, 'Memory Bandwidth (GB/s)': 224, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 3.9, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro P3200', 'Cores': 2304, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 6.1, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 1060 Max-Q', 'Cores': 1280, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 192, 'Performance (FP32 TFLOPS)': 3.8, 'VRAM (GB)': 6},
    {'Model': 'NVIDIA Tesla M60', 'Cores': 4096, 'L2-Cache (MB)': 4, 'Memory Bandwidth (GB/s)': 320, 'Memory Bus (bit)': 512, 'Performance (FP32 TFLOPS)': 9.6, 'VRAM (GB)': 16},
    {'Model': 'GeForce GTX TITAN BLACK', 'Cores': 2880, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 336, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 5.1, 'VRAM (GB)': 6},
    {'Model': 'GeForce GTX 980M', 'Cores': 1536, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 160, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 3.3, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA Quadro P2000', 'Cores': 1024, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 140, 'Memory Bus (bit)': 160, 'Performance (FP32 TFLOPS)': 3.0, 'VRAM (GB)': 5},
    {'Model': 'AMD Radeon RX 480', 'Cores': 2304, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 256, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 5.8, 'VRAM (GB)': 8},
    {'Model': 'AMD Radeon RX 470', 'Cores': 2048, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 211, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 4.9, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro M4000', 'Cores': 1664, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 2.6, 'VRAM (GB)': 8},
    {'Model': 'GeForce GTX 1050 Ti', 'Cores': 768, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 112, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 2.1, 'VRAM (GB)': 4},
    {'Model': 'GeForce GTX 1050 Ti Laptop', 'Cores': 768, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 112, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 2.1, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Tesla K80', 'Cores': 4992, 'L2-Cache (MB)': 3, 'Memory Bandwidth (GB/s)': 480, 'Memory Bus (bit)': 768, 'Performance (FP32 TFLOPS)': 8.7, 'VRAM (GB)': 24},
    {'Model': 'NVIDIA Tesla K40c', 'Cores': 2880, 'L2-Cache (MB)': 1.5, 'Memory Bandwidth (GB/s)': 288, 'Memory Bus (bit)': 384, 'Performance (FP32 TFLOPS)': 4.3, 'VRAM (GB)': 12},
    {'Model': 'GeForce GTX 960', 'Cores': 1024, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 112, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 2.3, 'VRAM (GB)': 4},
    {'Model': 'GeForce GTX 1050 Laptop', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 112, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.8, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro P4200', 'Cores': 2304, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 192, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 6.1, 'VRAM (GB)': 8},
    {'Model': 'NVIDIA Quadro M2200', 'Cores': 1024, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 82, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 2.3, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro P1000', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 82, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.8, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Tegra Xavier', 'Cores': 512, 'L2-Cache (MB)': 2, 'Memory Bandwidth (GB/s)': 137, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 1.3, 'VRAM (GB)': 32},
    {'Model': 'NVIDIA Quadro M2000M (1)', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 80, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.5, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro M2000M (2)', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 80, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.5, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro M2000M (3)', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 80, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.5, 'VRAM (GB)': 4},
    {'Model': 'GeForce GTX 960M', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 80, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.5, 'VRAM (GB)': 4},
    {'Model': 'NVIDIA Quadro K5000', 'Cores': 1536, 'L2-Cache (MB)': 0.5, 'Memory Bandwidth (GB/s)': 173, 'Memory Bus (bit)': 256, 'Performance (FP32 TFLOPS)': 2.1, 'VRAM (GB)': 4},
    {'Model': 'GeForce GT 1030', 'Cores': 384, 'L2-Cache (MB)': 0.5, 'Memory Bandwidth (GB/s)': 48, 'Memory Bus (bit)': 64, 'Performance (FP32 TFLOPS)': 1.1, 'VRAM (GB)': 2},
    {'Model': 'GeForce GTX 950M', 'Cores': 640, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 32, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 1.2, 'VRAM (GB)': 4},
    {'Model': 'GeForce 940MX', 'Cores': 384, 'L2-Cache (MB)': 0.5, 'Memory Bandwidth (GB/s)': 40, 'Memory Bus (bit)': 64, 'Performance (FP32 TFLOPS)': 0.8, 'VRAM (GB)': 2},
    {'Model': 'NVIDIA Tegra X2', 'Cores': 256, 'L2-Cache (MB)': 1, 'Memory Bandwidth (GB/s)': 59.7, 'Memory Bus (bit)': 128, 'Performance (FP32 TFLOPS)': 0.75, 'VRAM (GB)': 8},
    {'Model': 'GeForce GT 710', 'Cores': 192, 'L2-Cache (MB)': 0.5, 'Memory Bandwidth (GB/s)': 14.4, 'Memory Bus (bit)': 64, 'Performance (FP32 TFLOPS)': 0.36, 'VRAM (GB)': 2}
]

gpu_df = pd.DataFrame(gpu_data)


cpu_data = [
    {'Model': 'Intel Xeon Gold 6148', 'L3-Cache size (MB)': 27.5, 'Performance (FP32) (GFLOPS)': 768, 'Cores': 20, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 128},
    {'Model': 'AMD Threadripper 3970X', 'L3-Cache size (MB)': 128, 'Performance (FP32) (GFLOPS)': 1894.4, 'Cores': 32, 'Clock Speed (GHz)': 3.7, 'Memory Bandwidth (GB/s)': 102.4},
    {'Model': 'Intel Xeon Gold 6130', 'L3-Cache size (MB)': 22, 'Performance (FP32) (GFLOPS)': 614.4, 'Cores': 16, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 128},
    {'Model': 'Intel Xeon Gold 6126', 'L3-Cache size (MB)': 19.25, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 12, 'Clock Speed (GHz)': 2.6, 'Memory Bandwidth (GB/s)': 128},
    {'Model': 'Intel Core i9-7940X', 'L3-Cache size (MB)': 19.25, 'Performance (FP32) (GFLOPS)': 844.8, 'Cores': 14, 'Clock Speed (GHz)': 3.1, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Core i9-9940X', 'L3-Cache size (MB)': 19.25, 'Performance (FP32) (GFLOPS)': 844.8, 'Cores': 14, 'Clock Speed (GHz)': 3.3, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Core i9-9960X', 'L3-Cache size (MB)': 22, 'Performance (FP32) (GFLOPS)': 972.8, 'Cores': 16, 'Clock Speed (GHz)': 3.1, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Xeon W-2195', 'L3-Cache size (MB)': 24.75, 'Performance (FP32) (GFLOPS)': 806.4, 'Cores': 18, 'Clock Speed (GHz)': 2.3, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Xeon E5-2698 v4', 'L3-Cache size (MB)': 50, 'Performance (FP32) (GFLOPS)': 704, 'Cores': 20, 'Clock Speed (GHz)': 2.2, 'Memory Bandwidth (GB/s)': 76.8},
    {'Model': 'Intel Core i9-7900X', 'L3-Cache size (MB)': 13.75, 'Performance (FP32) (GFLOPS)': 563.2, 'Cores': 10, 'Clock Speed (GHz)': 3.3, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Xeon Gold 6248', 'L3-Cache size (MB)': 27.5, 'Performance (FP32) (GFLOPS)': 844.8, 'Cores': 20, 'Clock Speed (GHz)': 2.5, 'Memory Bandwidth (GB/s)': 128},
    {'Model': 'AMD Ryzen 9 3950X', 'L3-Cache size (MB)': 64, 'Performance (FP32) (GFLOPS)': 896, 'Cores': 16, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'AMD Ryzen 9 3900X', 'L3-Cache size (MB)': 64, 'Performance (FP32) (GFLOPS)': 576, 'Cores': 12, 'Clock Speed (GHz)': 3.8, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'AMD EPYC 7502', 'L3-Cache size (MB)': 128, 'Performance (FP32) (GFLOPS)': 1280, 'Cores': 32, 'Clock Speed (GHz)': 2.5, 'Memory Bandwidth (GB/s)': 204.8},
    {'Model': 'AMD EPYC 7302', 'L3-Cache size (MB)': 128, 'Performance (FP32) (GFLOPS)': 896, 'Cores': 16, 'Clock Speed (GHz)': 3.0, 'Memory Bandwidth (GB/s)': 204.8},
    {'Model': 'Intel Core i7-9800X', 'L3-Cache size (MB)': 16.5, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.8, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Core i9-9820X', 'L3-Cache size (MB)': 16.5, 'Performance (FP32) (GFLOPS)': 608, 'Cores': 10, 'Clock Speed (GHz)': 3.3, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Core i7-9700K', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Xeon Gold 6134', 'L3-Cache size (MB)': 24.75, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.2, 'Memory Bandwidth (GB/s)': 128},
    {'Model': 'Intel Core i9-9900K', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i7-7820X', 'L3-Cache size (MB)': 11, 'Performance (FP32) (GFLOPS)': 435.2, 'Cores': 8, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Xeon W-2135', 'L3-Cache size (MB)': 8.25, 'Performance (FP32) (GFLOPS)': 316.8, 'Cores': 6, 'Clock Speed (GHz)': 3.7, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Core i7-9700KF', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'AMD Ryzen 7 3800X', 'L3-Cache size (MB)': 32, 'Performance (FP32) (GFLOPS)': 499.2, 'Cores': 8, 'Clock Speed (GHz)': 3.9, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'AMD EPYC 7601', 'L3-Cache size (MB)': 64, 'Performance (FP32) (GFLOPS)': 1088, 'Cores': 32, 'Clock Speed (GHz)': 2.2, 'Memory Bandwidth (GB/s)': 170.6},
    {'Model': 'Intel Core i7-8700', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 403.2, 'Cores': 6, 'Clock Speed (GHz)': 3.2, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i7-8086K', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 403.2, 'Cores': 6, 'Clock Speed (GHz)': 4.0, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i7-9700F', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.0, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'AMD Ryzen 5 3600', 'L3-Cache size (MB)': 32, 'Performance (FP32) (GFLOPS)': 345.6, 'Cores': 6, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'AMD Threadripper 1920X', 'L3-Cache size (MB)': 32, 'Performance (FP32) (GFLOPS)': 652.8, 'Cores': 12, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 102.4},
    {'Model': 'AMD Ryzen 7 3700X', 'L3-Cache size (MB)': 32, 'Performance (FP32) (GFLOPS)': 460.8, 'Cores': 8, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'Intel Xeon E5-2620 v4', 'L3-Cache size (MB)': 20, 'Performance (FP32) (GFLOPS)': 307.2, 'Cores': 8, 'Clock Speed (GHz)': 2.1, 'Memory Bandwidth (GB/s)': 68.3},
    {'Model': 'AMD EPYC 7451', 'L3-Cache size (MB)': 64, 'Performance (FP32) (GFLOPS)': 921.6, 'Cores': 24, 'Clock Speed (GHz)': 2.3, 'Memory Bandwidth (GB/s)': 170.6},
    {'Model': 'Intel Xeon D-2183IT', 'L3-Cache size (MB)': 22, 'Performance (FP32) (GFLOPS)': 614.4, 'Cores': 16, 'Clock Speed (GHz)': 2.2, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Xeon W-2123', 'L3-Cache size (MB)': 8.25, 'Performance (FP32) (GFLOPS)': 204.8, 'Cores': 4, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'AMD Ryzen 5 3500X', 'L3-Cache size (MB)': 32, 'Performance (FP32) (GFLOPS)': 326.4, 'Cores': 6, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'Intel Core i7-6850K', 'L3-Cache size (MB)': 15, 'Performance (FP32) (GFLOPS)': 345.6, 'Cores': 6, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 76.8},
    {'Model': 'Intel Core i5-8400', 'L3-Cache size (MB)': 9, 'Performance (FP32) (GFLOPS)': 268.8, 'Cores': 6, 'Clock Speed (GHz)': 2.8, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i7-5930K', 'L3-Cache size (MB)': 15, 'Performance (FP32) (GFLOPS)': 345.6, 'Cores': 6, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 68.3},
    {'Model': 'Intel Xeon E5-2650 v4', 'L3-Cache size (MB)': 25, 'Performance (FP32) (GFLOPS)': 384, 'Cores': 12, 'Clock Speed (GHz)': 2.2, 'Memory Bandwidth (GB/s)': 76.8},
    {'Model': 'Intel Core i7-7700K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 268.8, 'Cores': 4, 'Clock Speed (GHz)': 4.2, 'Memory Bandwidth (GB/s)': 38.4},
    {'Model': 'Intel Core i7-9750H', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 345.6, 'Cores': 6, 'Clock Speed (GHz)': 2.6, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'IBM POWER9', 'L3-Cache size (MB)': 120, 'Performance (FP32) (GFLOPS)': 960, 'Cores': 24, 'Clock Speed (GHz)': 2.5, 'Memory Bandwidth (GB/s)': 230},  # 10MB/core, SMT4 assumed
    {'Model': 'Intel Core i7-8850H', 'L3-Cache size (MB)': 9, 'Performance (FP32) (GFLOPS)': 345.6, 'Cores': 6, 'Clock Speed (GHz)': 2.6, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'AMD Ryzen 7 2700X', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 435.2, 'Cores': 8, 'Clock Speed (GHz)': 3.7, 'Memory Bandwidth (GB/s)': 46.9},
    {'Model': 'Intel Core i7-8750H', 'L3-Cache size (MB)': 9, 'Performance (FP32) (GFLOPS)': 307.2, 'Cores': 6, 'Clock Speed (GHz)': 2.2, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i9-9880H', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 409.6, 'Cores': 8, 'Clock Speed (GHz)': 2.3, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i7-6700K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 256, 'Cores': 4, 'Clock Speed (GHz)': 4.0, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'NVIDIA Tegra X2', 'L3-Cache size (MB)': 2, 'Performance (FP32) (GFLOPS)': 48, 'Cores': 6, 'Clock Speed (GHz)': 1.5, 'Memory Bandwidth (GB/s)': 25.6},  # A57 + Denver cores
    {'Model': 'Intel Core i7-4790K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 256, 'Cores': 4, 'Clock Speed (GHz)': 4.0, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Xeon E5-2650 v2', 'L3-Cache size (MB)': 25, 'Performance (FP32) (GFLOPS)': 332.8, 'Cores': 8, 'Clock Speed (GHz)': 2.6, 'Memory Bandwidth (GB/s)': 59.7},
    {'Model': 'Intel Xeon E5-2695 v2', 'L3-Cache size (MB)': 35, 'Performance (FP32) (GFLOPS)': 499.2, 'Cores': 12, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 59.7},
    {'Model': 'Intel Xeon E5-2620 v3', 'L3-Cache size (MB)': 15, 'Performance (FP32) (GFLOPS)': 230.4, 'Cores': 6, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 59.7},
    {'Model': 'Intel Xeon Silver 4208', 'L3-Cache size (MB)': 11, 'Performance (FP32) (GFLOPS)': 332.8, 'Cores': 8, 'Clock Speed (GHz)': 2.1, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'AMD Ryzen 7 2700', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 409.6, 'Cores': 8, 'Clock Speed (GHz)': 3.2, 'Memory Bandwidth (GB/s)': 46.9},
    {'Model': 'AMD Ryzen 7 1700X', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 371.2, 'Cores': 8, 'Clock Speed (GHz)': 3.4, 'Memory Bandwidth (GB/s)': 46.9},
    {'Model': 'Intel Xeon Silver 4110', 'L3-Cache size (MB)': 11, 'Performance (FP32) (GFLOPS)': 332.8, 'Cores': 8, 'Clock Speed (GHz)': 2.1, 'Memory Bandwidth (GB/s)': 85.3},
    {'Model': 'Intel Core i5-7400', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 179.2, 'Cores': 4, 'Clock Speed (GHz)': 3.0, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Xeon E3-1231 v3', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 217.6, 'Cores': 4, 'Clock Speed (GHz)': 3.4, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Core i7-8569U', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 230.4, 'Cores': 4, 'Clock Speed (GHz)': 2.8, 'Memory Bandwidth (GB/s)': 37.5},
    {'Model': 'AMD Ryzen 7 1700', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 358.4, 'Cores': 8, 'Clock Speed (GHz)': 3.0, 'Memory Bandwidth (GB/s)': 46.9},
    {'Model': 'Intel Core i7-4770K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 243.2, 'Cores': 4, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Core i5-6500', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 179.2, 'Cores': 4, 'Clock Speed (GHz)': 3.2, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Xeon E3-1505M v5', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 192, 'Cores': 4, 'Clock Speed (GHz)': 2.8, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'AMD Ryzen 5 2600', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 326.4, 'Cores': 6, 'Clock Speed (GHz)': 3.4, 'Memory Bandwidth (GB/s)': 46.9},
    {'Model': 'Intel Core i5-6400', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 166.4, 'Cores': 4, 'Clock Speed (GHz)': 2.7, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i5-9300H', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 192, 'Cores': 4, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 41.6},
    {'Model': 'Intel Core i5-8279U', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 179.2, 'Cores': 4, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 37.5},
    {'Model': 'Intel Core i3-8100', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 166.4, 'Cores': 4, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 37.5},
    {'Model': 'Intel Xeon E5-1620 v3', 'L3-Cache size (MB)': 10, 'Performance (FP32) (GFLOPS)': 217.6, 'Cores': 4, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 59.7},
    {'Model': 'AMD Ryzen 5 1600', 'L3-Cache size (MB)': 16, 'Performance (FP32) (GFLOPS)': 307.2, 'Cores': 6, 'Clock Speed (GHz)': 3.2, 'Memory Bandwidth (GB/s)': 46.9},
    {'Model': 'Intel Xeon E5-2623 v4', 'L3-Cache size (MB)': 10, 'Performance (FP32) (GFLOPS)': 192, 'Cores': 4, 'Clock Speed (GHz)': 2.6, 'Memory Bandwidth (GB/s)': 68.3},
    {'Model': 'Intel Core i7-7700HQ', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 230.4, 'Cores': 4, 'Clock Speed (GHz)': 2.8, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i5-1035G1', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 179.2, 'Cores': 4, 'Clock Speed (GHz)': 1.0, 'Memory Bandwidth (GB/s)': 58.3},  # Ice Lake, DDR4-3200
    {'Model': 'Intel Core i7-7820HQ', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 230.4, 'Cores': 4, 'Clock Speed (GHz)': 2.9, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i7-8565U', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 204.8, 'Cores': 4, 'Clock Speed (GHz)': 1.8, 'Memory Bandwidth (GB/s)': 37.5},
    {'Model': 'Intel Core i7-3930K', 'L3-Cache size (MB)': 12, 'Performance (FP32) (GFLOPS)': 307.2, 'Cores': 6, 'Clock Speed (GHz)': 3.2, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'Intel Core i7-8550U', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 192, 'Cores': 4, 'Clock Speed (GHz)': 1.8, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i7-4870HQ', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 204.8, 'Cores': 4, 'Clock Speed (GHz)': 2.5, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'NVIDIA Carmel (ARMv8.2-A)', 'L3-Cache size (MB)': 4, 'Performance (FP32) (GFLOPS)': 96, 'Cores': 8, 'Clock Speed (GHz)': 1.5, 'Memory Bandwidth (GB/s)': 51.2},  # Estimated
    {'Model': 'Intel Core i3-7100', 'L3-Cache size (MB)': 3, 'Performance (FP32) (GFLOPS)': 115.2, 'Cores': 2, 'Clock Speed (GHz)': 3.9, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i7-3820', 'L3-Cache size (MB)': 10, 'Performance (FP32) (GFLOPS)': 217.6, 'Cores': 4, 'Clock Speed (GHz)': 3.6, 'Memory Bandwidth (GB/s)': 51.2},
    {'Model': 'Intel Core i7-7500U', 'L3-Cache size (MB)': 4, 'Performance (FP32) (GFLOPS)': 128, 'Cores': 2, 'Clock Speed (GHz)': 2.7, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i7-4850HQ', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 204.8, 'Cores': 4, 'Clock Speed (GHz)': 2.3, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Core i5-7300U', 'L3-Cache size (MB)': 3, 'Performance (FP32) (GFLOPS)': 115.2, 'Cores': 2, 'Clock Speed (GHz)': 2.6, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i7-3770K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 230.4, 'Cores': 4, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Core i5-8250U', 'L3-Cache size (MB)': 6, 'Performance (FP32) (GFLOPS)': 179.2, 'Cores': 4, 'Clock Speed (GHz)': 1.6, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i7-2600K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 217.6, 'Cores': 4, 'Clock Speed (GHz)': 3.4, 'Memory Bandwidth (GB/s)': 21.3},
    {'Model': 'Intel Core i7-2700K', 'L3-Cache size (MB)': 8, 'Performance (FP32) (GFLOPS)': 230.4, 'Cores': 4, 'Clock Speed (GHz)': 3.5, 'Memory Bandwidth (GB/s)': 21.3},
    {'Model': 'Intel Core i7-5500U', 'L3-Cache size (MB)': 4, 'Performance (FP32) (GFLOPS)': 115.2, 'Cores': 2, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Core i7-4510U', 'L3-Cache size (MB)': 4, 'Performance (FP32) (GFLOPS)': 102.4, 'Cores': 2, 'Clock Speed (GHz)': 2.0, 'Memory Bandwidth (GB/s)': 25.6},
    {'Model': 'Intel Core i5-6200U', 'L3-Cache size (MB)': 3, 'Performance (FP32) (GFLOPS)': 102.4, 'Cores': 2, 'Clock Speed (GHz)': 2.3, 'Memory Bandwidth (GB/s)': 34.1},
    {'Model': 'Intel Core i5-4258U', 'L3-Cache size (MB)': 3, 'Performance (FP32) (GFLOPS)': 102.4, 'Cores': 2, 'Clock Speed (GHz)': 2.4, 'Memory Bandwidth (GB/s)': 25.6},
]

cpu_df = pd.DataFrame(cpu_data)

import pandas as pd
from collections import defaultdict

# Assuming cpu_df and gpu_df are already defined in the code

# Step 1: Load the Excel file
time_df = pd.read_excel('data_to_calc.xlsx', sheet_name='Sheet4')

# Step 2: Process time_df to sum the pairs of columns for each AI model
time_columns = time_df.columns[2:]
#print(time_columns)
model_columns = defaultdict(list)
for col in time_columns:
    model_name = col.split('_')[-1]  # Extract model name (adjust if naming differs)
    if model_name[-1] != '1' and model_name != 'AI-Score':
      model_columns[model_name].append(col)

#print(model_columns)
for model_name in model_columns:
  #print(time_df[f'{model_name}'])
  time_df[f'{model_name}'] = time_df[f'{model_name}'] + time_df[f'{model_name}.1']
  time_df = time_df.drop(f'{model_name}.1', axis=1)
time_df = time_df.drop('Unnamed: 0', axis=1)
#print(time_df)
cpu_df = pd.DataFrame(cpu_data)
gpu_df = pd.DataFrame(gpu_data)
#cpu_df

#time_df = time_df[['Model'] + [f'time_{model_name}' for model_name in model_columns.keys()]]

# Step 3: Merge with cpu_df and gpu_df
cpu_df = cpu_df.merge(time_df, on='Model', how='left')
gpu_df = gpu_df.merge(time_df, on='Model', how='left')
print(gpu_df)
#gpu_df = gpu_df.iloc[:-1]

# Now cpu_df and gpu_df are expanded with time columns

gpu_df = gpu_df.iloc[:-1]

import matplotlib.pyplot as plt
import numpy as np

# Предполагается, что gpu_df уже загружен
characteristics = ['Cores', 'L2-Cache (MB)', 'Memory Bandwidth (GB/s)', 'Memory Bus (bit)', 'Performance (FP32 TFLOPS)', 'VRAM (GB)']
testt = [col for col in gpu_df.columns if col not in ['Model'] + characteristics + ['AI-Score']]

print(gpu_df.columns)
# Первая часть: для каждой характеристики строим график t vs характеристика
for char in characteristics:
    plt.figure(figsize=(8, 6))

    pl1y=gpu_df['MobileNet-V2']+gpu_df['Inception-V3']+gpu_df['Inception-V4']+gpu_df['Inc-ResNet-V2']+gpu_df['ResNet-V2-50']+gpu_df['ResNet-V2-152']+gpu_df['VGG-16']/7.0
    plt.scatter(gpu_df[char], pl1y, label='Classification', alpha=0.4, color='red')
    b1, a1 = np.polyfit(gpu_df[char], pl1y, deg=1)
    xseq1 = np.linspace(0, gpu_df[char].max(), num=100)
    plt.plot(xseq1, a1 + b1 * xseq1, color="red", lw=2.5)

    pl2y=gpu_df['SRCNN 9-5-5']+gpu_df['VGG-19 Super-Res']+gpu_df['ResNet-SRGAN']+gpu_df['ResNet-DPED']+gpu_df['U-Net']+gpu_df['Nvidia-SPADE']/6
    plt.scatter(gpu_df[char], pl2y, label='Image-to-Image mapping', alpha=0.4, color='blue')
    b2, a2 = np.polyfit(gpu_df[char], pl2y, deg=1)
    xseq2 = np.linspace(0, gpu_df[char].max(), num=100)
    plt.plot(xseq2, a2 + b2 * xseq2, color="blue", lw=2.5)

    pl3y=gpu_df['ICNet']+gpu_df['PSPNet']+gpu_df['DeepLab']/3
    plt.scatter(gpu_df[char], pl3y, label='Image Segmantation', alpha=0.4, color='green')
    b3, a3 = np.polyfit(gpu_df[char], pl3y, deg=1)
    xseq3 = np.linspace(0, gpu_df[char].max(), num=100)
    plt.plot(xseq3, a3 + b3 * xseq3, color="green", lw=2.5)

    #for testi in testt:
        #if testi != 'Pixel-RNN' and testi != 'LSTM':
          #plt.scatter(gpu_df[char], gpu_df[testi], label=testi, alpha=0.6)
    plt.xlabel(char)
    plt.ylabel('Время выполнения (t), с')
    plt.title(f'Время выполнения vs {char}')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True)
    plt.show()