import yaml

from map import Map

if __name__ == '__main__':
    with open('sample_map.yaml') as f:
        data = yaml.load(f)
    map = Map(data)
    while True:
        print(map.position.look())
        direction = input()
        map.move(direction)
