%define name notify-sharp
%define version 0
%define release %mkrel 1

Summary: C# desktop notification client
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}.tar.bz2
License: BSD
Group: System/Libraries
Url: http://www.ndesk.org/NotifySharp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: monodoc
BuildRequires: gtk-sharp2
BuildRequires: ndesk-dbus-glib
BuildArch: noarch
%define _requires_exceptions ^lib.*

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package contains the API documentation for the %name in
Monodoc format.


%prep
%setup -q -n %name
aclocal
autoconf
automake -a -c

%build
./configure --prefix=%_prefix
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%_prefix/lib/mono/gac/notify-sharp
%_prefix/lib/mono/notify-sharp
%_datadir/pkgconfig/notify-sharp.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/notify-sharp-docs.*
