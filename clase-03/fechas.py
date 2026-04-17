from datetime import datetime

# Obtener fecha y hora actual
ahora = datetime.now()
print(ahora)

# Obtener solo la fecha
print(datetime.now().date())
print(ahora.date())
# Obtener solo la hora
print(datetime.now().time())
print(ahora.time())

# Año, mes, día por separado

print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)

# Formatear la fecha en Python
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# https://www.cdisc.org/kb/articles/when-would-i-use-iso8601-interval-format?gad_source=1&gad_campaignid=22531944228&gbraid=0AAAAADntc1hnTVejssDfqwAUrzZ0u6qXf&gclid=CjwKCAjwtIfPBhAzEiwAv9RTJidWiPiCbkiMm2U0OkNtROPNPlebUlngYFFqlqPuvPH8uYjIiyslPBoCMGIQAvD_BwE
print(ahora.strftime("%Y-%m-%d"))

