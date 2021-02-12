#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (die with MemoryError)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Low-level, data-driven core of boto 3
Summary(pl.UTF-8):	Niskopoziomowy, oparty na danych rdzeń boto 3
Name:		python-botocore
Version:	1.20.5
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/botocore/
Source0:	https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
# Source0-md5:	22e2131b194cceb09adda93cd7033496
URL:		https://pypi.org/project/botocore/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-behave >= 1.2.5
BuildRequires:	python-dateutil >= 2.1
BuildRequires:	python-jmespath >= 0.7.1
BuildRequires:	python-jsonschema >= 2.5.1
BuildRequires:	python-mock >= 1.3.0
BuildRequires:	python-nose >= 1.3.7
BuildRequires:	python-urllib3 >= 1.25.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-behave >= 1.2.5
BuildRequires:	python3-dateutil >= 2.1
BuildRequires:	python3-jmespath >= 0.7.1
BuildRequires:	python3-jsonschema >= 2.5.1
BuildRequires:	python3-nose >= 1.3.7
BuildRequires:	python3-urllib3 >= 1.25.4
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-guzzle_sphinx_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI
(<https://github.com/aws/aws-cli>) as well as boto3
(<https://github.com/boto/boto3>).

%description -l pl.UTF-8
Niskopoziomowy interfejs do rosnącej liczby usług Amazon Web Services.
Pakiet botocore jest podstawą dla AWS CLI
(<https://github.com/aws/aws-cli>), jak i boto3
(<https://github.com/boto/boto3>).

%package -n python3-botocore
Summary:	Low-level, data-driven core of boto 3
Summary(pl.UTF-8):	Niskopoziomowy, oparty na danych rdzeń boto 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-botocore
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI
(<https://github.com/aws/aws-cli>) as well as boto3
(<https://github.com/boto/boto3>).

%description -n python3-botocore -l pl.UTF-8
Niskopoziomowy interfejs do rosnącej liczby usług Amazon Web Services.
Pakiet botocore jest podstawą dla AWS CLI
(<https://github.com/aws/aws-cli>), jak i boto3
(<https://github.com/boto/boto3>).

%package apidocs
Summary:	API documentation for Python botocore module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona botocore
Group:		Documentation

%description apidocs
API documentation for Python botocore module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona botocore.

%prep
%setup -q -n botocore-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py3_ver} tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/botocore
%{py_sitescriptdir}/botocore-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-botocore
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/botocore
%{py3_sitescriptdir}/botocore-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,development,reference,topics,tutorial,*.html,*.js}
%endif
