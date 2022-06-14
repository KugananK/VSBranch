from app import db, Countries, Cities

db.create_all() # Creates all table classes defined

uk = Countries(name = 'United Kingdom')
db.session.add(uk)
db.session.commit()

ldn = Cities(name='London', country = uk)
mcr = Cities(name='Manchester', country = uk)

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()

print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
print(f"London's country is: {ldn.country.name}")
print(f"Manchester's country is: {ldn.country.name}")