from conans import ConanFile


class CpptaskflowConan(ConanFile):
    name = "cpp-taskflow"
    version = "2.1.0"
    license = "MIT"
    description = "A fast C++ header-only library to help you quickly write parallel programs with complex task dependencies"
    topics = ("conan", "cpp-taskflow", "parallelism", "header-only")
    url = "https://github.com/cpp-taskflow/cpp-taskflow"
    homepage = "https://cpp-taskflow.github.io/"
    author = "T.-W. Huang, C.-X. Lin, G. Guo, and M. Wong"
    exports = ["LICENSE"]
    exports_sources = ["taskflow/*"]
    no_copy_source = True

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy(pattern="*", dst="include")

    def package_id(self):
        self.info.header_only()
