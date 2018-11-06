def movement(v=None, d=None, t=None):
    """ Method moving the arm on the z axis. """

    # Check arguments
    arg_count = 0
    if v is not None:
        print('Vitesse  = ' + str(v) + ' m/s')
        arg_count = arg_count + 1
    if d is not None:
        print('Distance = ' + str(d) + ' m')
        arg_count = arg_count + 1
    if t is not None:
        print('Temps    = ' + str(t) + ' m')
        arg_count = arg_count + 1
    if arg_count != 2: return None

    # Resolve equations v=d/t
    if v is None:
        return d/t
    if t is None:
        return d/v
    if d is None:
        return v*t
    return None

if __name__ == '__main__':
    print('Vitesse  = ' + str(movement(d=20, t=5.0)) + ' m/s')
    print('Distance = ' + str(movement(v=12.0, t=5.0)) + ' m')
    print('Temps    = ' + str(movement(d=20.0, v=7.0)) + ' s')