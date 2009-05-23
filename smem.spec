Name:		smem
Version:	0.1
Release:	%mkrel 1
Summary:	Memory reporting tool
Group:		Monitoring
License:	GPLv2+
URL:		http://www.selenic.com/%{name}/
Source0:	http://www.selenic.com/%{name}/download/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

Requires:	python python-matplotlib

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
