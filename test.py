import psutil

# Informationen über die Speicherauslastung abrufen
memory_usage = psutil.virtual_memory()

# Gesamter physischer Speicher
total_memory = memory_usage.total

# Verfügbare Speichermenge
available_memory = memory_usage.available

# Speicherauslastung in Prozent
memory_percent = memory_usage.percent

# Ausgabe der Speicherauslastung
print(f"Gesamter physischer Speicher: {total_memory} Bytes")
print(f"Verfügbare Speichermenge: {available_memory} Bytes")
print(f"Speicherauslastung: {memory_percent}%")
