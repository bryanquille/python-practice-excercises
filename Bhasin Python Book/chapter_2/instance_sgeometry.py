from sgeometry import SGeometry

geometry = SGeometry()

# Distance from origin to a point
geometry.distance_otc(5.0, 6.3)
print(geometry.distance_otc(5.0, 6.3))


# Distance between two points
geometry.distance_p1top2(5.0, 6.3, -53.4, 90.6)
print(geometry.distance_p1top2(5.0, 6.3, -53.4, 90.6))


# 3 points collinear
geometry.collinear(5, 6, 8, 9, -5, 3.4)
print(geometry.collinear(5, 6, 8, 9, -5, 3.4))
print(geometry.collinear(-4, -5, 0, -3, 8, 1))
