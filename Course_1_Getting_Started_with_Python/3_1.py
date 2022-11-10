hrs = input("Enter Hours:")
rph = input("Enter rate per Hour:")
h = float(hrs)
r = float(rph)
oh = (h - 40)
ovr = (r * 1.5)
gp = h * r

if h > 40:
    h = h - oh
    gp = (h * r) + (oh * ovr)

print(gp)
