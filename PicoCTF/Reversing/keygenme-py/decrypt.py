import hashlib
licenseKey = ""

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
bUsername_trial = b"GOUGH"

licenseKey += key_part_static1_trial

for i in [4,5,3,6,2,7,1,8]:
	licenseKey += hashlib.sha256(bUsername_trial).hexdigest()[i]

print(licenseKey)
