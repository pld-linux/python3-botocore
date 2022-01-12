#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (die with MemoryError)

Summary:	Low-level, data-driven core of boto 3
Summary(pl.UTF-8):	Niskopoziomowy, oparty na danych rdzeń boto 3
Name:		python3-botocore
Version:	1.23.33
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/botocore/
Source0:	https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
# Source0-md5:	ac4e471224a3be9e99afeba0ad1ab928
URL:		https://pypi.org/project/botocore/
BuildRequires:	python3-dateutil >= 2.1
BuildRequires:	python3-jmespath >= 0.7.1
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
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-guzzle_sphinx_theme
BuildRequires:	python3-jmespath >= 0.7.1
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.6
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
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py3_ver} tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/botocore
%{py3_sitescriptdir}/botocore-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,development,reference,topics,tutorial,*.html,*.js}
%endif
