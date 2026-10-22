"""Earliest finishes for dependency networks, with cycle/missing-node detection."""
def earliest_finish(tasks):
    finished, visiting = {}, set()

    def visit(name):
        if name in finished:
            return finished[name]
        if name in visiting:
            raise ValueError('Dependency cycle at ' + name)
        if name not in tasks:
            raise ValueError('Unknown dependency: ' + name)
        duration, dependencies = tasks[name]
        if type(duration) is not int or duration < 0:
            raise ValueError('Duration must be a non-negative integer')
        visiting.add(name)
        finished[name] = duration + max((visit(dep) for dep in dependencies), default=0)
        visiting.remove(name)
        return finished[name]

    for name in tasks:
        visit(name)
    return finished


if __name__ == '__main__':
    print(earliest_finish({'design': (3, []), 'purchase': (7, ['design']),
                           'pour': (2, ['purchase'])}))
