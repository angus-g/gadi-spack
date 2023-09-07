from spack.pkg.builtin.intel_oneapi_mkl import IntelOneapiMkl as BuiltinIntelOneapiMkl

class IntelOneapiMkl(BuiltinIntelOneapiMkl):
    @property
    def component_prefix(self):
        # we don't need to join the version into the prefix
        # on Gadi, because the paths have been rearranged
        return self.prefix.join(self.component_dir)
