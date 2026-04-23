import dolfinx.mesh


def cmap(mesh) -> dolfinx.fem.element.CoordinateElement:
    # Due to https://github.com/FEniCS/dolfinx/pull/4169
    if callable(mesh.geometry.cmap):
        return mesh.geometry.cmap()
    else:
        return mesh.geometry.cmap
