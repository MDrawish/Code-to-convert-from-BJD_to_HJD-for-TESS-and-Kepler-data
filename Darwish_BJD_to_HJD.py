from astropy.coordinates import solar_system_ephemeris, get_body_barycentric
from astropy import units as u
from astropy.constants import au

# Define your BJD (Barycentric Julian Date) values
bjd_values = [2452853.512687, 2452853.385369]

# Create a Time object with your BJD values
t = Time(bjd_values, format="jd", scale="tdb")

# Convert BJD to JD (Julian Date)
jd_values = t.jd

# Print the JD values
for bjd, jd in zip(bjd_values, jd_values):
    print(f'BJD: {bjd}, JD: {jd}')
    
#
# Define your JD (Julian Date) values
jd_values = [2452853.512687, 2452853.385369]

# Define the coordinates (e.g., RA and Dec) of your target
ra = 10.01978 * u.deg  # Right Ascension in degrees
dec = 38.92545 * u.deg  # Declination in degrees

# Create a Time object with your JD values
t = Time(jd_values, format="jd", scale="utc")

# Calculate the Barycentric velocity correction
with solar_system_ephemeris.set("builtin"):
    earth_barycentric = get_body_barycentric("earth", t)
    hjd_bary = get_body_barycentric("sun", t)

# Calculate the HJD values
hjd_values = t.tdb - (earth_barycentric.norm() / au) + (hjd_bary.norm() / au)

# Print the HJD values
for jd, hjd in zip(jd_values, hjd_values):
    print(f'JD: {jd}, HJD: {hjd}')