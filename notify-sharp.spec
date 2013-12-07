Summary:	C Sharp desktop notification client
Name:		notify-sharp
Version:	0.4.0
Release:	10
License:	MIT
Group:		System/Libraries
Url:		http://www.ndesk.org/NotifySharp
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch
BuildRequires:	monodoc
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(mono)
BuildRequires:	pkgconfig(ndesk-dbus-glib-1.0)

%description
notify-sharp is a C Sharp client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the pkgconfig file for %{name}.

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post,postun):	mono-tools >= 1.1.9

%description doc
This package contains the API documentation for the %{name} in
Monodoc format.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
%makeinstall_std pkgconfigdir=%{_datadir}/pkgconfig

%post doc
%{_bindir}/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files
%doc AUTHORS NEWS README
%{_prefix}/lib/mono/gac/notify-sharp
%{_prefix}/lib/mono/notify-sharp

%files devel
%doc ChangeLog
%{_datadir}/pkgconfig/notify-sharp.pc

%files doc
%{_prefix}/lib/monodoc/sources/notify-sharp-docs.*

