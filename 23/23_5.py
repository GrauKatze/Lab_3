def same_by(characteristic,objects):
    var = 0;
    for id,v in enumerate(object):
        objects[id] = characteristic[v]
    for i in objects:
        if i != objects[0]:
            return False
    return True 
