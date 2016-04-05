from pygravity import Planet, World


sun = Planet(0, 0, 1.9885 * 10**30, 0, 0, 'sun')
mercury = Planet(46 * 10 ** 9, 0, 3.33 * 10 ** 23, 0, 47360, 'mercury')
venera = Planet(107.5 * 10 ** 9, 0, 4.9775 * 10 ** 24, 0, 35000, 'venera')
earth = Planet(147.1 * 10 ** 9, 0, 5.9726 * 10 ** 24, 0, 29783, 'earth')
mars = Planet(206.66 * 10 ** 9, 0, 6.4 * 10 ** 23, 0, 24130, 'mars')
jupiter = Planet(740.57 * 10 ** 9, 0, 1.8986 * 10 ** 27, 0, 13070, 'jupiter')
saturn = Planet(1353.57 * 10 ** 9, 0, 5.6846 * 10 ** 26, 0, 9690, 'saturn')
uran = Planet(2748.94 * 10 ** 9, 0, 8.6832 * 10 ** 25, 0, 6810, 'uran')
neptun = Planet(4452.94 * 10 ** 9, 0, 1.0243 * 10**26, 0, 5434.9, 'neptun')
asteroid = Planet(4452.94 * 10 ** 8, 4452.94 * 10 ** 8, 1.0243 * 10**8, -438, -5434.9, 'asteroid')


world = World(60*5)
world.add_planets(sun, mercury, venera, earth, mars, jupiter, saturn, uran, neptun, asteroid)
world.run(10000000)

