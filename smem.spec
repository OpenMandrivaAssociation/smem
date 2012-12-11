Name:		smem
Version:	0.9
Release:	%mkrel 2
Summary:	Memory reporting tool
Group:		Monitoring
License:	GPLv2+
URL:		http://www.selenic.com/%{name}/
Source0:	http://www.selenic.com/%{name}/download/%{name}-%{version}.tar.gz
Requires:	python
Requires:	python-matplotlib
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
smem is a tool that can give numerous reports on memory usage on Linux systems.
Unlike existing tools, smem can report proportional set size (PSS), which is a
more meaningful representation of the amount of memory used by libraries and
applications in a virtual memory system.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -D smem %{buildroot}/%{_bindir}/smem
install -D capture %{buildroot}/%{_sbindir}/smem-capture

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/smem
%{_sbindir}/smem-capture


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-2mdv2011.0
+ Revision: 614919
- the mass rebuild of 2010.1 packages

* Fri Nov 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1mdv2010.1
+ Revision: 465686
- new version

* Sat May 23 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.1-1mdv2010.0
+ Revision: 378992
- initial release
- import smem


