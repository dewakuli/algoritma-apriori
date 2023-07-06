# APRIORI
Fungsi dari algoritma Apriori adalah untuk menemukan aturan asosiasi yang dapat digunakan untuk mengidentifikasi hubungan antara item atau elemen dalam kumpulan data. Aturan asosiasi ini membantu dalam analisis dan pengambilan keputusan di berbagai bidang, seperti pemasaran, penjualan, dan rekomendasi produk.

## kasus yang di angkat
dalam kasus ini mengunakan dataset penjualan di ustu toko (data buatan gak rill) dengan sumber perhitungan sebagai berikut:
### Support
Support menunjukkan popularitas rata-rata produk atau item dalam database. Kita bisa mendapatkan nilai support dengan membagi jumlah total transaksi yang mengandung produk itu dengan jumlah total transaksi.
- Support(item) = jumlah transaksi item / total transaksi semua produk
### Confidence
Confidence mengacu pada kemungkinan seorang pelanggan membeli item1 dan item2 secara bersamaan. 
- Confidence = jumlah transaksi kombinasi item1 dan item2 / total transaksi item1
### lift
Lift adalah peningkatan rasio penjualan item 1 saat kita menjual item2.
- Lift = support(kopi dan minyak) / (support(kopi) * support(minyak))
# penjabaran
## install library
instalasi bisa menggunaka Virtual Environment / cmd
```bash
pip install pandas
pip install numpy
pip install apyori
pip install matplotlib
```

## 1. Menambahkan library
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori
```
## 2. baca data
```
store_data = pd.read_csv("store_data.csv", header=None)
display(store_data.head())
print(store_data.shape)
```
## 3. Menampilkan total Record
```
records = []
for i in range(1, 7501):
    records.append([str(store_data.values[i, j]) for j in range(0, 20)])
print(type(records))
```

## 4. Proses Algoritma Apriori
```
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_results = list(association_rules)
print("terdapat {} record.".format(len(association_results)))
```

## 5. Asosiasi dan hasil perhitungan
```
for item in association_results:
    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    # second index of the inner list
    print("Support: " + str(item[1]))

    # third index of the list located at 0th
    # of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
```
