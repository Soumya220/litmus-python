#!/usr/bin/env python

import os
import sys
import io

import setuptools

def get_version_from_package() -> str:
	"""
    Read the package version from the source without importing it.
    """
	path = os.path.join(os.path.dirname(__file__), "__init__.py")
	path = os.path.normpath(os.path.abspath(path))
	with open(path) as f:
		for line in f:
			if line.startswith("__version__"):
				token, version = line.split(" = ", 1)
				version = version.replace("'", "").strip()
				return version

name = 'litmus-python'
desc = ''

with io.open('README.md', encoding='utf-8') as strm:
	long_desc = strm.read()

classifiers = [
	'Development Status :: 2 - Pre-Alpha',
	'Intended Audience :: Developers',
	'License :: Freely Distributable',
	'Operating System :: OS Independent',
	'License :: OSI Approved :: Apache Software License',
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: Implementation',
	'Programming Language :: Python :: Implementation :: CPython'
]
license = 'Apache License Version 2.0'
packages = [
	'chaosLib',
	'chaosLib/litmus',
	'chaosLib/litmus/pod_delete',
	'chaosLib/litmus/pod_delete/lib',
	'pkg',
	'pkg/',
	'pkg/maths',
	'pkg/result',
	'pkg/types',
	'pkg/status',
	'pkg/utils',
	'pkg/utils/k8serror',
	'pkg/utils/client',
	'pkg/utils/annotation',
	'pkg/utils/common',
	'pkg/utils/exec',
	'pkg/generic',
	'pkg/events',
	'pkg/generic/pod_delete',
	'pkg/generic/pod_delete/types',
	'pkg/generic/pod_delete/environment',
	'pkg/status',
	'bin',
	'bin/experiment',
	'experiments',
	'experiments/generic',
	'experiments/generic/pod_delete',
	'chaosLib/litmus/aws_az_chaos',
	'chaosLib/litmus/aws_az_chaos/lib',
	'pkg/aws_az',
	'pkg/aws_az/environment',
	'pkg/aws_az/types',
	'pkg/aws_status',
	'experiments/aws_az',
	'experiments/aws_az/aws_az_chaos',
	'experiments/aws_az/aws_az_chaos/experiment',
 	'experiments/generic/pod_delete/experiment',
	'chaosLib/litmus/pod_cpu_hog',
	'chaosLib/litmus/pod_cpu_hog/lib',
	'pkg/generic',
	'pkg/generic/environment',
	'pkg/generic/types',
	'experiments/generic',
	'experiments/generic/pod_cpu_hog',
	'experiments/generic/pod_cpu_hog/experiment',
	'chaosLib/litmus/ec2_terminate_by_id',
	'chaosLib/litmus/ec2_terminate_by_id/lib',
	'pkg/kube_aws',
	'pkg/kube_aws/environment',
	'pkg/kube_aws/types',
	'experiments/kube_aws',
	'experiments/kube_aws/ec2_terminate_by_id',
	'experiments/kube_aws/ec2_terminate_by_id/experiment',
	'chaosLib/litmus/ec2_terminate_by_tag',
	'chaosLib/litmus/ec2_terminate_by_tag/lib',
	'pkg/kube_aws',
	'pkg/kube_aws/environment',
	'pkg/kube_aws/types',
	'experiments/kube_aws',
	'experiments/kube_aws/ec2_terminate_by_tag',
	'experiments/kube_aws/ec2_terminate_by_tag/experiment'
]
needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
package_data = {
	'': ['*.json', '*.yaml', "*.j2"]
}
install_require = []
with io.open('requirements.txt') as f:
	install_require = [l.strip() for l in f if not l.startswith('#')]
pytest_runner = ['pytest_runner'] if needs_pytest else []

setup_params = dict(
	name=name,
	version=get_version_from_package(),
	description=desc,
	long_description=long_desc,
	long_description_content_type='text/markdown',
	classifiers=classifiers,
	license=license,
	packages=packages,
	package_data=package_data,
	include_package_data=True,
	install_requires=install_require,
	setup_requires=pytest_runner,
	python_requires='>=3.5.*'
)


def main():
	"""Package installation entry point."""
	setuptools.setup(**setup_params)


if __name__ == '__main__':
	main()
