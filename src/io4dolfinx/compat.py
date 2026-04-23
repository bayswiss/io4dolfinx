import dolfinx.mesh


def cmap(mesh) -> dolfinx.fem.element.CoordinateElement:
    # Due to https://github.com/FEniCS/dolfinx/pull/4169
    try:
        return mesh.geometry.cmap()
    except TypeError:
        return mesh.geometry.cmap
