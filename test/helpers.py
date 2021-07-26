import jax
import jax.random as jrandom


def random_pytree(key, treedef):
    keys = jrandom.split(key, treedef.num_leaves)
    leaves = []
    for key in keys:
        dimkey, sizekey, valuekey = jrandom.split(key, 3)
        num_dims = jrandom.randint(dimkey, (), 0, 5)
        dim_sizes = jrandom.randint(sizekey, (num_dims,), 0, 5)
        value = jrandom.normal(valuekey, dim_sizes)
        leaves.append(value)
    return jax.tree_unflatten(treedef, leaves)


treedefs = [jax.tree_structure(x) for x in (None, 0, [0], {'a': 0}, {'a': 0, 'b': 0}, {'a': [0, 0], 'b': 0},)]
