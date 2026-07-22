pkgname = "libimagequant"
pkgver = "4.4.1"
pkgrel = 0
build_style = "cargo"
make_dir = "imagequant-sys"
hostmakedepends = [
    "cargo-auditable",
    "cargo-c",
    "pkgconf",
]
makedepends = ["rust-std"]
pkgdesc = "Palette quantization library"
license = "GPL-3.0-or-later"
url = "https://github.com/ImageOptim/libimagequant"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2464a3e922b5a220b633d674062b82f0670114f8f3dd30d1935a621c95965f1b"


def prepare(self):
    self.cargo.vendor(wrksrc=".")


def install(self):
    self.cargo.cinstall()


@subpackage("libimagequant-devel")
def _(self):
    return self.default_devel()
