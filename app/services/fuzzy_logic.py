import numpy as np
import skfuzzy as fuzz

def calculate_discount(sold_product, loyalty):
    # Definisikan rentang jumlah produk terjual, loyalitas, dan diskon
    max_sold = 100  # Tetapkan batas maksimum untuk kategori produk terjual tinggi
    sold_product_range = np.arange(0, max_sold + 1, 1)
    loyalty_range = np.arange(0, 101, 1)
    discount_range = np.arange(0, 91, 1)

    # Fuzzy sets untuk jumlah produk terjual
    sold_low = fuzz.trimf(sold_product_range, [0, 0, 30])
    sold_medium = fuzz.trimf(sold_product_range, [20, 50, 80])
    sold_high = fuzz.trimf(sold_product_range, [70, 100, 100])

    # Fuzzy sets untuk loyalitas
    loyalty_low = fuzz.trimf(loyalty_range, [0, 0, 40])
    loyalty_medium = fuzz.trimf(loyalty_range, [30, 50, 70])
    loyalty_high = fuzz.trimf(loyalty_range, [60, 100, 100])

    # Fuzzifikasi
    sold_level_low = fuzz.interp_membership(sold_product_range, sold_low, min(sold_product, max_sold))
    sold_level_medium = fuzz.interp_membership(sold_product_range, sold_medium, min(sold_product, max_sold))
    sold_level_high = fuzz.interp_membership(sold_product_range, sold_high, min(sold_product, max_sold))

    loyalty_level_low = fuzz.interp_membership(loyalty_range, loyalty_low, loyalty)
    loyalty_level_medium = fuzz.interp_membership(loyalty_range, loyalty_medium, loyalty)
    loyalty_level_high = fuzz.interp_membership(loyalty_range, loyalty_high, loyalty)

    # Debugging: Print nilai keanggotaan
    print(f"Sold Levels: Low={sold_level_low}, Medium={sold_level_medium}, High={sold_level_high}")
    print(f"Loyalty Levels: Low={loyalty_level_low}, Medium={loyalty_level_medium}, High={loyalty_level_high}")

    # Aturan fuzzy
    rule1 = np.fmin(sold_level_high, loyalty_level_high)  # Diskon tinggi hingga 90%
    rule2 = np.fmin(sold_level_high, loyalty_level_medium)  # Diskon hingga 85%
    rule3 = np.fmin(sold_level_high, loyalty_level_low)  # Diskon tinggi hingga 70%
    rule4 = np.fmin(sold_level_medium, loyalty_level_low)  # Diskon kecil, minimum 10%
    rule5 = np.fmin(sold_level_medium, np.fmax(loyalty_level_medium, loyalty_level_high))  # Diskon medium hingga 60%
    rule6 = np.fmin(sold_level_low, np.fmax(loyalty_level_low, loyalty_level_medium))  # Tidak ada diskon jika sold_low dan loyalty_low
    rule7 = np.fmin(sold_level_low, loyalty_level_medium)

    # Output fuzzy
    discount_high = fuzz.trimf(discount_range, [80, 90, 90])
    discount_medium_high = fuzz.trimf(discount_range, [60, 70, 80])
    discount_medium = fuzz.trimf(discount_range, [40, 50, 60])
    discount_low = fuzz.trimf(discount_range, [10, 20, 30])
    discount_none = fuzz.trimf(discount_range, [0, 0, 10])

    # Agregasi aturan
    aggregated = np.fmax(rule1 * discount_high,
                         np.fmax(rule2 * discount_medium_high,
                                np.fmax(rule3 * discount_medium_high,
                                       np.fmax(rule4 * discount_low,
                                              np.fmax(rule5 * discount_medium,
                                                      np.fmax(rule6 * discount_none, rule7 * discount_none))))))


    # Penanganan kasus eksplisit untuk sold_low dan loyalty_low
    if sold_level_low > 0 and loyalty_level_low > 0:
        print("Anda kurang berbakti, tidak ada diskon.")
        return 0

    # Penanganan kasus maksimum eksplisit
    if sold_level_high == 1.0 and loyalty_level_high == 1.0:
        return 90  # Jika keduanya maksimum, kembalikan 90% langsung

    
    # Penanganan Kasus sold_low and loyalty_medium
    if sold_level_low > 0 and loyalty_level_medium > 0:
        print("Tidak ada diskon untuk sold rendah dan loyalitas medium.")
        return 0

    # Defuzzifikasi
    if np.sum(aggregated) == 0:
        print("Anda kurang berbakti, tidak ada diskon.")
        return 0

    discount = fuzz.defuzz(discount_range, aggregated, 'centroid')

    # Tambahkan variasi lebih luas pada output diskon
    variation = np.random.uniform(-10, 10)  # Variasi lebih luas
    discount = max(1, min(90, discount + variation))  # Pastikan diskon tetap dalam rentang 1-90%

    return int(round(discount))  # Pastikan hasil adalah integer