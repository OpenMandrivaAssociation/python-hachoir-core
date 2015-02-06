%define module_name hachoir-core

Summary:	Python library to edit binary file and metadata
Name:		python-%{module_name}
Version: 	1.3.3
Release: 	3
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://hachoir.org/
BuildArch:	noarch
BuildRequires:	python-setuptools
Obsoletes:	python-hachoir

%description
Hachoir is a library written in Python which allows to see and edit a binary 
file (or any binary stream) field per field. 
A field is the most basic information: a number, a string of characters, 
a flag (yes/no), etc. Only supported formats can be opened, it's not a magic 
tool.
 
It can be used to extract some informations (eg. metadata), edit some fields 
of a file without original program, or convert a file from a format to another.

%prep
%setup -q -n %{module_name}-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%doc doc/* 
%py_puresitedir/*



%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 1.3.3-2mdv2011.0
+ Revision: 594039
- update file list

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.3-1mdv2010.1
+ Revision: 515897
- update to 1.3.3

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 500606
- update to new version 1.3.2

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2010.0
+ Revision: 442150
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 320019
- rebuild with python 2.6
- clean spec
- new release 1.2.1

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 242411
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Michael Scherer <misc@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 52793
- new version 1.0.1

* Fri Jun 15 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.0-1mdv2008.0
+ Revision: 40026
- New release 0.9.0


* Sun Mar 04 2007 Michael Scherer <misc@mandriva.org> 0.7.2-1mdv2007.0
+ Revision: 131965

