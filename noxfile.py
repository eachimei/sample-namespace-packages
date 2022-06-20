# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil
import glob
import nox

HERE = os.path.abspath(os.path.dirname(__file__))

nox.options.report = "report.json"
#nox.options.stop_on_first_error = True

# -- REQUIRES: nox >= 2018.10.17
# SEE: https://nox.readthedocs.io/en/stable/index.html
USE_PYTHON_VERSIONS_DEFAULT = ["3.6", "3.7", "3.8", "3.9"]
USE_PYTHON_VERSIONS = os.environ.get("NOXFILE_PYTHON_VERSIONS", "").split()
if not USE_PYTHON_VERSIONS:
    USE_PYTHON_VERSIONS = USE_PYTHON_VERSIONS_DEFAULT


install_commands = (
    ('pip', 'install', '.'),
    ('pip', 'install', '-e', '.'),
    ('python', 'setup.py', 'install'),
    ('python', 'setup.py', 'develop'))

uninstall_names = ("a", "b")


def uninstall_test_flow(session, name):
    pkg_name = f'example_pkg.{name}'
    if name == "a":
        test_file = 'verify_package_b.py'
    elif name == "b":
        test_file = 'verify_package_a.py'
    else:
        raise ValueError(f"invalid subpackage name {name}")
    session.run('pip', 'uninstall', pkg_name, '--yes')
    session.run('python', test_file)

def clean_cwd():
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    for path in glob.glob('*.egg-info'):
        shutil.rmtree(path, ignore_errors=True)

def install_packages(session, package_a, package_b, command_a, command_b):
    session.chdir(package_a)
    clean_cwd()
    session.run(*command_a)
    session.chdir(HERE)
    session.chdir(package_b)
    clean_cwd()
    session.run(*command_b)
    session.chdir(HERE)


@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
@nox.parametrize('uninstall_name', uninstall_names)
def session_pkgutil(session, command_a, command_b, uninstall_name):
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'pkgutil/pkg_a', 'pkgutil/pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
    uninstall_test_flow(session, uninstall_name)


@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
@nox.parametrize('uninstall_name', uninstall_names)
def session_pkg_resources(session, command_a, command_b, uninstall_name):
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'pkg_resources/pkg_a', 'pkg_resources/pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
    uninstall_test_flow(session, uninstall_name)

@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
@nox.parametrize('uninstall_name', uninstall_names)
def session_pep420(session, command_a, command_b, uninstall_name):
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'native/pkg_a', 'native/pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
    uninstall_test_flow(session, uninstall_name)


@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
@nox.parametrize('uninstall_name', uninstall_names)
def session_cross_pkg_resources_pkgutil(
        session, command_a, command_b, uninstall_name):
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'pkg_resources/pkg_a', 'pkgutil/pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
    uninstall_test_flow(session, uninstall_name)


@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
@nox.parametrize('uninstall_name', uninstall_names)
def session_cross_pep420_pkgutil(
        session, command_a, command_b, uninstall_name):
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'native/pkg_a', 'pkgutil/pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
    uninstall_test_flow(session, uninstall_name)


@nox.session(python=USE_PYTHON_VERSIONS)
@nox.parametrize('command_a', install_commands)
@nox.parametrize('command_b', install_commands)
@nox.parametrize('uninstall_name', uninstall_names)
def session_cross_pep420_pkg_resources(
        session, command_a, command_b, uninstall_name):
    session.install('--upgrade', 'setuptools', 'pip')
    install_packages(
        session, 'native/pkg_a', 'pkg_resources/pkg_b',
        command_a, command_b)
    session.run('python', 'verify_packages.py')
    uninstall_test_flow(session, uninstall_name)