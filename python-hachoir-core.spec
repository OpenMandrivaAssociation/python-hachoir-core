%define module_name hachoir-core

Summary:	Python library to edit binary file and metadata
Name:		python-%{module_name}
Version: 	1.2.1
Release: 	%mkrel 2
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://hachoir.org/
BuildArch:	noarch
%{py_requires -d}
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

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%doc doc/* 
%dir %{py_puresitedir}/hachoir_core


