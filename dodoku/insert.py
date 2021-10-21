from dodoku.build import Build

def _insert(parms):
    #result = {'cell', 'value', 'grid', 'integrity', 'status'}
    builder = Build()
    grid = parms.get('grid')
    
    result = builder.gridbuilder(grid)
    return result

    