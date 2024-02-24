days_to_convert = input()
days_to_convert = int(days_to_convert)

# YEARS
years = days_to_convert // 365
days_to_convert = days_to_convert % 365

#MONTHS
months = days_to_convert // 30

days = days_to_convert % 30


print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")