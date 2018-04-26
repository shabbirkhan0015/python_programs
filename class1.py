class py_solution:
    def sub_sets(self, set):
        return self.subsetsRecur([], sorted(set))
    
    def subsetsRecur(self, current, set):
        if set:
            return self.subsetsRecur(current, set[1:]) + self.subsetsRecur(current + [set[0]], set[1:])
        return [current]
print(py_solution().sub_sets([4,5,6]))