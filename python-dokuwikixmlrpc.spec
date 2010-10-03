%define 	module	dokuwikixmlrpc
Summary:	Python module for the DokuWiki XML-RPC backend
Name:		python-%{module}
Version:	20100719
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://github.com/chimeric/dokuwikixmlrpc/tarball/2010-07-19/#/%{name}.tgz
# Source0-md5:	bd0f6c1d269824b60119cd85e9b5f77c
URL:		http://github.com/chimeric/dokuwikixmlrpc
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dokuwikixmlrpc is a Python module which implements DokuWikis XML-RPC
interface. It can be used to send/retrieve data from remote Dokuwiki
instances.

%prep
%setup -qc
mv chimeric-dokuwikixmlrpc-*/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/dokuwikixmlrpc
%{py_sitescriptdir}/dokuwikixmlrpc/*.py[co]
