import ivy
from ivy.functional.frontends.jax.func_wrapper import to_ivy_arrays_and_back


@to_ivy_arrays_and_back
def svd(x, /, *, full_matrices=True, compute_uv=True):
    if not compute_uv:
        return ivy.svdvals(x)
    return ivy.svd(x, full_matrices=full_matrices)


@to_ivy_arrays_and_back
def cholesky(x, /, *, symmetrize_input=True):
    def symmetrize(x):
        # TODO : Take Hermitian transpose after complex numbers added
        return (x + ivy.swapaxes(x, -1, -2)) / 2

    if symmetrize_input:
        x = symmetrize(x)

    return ivy.cholesky(x)


@to_ivy_arrays_and_back
def eigh(x, /, *, lower=True, symmetrize_input=True, sort_eigenvalues=True):
    UPLO = "L" if lower else "U"

    def symmetrize(x):
        # TODO : Take Hermitian transpose after complex numbers added
        return (x + ivy.swapaxes(x, -1, -2)) / 2

    if symmetrize_input:
        x = symmetrize(x)

    return ivy.eigh(x, UPLO=UPLO)

  @to_ivy_arrays_and_back
    def all_gather(x, axis_name, *, axis_index_groups=None, axis=0, tiled=False): 
        return all_gather(x, 'i', axis_index_groups=[[0, 2], [3, 1]])         
    
      @to_ivy_arrays_and_back
    def psum(x, axis_name, *, axis_index_groups=None):
        return tree_util.tree_map(def v: v / n, x)         
