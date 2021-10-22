from dodoku.build import Build

def _insert(parms):
    result = {'grid': None, 'integrity': None, 'status': None}
    builder = Build()
    grid = parms.get('grid')
    grid = grid.replace('[', '')
    grid = grid.replace(']', '')
    buildresult = builder.gridbuilder(grid)

    result['grid'] = parms.get('grid')
    result['integrity'] = buildresult
    result['status'] = 'ok'
    return result

    