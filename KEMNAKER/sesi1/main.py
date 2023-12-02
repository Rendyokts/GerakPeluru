def kelvin_to_celcius(kelvin):
    """
    Mengkonversi suhu dari Kelvin ke celcius.

    Parameters:
    kelvin (float): Suhu dalam Kelvin.

    Returns:
    float: Suhu dalam celcius.
    """
    celcius = kelvin - 273.15
    return celcius


def celcius_to_kelvin(celcius):
    """
    Mengkonversi suhu dari celcius ke Kelvin.

    Parameters:
    celcius (float): Suhu dalam celcius.

    Returns:
    float: Suhu dalam Kelvin.
    """
    kelvin = celcius + 273.15
    return kelvin


def celcius_to_fahrenheit(celcius):
    """
    Mengkonversi suhu dari celcius ke Fahrenheit.

    Parameters:
    celcius (float): Suhu dalam celcius.

    Returns:
    float: Suhu dalam Fahrenheit.
    """
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit


def convert_temperature(temperature, from_unit, to_unit):
    """
    Mengkonversi suhu dari satu unit ke unit lainnya.

    Parameters:
    temperature (float): Suhu yang akan dikonversi.
    from_unit (str): Unit asal ("C" untuk celcius, "K" untuk Kelvin).
    to_unit (str): Unit tujuan ("C" untuk celcius, "K" untuk Kelvin, "F" untuk Fahrenheit).

    Returns:
    float: Suhu yang sudah dikonversi.
    """
    if from_unit == "C" and to_unit == "K":
        # Jika konversi dari celcius ke Kelvin
        return celcius_to_kelvin(temperature)
    elif from_unit == "K" and to_unit == "C":
        # Jika konversi dari Kelvin ke celcius
        return kelvin_to_celcius(temperature)
    elif from_unit == "C" and to_unit == "F":
        # Jika konversi dari celcius ke Fahrenheit
        return celcius_to_fahrenheit(temperature)
    else:
        print("Konversi tidak didukung.")
        return None


# Contoh penggunaan
suhu_celcius = 30
suhu_kelvin = convert_temperature(suhu_celcius, "C", "K")
print(f"{suhu_celcius} celcius = {suhu_kelvin:.2f} Kelvin")

suhu_fahrenheit = convert_temperature(suhu_celcius, "C", "F")
print(f"{suhu_celcius} celcius = {suhu_fahrenheit:.2f} Fahrenheit")
