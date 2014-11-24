Name:		smem
Version:	1.4
Release:	1
Summary:	Memory reporting tool
Group:		Monitoring
License:	GPLv2+
URL:		http://www.selenic.com/%{name}/
Source0:	http://www.selenic.com/smem/download/%{name}-%{version}.tar.gz
Requires:	python
Requires:	python-matplotlib
BuildArch:	noarch

%description
smem is a tool that can give numerous reports on memory usage on Linux systems.
Unlike existing tools, smem can report proportional set size (PSS), which is a
more meaningful representation of the amount of memory used by libraries and
applications in a virtual memory system.

%prep
%setup -q

%build

%install
install -D smem %{buildroot}/%{_bindir}/smem
install -D capture %{buildroot}/%{_sbindir}/smem-capture

%clean

%files
%defattr(-,root,root,-)
%{_bindir}/smem
%{_sbindir}/smem-capture
