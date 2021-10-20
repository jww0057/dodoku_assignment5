import hashlib
import random

def _create(parms):
    result = {'grid', 'integrity', 'status'}
    level = ''
    if 'level' not in parms or parms['level'] == '':
        level = '1'
    else:
        level = parms['level']
    
    if level == '1' or level == '':
        result['grid'] = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0]
        result['integrity'] = integrity1()
        result['status'] = status()
    
    # elif level == '2':
    #     result['grid'] = '[0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0' \
    #                      ',0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,-8,0,-4,0,0,-1,0,0,0,0,-9,0,0,0,0,0,0,0,0,0,0,0,' \
    #                      '-7,0,-5,-8,0,0,0,-2,0,0,0,-6,-1,0]'
    #     result['integrity'] = integrity2()
    #     result['status'] = status()
    #
    # elif level == '3':
    #     result['grid'] = '[0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,' \
    #                      '-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,0,0,-6,0,-4,0,0,0,0,0,0,0,-5,0,0,0,0,0,-9,-8,-2,0,0,0,-4,-3,' \
    #                      '0,0,-7,0,0,0,0,0,0]'
    #     result['integrity'] = integrity3()
    #     result['status'] = status()

    return result

def status():
    status = 'ok'
    return status

def integrity1():
    theString = '0-800-50-200-200-30000-40-100-900-600-90000-60-5-10-300000-70000000-30000-40-20000-2-70-40-40-100-\
                8000000-50-60-50-6-70000-60-90000-200000-60-100000-90-5-40-70000-300-100-400-90-600-90000-30-9-50-8000-1'
    myHash = hashlib.sha256()
    myHash.update(theString.encode())
    myHashDigest = myHash.hexdigest()
    randomStart = random.randint(0, len(myHashDigest) - 8)
    result = myHashDigest[randomStart:randomStart + 8]
    return result

def integrity2():
    theString = '0-900000-80-6-30-50-800-900000-10-400-4000-20000-80-100-70000-70-600-1000-300000000-500-6-500-4-' \
                '900000-7-800-1-900-600000000-2000-700-40-10000-500-10-90000-9000-800-60-500000-500-30-90-6-70-200000-10'
    myHash = hashlib.sha256()
    myHash.update(theString.encode())
    myHashDigest = myHash.hexdigest()
    randomStart = random.randint(0, len(myHashDigest) - 8)
    result = myHashDigest[randomStart:randomStart + 8]
    return result

def integrity3():
    theString = '0000-90000000-50-800000-9-20-3-1000-4-70-50-2-60-600-70-400-50-9-50-20-8-4000-1-80-70000-20000000-' \
                '90-2000-90-40000000-40000-80-3-7000-8-10-70-3-40-300-50-800-60-7-60-10-5-2000-3-10-6-900000-20-50000000-30000'
    myHash = hashlib.sha256()
    myHash.update(theString.encode())
    myHashDigest = myHash.hexdigest()
    randomStart = random.randint(0, len(myHashDigest) - 8)
    result = myHashDigest[randomStart:randomStart + 8]
    return result