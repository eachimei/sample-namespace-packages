| Type | Interpreter | Package A command | Package B command | Uninstall | Status |
| --- | --- | --- | --- | --- | --- |
| pep420 | python3.9 | pip install . | pip install . | A | ✅ |
| pep420 | python3.9 | pip install . | pip install . | B | ✅ |
| pep420 | python3.9 | pip install . | pip install -e . | A | ✅ |
| pep420 | python3.9 | pip install . | pip install -e . | B | ✅ |
| pep420 | python3.9 | pip install -e . | pip install . | A | ✅ |
| pep420 | python3.9 | pip install -e . | pip install . | B | ✅ |
| pep420 | python3.9 | pip install -e . | pip install -e . | A | ✅ |
| pep420 | python3.9 | pip install -e . | pip install -e . | B | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install . | pip install . | A | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install . | pip install . | B | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install . | pip install -e . | A | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install . | pip install -e . | B | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install -e . | pip install . | A | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install -e . | pip install . | B | ✅ |
| cross_pep420_pkg_resources | python3.9 | pip install -e . | pip install -e . | A | ❌ |
| cross_pep420_pkg_resources | python3.9 | pip install -e . | pip install -e . | B | ❌ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install . | pip install . | A | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install . | pip install . | B | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install . | pip install -e . | A | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install . | pip install -e . | B | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install -e . | pip install . | A | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install -e . | pip install . | B | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install -e . | pip install -e . | A | ✅ |
| cross_pep420_toml_pkg_resources | python3.9 | pip install -e . | pip install -e . | B | ✅ |
