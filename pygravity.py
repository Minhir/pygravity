from math import sqrt

data_file = open('data.dat', 'w')

class Planet():

    def __init__(self, x, y, m, v_x, v_y, name):
        self.x = x
        self.y = y
        self.m = m
        self.v_x = v_x
        self.v_y = v_y
        self.name = name


class World():

    def __init__(self, step=0.001, G=6.67*10**-11):
        self.step = step
        self.G = G
        self.planet_list = []

    def distance(self, p1, p2):
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def force_between(self, p1, p2):
        distance = self.distance(p1, p2)
        F = p2.m / distance ** 2
        return F * (p2.x - p1.x) / distance, F * (p2.y - p1.y) / distance

    def add_planets(self, *args):
        for i in args:
            self.planet_list.append(i)

    def step_count(self):
        delta_f_x = []
        delta_f_y = []
        for i in self.planet_list:
            f_x, f_y = 0, 0
            for j in self.planet_list:
                if i == j:
                    continue
                f_x_d, f_y_d = self.force_between(i, j)
                f_x += f_x_d
                f_y += f_y_d
            delta_f_x.append(f_x * self.G * i.m)
            delta_f_y.append(f_y * self.G * i.m)
        for i in range(len(self.planet_list)):
            mass = self.planet_list[i].m
            speed_delta_x = self.step * delta_f_x[i] / mass
            speed_delta_y = self.step * delta_f_y[i] / mass
            self.planet_list[i].x += self.step * (self.planet_list[i].v_x + speed_delta_x / 2)
            self.planet_list[i].y += self.step * (self.planet_list[i].v_y + speed_delta_y / 2)
            self.planet_list[i].v_x = self.planet_list[i].v_x + speed_delta_x
            self.planet_list[i].v_y = self.planet_list[i].v_y + speed_delta_y

    def run(self, number_of_steps):
        for i in range(number_of_steps):
            self.step_count()
            if i % 10000 == 0:
                print(1. * i / number_of_steps)
                print_list = []
                for j in self.planet_list:
                    print_list.append(j.x)
                    print_list.append(j.y)
                data_file.write(' '.join(list(map(str, print_list))))
                data_file.write('\n')

