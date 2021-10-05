#tehdään kaikille neljälle muutokselle funktiot
def celciusToFarenheit(celcius):
    celcius = celcius * 9/5 + 32
    return celcius

def celciusToKelvin(celcius):
    cToK = celcius + 273.15
    return cToK

def farenheitToCelcius(farenheit):
    farenheit = (farenheit - 32) * 5/9
    return farenheit

def farenheitToKelvin(farenheit):
    importedCel = farenheitToCelcius(farenheit) 
    fToK = importedCel + 273.15
    return fToK

#pääfunktio joka kutsuu muita funktioita tarvittaessa
def main():
    paatos = input("Aloitetaanko (C)elciuksella vai (F)arenheiteilla?: ")
    if paatos.lower() == "c":
        asteet = int(input("Anna lämpötila celciuksissa: "))
        print(f"{asteet}C = {celciusToFarenheit(asteet)}F")
        print(f"{asteet}C = {celciusToKelvin(asteet)}F")


    elif paatos.lower() == "f":
        asteet = int(input("Anna lämpötila Fahrenheiteissa: "))
        print(f"{asteet}F = {farenheitToCelcius(asteet)}C")
        print(f"Ja {asteet}F = {farenheitToKelvin(asteet)}K")
    
    else:
        print("ei onnistunut, yritä uudelleen.")

    print("kiitos!")

main()