import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import bisect

data = pd.read_excel('data_to _calc.xlsx', sheet_name='Sheet1')

models = ['Inception-V4', 'ResNet-V2-152', 'VGG-16', 'Nvidia-SPADE', 'Pixel-RNN']

# t = inference time + training time
def calculate_t(device, model):
    try:
        inf_col = f"{model} inf"
        train_col = f"{model} train"
        inf_time = data.loc[data['Model'] == device, inf_col].values[0]
        train_time = data.loc[data['Model'] == device, train_col].values[0]
        return inf_time + train_time
    except IndexError:
        print(f"Данные отсутствуют для {device}, {model}")
        return None

r_peak_videocards = {
    'Tesla V100 SXM2 32Gb': 15.7,
    'NVIDIA Quadro GV100': 16.66,
    'NVIDIA TITAN V': 14.9,
    'GeForce RTX 2080 Ti': 13.45,
    'NVIDIA Quadro RTX 8000': 16.3,
    'GeForce GTX 1080 Ti': 11.3,
    'GeForce RTX 2080': 10.1,
    'NVIDIA Quadro P6000': 12,
    'NVIDIA TITAN Xp CE': 12.15,
    'NVIDIA Tesla P40': 12,
    'GeForce GTX 1080': 8.9
}

l2_cache_videocards = {
    'Tesla V100 SXM2 32Gb': 6,
    'NVIDIA Quadro GV100': 6,
    'NVIDIA TITAN V': 4.5,
    'GeForce RTX 2080 Ti': 5.5,
    'NVIDIA Quadro RTX 8000': 6,
    'GeForce GTX 1080 Ti': 2.75,
    'GeForce RTX 2080': 4,
    'NVIDIA Quadro P6000': 3,
    'NVIDIA TITAN Xp CE': 3,
    'NVIDIA Tesla P40': 3,
    'GeForce GTX 1080': 2
}

r_peak_processors = {
    'Intel Xeon Gold 6148': 1536,
    'Intel Xeon Gold 6130': 1075.2,
    'Intel Core i9-9940X': 1478.4,
    'Intel Xeon W-2195': 1324.8,
    'Intel Xeon Gold 6248': 1600,
    'Intel Core i7-9800X': 973,
    'Intel Core i7-9700K': 460.8,
    'Intel Core i9-9900K': 460.8,
    'Intel Core W-2123': 460.8,
    'Intel Core i7-4790K': 256
}


l3_cache_processors = {
    'Intel Xeon Gold 6148': 27.5,
    'Intel Xeon Gold 6130': 22,
    'Intel Core i9-9940X': 19.25,
    'Intel Xeon W-2195': 24.75,
    'Intel Xeon Gold 6248': 27.5,
    'Intel Core i7-9800X': 16.5,
    'Intel Core i7-9700K': 12,
    'Intel Core i9-9900K': 16,
    'Intel Core W-2123': 8.25,
    'Intel Core i7-4790K': 8
}

memory_bandwidth_processors = {
    'Intel Xeon Gold 6148': 120,
    'Intel Xeon Gold 6130': 120,
    'Intel Core i9-9940X': 85,
    'Intel Xeon W-2195': 85,
    'Intel Xeon Gold 6248': 140,
    'Intel Core i7-9800X': 85,
    'Intel Core i7-9700K': 41,
    'Intel Core i9-9900K': 41,
    'Intel Core W-2123': 85,
    'Intel Core i7-4790K': 25
}
videocards = list(r_peak_videocards.keys())
processors = list(r_peak_processors.keys())

balance_processors = {
    proc: r_peak_processors[proc] / memory_bandwidth_processors[proc]
    for proc in processors
    if proc in r_peak_processors and proc in memory_bandwidth_processors
}

plt.figure(figsize=(12, 8))

i_vl = 0
marks = ['o', 'v', '+', 'x', '^']
for videocard in videocards:
    r_peak = r_peak_videocards[videocard]
    l2_cache = l2_cache_videocards[videocard]
    y_values = []
    x_values = []

    shade_vl = (1.0-i_vl,0.4, 1.0)
    for model in models:
        t = calculate_t(videocard, model)
        if t is not None:
            y = t * r_peak * 1e12
            x = l2_cache * 1e6
            y_values.append(y)
            x_values.append(x)
    if y_values:
      for ges, mark in enumerate(marks):
          plt.plot(x_values[ges], y_values[ges], marker=mark, color='black', markersize = 15)
      plt.plot(x_values, y_values, color = shade_vl, linestyle='dotted', linewidth=4, alpha = 0.7, label = videocard)
      i_vl+=0.1

i=0
for model in models:
    y_values = []
    x_values = []
    i+=0.13
    k=i-0.2
    shade = (-0.13+i,0.5+k, 1.0)
    for videocard in videocards:
        r_peak = r_peak_videocards[videocard]
        l2_cache = l2_cache_videocards[videocard]
        t = calculate_t(videocard, model)
        if t is not None:
            y = t * r_peak * 1e12
            x = l2_cache * 1e6
            y_values.append(y)
            x_values.append(x)
    if y_values:
        #x_values.sort()
        x = np.array(x_values).reshape(-1,1)
        y = np.array(y_values)
        reg = LinearRegression().fit(x,y)
        x_pred = np.array(x_values).reshape(-1,1)
        y_pred = reg.predict(x_pred)
        plt.plot(x_pred, y_pred, color=shade, label=f'Линейная аппроксимация {model}')
plt.xlabel('L2Cache (MB)')
plt.ylabel('$t \\times R_{\\text{peak}}$')
plt.title('Видеокарты: $t \\times R_{\\text{peak}} / \\text{L2 Cache}$')
#plt.yscale('log')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.show()

### График 2: Процессоры - t * R_peak / balance
plt.figure(figsize=(12, 8))
i_vl = 0
marks = ['o', 'v', '+', 'x', '^']
for processor in processors:
    r_peak = r_peak_processors[processor]
    balance = balance_processors[processor]
    y_values = []
    x_values = []

    shade_vl = (1.0-i_vl,0.4, 1.0)
    for model in models:
        t = calculate_t(processor, model)
        if t is not None:
            y = (t * r_peak * 1e9)
            x_values.append(balance)
            y_values.append(y)
    if y_values:
      for ges, mark in enumerate(marks):
          plt.plot(x_values[ges], y_values[ges], marker=mark, color='black', markersize = 15)
      plt.plot(x_values, y_values, color = shade_vl, linestyle='dotted', linewidth=4, alpha = 0.7, label=processor)
      i_vl+=0.1

i=0
for model in models:
    y_values = []
    x_values = []
    i+=0.13
    k=i-0.2
    shade = (-0.13+i,0.5+k, 1.0)
    for processor in processors:
        r_peak = r_peak_processors[processor]
        balance = balance_processors[processor]
        t = calculate_t(processor, model)
        if t is not None:
            y = (t * r_peak * 1e9)
            x_values.append(balance)
            y_values.append(y)
    if y_values:
        #x_values.sort()
        x = np.array(x_values).reshape(-1,1)
        y = np.array(y_values)
        reg = LinearRegression().fit(x,y)
        x_pred = np.array(x_values).reshape(-1,1)
        y_pred = reg.predict(x_pred)
        plt.plot(x_pred, y_pred, color=shade, label=f'Линейная аппроксимация {model}')

plt.xlabel("Balance (FLOPs/B)")
plt.ylabel('$t \\times R_{\\text{peak}}$')
plt.title('Процессоры: $t \\times R_{\\text{peak}} / \\text{Balance}$')
#plt.yscale('log')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.show()

### График 3: Процессоры - t * R_peak / L3 Cache
plt.figure(figsize=(12, 8))

i_vl = 0
marks = ['o', 'v', '+', 'x', '^']
for processor in processors:
    r_peak = r_peak_processors[processor]
    l3_cache = l3_cache_processors[processor]
    y_values = []
    x_values = []

    shade_vl = (1.0-i_vl,0.4, 1.0)
    for model in models:
        t = calculate_t(processor, model)
        if t is not None:
            y = t * r_peak * 1e9
            x = l3_cache * 1e6
            x_values.append(x)
            y_values.append(y)
    if y_values:
      for ges, mark in enumerate(marks):
          plt.plot(x_values[ges], y_values[ges], marker=mark, color='black', markersize = 15)
      plt.plot(x_values, y_values, color = shade_vl, linestyle='dotted', linewidth=4, alpha = 0.7, label=processor)
      i_vl+=0.1

i=0
for model in models:
    y_values = []
    x_values = []
    i+=0.13
    k=i-0.2
    shade = (-0.13+i,0.5+k, 1.0)
    for processor in processors:
        r_peak = r_peak_processors[processor]
        l3_cache = l3_cache_processors[processor]
        t = calculate_t(processor, model)
        if t is not None:
            y = t * r_peak * 1e9
            x = l3_cache * 1e6
            x_values.append(x)
            y_values.append(y)
    if y_values:
        #x_values.sort()
        x = np.array(x_values).reshape(-1,1)
        y = np.array(y_values)
        reg = LinearRegression().fit(x,y)
        x_pred = np.array(x_values).reshape(-1,1)
        y_pred = reg.predict(x_pred)
        plt.plot(x_pred, y_pred, color=shade, label=f'Линейная аппроксимация {model}')
plt.xlabel('L3Cache (MB)')
plt.ylabel('$t \\times R_{\\text{peak}}$')
plt.title('Процессоры: $t \\times R_{\\text{peak}} / \\text{L3 Cache}$')
#plt.yscale('log')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.grid(True)
plt.show()