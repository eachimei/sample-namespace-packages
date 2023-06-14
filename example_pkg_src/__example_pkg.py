import types
import os
import importlib
import importlib.util
from importlib.machinery import  ModuleSpec, PathFinder
import sys
# no clue what versions this works for
from _frozen_importlib_external import _NamespacePath
MODULE_NAME = 'example_pkg'
finder = PathFinder()
loader = None #?
namespace_path = _NamespacePath(MODULE_NAME, [], finder._get_spec)
module_spec = ModuleSpec(MODULE_NAME, loader, origin=None, loader_state=None, is_package=True)
module_spec.submodule_search_locations = namespace_path
module = importlib.util.module_from_spec(module_spec)
module_path = os.path.join(os.path.dirname(__file__), MODULE_NAME)
namespace_path.append(module_path)
module.__dict__['__path__'] = namespace_path
sys.modules[MODULE_NAME] = module

"""
ModuleSpec(name='example_pkg', loader=<_frozen_importlib_external._NamespaceLoader object at 0x0000029382DC9D30>, submodule_search_locations=_NamespacePath(['c:\\prototyping2023\\namespace_packages\\native\\pkg_a\\example_pkg', 'c:\\prototyping2023\\namespace_packages\\native\\pkg_b\\example_pkg']))

> from _frozen_importlib_external import _NamespacePath

|  _NamespacePath(name, path, path_finder)

 Represents a namespace package's path.  It uses the module name
 |  to find its parent module, and from there it looks up the parent's
 |  __path__.  When this changes, the module's own path is recomputed,
 |  using path_finder.  For top-level modules, the parent module's path
 |  is sys.path.

>>> example_pkg.__path__._path_finder
<bound method PathFinder._get_spec of <class '_frozen_importlib_external.PathFinder'>>
"""