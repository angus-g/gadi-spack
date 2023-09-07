from spack.package import *

class Triangle(Package):
    """Triangle is a two-dimensional mesh generator and Delaunay
    triangulator. Triangle generates exact Delaunay triangulations,
    constrained Delaunay triangulations, conforming Delaunay
    triangulations, Voronoi diagrams, and high-quality triangular
    meshes."""

    homepage = "https://www.cs.cmu.edu/~quake/triangle.html"
    url = "https://www.netlib.org/voronoi/triangle.zip"

    version("1.6", sha256="1766327add038495fa3499e9b7cc642179229750f7201b94f8e1b7bee76f8480")

    variant("showme", default=True, description="Install the graphical Show Me tool")
    depends_on("libx11", type="link", when="+showme")

    def install(self, spec, prefix):
        make()
        mkdirp(prefix.bin)
        mkdirp(prefix.include)

        install("triangle", prefix.bin)
        install("triangle.h", prefix.include)
        if "+showme" in spec:
            install("showme", prefix.bin)
