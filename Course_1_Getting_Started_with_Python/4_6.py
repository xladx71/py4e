def computepay(h, r):
    gp = h * r
    return gp

hrs = input("Enter Hours:")
rph = input("Enter rate per Hour:")
h = float(hrs)
r = float(rph)
oh = (h - 40)
ovr = (r * 1.5)

if h > 40:
    h = h - oh
    p = computepay(h, r) + (oh * ovr)
else : p = computepay(h, r)

print("Pay", p)
